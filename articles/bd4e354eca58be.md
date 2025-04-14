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
📽DaVinci Resolve 19 で確認しています。
:::

# Variable Blur

VariBlurノードを使用したhalftoneです

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

## 1. 可変ぼかし

VariBlurノードを使用して
入力画像の明るさに応じてドットのぼかし具合を変更します

![Dot](/images/articles/halftone/variblur/variblur.png)
_VariBlur_

👆 少し見づらいですが、Foregroundの入力画像(左側)の明るい部分でドットのボケが強くなってます

**ボケが大きくなるほどドットが薄くなります**
結果、明るいところはほとんどドットが見えなくなります


このままだと後々扱いにくいので
`InvertColor`を使い入力画像を反転させ、**暗いところほどドットがボケる**ように変更します

![Dot](/images/articles/halftone/variblur/invert-color.png)
_InvertColor_


# 🐔おわりに

これでTool(node)間のCライブラリとのやり取りが楽になるかもしれませんが
有効的な活用方法は謎です🤔🤔🤔😭