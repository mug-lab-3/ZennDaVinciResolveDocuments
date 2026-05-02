---
title: "【DaVinci Resolve】 Reactorへのエフェクト/ツール登録申請方法 【Fusion】"
emoji: "📮"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: [davinciresolve, fusion, reactor]
published: false
---

# 🐥 はじめに

みなさん、こんにちは [Mug](https://www.youtube.com/channel/UCuhx0M-PBn4qJ-SUKQ6gVaA)です🐼

DaVinci Resolveには`Reactor`という、ユーザーコミュニティによって作成されているパッケージマネージャーがあります
Reactorではコミュニティによって作成されたエフェクトやツールが多数登録されていて、誰でも簡単にインストールして使用することができます
そして、このReactorに登録されているツールは誰でも作成することができ、
手順に従って申請することで、自作のエフェクトやツールをReactorに登録することができるんです！！

今回はその、登録申請手順を紹介します👍

:::message
この記事では、2026/4/27現在の申請手順で解説しています
:::

# 🔗 参考情報

この記事は下記の内容を日本語で分かりやすくまとめたものです 💦
より詳細な情報は下記リンク先を参照ください 👀

- [Submission Guidelines](https://www.steakunderwater.com/wesuckless/viewtopic.php?t=1798/)
- [Atom Packages Documentation](https://www.steakunderwater.com/wesuckless/viewtopic.php?t=1799)
- [Atomizer Documentation](https://www.steakunderwater.com/wesuckless/viewtopic.php?t=1811)
- [GitLab Reactor: Creating Atom Packages](https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Docs/Creating-Atom-Packages.md#creating-atom-packages)

# 📋 事前準備

事前に下記を準備する必要があります
特に1の登録したいエフェクトやツールは不備があると手戻りが発生したり
Reactor運営に迷惑をかけてしまう可能性があるので
しっかりと準備(確認)してから申請しましょう 👀

1. 登録したいエフェクト/ツールの準備
2. [WeSuckLessへの登録](https://zenn.dev/muglab3/articles/39490b884d0bec)
3. [Reactorのインストール](https://zenn.dev/muglab3/articles/5cbf32f87031c4)
4. 紹介用のスクリーンキャプチャや動画
5. 紹介用の**英語**での説明文

# 1. Atom Packageの作成

申請するためにはエフェクトやツールのまとまりを`Atom Package`という形式で作成する必要があります
これは、Reactorに含まれる`Atomizer`というツールを使うと簡単に作成できるので
この記事では`Atomizer`を使って`Atom Package`を作成する手順を紹介します 👍

## 1-1 Atomizerの起動

DaVinci Resolveを起動し、メニューバーの 
`Workspace > Scripts > Comp > Reactor > Tools > Atomizer` を選択して
Atomizerを起動します
起動したら`Crate New Atom Package`を選択します

![Luanch Atomizer](/images/articles/reactor-submission/launch-atomaizer.png)
_Luanch Atomizer_


![Create New Atom Package](/images/articles/reactor-submission/crate-new-atom-package.png)
_Create New Atom Package_


## 1-2. Workspaceの準備

まず初めに`Wroking Directory`と`Package Name`を設定します

`Wroking Directory`は、作成するパッケージを保存する場所で、任意のフォルダでOKです
その中にPackage用のフォルダが作られます

`Package Name`は申請するパッケージのIDとなります
`com`から初めて所属名,ツール/エフェクト名と`.`でつなぎます
内容に制限はありませんが、英語です
サブグループが必要ならばツール/エフェクト名の前に追加します
よくわからなければ他のエフェクトを参考にしましょう ☝️

入力が終わったら`Continue`をクリックします

:::message alert
Package Nameは一度申請したあとは変更できません
:::  

`Package Name`は、作成するパッケージの名前です
今回は`My Tool`というパッケージを作成するので、`Package Name`を`My Tool`に設定します

![Set Workspace Directory & Package Name](/images/articles/reactor-submission/atom-input-work-dir.png)
_Set Workspace Directory & Package Name_

![Package ID](/images/articles/reactor-submission/atom-id.png)
_Package ID_

## 1-3. Package情報の作成

Packageに関する必要情報を入力していきます

![Package Information](/images/articles/reactor-submission/atom-input-pkg-info.png)
_Package Information_

### **Author** 

作者名を入力します、英語ならば何でも良いです

### **PackageName** 

ツール/エフェクト名を入力します
(自動的に入力されているはず)

### **Category** 

カテゴリを設定します、任意のものを選択
わからなければ`Reactor`を起動し、他のツールやエフェクトを見ながら
それっぽいものを設定します 

### **Version** 

バージョンです
`1.0`のような形式(浮動小数点数)で入力します

### **Date** 

**現在のバージョン**のリリース日を入力します
いつでも良いです
`Today`ボタンを押せば現在日時が入力されます


### **Donation URL / Donation Amount** 

寄付受付URLと寄付希望額を入力します
ここは任意です、不要な場合は`空`に設定します
この欄に`空`以外の設定を行うと、そのツール/エフェクトの
インストールやアップデート時に、ユーザーへ寄付を募っている旨のダイアログが表示されるようになります

寄付設定を行う場合は、PayPal等で別途送金用のURLを取得し、`Donation URL`に入力します
`Donation Amount`には`$5.00 USD`のように寄付希望額と単位を入力します

### Description

ツール/エフェクトの説明文を入力します
すべて英語でします
htmlタグが使用できるので、読みやすいように整形します

この内容がReactor各ツール/エフェクトのページに記載されます

:::message
Reactorでの表示欄は狭いので、あまりに長文だと読みにくいです
適度な長さで記載しましょう ✍️
:::

![Package Description](/images/articles/reactor-submission/reactor-description.png)
_Package Description_


## 1-4. ツール/エフェクトの配置

パッケージフォルダに実際のツールやエフェクトを配置します
`Wroking Directory`の中に、`com`から始まるパッケージ名フォルダが作成されているので
そのなかに、`Fusion`フォルダ内と**同じ構造になるように**ツールやエフェクトのファイルを配置します
このときブランド名フォルダを作成し、その中に配置するようにすると
他の人のエフェクトやツールと混ざらなくなるのでおすすめです 👍

:::message
`Atomizer`はまだ閉じないでください 🖐️
:::

![Tool/Effect files](/images/articles/reactor-submission/atom-resource-dirs.png)
_Tool/Effect files_

:::message
`Fusion`フォルダとは下記のことです

| OS | Path |
| :--- | :--- |
| Windows | C:\ProgramData\Blackmagic Design\DaVinci Resolve\Support\Fusion |
| Mac | ~/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion |
| Linux | ~/.local/share/DaVinciResolve/Fusion |
:::

## 1-5. Deploy欄への反映

ツールやエフェクトファイルを配置したら`Atom`パッケージに反映させます
右下にある🔄️シンクボタンを押します
正しく配置できていれば`Deploy`の部分に反映されます
`Deploy`に表示されたことを確認し、`Save Atom`を押して`.atom`ファイルに保存します

![Add resources to deploy](/images/articles/reactor-submission/atom-sync-resources.png)
_Add resources to deploy_


![Save to Atom Package file](/images/articles/reactor-submission/atom-save-atom.png)
_Save to Atom Package file_

## 1-6. 内容の確認

`View Raw Text`ボタンを押し、`.atom`ファイルの内容を確認します
パッケージ情報として入力した内容が反映されていない場合は
`Save Atom`を押してから再度確認します

![View raw text](/images/articles/reactor-submission/atom-view-raw-text.png)
_View raw text_ 

![Raw text window](/images/articles/reactor-submission/atom-raw-text-window.png)
_Raw text window_ 

## 1-7. AtomパッケージのZip化

申請用にパッケージフォルダをZip化します
`com.xxxx.yyy`のフォルダごと`zip`として圧縮してください

![Package folder](/images/articles/reactor-submission/atom-resource-dirs.png)
_Package Folder_




# 1. .atomファイルの準備

Reactorでは `.atom` という形式のファイルでパッケージ情報を管理します。
中身はLuaのテーブル形式のようなテキストファイルで、ツールの名前、バージョン、作者名、カテゴリなどを記述します。

![Atom file sample placeholder](/images/articles/reactor-submission/atom-sample.png)
_`.atom` ファイルの記述例_

後ほど、具体的なテンプレートなどを追記する予定です💪

# 📮 2. 申請の流れ

実際の申請は、WeSuckLessのフォーラムを通じて行います。

## 2.1 WeSuckLessへの登録

まだアカウントを持っていない場合は、[WeSuckLess Forums](https://www.steakunderwater.com/wesuckless/) でアカウントを作成しましょう。

## 2.2 申請トピックの作成

1. フォーラム内の **"Reactor Submissions"** セクションへ行きます。
2. 新しくトピックを作成します。
3. トピックの内容には、ツールの機能説明、スクリーンショット等を記載します。
4. **重要：** 作成した `.atom` ファイルと、ツールを同梱した `.zip` ファイルをトピックに添付します。

![Reactor Submission Form Placeholder](/images/articles/reactor-submission/forum-sample.png)
_掲示板での投稿イメージ_

# ⏳ 審査と公開

投稿すると、Reactorの管理者の方々が内容をチェックしてくれます。
修正が必要な場合はリプライでアドバイスがもらえます。
問題がなければ、数日〜数週間でReactorのメインリポジトリに取り込まれ、世界中のユーザーがインストールできるようになります🎉🎉🎉

# 🐔 おわりに

Reactorに自分のツールが掲載されるのは、開発者としてとても嬉しい瞬間です😊
コミュニティへの貢献にもなりますし、フィードバックをもらうことでツールの改善にも繋がります。

この記事はまだ下書き段階ですが、後ほど各ステップのより詳細なテクニックなどを追記して仕上げていく予定です！

この記事が参考になった場合は、ぜひコメントやSNSでシェアしていただけると励みになります。
ではまた！🐼
