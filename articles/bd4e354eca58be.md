---
title: "【DaVinci Resolve】 Halftone(ハーフトーン)エフェクトを作る 【Fusion】"
emoji: "💠"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: [davinciresolve, lua, fusion]
published: true
---


# 🐥 はじめに

みなさん、こんにちは。[Mug](https://www.youtube.com/channel/UCuhx0M-PBn4qJ-SUKQ6gVaA)です🐼

本記事では印刷物などで見られるHalftone（ハーフトーン）表現を、📽[DaVinci Resolve](https://www.blackmagicdesign.com/jp/products/davinciresolve) の Fusion で再現する方法を紹介します 

Halftone とは、小さなドットのサイズや密度を変化させることで階調（濃淡）を表現する技法です
- 暗い部分ほど大きなドット ⚫ 
- 明るい部分ほど小さな（またはドットなし）ドット ⬜ 

> @[card](https://ja.wikipedia.org/wiki/%E7%B6%B2%E7%82%B9)


上記を踏まえて、今回は以下の3つのアプローチを紹介します 😤 
1. VariBlur ノードを使った Halftone  
2. Particle ノードを使った Halftone  
3. MugAdvancedHalftone（Fuse）を使った Halftone ← オススメ💯💮  

:::message
* この記事では黒色ドット（グレースケール）の Halftone のみを扱います
* 📽DaVinci Resolve 19 で確認しています
:::

:::message
2026/04/06 より高品質なMugAdvancedHalftoneに置き換えました✨
:::

# 1 Variable Blurによるhalftone

`VariBlur`を使用したhalftoneです

![Halftone example using 'VariBlur'](/images/articles/halftone/variblur/variblur-sample.png)
_完成品_

> 📺 参考動画(元ネタ)
> @[card](https://youtu.be/oeXPrPilrg8?si=v-3qiQ1e314lERoF)

## 1.1 ドット作成

`Shape`等を使用してドットを作成し

![Dot preview](/images/articles/halftone/variblur/dot.png)
_Dot作成_

![Node connection order](/images/articles/halftone/variblur/dot-node.png)
_ノード接続: `sEllipse` → `sRender`_

`Transform`の`Edges`をMirrorに設定、サイズを縮小することで全面にドットを描画します

![Edge settings](/images/articles/halftone/variblur/mirror-dots.png)
_`Edges`をMirrorに設定_

![Node connection order](/images/articles/halftone/variblur/mirror-node.png)
_ノード接続: `sEllipse` → `sRender` → `Transform`_

![Preview after dot size adjustment](/images/articles/halftone/variblur/small-dots.png)
_サイズ調整後のプレビュー_

`Transform`のサイズを👆 のような見た目になるように調整(小さく)します

## 1.2 ドットぼかし

`VariBlur`を使用して入力映像の明るさに応じたドットのぼかしを設定します

`VariBlur`とは`Background`に接続したイメージを
`Foreground`に接続したイメージの明るさに応じてボケさせるノードです
明るい部分ほど大きくボケます

![Preview 'VariBlur'](/images/articles/halftone/variblur/variblur.png)
_`VariBlur`プレビュー_

![Node connection order](/images/articles/halftone/variblur/variblur-node.png)
_ノード接続: `VariBlur` (Background: `Transform`, Foreground: `Input Image`)_

👆 少し見づらいですが、Foregroundの入力映像(左側)の明るい部分でドットのボケが強くなってます👀

📢 **ボケが大きくなるほどドットが薄くなります**
結果、明るいところはほとんどドットが見えなくなります

上記画像のようになるように`VariBlur`の`Blur Size`を調整します

ただ、このままだと後々扱いにくいので
`InvertColor`を使い入力映像を反転させ、 **暗いところほどドットがボケる(=薄くなる)** ように変更します

![InvertColor preview](/images/articles/halftone/variblur/invert-color.png)
_`InvertColor`プレビュー_

![Node connection order](/images/articles/halftone/variblur/invert-color-node.png)
_ノード接続: `Input Image` → `InvertColor` → `VariBlur`(Foreground)_

## 1.3 背景色設定

`Background`をドットとマージします
これがhalftoneの背景色となります、好きな色を設定します🤩

![Background preview](/images/articles/halftone/variblur/background.png)
_`Background`プレビュー_

![Node connection order](/images/articles/halftone/variblur/background-node.png)
_ノード接続: `Merge` (Background: `Background`, Foreground: `Transform`)_

## 1.4 コントラスト調整

`ColorCurves`を使用してドットのコントラストを調整します
カーブ設定を👇下記画像のような形にしてコントラストを上げます
これは入力映像に合わせて調整します💪

![ColorCurves preview](/images/articles/halftone/variblur/color-curves.png)
_`ColorCurves`プレビュー_

![Node connection order](/images/articles/halftone/variblur/color-curves-node.png)
_ノード接続: `VariBlur` → `ColorCurves` → `MediaOut`_

これで完成です🎉

## 1.5 まとめ

### 全体像

![All nodes](/images/articles/halftone/variblur/variblur-all.png)
_ノード構成全体_

### 👍 イイねポイント

* それっぽい見た目
* 処理が軽め

### 🤢 残念ポイント

* ノードの組み合わせが難しい
* 各パラメータの調整が非常に難しい
* ドットサイズ変化が急でラインが目立つ


# 2 Particleによるhalftone

`Particle`を使用したhalftoneです

![Halftone example using 'Particle'](/images/articles/halftone/variblur/particle-sample.png)
_完成品_

> 📺 参考動画(元ネタ)
> @[card](https://youtu.be/lOfIFvMmFe8?si=zpGnpxEsbkW8v37R)


## 2.1 Particle化

`pImageEmitter`を使用して入力映像をparticle化します
ただ接続しただけでは何も表示されないため😑
`pImageEmitter`の各パラメータを下記のように設定します

### ⚙️ Controlsページ ⚙️

1. X Densityを0.1
1. Y Densityを0.1
1. Create Particles Every Frameにチェック✅
1. Lifespanを1.0

### ⚙️ Styleページ ⚙️

1. StyleをNGon
1. NGon Sidesを12
1. Sizeを2.0

### 🗒️設定値解説 🗒️

* `Density`はドット分割数です、大きくするとより細かなドットとなります
 → 大きくすればするほど処理が重くなります😵‍💫
* `Create Prticles Every Frame`, `Lifespan`を設定することでParticleの生成を固定化します
* ドット状になるようにStyleを設定します
* `Size`を2.0にすることである程度暗いところがきれいに塗りつぶされるように設定します
 → これはお好みで調整します👍

👇 正しく設定できれば下記のように少し解像度が下がったような映像になります👀

![pImageEmitter preview](/images/articles/halftone/variblur/pimageemitter.png)
_`pImageEmitter`プレビュー_

![Node connection order](/images/articles/halftone/variblur/pimageemitter-node.png)
_ノード接続: `Input Image` → `pImageEmitter` → `pRender`_

![pImageEmitter controls settings](/images/articles/halftone/variblur/pimageemitter-param1.png)
_`pImageEmitter` Controlsの設定_

![pImageEmitter style settings](/images/articles/halftone/variblur/pimageemitter-param2.png)
_`pImageEmitter` Styleの設定_

## 2.2 輝度に応じたドットサイズ設定

`pCustom`を使用してParticleごとに異なるサイズのドットとなるようにします
各Particleの輝度を算出し、その輝度に比例してParticleサイズを設定します🤔

具体的には`pCustom`でParticleページのSizeを👇下記のように設定します

```lua
size * (1 - ((r * 0.299) + (g * 0.587) + (b * 0.114)))
```
この計算式は輝度が最大のとき`size * 1.0`となります
`size`とは`pImageEmitter`のStyleで設定したサイズです、つまり2.0です


![pCustom preview](/images/articles/halftone/variblur/pcustom.png)
_`pCustom`プレビュー_

![Node connection order](/images/articles/halftone/variblur/pcustom-node.png)
_ノード接続: `pImageEmitter` → `pCustom` → `pRender`_

![pCustom settings](/images/articles/halftone/variblur/pcustom-param1.png)
✂️ --- 中略 ---✂️
![pCustom size setting](/images/articles/halftone/variblur/pcustom-param2.png)
_`pCustom` ParticleページSizeの設定_

## 2.3 ドット色設定

`pCustom`を使用してParticleの色を上書き設定します
Red, Green, Blueに好きな色を設定します😍
今回は黒にします

:::message
色の設定範囲は`0.0 - 1.0`です
:::

![pCustom color settings](/images/articles/halftone/variblur/pcustom-color.png)
_`pCustom` ParticleページRed/Green/Blueの設定_


## 2.4 背景色設定

`Background`をマージして背景色を設定します
これは好きな色を設定します😍
今回は白にします

![Background color settings](/images/articles/halftone/variblur/particle-background.png)
_`Background` の設定_

![Node connection order](/images/articles/halftone/variblur/particle-background-node.png)
_ノード接続: `Merge` (Background: `Background`, Foreground: `pRender`)_

:::message
Foreground/Backgroundの接続先に注意❗
:::

## 2.5 コントラスト調整

`BrightnessContrast`を使用して入力映像のコントラストを調整します
これは📽️映像を見ながら好みのドット感になるように設定します👀

![BrightnessContrast settings](/images/articles/halftone/variblur/particle-contrast.png)
_`BrightnessContrast`の調整_

これで完成です🎉

## 2.6 まとめ

### 全体像

![All nodes](/images/articles/halftone/variblur/particle-all.png)
_ノード構成全体_

### 👍 イイねポイント

* きれいな円形ドット
* 正確なhalftone表現

### 🤢 残念ポイント

* ノードの組み合わせが非常に難しい
* 処理が非常に重い🐘🐘🐘

# 3 MugAdvanced Halftoneによるhalftone

`MugAdvancedHalftone`を使用したhalftoneです
これは私が作ったエフェクトで、実はこの記事はこれを自慢するのが目的の記事です🤫


![Halftone example using 'MugAdvancedHalftone'](/images/articles/halftone/variblur/mah-sample.png)
_完成品_

> 📺 参考動画
> @[card](https://youtu.be/Ult0oDwV73E)


## 3.1 インストール

わたしのGitHubページからfuseファイルをダウンロードし、💻各OSごとの格納先に保存します

### 🗒️ Fuseファイル

https://github.com/mug-lab-3/mug-advanced-halftone/blob/main/MugAdvancedHalftone.fuse


### 📁 各OSごとのFuseファイル格納先

| OS | Path | 
| ---- | ---- |
| macOS | ~/Library/Application Support/Blackmagic Design/DaVinci Resolve/Support/Fusion/Fuses |
| Windows |%appdata%\Blackmagic Design\DaVinci Resolve\Support\Fusion\Fuses |
| Linux |/.local/share/DaVinciResolve/Fusion/Fuses |

## 3.2 接続

インストールするとエフェクトの`Tools → Fuses → Mug`に`MugAdvancedHalftone`というものが追加されます
これを接続します👍

![Effect path](/images/articles/halftone/variblur/mah-effects-path.png)
_エフェクトパネルからの追加_

`Select Tool`(Shift + Space)からはMAHの省略名で検索できます👍

![Effect path](/images/articles/halftone/variblur/mah-shortcut.png)
_`Select Tool` からの追加_

![Effect path](/images/articles/halftone/variblur/mah-preview.png)
_ノード接続: `MediaIn` → `MugAdvancedHalftone` → `MediaOut`_

## 3.3 調整

映像を見ながら`MugAdvancedHalftone`のインスペクタで各パラメータを調整します
直感的に設定できる(と思う)のでお好みで調整します😊

:::message
入力映像の解像度が高いほうがきれいなhalftoneになります
解像度が低い場合はResizeノードで解像度を上げてからhalftoneをかけるのが
おすすめテクニックです🐼
:::

![MugAdvancedHalftone settings](/images/articles/halftone/variblur/mah-settings.png)
_設定例_

これで完成です😮🎉

## 3.4 まとめ

### 全体像

![All nodes](/images/articles/halftone/variblur/mah-all.png)
_ノード構成全体_

### 👍 イイねポイント

* きれいな円形ドット
* 正確なhalftone表現
* 非常に軽い動作
* 非常にシンプルなノード構成
* 直感的なドット調整
* 多機能

### 🤢 残念ポイント

* Fuseファイルのインストールが必要

# 🐔 おわりに

1, 2で紹介した方法で満足できなかったので自分でエフェクトを作りました
`MugAdvancedHalftone`は結構頑張って作ったので使ってもらえるとすごく嬉しいです☺️
ソースコードを公開しているのでFuseの参考にもどうぞ！

この記事が参考になった場合は、ぜひコメントやSNSでシェアしていただけると嬉しいです！
また、フィードバックや質問があればお気軽にお知らせください
