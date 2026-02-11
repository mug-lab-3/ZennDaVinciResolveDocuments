---
title: "FFmpegで文字起こし"
emoji: "✒️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: [ffmpeg, whisper, davinciresolve]
published: true
---

# 🐥はじめに

みなさん、こんにちは。[Mug](https://www.youtube.com/channel/UCuhx0M-PBn4qJ-SUKQ6gVaA)です🐼  
本記事はDaVinci Resolveでの利用を前提に、FFmpegを使って動画から文字起こしを行う手順をまとめています。

FFmpeg 8.0 (Huffman)ではWhisperフィルターが追加され、音声を分離したり変換したり
難しいプログラミングをしなくても動画から簡単に文字起こしができるようになりました😊🎉

## FFmpegとは？

https://ffmpeg.org/

`FFmpeg`は動画や音声の変換や切り出しなど幅広い処理に対応した、とても有名なソフトウェアです。
無料で利用できます0️⃣💴👍

## Whisper(whisper.cpp)とは？

https://github.com/ggml-org/whisper.cpp

OpenAI[^1]が作った音声認識AIモデル🤖がWhisperです。このモデルを使うと音声をテキスト化できます。
それをC++で実装したものがwhisper.cppで、こちらも無料です0️⃣💴👍

[^1]: OpenAIは🤖ChatGPTを作っている会社です

## つまりどういうことなの？🤔

無料アプリを使って、簡単に動画ファイルから文字起こしができるということです！🥳🎆

# 準備

まずは準備です🧘‍♀️
文字起こしを行うには`FFmpeg`と`whisper.cpp`のモデルが必要です。
どちらも🌐インターネットからダウンロードできます！

## FFmpeg

FFmpeg公式サイト[^2]の[**ダウンロードページ**](https://www.ffmpeg.org/download.html)から、使用しているOSに合うものをダウンロードします。

:::message alert
2026/2/11 追記
こちらで配布されているMac版のFFmpegに、whisperが含まれていないようです...
Macではこの方法で文字起こしが出来ません😭
:::

[^2]: https://ffmpeg.org/

![OS選択](/images/articles/whisper/select-operating-system.png)
*OS選択*

OSを選択するとダウンロード元リンクが表示されます。どれを選んでもファイル自体は同じなので、どれでも大丈夫です🤭

![ダウンロード元選択(Windowsの例)](/images/articles/whisper/select-download-link-windows.png)
*ダウンロード元選択(Windowsの例)*

リンク先によってダウンロード方法が異なるので、下記の画像を参考にしてください🙏  
複数選択肢がある場合は`Full`や`Main`と書かれているものを選ぶようにします👀

![ダウンロード元リンク(Windowsの例)](/images/articles/whisper/download-link-windows.png)
*ダウンロードファイル(Windowsの例)*

![ダウンロード元リンク(Macの例)](/images/articles/whisper/download-link-mac.png)
*ダウンロード元選択(Macの例)*

ダウンロードできたら展開します。ここからは __Windows__ での手順を例に説明します。

ダウンロードしたファイルを右クリックして`すべて展開...`を選択します。

![展開](/images/articles/whisper/all-expand.png)
*すべて展開*

展開先を選択して`展開`を押します。

:::message
後で展開先ディレクトリを開くので、アクセスしやすい場所に展開しておきましょう。
:::

![展開先を選択](/images/articles/whisper/select-expand-directory.png)
*展開先を選択*

以下のようなファイル・ディレクトリが作成されていればOKです🙆‍♀️

![FFmpegファイル](/images/articles/whisper/ffmpeg-directories.png)
*FFmpegファイル*


以上で`FFmpeg`の準備は完了です🎉💯

## whisper.cpp Model

[HuggingFaceのwhisper.cppリポジトリ](https://huggingface.co/ggerganov/whisper.cpp/tree/main)からモデルをダウンロードします

![モデル](/images/articles/whisper/models.png)
*モデル*

>Models are multilingual unless the model name includes .en. Models ending in -q5_0 are quantized. Models ending in -tdrz support local diarization (marking of speaker turns) using tinydiarize. 

モデルがたくさんあって迷うと思いますが😵‍💫
whisper.cppでは上記のように特徴が説明されています。  
また、大きいモデルほど精度は上がりますが、CPU負荷とメモリ消費も大きくなります。  
今回は[公式READMEのMemory usage表](https://github.com/ggml-org/whisper.cpp#memory-usage)を参考に、.en付きや量子化モデルを外して
使いやすい3モデルをピックアップしました😤
今回はこの中から選んでダウンロードします。

| モデル名 | 目安 |
| ------- | ------- |
| ggml-large-v3.bin | ダウンロード約3.1GB / 実行時メモリ約3.9GB。16GB以上のRAMがあるPC向け。精度優先で長時間素材を扱うときに。 |
| ggml-medium.bin | ダウンロード約1.53GB / 実行時メモリ約2.1GB。8～16GB RAMで実用的。精度と速度のバランスを取りたいときに。 |
| ggml-small.bin | ダウンロード約0.49GB / 実行時メモリ約0.85GB。8GB未満やノートPCでも動かしやすい。手早く粗い文字起こしを確認したいときに。 |

:::message
どれか1つあれば十分ですが、状況に合わせて切り替えたい場合は3つとも準備しておくと便利です。
さらに余裕があれば`-q5_0`などの量子化モデルも用意しておくと🙆‍♀️
:::

これらをダウンロードしたら、先ほど展開した`FFmpeg`ディレクトリ内に📁`models`ディレクトリを作成し、その中に配置します。

![modelsディレクトリ](/images/articles/whisper/models-directory.png)
*modelsディレクトリを作成*

![モデルファイル](/images/articles/whisper/model-bin-files.png)
*モデルファイル*

:::message
例として3ファイルとも入れていますが、どれか1つ以上あれば大丈夫です👍
:::

👇このような構成です (Windowsの例です)

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

以上でモデルの準備は完了です🎉✨

## 文字起こしの実行

準備が整ったので、いよいよ文字起こしを実行してみます🕺💃  
まずは`FFmpeg`の公式ドキュメントを確認します。

https://ffmpeg.org/ffmpeg-filters.html#whisper-1

上記がWhisperフィルターの使用方法が書かれている箇所ですが、慣れていないと少し分かりづらいかもしれません😥  
幸い、すぐに使えるサンプルが用意されています！

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

上記がそのサンプルです。ここから目的に合わせて調整していきます🫡

変更するのは次の6点です💦💦  
詳細は[公式ドキュメント](https://ffmpeg.org/ffmpeg-filters.html#whisper-1)も参照してください🙏

1. `-itsoffset 01:00:00`
  タイムコード先頭位置指定です、DaVinci Resolveで使用する場合に必要なおまじないです
1. `-i input.mp4`
  文字起こし対象の動画ファイルに変更します。
1. `model=../whisper.cpp/models/ggml-base.en.bin`
  モデルのパスを実際に配置したモデルファイルへ変更します。
1. `:language=en`
  言語設定は自動判別に任せるので削除します。
1. `:queue=3`
  リアルタイム処理ではないのでキューサイズを大きめにします。
1. `destination=output.srt`
  出力先の指定です、ここに出力され、 **同名のファイルが存在する場合上書きされます**。
  **Windowsの場合** はbin内に出来てしまうので、一つ上の階層になるように`../output.srt`とするほうが無難です。  
  (この記事ではそのままにしています)

調整後は以下のようになります。`video.mp4`は文字起こししたいファイル、`ggml-large-v3.bin`は使用したいモデルにそれぞれ置き換えてください。

```bash
ffmpeg -itsoffset 01:00:00 -i video.mp4 -vn -af "whisper=model=../models/ggml-large-v3.bin\
:queue=20\
:destination=output.srt\
:format=srt" -f null -
```

:::message
コマンド作成アプリを用意しました！😤
コマンドの書き換えが少し楽になります
https://mug-lab-3.github.io/ffmpeg-whisper-command-creator/
:::

# 文字起こし実行

では文字起こしを実行してみます✋
ターミナルを起動して`FFmpeg`を展開したディレクトリ内の`bin`ディレクトリに移動し、前章で組み立てたコマンドを実行します  
正常に完了すると、`output.srt`として文字起こし結果が出力されます。

:::details コマンド
```bash
ffmpeg -itsoffset 01:00:00 -i video.mp4 -vn -af "whisper=model=../models/ggml-large-v3.bin\
:queue=20\
:destination=output.srt\
:format=srt" -f null -
```
:::

:::message
**Windows**: ターミナルはbinディレクトリを右クリックして「ターミナルで開く」を選択して開きます
:::

:::message
Macで実行するときは、初回に以下が必要になる場合があります🤔
- Gatekeeperでブロックされたら`xattr -d com.apple.quarantine ./ffmpeg`で解除する
- 実行権限が無いときは`chmod +x ./ffmpeg`を付与する
- `ffmpeg`が見つからないと言われたら`./ffmpeg`のように前に`./`を付ける
:::
![コマンド入力](/images/articles/whisper/exec-command.png)
*コマンド入力*

![実行完了](/images/articles/whisper/done-command.png)
*実行完了*

![文字起こし結果](/images/articles/whisper/output-file.png)
*文字起こし結果*

コマンド実行に慣れていない方向けにbatファイルも用意しました😤  
__Windowsの場合は__ これを実行するだけでOKです！！

Macの方はターミナルでコマンドを実行してください🙏🙏🙏


## Windows用バッチファイル

[run-ffmpeg-whisper.bat](https://github.com/mug-lab-3/ZennDaVinciResolveDocuments/blob/main/images/articles/whisper/run-ffmpeg-whisper.bat)をダウンロードし、`FFmpeg`を展開したディレクトリに置きます。

![batファイルのダウンロード](/images/articles/whisper/download-bat.png)
*batファイルのダウンロード*

![run-ffmpeg-whisper.bat](/images/articles/whisper/put-bat.png)
*run-ffmpeg-whisper.bat*


batファイルの準備ができたら、このbatに文字起こししたい動画をドラッグ&ドロップします。

![ドラッグ&ドロップ](/images/articles/whisper/dad-to-bat.png)
*ドラッグ&ドロップ*


batファイルを正しく配置できていればターミナルが起動し、使用するモデルを聞かれます。modelsディレクトリに置いたモデルが選択肢になります。

![モデル選択](/images/articles/whisper/select-model.png)
*モデル選択*


モデルを選択すると以下のように表示されるので、`Enter`キーを押すと文字起こしが開始されます🚀✨

![文字起こし開始](/images/articles/whisper/ready-to-exec.png)
*文字起こし開始*


しばらく待っていると文字起こしが完了します。
以下のように表示されればOKです🙆‍♀️

![文字起こし完了](/images/articles/whisper/done-exec.png)
*文字起こし完了*


正常に文字起こしが完了すると`srt`ディレクトリが作成され、その中に文字起こし結果ファイルが生成されます🖨️

![srtディレクトリ](/images/articles/whisper/srt-directory.png)
*srtディレクトリ*

![文字起こし結果](/images/articles/whisper/bat-output-file.png)
*文字起こし結果*

# 文字起こし結果の確認

文字起こしが完了すると`srt`ファイルが作成されます。
これは字幕ファイルと呼ばれるテキストファイルで、📝テキストエディタで開けます。

*SRTファイルフォーマット*

```text
テキスト番号
開始時間 --> 終了時間
内容
```
*例*
![srtファイル](/images/articles/whisper/result.png)
*srtファイル*

文字起こし結果は完璧ではないので、多少の誤りは発生します🥺  
気になる場合は✋手作業で修正するか、🤖AIに手伝ってもらいましょう。
どちらの場合でも修正するのは __内容__ の部分だけにしてください。
それ以外を変更すると、他のアプリで読み込めなくなる可能性があります😱

また、変換精度や速度についてはモデルを変えてみたり、`queue`の値を変更してみたりすると
変わってくるので、いろいろ試してみると良いです👍

:::message
テキストの区切り方が不自然に感じられる場合は、`queue=`の値を大きくすると自然な区切りに近づきます(多分🙈)。  
わたしがお試ししたファイルでは20より100の方がきれいに感じました💦💦

👇batファイルの場合は以下を変更します。
![batファイル](/images/articles/whisper/change-queue-bat.png)
*batファイル*
:::

# DaVinci Resolveで読み込み

文字起こし結果の`srt`ファイルは、DaVinci Resolveに読み込んで字幕として設定できます👍

メディアプールに`srt`ファイルをドラッグ&ドロップします。

![srtファイル登録](/images/articles/whisper/add-sub-to-media-pool.png)
*srtファイル登録*

追加された字幕クリップを右クリックして、`Insert Selected Subtitles to...`の`Timline Using Timecode`を選択します。

![タイムラインへの挿入](/images/articles/whisper/insert-subtitle.png)
*タイムラインへの挿入*

![字幕トラック追加](/images/articles/whisper/added-subtitle.png)
*字幕トラック追加*

お疲れさまでした、これで完成です💮🎓💯

# 🐔 おわりに

簡単と言いつつとても長くなってしまいました💦  
この方法のポイントはPythonのインストールやスクリプト作成が不要な点です。
プログラミングの知識がなくても実行できます！！

「これができるなら、文字起こしのためにDaVinci Resolve有料版(DaVinci Resolve Studio)は要らないのでは？」
と思うかもしれませんが、有料版には文字起こし結果と連動したテキストベース編集など💪強力で🏪便利な機能が備わっています。
今回の内容で完全に置き換えられるわけではないのです😤


ちなみに、文字起こしをしたいだけなら👇vibeの方が簡単って聞きました😇
https://thewh1teagle.github.io/vibe/

