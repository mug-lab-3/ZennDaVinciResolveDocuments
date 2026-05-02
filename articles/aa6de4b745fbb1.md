---
title: "【DaVinci Resolve】 Reactorへのツール/エフェクト登録申請方法 【Fusion】"
emoji: "📮"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: [davinciresolve, fusion, reactor]
published: true
---

# 🐥 はじめに

みなさん、こんにちは [Mug](https://www.youtube.com/channel/UCuhx0M-PBn4qJ-SUKQ6gVaA)です🐼

DaVinci Resolveには`Reactor`という
ユーザーコミュニティによって運営されている便利な🧰パッケージマネージャーがあります
`Reactor`には、👥コミュニティによって作成されたツール/エフェクトが多数登録されていて
誰でも簡単にインストールして使用することができます
そして、この`Reactor`に登録されているツールは誰でも作成可能で
手順に従って申請すれば
自作のツール/エフェクトを`Reactor`に登録できちゃうんです！！😆👍

今回はその、登録申請手順を紹介します😤

:::message
この記事では、2026/4/27現在の申請手順で解説しています
:::

# 🔗 参考情報

この記事は下記の内容を日本語で分かりやすくまとめたものです
より詳細な情報は下記リンク先を参照ください👀

- [Submission Guidelines](https://www.steakunderwater.com/wesuckless/viewtopic.php?t=1798/)
- [Atom Packages Documentation](https://www.steakunderwater.com/wesuckless/viewtopic.php?t=1799)
- [Atomizer Documentation](https://www.steakunderwater.com/wesuckless/viewtopic.php?t=1811)
- [GitLab Reactor: Creating Atom Packages](https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Docs/Creating-Atom-Packages.md#creating-atom-packages)

# 📋 事前準備

事前に下記を準備する必要があります
特に「1. 登録したいツール/エフェクトの準備」は、内容に不備があると手戻りが発生したり
Reactor運営の方々に迷惑をかけてしまう可能性があるので🥺
しっかりと準備(確認)してから申請しましょう

:::message
**【💡 申請前のチェック】**
似たような機能を持つツール/エフェクトが**すでにReactorに登録されていないか**事前に確認しておきましょう！
もし既に似たようなツールがある場合は、「既存のツールとはどこが違うのか（差別化ポイント）」を説明できるように準備しておくとスムーズです👍
:::

1. 登録したいツール/エフェクトの準備
2. [WeSuckLessへの登録](https://zenn.dev/muglab3/articles/39490b884d0bec)
3. [Reactorのインストール](https://zenn.dev/muglab3/articles/5cbf32f87031c4)
4. 紹介用のスクリーンキャプチャや動画
5. 紹介用の説明文

:::message alert
**やりとりや入力はすべて英語です！**
申請先のWeSuckLessは英語圏のコミュニティなので
フォーラムへの投稿はもちろん、作成するパッケージ内の名前や説明文など
**すべて英語**で入力・やりとりする必要があります
🌍翻訳ツール等を活用して準備を進めましょう！
:::

# 1. Atom Packageの作成

申請するためには
ツール/エフェクトのまとまりを`Atom Package`という形式で作成する必要があります
これは、Reactorに含まれる`Atomizer`というツールを使うと簡単に作成できるので
この記事では`Atomizer`を使って`Atom Package`を作成する手順を紹介します👍

## Atomizerの起動

DaVinci Resolveを起動し、メニューバーの 
`Workspace > Scripts > Comp > Reactor > Tools > Atomizer` を選択して
Atomizerを起動します
起動したら`Create New Atom Package`を選択します

![Launch Atomizer](/images/articles/reactor-submission/launch-atomaizer.png)
_Launch Atomizer_


![Create New Atom Package](/images/articles/reactor-submission/crate-new-atom-package.png)
_Create New Atom Package_


## Workspaceの準備

まず初めに`Working Directory`と`Package Name`を設定します

`Working Directory`は、作成するパッケージを保存する場所で
任意のフォルダで🙆‍♀️OKです、その中にPackage用のフォルダが作られます

`Package Name`は申請するパッケージの`ID`となります
`com`から始めて、所属名やツール/エフェクト名などを`.`でつなぎます
サブグループが必要ならば、ツール/エフェクト名の前に追加します
よくわからなければ他のエフェクトを参考にしましょう☝️

入力が終わったら`Continue`をクリックします

:::message alert
Package Name (Package ID) は一度申請したあとは変更できません
私はtypoしたまま申請してしまいました😭
気をつけましょう
:::  

![Set Workspace Directory & Package Name](/images/articles/reactor-submission/atom-input-work-dir.png)
_Set Workspace Directory & Package Name_

![Package ID](/images/articles/reactor-submission/atom-id.png)
_Package ID_

## Package情報の作成

Packageに関する必要情報を入力していきます✒️

![Package Information](/images/articles/reactor-submission/atom-input-pkg-info.png)
_Package Information_

**【 Author 】**

作者名を入力します
任意の名前でOKです

**【 PackageName 】**

ツール/エフェクト名を入力します
(自動的に入力されているはず👀)

**【 Category 】**

カテゴリを設定します
任意のものを選択すれば良いですが
わからなければ`Reactor`を起動して
他のツール/エフェクトを参考にしながら、それっぽいものを設定しましょう🧐

**【 Version 】**

バージョンです
`1.0`のような形式で入力します

**【 Date 】**

**現在のバージョン**のリリース日を入力します
いつでも良いです、`Today`ボタンを押せば現在日時が入力されます


**【 Donation URL / Donation Amount 】**

寄付受付URLと寄付希望額を入力します
ここは任意です
不要な場合は`空`に設定します
この欄に`空`以外の設定を行うと、そのツール/エフェクトの
インストールやアップデート時に
ユーザーへ寄付を募っている旨のダイアログが表示されるようになります

寄付設定を行う場合は、PayPal等で別途送金用のURLを取得し
`Donation URL`に入力します
`Donation Amount`には`$5.00 USD`のように寄付希望額と単位を入力します

**【 Description 】**

ツール/エフェクトの説明文を入力します
HTMLタグが使用できるので、読みやすいように整形します

この内容がReactorの各ツール/エフェクトのページに記載されます

:::message
Reactorでの表示欄は狭いのであまりに長文だと読みにくいです
適度な長さで記載しましょう️️✒️
:::

![Package Description](/images/articles/reactor-submission/reactor-description.png)
_Package Description_


## ツール/エフェクトの配置

パッケージフォルダに実際のツール/エフェクトを配置します
`Working Directory`の中に、`com`から始まるパッケージ名フォルダが作成されているので
そのなかに、`Fusion`フォルダ内と **同じ構造になるように** ツール/エフェクトのファイルを配置します
このときブランド名フォルダを作成し、その中に配置するようにして
他の人のツール/エフェクトと混ざらないようにします


![Tool/Effect files](/images/articles/reactor-submission/atom-resource-dirs.png)
_Tool/Effect files_

:::message
`Fusion`フォルダとは以下のことです

| OS | Path |
| :--- | :--- |
| Windows | C:\ProgramData\Blackmagic Design\DaVinci Resolve\Support\Fusion |
| Mac | ~/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion |
| Linux | ~/.local/share/DaVinciResolve/Fusion |
:::

## Deploy欄への反映

ツール/エフェクトファイルを配置したら`Atom`パッケージに反映させます
右下にある🔄️シンクボタンを押します
正しく配置できていれば`Deploy`の部分に反映されます
`Deploy`に表示されたことを確認し、`Save Atom`を押して`.atom`ファイルに変更を保存します

![Add resources to deploy](/images/articles/reactor-submission/atom-sync-resources.png)
_Add resources to deploy_


![Save to Atom Package file](/images/articles/reactor-submission/atom-save-atom.png)
_Save to Atom Package file_

## 内容の確認

`View Raw Text`ボタンを押し、`.atom`ファイルの内容を確認します
パッケージ情報として入力した内容が反映されていない場合は
`Save Atom`を押してから再度確認します

:::message
`Atomizer`はまだ閉じないでください🖐️
:::

![View raw text](/images/articles/reactor-submission/atom-view-raw-text.png)
_View raw text_ 

![Raw text window](/images/articles/reactor-submission/atom-raw-text-window.png)
_Raw text window_ 

## AtomパッケージのZip化

申請用にパッケージフォルダをZip化します
`com.xxxx.yyy`のフォルダごと`zip`として圧縮してください

![Package folder](/images/articles/reactor-submission/atom-resource-dirs.png)
_Package Folder_

![Zipped Package](/images/articles/reactor-submission/atom-zipped.png)
_Zipped Package_


# 📮 2. Reactor登録申請

Reactorへの登録申請はWeSuckLessのフォーラムを通じて行います

## Topicの作成

[Reactor Submissions](https://www.steakunderwater.com/wesuckless/viewforum.php?f=33)のページにアクセスして
新しいTopicを作成しましょう✨

![New Topic Button](/images/articles/reactor-submission/wsl-new-topic.png)
_New Topic Button_ 

## Templateの挿入

`Atomizer`の`Copy BB Code`ボタンをクリックし
topicに記載するテンプレートをコピーします
コピーができたら
まずはそのままtopicのdescriptionに貼り付けてしまいましょう

:::message
無事にテンプレートを貼り付けられたら、`Atomizer`はもう閉じてしまって🙆‍♀️OKです
:::

![Copy BB Code](/images/articles/reactor-submission/atom-copy-bbcode.png)
_Copy BB Code_ 

![Insert Template](/images/articles/reactor-submission/wsl-insert-template.png)
_Insert Template_ 

## 必要事項の入力

Topicタイトル、本文を入力していきます
よくわからなかったら[私が申請した内容](https://www.steakunderwater.com/wesuckless/viewtopic.php?t=8618)を参考にしてください

**【 Topic prefix 】**

新規申請を意味するタグ、`[SUBMISSION]`を選択します

**【 Subject 】**

`Topic prefix`で選択したタグが自動的に入力されるので
その後にツール/エフェクト名や、内容を表す件名を入力します

**【 Description 】**

先ほど貼り付けた`BBCode`を整形していきます
`<XXXX here>`と書かれているところはプレースホルダーなので
実際の内容に置き換えていきます

**【 📝 説明文（Description）の入力 】**

`<Write a Description Here>` の部分を消して、説明文を入力します。
ここはフォーラムのトピックの1行目になる部分です！
いきなりツールの説明に入るのではなく、まずは簡単な挨拶をして「新しいツールを作ったのでReactorに登録したいです！」という目的をしっかり伝えましょう👋
続けて、ツールの概要やアピールポイント、使い方などを記載します

![Write description](/images/articles/reactor-submission/wsl-description.png)
_Write description_ 

**【 🖼️ スクリーンショットの添付 】**

`<Attach Your Screenshot Image Here>` の部分を消して、ツール/エフェクトのスクリーンショット（または動画リンク）を添付します
下部にある`attachments`ボタンから添付ファイルをアップロードすることができます
アップロードすると`description`欄の**カーソル位置**に画像タグが挿入されるので
画像を挿入したい位置にカーソルを合わせてから`addfiles`ボタンをクリックしましょう
:::message alert
**添付ファイルのサイズに注意！**
巨大なファイルは🙅‍♀️NGなので、ファイルサイズは可能な限り軽量化しておきましょう！
:::

:::message
自動挿入されるAltテキストはファイル名になります
わかり易い内容に変更しましょう
特に日本語ファイル名の場合、Altテキストは必ず変更しましょう
:::

![Attachment button](/images/articles/reactor-submission/wsl-upload-attachments.png)
_Attachment button_ 

![Insert attachment](/images/articles/reactor-submission/wsl-insert-attachments.png)
_Insert attachment_ 

**【 🗑️ 変更履歴（Changelog）の削除 】**

`Changelog` （更新履歴）を記載する部分ですが
通常、最初のリリースでは記載が不要なので
この部分はプレースホルダーごと削除してしまいましょう🗑️

![Remove changelog](/images/articles/reactor-submission/wsl-remove-changelog.png)
_Remove changelog_ 

**【 ⚠️ Atom File Contentsの確認 】**

`Atom File Contents` の部分には、`Atomizer`で作成した内容が記載されています
ここはフォーマットの一部なので、🙅‍♀️**変更しないようにしましょう**

![Atom File Contents](/images/articles/reactor-submission/wsl-atom-file-contents.png)
_Atom File Contents_ 

**【 📦 Zipファイルの添付 】**

`<Attach Your Zipped Atom Package Here>` の部分を消して、zip化したAtomパッケージファイルを添付します
スクリーンショットと同様に
カーソルを合わせた状態で`addfiles`ボタンをクリックし
zipファイルをアップロードします

![Attach atom pkg](/images/articles/reactor-submission/wsl-attach-atom-pkg.png)
_Attach atom pkg_ 

![Insert zipped atom package](/images/articles/reactor-submission/wsl-upload-zipped-atom-pkg.png)
_Insert zipped atom package_ 

## Preview

すべての入力が終わったら`Preview`ボタンをクリックして表示を確認します
問題があれば入力し直してpreviewを繰り返します


![Topic Preview](/images/articles/reactor-submission/wsl-topic-preview.png)
_Topic Preview_

## Submit

表示に問題がなければ、いよいよ`Submit`ボタンをクリックしてトピックを投稿します
これでReactorへの登録申請は完了です！お疲れ様でした🎉

![Submit Topic](/images/articles/reactor-submission/wsl-submit-topic.png)
_Submit Topic_


# 3. ⏳ 審査と公開

Topicを`SUBMISSION`で投稿すると
Reactorの管理者の方々が内容をチェックしてくれます
通常は数日ほどで見てもらえますが、専業ではないので気長に待ちましょう🙂‍↕️
問題がなければReactorのリポジトリに取り込まれ
世界中のユーザーがインストールできるようになります🎉🎉🎉

:::message
**【💡 今後のアップデートに向けて】**
今回作成した`Working Directory`（作業フォルダ）は、後日ツールをバージョンアップする際にもそのまま使用します！
「申請が終わったから」と捨ててしまわずに、開発用フォルダとして大切に保管しておきましょう📦
:::

# 🐔 おわりに

自分が作ったツールがReactorに掲載されるのは
開発者としてとても嬉しい瞬間ですよね😊
コミュニティへの貢献にもなりますし
フィードバックをもらうことでツールの改善にも繋がります

この記事を参考に、ぜひ皆さんもReactorへの登録に挑戦してみてください！！
