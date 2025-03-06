---
title: "【DaVinci Resolve】 ポインタ型と数値型の相互変換 【Fusion】"
emoji: "🔃"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: [davinciresolve, lua, fusion]
published: true
---

# 🐥はじめに

みなさん、こんにちは。[Mug](https://www.youtube.com/@MugLabVideoEditing)です🐼
これは📽[DaVinci Resolve](https://www.blackmagicdesign.com/jp/products/davinciresolve)のFusionについての記事です

Fusion では`SetData`/`GetData`というAPIがあり、これを使用すると
Tool(Node)間で任意データをやり取りすることができます👍
しかし、`SetData`/`GetData`には制限があり、`Number`,`Point`,`table`のような
基本型しか使用することができません😭

Fusionで使われているLuaではC言語の関数を呼び出すことができ
その結果をポインタで受け取ることがあります
それを前述の`SetData`/`GetData`でどうにか取り回すことができないかな？
と言うのが今回のお話です😤

**すごーくニッチ🤏な内容です**

:::message
📽DaVinci Resolve 19 で確認しています。
:::

# 🏫 SetData/GetData

まずは SetData/GetData の使い方からです☝️
`Fusion:SetData`でデータを保存し、`Fusion:GetData`で保存したデータを読み取ります
`Fusion`とは*Fusion object*を表していて`self`や`comp`に置き換えて使用します

## SetData

任意の値(Number, Point, table)を共有データとして保存します

引数：

1. `key`(string)
1. `value`(Number, Point, table)

```lua
self:SetData("key", value)
```

## GetData

[`SetData`](#setdata)で保存された値を取得します
戻り値として対応するデータが返ってきます

引数:

1. `key`(string)、[`SetData`](#setdata)で指定した文字列

```lua
local value = self:GetData("key")
```

## Samples

### Sample 1

この例では Rectangle1 の`Start Render Scripts`で、self(Rectangle1)へ
`"zoom"`, `"angle"`という`数値`データを保存([SetData](#setdata))しています
それを Transform1 で取得([GetData](#getdata))し、`Size`,`Angle`の値として設定しています 😤

![sample1](/images/articles/native-pointer/set-get-data-sample1.png)
_sample 1_

### Sample 2

この例ではcompオブジェクトに対して`文字列`データの保存・取得を行っています 😤

:::message
Tool(node)のスクリプトでは制限が強く`comp`への保存はできません 😭
consoleやfuseでは使用できます
:::

![sample2](/images/articles/native-pointer/set-get-data-sample2.png)
_sample 2_

# 📚 FFI Library

DaVinci Resolve で使用されている Lua の runtime は[Lua JIT](https://luajit.org/)です
この Lua JIT では [FFI Library](https://luajit.org/ext_ffi_api.html)というものが使用でき
これによりC言語で作成されたライブラリを使用することができます

## Load FFI Library

FFI Libraryはデフォルトでは読み込まれません
FFI Libraryには、まず`require`を用いて明示的にLibraryを読み込む必要があります

```lua
local ffi = require("ffi")
```

## 型定義

C言語ライブラリを使用するにはexportされた関数のプロトタイプ宣言, 型定義を行う必要があり
そのために`ffi.cdef`を使用します
`[[`と`]]`の間にC言語の書式で記述します


以下[公式のチュートリアル](https://luajit.org/ext_ffi_tutorial.html)から抜粋

```lua
ffi.cdef[[
void Sleep(int ms);
int poll(struct pollfd *fds, unsigned long nfds, int timeout);
]]
```

:::message
この方法で使用できるのはCライブラリと標準のシステムライブラリのみです
独自のライブラリを使用するには`ffi.load`により読み込む必要があります
詳細は[公式ページ](https://luajit.org/ext_ffi_api.html)を参照してください 👀
:::


## 実行

関数宣言までできればあとは通常のLua関数と同じように呼び出せます
以下は[公式のチュートリアル](https://luajit.org/ext_ffi_tutorial.html)から抜粋です

:::message
宣言した関数はデフォルトでは`ffi.C`にマッピングされます
:::

```lua
local sleep
if ffi.os == "Windows" then
  function sleep(s)
    ffi.C.Sleep(s*1000)
  end
else
  function sleep(s)
    ffi.C.poll(nil, 0, s*1000)
  end
end

for i=1, 10 do
  print("count: " .. i)
  sleep(0.5)
end
```

## まとめ

スクリプト全文を記載します
👇こちらをDaVinci Resolveのconsoleに貼り付ければ動きを確認することができます😊✌️

::::details FFIチュートリアルスクリプト全文
```lua
local ffi = require("ffi")

ffi.cdef[[
void Sleep(int ms);
int poll(struct pollfd *fds, unsigned long nfds, int timeout);
]]

local sleep
if ffi.os == "Windows" then
  function sleep(s)
    ffi.C.Sleep(s*1000)
  end
else
  function sleep(s)
    ffi.C.poll(nil, 0, s*1000)
  end
end

for i=1, 10 do
  print("count: " .. i)
  sleep(0.5)
end
```
::::

# 🔃 ポインタ型/数値型 相互変換

さて、ここからが本題です🐼

下記は`malloc`したメモリに書き込み、それをdumpするサンプルです

:::message
mallocの戻り値が`void*`であるため[ffi.cast](https://luajit.org/ext_ffi_api.html#ffi_cast)を使用してcastする必要があります
:::

```lua
local ffi = require("ffi")

ffi.cdef [[
void* malloc(size_t size);
void free(void *p);
]]

local size = 10
local mallocAddress = ffi.C.malloc(size)
local luaNativeData = ffi.cast("unsigned char*", mallocAddress)

dump(mallocAddress)
dump(luaNativeData)

local offset = 100
for i = 0, (size - 1) do
    luaNativeData[i] = i + 100
end

for i = 0, (size - 1) do
    print("[" .. i .. "]: " .. luaNativeData[i])
end

ffi.C.free(mallocAddress)
```

実行すると👇下記のように出力されます

```lua
cdata<void *>: 0x024bb5317100
cdata<unsigned char *>: 0x024bb5317100
[0]: 100
[1]: 101
[2]: 102
[3]: 103
[4]: 104
[5]: 105
[6]: 106
[7]: 107
[8]: 108
[9]: 109
```

## ポインタ(cdata型)を直接SetDataする

では次に、別のtoolから使えるように`luaNativeData`を[SetData](#setdata)してみます
すると...crashします😭😭😭

:::message alert
DaVinci Resolveが異常終了するので試さないように！🙅‍♀️🆖
:::

```lua
-- freeをcomp:SetDataに置き換え
-- ffi.C.free(mallocAddress)
comp:SetData("native data", luaNativeData)
```

## ポインタを数値型にcastする？

ポインタを直接SetDataすると異常終了するので
数値型にcastすればよいのでは？🤔
と思うかもしれません

しかし、現代の💻PCではポインタは64bit型に格納する必要があり
これもまたSetDataで保存することができません

👇を実行すると
```lua
local ffi = require("ffi")

ffi.cdef [[
void* malloc(size_t size);
void free(void *p);
]]

local size = 10
local mallocAddress = ffi.C.malloc(size)
local luaNativeData = ffi.cast("unsigned char*", mallocAddress)
local uint64Cast = ffi.cast("uint64_t", mallocAddress)

dump(mallocAddress)
dump(luaNativeData)
dump(uint64Cast)
print(string.format("uint64Cast hex: 0x%x", uint64Cast))

-- 以下SetDataのコメントアウトを外すとcrashします
-- comp:SetData("native data", uint64Cast)

ffi.C.free(mallocAddress)
```

👇下記のように出力されます
`mallocAddress`と`uint64Cast`が同じ値を指していることと
uint64Castのdumpに`ULL`(uint64_t型)とついていることがポイントです
```lua
cdata<void *>: 0x021fc769aba0
cdata<unsigned char *>: 0x021fc769aba0
2335512832928ULL
uint64Cast hex: 0x21fc769aba0
```

## uint32_tにcastしてみる 

では何ならSetDataできるのかと言うと
[公式ページに書かれている変換表](https://luajit.org/ext_ffi_semantics.html#convert)でoutputがnumberになる型です
今回はuint32_tを使います

```lua
local ffi = require("ffi")

ffi.cdef [[
void* malloc(size_t size);
void free(void *p);
]]

local size = 10
local mallocAddress = ffi.C.malloc(size)
local uint32Cast = ffi.cast("uint32_t", mallocAddress)

dump(mallocAddress)
dump(uint32Cast)

-- 以下SetDataのコメントアウトを外すとcrashします
-- comp:SetData("native data", uint32Cast)

ffi.C.free(mallocAddress)
```

これを実行した結果が👇下記です
残念ですが、結局`cdata`型なのでSetDataできません😭
```
cdata<void *>: 0x021fc769da40
cdata<unsigned char *>: 0x021fc769da40
cdata<unsigned int>: 0x021f3d256848
```

:::message
アドレスが一致しませんが、これはひとまずおいておきます🫡
:::


### cdata<uint32_t>を数値型へ変換する

ではこの`cdata<unsigned int>`を数値型に変換してみましょう

```lua
local ffi = require("ffi")

ffi.cdef [[
void* malloc(size_t size);
void free(void *p);
]]

local size = 10
local mallocAddress = ffi.C.malloc(size)
local uint32Cast = ffi.cast("uint32_t", mallocAddress)

dump(mallocAddress)

-- tonumberで数値型に変換する
local numberUint32 = tonumber(uint32Cast)
dump(numberUint32)
print(string.format("numberUint32 hex: 0x%x", numberUint32))

ffi.C.free(mallocAddress)
```

👇数値になりました！！😋
```lua
cdata<void *>: 0x021fc769dbe0
3345603552
numberUint32 hex: 0xc769dbe0
```

しかし❗
アドレスが一致しません😭
これは **ポインタ(アドレス)を32bitで保存している** ため、
上位bitが落ちてしまっているためです😖


### 共用体

単純に`uint32_t`へcastしてしまうとbit数が足りないため正しくアドレスが残りません
そこで、 **共用体** の出番です😤

共用体を使って２つの`uint32_t`へ分割してアドレスを保存します

```lua
local ffi = require("ffi")

-- i64構造体とwrapper共用体を定義
ffi.cdef [[
typedef struct i64{unsigned int l; unsigned int h;} i64_t;
typedef union wrapper{ i64_t i; unsigned char* p; } wrapper_t;

void* malloc(size_t size);
void free(void *p);
]]

local size = 10
local mallocAddress = ffi.C.malloc(size)
dump(mallocAddress)

-- 共用体のpにアドレスをいれることで
-- iから32bitに分割された数値として取得できる
local wrapper = ffi.new("wrapper_t")
wrapper.p = mallocAddress

local highAddress = tonumber(wrapper.i.h)
local loAddress = tonumber(wrapper.i.l)
print(string.format("numberUint32 hex: high=0x%x, lo=0x%08x", highAddress, loAddress))

ffi.C.free(mallocAddress)
```

👇ついにできました！！😊✌️
```lua
cdata<void *>: 0x0222e8484b40
numberUint32 hex: high=0x222, lo=0xe8484b40
```
:::message
CPUのバイトオーダーによってhigh, loが逆の可能性がありますが影響はないはずです...🤔
:::


### まとめ

ついにアドレスを数値に変換することができました🎉
ではSetData/GetDataしてみます🫡

```lua
local ffi = require("ffi")

ffi.cdef [[
typedef struct split_u64{uint32_t l; uint32_t h;} split_u64_t;
typedef union wrapper{ split_u64_t i; uint8_t* p; } wrapper_t;
void* malloc(size_t size);
void free(void *p);
]]

local size = 10
local mallocAddress = ffi.C.malloc(size)
local luaNativeData = ffi.cast("unsigned char*", mallocAddress)

dump(mallocAddress)

local offset = 100
for i = 0, (size - 1) do
    luaNativeData[i] = i + 100
end

local wrapper = ffi.new("wrapper_t")
wrapper.p = mallocAddress

-- table(配列)で2つに分割されたアドレスを保存
comp:SetData("native pointer", {wrapper.i.l, wrapper.i.h})

-- table(配列)からアドレスを復元
local addressTable = comp:GetData("native pointer")
local decodeWrapper = ffi.new("wrapper_t")
decodeWrapper.i.l = addressTable[1]
decodeWrapper.i.h = addressTable[2]

dump(decodeWrapper.p)

for i = 0, (size - 1) do
    print("[" .. i .. "]: " .. decodeWrapper.p[i])
end

ffi.C.free(decodeWrapper.p)
```

👇かんぺきです😋
```lua
cdata<void *>: 0x0288afc83830
cdata<unsigned char *>: 0x0288afc83830
[0]: 100
[1]: 101
[2]: 102
[3]: 103
[4]: 104
[5]: 105
[6]: 106
[7]: 107
[8]: 108
[9]: 109
```

# 🐔おわりに

これでTool(node)間のCライブラリとのやり取りが楽になるかもしれませんが
有効的な活用方法は謎です🤔🤔🤔😭
