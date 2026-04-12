---
title: "【DaVinci Resolve】 Reactorへのエフェクト/ツール登録申請方法 【Fusion】"
emoji: "📮"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: [davinciresolve, fusion, reactor]
published: false
---

# 🐥 はじめに

みなさん、こんにちは。[Mug](https://www.youtube.com/channel/UCuhx0M-PBn4qJ-SUKQ6gVaA)です🐼

DaVinci Resolveには`Reactor`という、ユーザーコミュニティによって作成されているパッケージマネージャーがあります
Reactorではコミュニティによって作成されたエフェクトやツールが多数登録されていて、誰でも簡単にインストールして使用することができます
そして、このReactorに登録されているツールは誰でも作成することができ、
手順に従って申請することで、自作のエフェクトやツールをReactorに登録することができるんです！😮

今回はその手順を解説します👍

:::message
この記事では、2026/4/13現在の申請手順で解説しています
:::

# 📦 Reactorとは

Reactorは、[WeSuckLess](https://www.steakunderwater.com/wesuckless/)コミュニティによって運営されている、DaVinci Resolve / Fusion 向けの強力なパッケージマネージャーです。
これを使うことで、ユーザーは複雑なインストール手順を意識することなく、ボタン一つでエフェクトやツールを導入・管理できるようになります✨

:::message alert
Reactorは、DaVinci Resolveの公式ツールではありません
:::

# 📝 申請に必要なもの

登録にあたって、まずは以下の準備が必要です☝️

1. [WeSuckLess](https://www.steakunderwater.com/wesuckless/)コミュニティのアカウント
2. Reactor (Atomizer)
3. 登録したいエフェクト/ツール本体 (.fuse, .setting, .lua など)
4. Atomパッケージファイル (.atom)
5. 解説用素材
   - 掲示板に投稿するためのスクリーンショットやGIF、動画など

# 1. WeSuckLessへのユーザー登録

[WeSuckLess](https://www.steakunderwater.com/wesuckless/)にアクセスして、アカウントを作成します


1-1 右上のチェックマークをクリックしてユーザー登録
![Register](/images/articles/reactor-submission/register-wsl.png)
_Register_

1-2 利用規約をよく読み同意する

![Agree terms](/images/articles/reactor-submission/agree-terms.png)
_Agree terms_

1-3 ユーザー情報を入力する

必要事項を記載し、最後のクイズを解いてsubmitします

![Registration 1](/images/articles/reactor-submission/registration1.png)
![Registration 2](/images/articles/reactor-submission/registration2.png)
_Registration_

![Registration complete](/images/articles/reactor-submission/registration-complete.png)
_Registration complete_

1-4 アクティベーション

登録したメールアドレスにメールが届くので、メール内のリンクをクリックしてアクティベーションします

:::message
メールが届かない場合は、迷惑メールフォルダを確認してください👀
:::

![Activation](/images/articles/reactor-submission/wsl-activation.png)
_Activation_

1-6 ログイン確認

右上の電源ボタンをクリックして、登録したユーザー名、パスワードでログインできることを確認します
右上のアイコンが変化して、色々出ていればログイン成功です🎉

![Login 1](/images/articles/reactor-submission/login-wsl1.png)
![Login 2](/images/articles/reactor-submission/login-wsl2.png)
![Login 3](/images/articles/reactor-submission/logged-in-wsl.png)
_Logged in_

# 2. Reactor (Atomizer)のインストール

本来は必須ではないですが、Reactorに含まれる`Atomizer`が、Atomファイルを作ったり
登録申請をするうえでとても便利なのでインストールしておきます




# 🛠️ 1. .atomファイルの準備

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
