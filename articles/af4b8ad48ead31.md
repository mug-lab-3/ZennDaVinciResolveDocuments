---
title: "FFmpegで文字起こし"
emoji: "✒️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: [ffmpeg, whisper, davinciresolve]
published: false
---

# 🐥はじめに

みなさん、こんにちは。[Mug](https://www.youtube.com/channel/UCuhx0M-PBn4qJ-SUKQ6gVaA)です🐼
これはDaVinci Resolveで読み込むことを前提として
FFmpegを使って動画から文字起こしをする方法の記事です

FFmpeg 8.0 (Huffman)からフィルターにWhisperが追加されました
これによって、音声を分離したり変換したりすることなく、動画から
直接文字起こしができるようになりました😊🎉

## FFmpegとは？

https://ffmpeg.org/

`FFmpeg`は動画や音声について変換したり切り出したり
色々できるソフトウェアで、すごーく有名なものです！
無料で使用できます！💰👌

## Whisper(whisper.cpp)とは？

https://github.com/ggml-org/whisper.cpp

Open AIが作った音声認識AIモデル🤖がWhisperです
このモデルを使うと音声をテキストに起こすことができます
それをC++で実装したものがwhisper.cppです😤
こちらも無料です💰👌

## つまりどういうこと？🤔

無料で簡単に動画ファイルから文字起こしができるよ！

# 準備

さて、準備です。
難しいことは何もないですが、多少の準備が必要です🙏
文字起こしを行うには`FFmpeg`と`whisper.cpp model`を用意する必要があります
それぞれ🌐インターネットからダウンロードします！

## FFmpeg

FFmpeg公式サイトの[ダウンロードページ](https://www.ffmpeg.org/download.html) から
使用しているOSにあったものをダウンロードします

![OS選択](/images/articles/whisper/select-operating-system.png)
*OS選択*

OSを選択するとダウンロード元リンクが表示されます
どれを選んでもファイル自体は同じなので適当に選択します🤭

![ダウンロード元選択(Windowsの例)](/images/articles/whisper/select-download-link-windows.png)
*ダウンロード元選択(Windowsの例)*

リンク先から`FFmpeg`をダウンロードします。
リンク先によってダウンロード方法が異なるので、下記を参考にしてください🙏
複数あるようならFullとかMainとか書かれているものを選びます👀

![ダウンロード元リンク(Windowsの例)](/images/articles/whisper/download-link-windows.png)
*ダウンロードファイル(Windowsの例)*

![ダウンロード元リンク(Macの例)](/images/articles/whisper/download-link-mac.png)
*ダウンロード元選択(Macの例)*

ダウンロードできたら展開します
ここからはWindowsでの方法を示します

ダウンロードしたファイルを右クリックして、`すべて展開...`を選択

![展開](/images/articles/whisper/all-expand.png)
*すべて展開*

展開先を選択して`展開`を押します

:::message
後で展開先ディレクトリを開くので
使いやすいところに展開するようにします
:::

![展開先を選択](/images/articles/whisper/select-expand-directory.png)
*展開先を選択*

以下のようなファイル、ディレクトリが作成されていればOKです🙆‍♀️

![FFmpegファイル](/images/articles/whisper/ffmpeg-directories.png)
*FFmpegファイル*


以上で`FFmpeg`の準備は終わりです🎉💯

## whisper.cpp Model

[HuggingFaceのwhisper.cppリポジトリ](https://huggingface.co/ggerganov/whisper.cpp/tree/main)からモデルをダウンロードします

![モデル](/images/articles/whisper/models.png)
*モデル*


>Models are multilingual unless the model name includes .en. Models ending in -q5_0 are quantized. Models ending in -tdrz support local diarization (marking of speaker turns) using tinydiarize. 

モデルがいっぱいあってどうしたらいいの？という感じだと思いますが
whisper.cppでは各のモデルについて上記のように説明されています
これらを踏まえて、今回はファイル名に`.en`と書かれているのは使わないです
`-q5_0`や`-tdrz`とついているものも見送ります🫡
よって以下の3つから選びます
大きいほうが文字起こし精度が高いです(多分)🫠

| モデル名 | 目安 |
| ------- | ------- |
| ggml-large-v3.bin | つよつよPCならこれ |
| ggml-medium.bin | そこそこPCならこれ |
| ggml-small.bin | 自信ないかもならこれ |

:::message
どれか1つあれば良いですが、余裕があるなら3つとも準備しておくと良いです
さらに余裕があるなら`-q5_0`とかも準備しておくと🙆‍♀️
:::

これらをダウンロードしたら先ほど展開した`FFmpeg`の中に
`models`📁ディレクトリを作成して、その中に置きます

![modelsディレクトリ](/images/articles/whisper/models-directory.png)
*modelsディレクトリを作成*

![モデルファイル](/images/articles/whisper/model-bin-files.png)
*モデルファイル*

:::message
例として3ファイルとも入れていますが、どれか1つ以上あれば良いです
:::

👇このような構成です

```text
mug@mug-main:/mnt/c/Users/mug/OneDrive/Documents/ffmpeg$ tree --dirsfirst
.
├── bin
│   ├── ffmpeg.exe
│   ├── ffplay.exe
│   └── ffprobe.exe
├── doc
│   ├── bootstrap.min.css
│   ├── community.html
│   ├── default.css
│   ...
├── models
│   ├── ggml-large-v3.bin
│   ├── ggml-medium.bin
│   └── ggml-small.bin
├── presets
│   ├── libvpx-1080p.ffpreset
│   ├── libvpx-1080p50_60.ffpreset
│   ├── libvpx-360p.ffpreset
│   ...
├── LICENSE
└── README.txt
```

以上でモデルの準備は終わりです🎉✨

## 文字起こしの実行

準備が整ったのでいよいよ文字起こしをしてみます👏👏👏
方法は`FFmpeg`の公式ドキュメントを確認します

https://ffmpeg.org/ffmpeg-filters.html#whisper-1

上記がWhisperフィルタの使用方法が書かれている箇所ですが
慣れていないとこれだけ書かれてもよくわからないと思います😥

ですが、幸いわかりやすいサンプルがついています！

## パラメータ組み立て

https://ffmpeg.org/ffmpeg-filters.html#Examples-38

> Run a transcription with srt file generation
> ```bash
> ffmpeg -i input.mp4 -vn -af "whisper=model=../whisper.cpp/models/ggml-base.en.bin\
> :language=en\
> :queue=3\
> :destination=output.srt\
> :format=srt" -f null -
> ```

上記がそのサンプルです
これをもとに今回の目的に合うように調整します🫡

変更するのは次の箇所です
詳細については[公式ドキュメント](https://ffmpeg.org/ffmpeg-filters.html#whisper-1)を見てもらいたいです🙏

1. `-i` インプットファイルの指定です、文字起こし対象ファイルに変更します
1. `whisper=model=` モデル指定です、モデルパスをモデル配置先・ファイルに変更します
1. `:language=en` 文字起こし言語設定です、言語は自動検出にするのでこの部分は削除します
1. `:queue=3` キューイングサイズです、今回はリアルタイム処理ではないので長めにします


以下のようになります
ただし、`video.mp4`の部分は文字起こししたいファイルへのパス
`ggml-large-v3.bin`使用したいモデルへ __それぞれ置き換える必要があります__

```bash
ffmpeg -i video.mp4 -vn -af "whisper=model=../models/ggml-large-v3.bin\
:queue=20\
:destination=output.srt\
:format=srt" -f null -
```

# 文字起こし実行

では文字起こしをやってみます🥳
ターミナルを起動して`FFmpeg`を展開したディレクトリ内の`bin`ディレクトリに移動します
その状態で前の章で組み立てた以下のコマンドを実行すればOKです🙆‍♀️
正常に完了すると、`output.srt`として文字起こし結果が出力されます

```
ffmpeg -i video.mp4 -vn -af "whisper=model=../models/ggml-large-v3.bin\
:queue=20\
:destination=output.srt\
:format=srt" -f null -
```
![コマンド入力](/images/articles/whisper/exec-command.png)
*コマンド入力*

![実行完了](/images/articles/whisper/done-command.png)
*実行完了*

![文字起こし結果](/images/articles/whisper/output-file.png)
*文字起こし結果*

ただ、コマンド実行に慣れていない方のためにbatファイルを用意しました😤
__Windowsの場合は__ これを実行するだけで良いです！！

Macの方は、、、ごめんなさいー🙏🙏🙏
ターミナルでコマンドを実行してください。。。

## Windows用バッチファイル

[run-ffmpeg-wisper.bat](https://github.com/mug-lab-3/ZennDaVinciResolveDocuments/blob/main/images/articles/whisper/run-ffmpeg-wisper.bat)をダウンロードして、`FFmpeg`を展開したディレクトリに置きます

![batファイルのダウンロード](/images/articles/whisper/download-bat.png)
*batファイルのダウンロード*

![run-ffmpeg-wisper.bat](/images/articles/whisper/put-bat.png)
*run-ffmpeg-wisper.bat*


batファイルの準備ができたらこのbatに向かって
文字起こししたい動画をドラッグ&ドロップします

![ドラッグ&ドロップ](/images/articles/whisper/dad-to-bat.png)
*ドラッグ&ドロップ*


batファイルを正しく配置できていればターミナルが起動して
使用するモデルを聞かれるので好きな🤖モデル番号を入力します
(modelsディレクトリにおいてあるモデルが選択肢になります)

![モデル選択](/images/articles/whisper/select-model.png)
*モデル選択*


モデルを選択すると以下のように表示されるので
`Enter`を押すと文字起こしが開始されます🤩

![文字起こし開始](/images/articles/whisper/ready-to-exec.png)
*文字起こし開始*


しばらく待っていると文字起こしが完了します
以下のように出ていればOKです

![文字起こし完了](/images/articles/whisper/done-exec.png)
*文字起こし完了*


正常に文字起こしが完了すると`srt`ディレクトリが作られます
その中に文字起こし結果ファイルが出来上がります🔥

![srtディレクトリ](/images/articles/whisper/srt-directory.png)
*srtディレクトリ*

![文字起こし結果](/images/articles/whisper/bat-output-file.png)
*文字起こし結果*

# 文字起こし結果の確認

文字起こしが完了すると`srt`ファイルが作られます
これは字幕ファイルと呼ばれるもので、テキストファイルになっています
(📝テキストエディタで開けます)

*SRTファイルフォーマット*

```text
テキスト番号
開始時間 --> 終了時間
内容
```
*例*
![srtファイル](/images/articles/whisper/result.png)
*srtファイル*

文字起こし結果は完ぺきではないので
多少間違っているところがあります🥺
気になる場合は✋手作業で頑張って直したり、🤖AIを使って直したりします
どちらの場合でも修正するのは __内容__ の部分だけです
それ以外ところを修正すると、ほかのアプリから読み込めなくなる可能性があります

:::message
テキストの区切り方が変なところで区切られてて気になる場合
`queue=`の値をもっと大きくすると自然な区切りに近づきます(多分🙈)
お試しファイルだと20より100とかの方がきれいな気がしました💦💦

👇batファイルの場合は以下を変更
![batファイル](/images/articles/whisper/change-queue-bat.png)
*batファイル*
:::


# DaVinci Resolveで読み込み

文字起こし結果の`srt`ファイルはDaVinci Resolveで読み込んで
字幕として設定することができます✋

メディアプールに`srt`ファイルをドラッグ&ドロップ

![srtファイル登録](/images/articles/whisper/add-sub-to-media-pool.png)
*srtファイル登録*

登録した`srt`ファイルを`タイムライン`にドラッグ&ドロップ

![タイムラインへドラッグ&ドロップ](/images/articles/whisper/sub-to-timeline.png)
*タイムラインへドラッグ&ドロップ*

![字幕トラック追加](/images/articles/whisper/added-subtitle.png)
*字幕トラック追加*

:::message
字幕開始位置は手動で合わせる必要があります
:::

これで完成です💮🎓

# 🐔 おわりに

簡単といいつつとても長くなってしまいました💦
この方法のポイントはpythonのインストールとスクリプトの作成が不要なところです
なのでプログラミングの知識がなくてもできます！！

また、これができるなら文字起こしのために
DaVinci Resolve有料版ことDaVinci Resolve Studioは要らない？
と思うかもしれませんが、有料版では文字起こし結果と連動して
文字ベースで編集する機能があったりして、それが💪強力で💃魅力的ですので、
今回の内容で完全に置き換えられるわけではないです
