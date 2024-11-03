---
title: "【DaVinci Resolve】AIを使用してButtonControlのExecuteに設定するスクリプトを作る話"
emoji: "🤖"
type: "idea" # tech: 技術記事 / idea: アイデア
topics: ["davinciresolve"]
published: true
---


# 🐥はじめに

みなさん、こんにちは。[Mug](https://www.youtube.com/@MugLabVideoEditing)です✨

これは📽[DaVinci Resolve](https://www.blackmagicdesign.com/jp/products/davinciresolve)についての記事です。

Fusionエフェクトではインスペクタに任意のコントロールを追加することができますが、その中に`ButtonControl`というものがあります。
この`ButtonControl`では、ボタンを押したときの処理を`Execute`に[Luaスクリプト](https://www.lua.org/)で記述して使用します。
**そのため、Luaスクリプトの🎓知識がなければ`ButttonControl`を使用するのは難しいです**😭

なので今回は、LuaスクリプトをAIに作ってもらい、Luaスクリプトの🎓知識がなくても
`ButtonControl`を使えるようにしようというお話です。


関連記事 Control一覧:
https://zenn.dev/muglab3/articles/9ddd0d47321d49


# 📋やりたいこと

Textノードに`ButtonControl`を追加し、そのボタンを押した時に
テキストを今日の`月/日(曜日)`に設定します😤
下記のようなイメージ💭です。

![](https://storage.googleapis.com/zenn-user-upload/6ae51186293b-20241104.png)
*ゴール*


# 🤖スクリプトを作る

* 「」部分が 🤖AIに指示した内容(会話🗣️)
* 👉は出力に対する私の感想
* コードはその指示で出力されたスクリプト

:::message
🤖AIには[GitHub Copilot](https://github.com/features/copilot)で`GPT-4o`を使用しています。
:::


## 1. 🏠Base作成

**「Luaスクリプトで今日の日付と曜日を出力するスクリプトを作って」**
👉printで出力される通常のLuaスクリプトが生成されます。
　これをベースにDaVinciResolveで使えるように直していきます👍
```lua
-- Luaスクリプトで今日の日付と曜日を出力する

-- 現在の日付と時刻を取得
local current_time = os.date("*t")

-- 日付をフォーマットして出力
local formatted_date = string.format("%04d-%02d-%02d", current_time.year, current_time.month, current_time.day)
print("今日の日付: " .. formatted_date)

-- 曜日を取得して出力
local days_of_week = {"日曜日", "月曜日", "火曜日", "水曜日", "木曜日", "金曜日", "土曜日"}
local day_of_week = days_of_week[current_time.wday]
print("今日の曜日: " .. day_of_week)
```

## 2. 💫DaVinci ResolveのFusion用に修正

**「出力は用意してあるDaVinci ResolveのText1ノードのテキストに設定して」**
👉これでDavinci ResolveのFusion用に修正されますが、`comp`の取得方法に問題がありエラーになります😢
>resolve.Fusion()

これはnilになります。

```lua
-- Luaスクリプトで今日の日付と曜日を出力する

-- 現在の日付と時刻を取得
local current_time = os.date("*t")

-- 日付をフォーマットして出力
local date_str = string.format("%04d-%02d-%02d", current_time.year, current_time.month, current_time.day)
local days_of_week = {"日曜日", "月曜日", "火曜日", "水曜日", "木曜日", "金曜日", "土曜日"}
local day_of_week_str = days_of_week[current_time.wday]

-- DaVinci ResolveのFusion APIを使用してText1ノードのテキストを設定
resolve = Resolve()
fusion = resolve.Fusion()
comp = fusion:GetCurrentComp()
text_node = comp:FindTool("Text1")

if text_node then
    text_node.StyledText = "今日の日付: " .. date_str .. "\n今日の曜日: " .. day_of_week_str
else
    print("Text1ノードが見つかりませんでした。")
end
```

## 3. 😵エラーを修正

**「compはすでに定義されているのでそれを使用して」**
  👉これで直るけど、この指示を出すにはスクリプトとDaVinci Resolve Fusionの理解が必要😢

```lua
-- Luaスクリプトで今日の日付と曜日を出力する

-- 現在の日付と時刻を取得
local current_time = os.date("*t")

-- 日付をフォーマットして出力
local date_str = string.format("%04d-%02d-%02d", current_time.year, current_time.month, current_time.day)
local days_of_week = {"日曜日", "月曜日", "火曜日", "水曜日", "木曜日", "金曜日", "土曜日"}
local day_of_week_str = days_of_week[current_time.wday]

-- DaVinci ResolveのFusion APIを使用してText1ノードのテキストを設定
text_node = comp:FindTool("Text1")

if text_node then
    text_node.StyledText = "今日の日付: " .. date_str .. "\n今日の曜日: " .. day_of_week_str
else
    print("Text1ノードが見つかりませんでした。")
end
```


## 4. 📋フォーマット修正

「月/日(曜日)のフォーマットにして」
👉具体的なフォーマットを指定して完成🎉
この内容を`Execute`にコピペします👍

```lua
-- Luaスクリプトで今日の日付と曜日を出力するスクリプト

-- 現在の日付と時刻を取得
local current_date = os.date("*t")

-- 日付をフォーマット
local formatted_date = string.format("%02d/%02d", current_date.month, current_date.day)

-- 曜日を取得
local days_of_week = {"日", "月", "火", "水", "木", "金", "土"}
local formatted_weekday = days_of_week[current_date.wday]

-- Text1ノードを取得
text_node = comp:FindTool("Text1")

-- Text1ノードのテキストを設定
if text_node then
    text_node.StyledText = formatted_date .. "(" .. formatted_weekday .. ")"
else
    print("Text1ノードが見つかりませんでした。")
end

-- 日付と曜日だけを出力
print(formatted_date .. "(" .. formatted_weekday .. ")")
```

# 🐔おわりに

このようにスクリプトを0から作ってもらい完成させることが出来ます。
だた、[エラー修正](#3-エラーを修正)では内容を理解して訂正指示を出す必要がありここが問題です。
👉これができる人間は🤖AIを使わなくても作れるので🤢

結論としては、**全くなんの知識もないと難しい** になります😭

ただ、必ずしも同じ結果になるとは限りません。
学習が進んだり他のAIを使用した場合はすんなりうまくいく可能性があります🐼🐼🐼