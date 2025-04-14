---
title: "【DaVinci Resolve】 Halftone(ハーフトーン)エフェクトを作る 【Fusion】"
emoji: "💠"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: [davinciresolve, lua, fusion]
published: false
---


# 🐥はじめに

みなさん、こんにちは。[Mug](https://www.youtube.com/@MugLabVideoEditing)です🐼
これは📽[DaVinci Resolve](https://www.blackmagicdesign.com/jp/products/davinciresolve)のFusionについての記事です

印刷物において濃淡を表現する方法としてHalftone(ハーフトーン)というものがあります
Halftoneではドットの密度によって濃淡を表現します🤔

つまり暗いところは⚫黒で塗りつぶすようにし、明るいところはドットを描かず(インクを使わず)⬜紙色のまま
中間色はドットをまばらにすることで白と黒が混ざったように見せるというものです
※ この記事では黒色のドットのみとします

この記事ではDaVinci ResolveでこのHalftone(ハーフトーン)を再現する方法をいくつか紹介します✌️

:::message
📽DaVinci Resolve 19 で確認しています
:::

# Variable Blurによるhalftone

VariBlurノードを使用したhalftoneです

:::message
画像が小さくて見えない場合は画像だけを別のタブで開いて見てください🙏
:::


## 1. ドット作成

`Shape`等を使用してドットを作成し

![Dot](/images/articles/halftone/variblur/dot.png)
_Dot_

![Dot](/images/articles/halftone/variblur/dot-node.png)
_`sEllipse` → `sRender`_

`Transform`の`Edges`をMirrorに設定、サイズを縮小することで全面にドットを描画します

![Dot](/images/articles/halftone/variblur/mirror-dots.png)
_`Edges`=Mirror_

![Dot](/images/articles/halftone/variblur/mirror-node.png)
_`Transform`_

![Dot](/images/articles/halftone/variblur/small-dots.png)
_Small-Dots_

`Transform`のサイズを👆 のような見た目になるように調整(小さく)します

## 2. 可変ぼかし

VariBlurノードを使用して
入力画像の明るさに応じてドットのぼかし具合を変更します

`VariBlur`とは`Background`に接続したイメージを
`Foreground`に接続したイメージの明るさに応じてボケ具合を変えるノードです
明るい部分ほど大きくボケます

![Dot](/images/articles/halftone/variblur/variblur.png)
_VariBlur_

![Dot](/images/articles/halftone/variblur/variblur-node.png)
_`VariBlur` (Background: `Transform`, Foreground: `Input Image`)_

👆 少し見づらいですが、Foregroundの入力画像(左側)の明るい部分でドットのボケが強くなってます

**ボケが大きくなるほどドットが薄くなります**
結果、明るいところはほとんどドットが見えなくなります

上記画像のようになるように`VariBlur`の`Blur Size`を調整します

このままだと後々扱いにくいので
`InvertColor`を使い入力画像を反転させ、**暗いところほどドットがボケる**ように変更します

![Dot](/images/articles/halftone/variblur/invert-color.png)
_InvertColor_

![Dot](/images/articles/halftone/variblur/invert-color-node.png)
_`Input Image` → `InvertColor` → `VariBlur`(Foreground)_

## 3. 背景色

`Background`をドットとマージします
これがhalftoneの背景色となります、好きな色を設定します🤩

![Dot](/images/articles/halftone/variblur/background.png)
_Background_

![Dot](/images/articles/halftone/variblur/background-node.png)
_`Marge` (Background: `Background`, Foreground: `Transform`)_

## 4. コントラスト調整

`ColorCurves`をドットのコントラストを調整します
👇カーブ設定を画像のような形にしてコントラストを上げます、入力画像に合わせて調整します💪

![Dot](/images/articles/halftone/variblur/color-curves.png)
_`ColorCurves`_

![Dot](/images/articles/halftone/variblur/color-curves-node.png)
_`VariBlur` → `ColorCurves` → `MediaOut`_

## 評価

これで完成です

👍**イイねポイント**👍
* それっぽい見た目
* 処理が軽め

🤢**残念ポイント**🤢
* ノードの組み合わせが難しい
* 各パラメータの調整が難しい
* 垂直方向のラインが目立つ


# Particleによるhalftone

# MugSimpleHalftoneによるhalftone

# 🐔おわりに
