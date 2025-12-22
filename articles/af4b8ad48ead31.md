---
title: "FFmpegで文字起こし"
emoji: "✒️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: [ffmpeg, whisper, davinciresolve]
published: false
---

# 🐥はじめに

みなさん、こんにちは。[Mug](https://www.youtube.com/channel/UCuhx0M-PBn4qJ-SUKQ6gVaA)です🐼
FFmpegを使って __無料__ で __簡単__ に、動画から文字起こしをする方法の記事です
また、文字起こし結果を📹DaVinci Resolveで使用する方法についても紹介します🫡 

# FFmpegとは？

`FFmpeg`は動画や音声について色々できるソフトウェアで、すごーく有名なものです！
できることが多いのでちょっとざっくりした紹介になってしまいますが
本当に色々できるんですー💦💦

さて、そんな`FFmpeg`ですが Version 8.0からフィルターとして`Whisper`が使えるようになりました！
これによってなんと！動画から文字起こしをすることが可能となりました😤

# Whisperとは？

`Whisper`とは、`OpenAI`が作った音声認識システムです
`OpenAI`は`ChatGPT`を作っているところです
そのことからも分かる通り、`Whisper`はAI技術を利用した音声認識システムで
オープンソースとして公開されています。
音声認識システムとしては、すごーく有名なものです！

# 準備

文字起こしを行うには`FFmpeg`と`model`を用意する必要があります

## FFmpeg

FFmpeg公式サイトの[ダウンロードページ](https://www.ffmpeg.org/download.html) から
使用しているOSにあったものをダウンロードします

![OS選択](/images/articles/whisper/select-operating-system.png)
*OS選択*

OSを選択するとダウンロード元リンクが表示されます。
どれを選んでもファイル自体は同じなので、適当に選択します🤭

![ダウンロード元リンク](/images/articles/whisper/select-download-link-windows.png)
*ダウンロード元選択(Windows)*

リンク先から`FFmpeg`をダウンロードします。
リンク先によってダウンロード方法が異なるので、下記を参考にしてください🙏

![ダウンロード元リンク(Windows)](/images/articles/whisper/download-link-windows.png)
*ダウンロード元選択(Windows)*

![ダウンロード元リンク(Mac)](/images/articles/whisper/download-link-mac.png)
*ダウンロード元選択(Mac)*

ダウンロードできたら展開します
ここではWindowsでの方法を示します

ダウンロードしたファイルを右クリックして、`すべて展開...`を選択