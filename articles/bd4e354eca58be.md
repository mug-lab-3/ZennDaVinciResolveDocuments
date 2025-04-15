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

つまり暗いところは⚫大きなドットにし、明るいところはドットを描かず(インクを使わず)⬜紙色のまま
中間色はドットを中間サイズのドットにすることでドット密度が下がり、白と黒が混ざったように見せるというものです
※ この記事では黒色のドットのみ(Gray Scale)とします

この記事ではDaVinci ResolveでこのHalftone(ハーフトーン)を再現する方法をいくつか紹介します✌️

https://ja.wikipedia.org/wiki/%E7%B6%B2%E7%82%B9

:::message
📽DaVinci Resolve 19 で確認しています
:::

# Variable Blurによるhalftone

`VariBlur`を使用したhalftoneです

![Dot](/images/articles/halftone/variblur/variblur-sample.png)
_完成品_


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

👆 少し見づらいですが、Foregroundの入力映像(左側)の明るい部分でドットのボケが強くなってます

**ボケが大きくなるほどドットが薄くなります**
結果、明るいところはほとんどドットが見えなくなります

上記画像のようになるように`VariBlur`の`Blur Size`を調整します

このままだと後々扱いにくいので
`InvertColor`を使い入力映像を反転させ、**暗いところほどドットがボケる**ように変更します

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
_`Merge` (Background: `Background`, Foreground: `Transform`)_

## 4. コントラスト調整

`ColorCurves`をドットのコントラストを調整します
👇カーブ設定を画像のような形にしてコントラストを上げます、入力画像に合わせて調整します💪

![Dot](/images/articles/halftone/variblur/color-curves.png)
_`ColorCurves`_

![Dot](/images/articles/halftone/variblur/color-curves-node.png)
_`VariBlur` → `ColorCurves` → `MediaOut`_

## まとめ

これで完成です

![Dot](/images/articles/halftone/variblur/variblur-all.png)
_ノード構成全体_

### 👍**イイねポイント**👍

* それっぽい見た目
* 処理が軽め

### 🤢**残念ポイント**🤢

* ノードの組み合わせが難しい
* 各パラメータの調整が難しい
* ドットサイズ変化が急

## 参考動画

https://youtu.be/oeXPrPilrg8?si=v-3qiQ1e314lERoF


# Particleによるhalftone

`Particle`を使用したhalftoneです

![Dot](/images/articles/halftone/variblur/particle-sample.png)
_完成品_

:::message
画像が小さくて見えない場合は画像だけを別のタブで開いて見てください🙏
:::

## 1. Particle化

`pImageEmitter`を使用して入力映像をparticle化します
ただ接続したたけど何も表示されないため`pImageEmitter`の
各パラメータを下記のように設定します

⚙️ Controls ⚙️
1. Densityを0.1
1. Create Particles Every Frameにチェック
1. Lifespanを1

⚙️ Style ⚙️
1. StyleをNGon
1. NGon Sidesを12
1. Sizeを2.0

* Densityはドット分割数です、大きくするとより細かなドットとなります
* `Create Prticles Every Frame`, `Lifespan`を設定することでParticleの生成を固定化します
* ドット状になるようにStyleを設定します
* SizeはDensityに合わせてちょうどドットで埋まるようなサイズに設定します
 → Densityを変更したらSizeも変更します

正しく設定できれば下記のようになります✨

![pImageEmitter-Preview](/images/articles/halftone/variblur/pimageemitter.png)
_`pImageEmitter`_

![pImageEmitter-Node](/images/articles/halftone/variblur/pimageemitter-node.png)
_`Input Image` → `pImageEmitter` → `pRender`_

![pImageEmitter-Controls](/images/articles/halftone/variblur/pimageemitter-param1.png)
_`pImageEmitter` Controlsの設定_

![pImageEmitter-Style](/images/articles/halftone/variblur/pimageemitter-param2.png)
_`pImageEmitter` Styleの設定_

## 2. 輝度に応じたドットサイズ設定

pCustomを使用してParticleごとに異なるサイズになるようにします
各Particleの輝度を算出し、その輝度に比例してParticleサイズを設定します

具体的には`pCustom`のParticleページのSizeを下記のように設定します

```lua
size * (1 - ((r * 0.299) + (g * 0.587) + (b * 0.114)))
```
これは輝度が最大のとき`size * 1.0`となります
`size`とは`pImageEmitter`のStyleで設定したサイズです、つまり2.0です


![pCustom-Preview](/images/articles/halftone/variblur/pcustom.png)
_`pCustom`_

![pCustom-Preview](/images/articles/halftone/variblur/pcustom-node.png)
_`pImageEmitter` → `pCustom` → `pRender`_

![pCustom-Preview](/images/articles/halftone/variblur/pcustom-param1.png)
✂️ --- 中略 ---✂️
![pCustom-Preview](/images/articles/halftone/variblur/pcustom-param2.png)
_`pCustom` ParticleページSizeの設定_

## 3. ドット色設定

`pCustom`を使用してParticleの色を上書き設定します
Red, Green, Blueに好きな色を設定します
※ ここでは黒にします
※ 色の設定範囲は`0.0 - 1.0`です

![pCustom-Color](/images/articles/halftone/variblur/pcustom-color.png)
_`pCustom` ParticleページRed/Green/Blueの設定_


## 4. 背景色設定

`Background`をマージして背景色を設定します
これは好きな色を設定します
※ ここでは白にします

![Background-Color](/images/articles/halftone/variblur/particle-background.png)
_`Background` の設定_

![Background-Node](/images/articles/halftone/variblur/particle-background-node.png)
_`Merge` (Background: `Background`, Foreground: `pRender`)_


## 5. ドットサイズ調整

映像を見ながら`pImageEmitter`のDensity, Sizeを好みの画になるように調整します

今回は以下のように設定し直しました
* Density = 0.2
* Size = 1.4

※ Densityを上げれば上げるほど重くなります🐘

![Contrst](/images/articles/halftone/variblur/particle-contrast.png)
_`pImageEmitter`再調整_

## まとめ

これで完成です

![Dot](/images/articles/halftone/variblur/particle-all.png)
_ノード構成全体_

### 👍**イイねポイント**👍

* きれいな円形ドット
* 正確なhalftone表現

### 🤢**残念ポイント**🤢

* ノードの組み合わせが難しい
* 非常に動作が重い🐘🐘🐘

## 参考動画
https://youtu.be/lOfIFvMmFe8?si=zpGnpxEsbkW8v37R


# MugSimpleHalftoneによるhalftone

# 🐔おわりに
