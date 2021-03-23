# Sirene コントロールパネル

このアプリケーションは、リコーダー自動演奏装置「Sirene」を操作するためのものです。

## 目次
- [Sirene コントロールパネル](#sirene-コントロールパネル)
  - [目次](#目次)
  - [インストール](#インストール)
  - [起動](#起動)

## インストール
必要なソフトウェアは以下の通りです：

- Python 3.8以降
  - poetry
- node 15.10.0以降

まず、リポジトリをクローンします。その際に、`--recursive`オプションを付けてください。
```sh
$ git clone --recursive https://github.com/frodo821/sirene-server sirene
$ cd sirene
```

つぎに、フロントエンドのビルドをします。
```sh
$ cd frontend
$ npm install
$ npm run build
$ cd ..
```

最後に、サーバーの依存ライブラリのインストールをします。
```sh
$ poetry install
```

これで準備は完了です。

## 起動
起動には`uvicorn`というASGIサーバーを利用します。
これは、先のインストールステップでインストールされるものです。

以下のコマンドで起動できます。
```sh
$ poetry run uvicorn app:app
```

起動したのち、ブラウザで`http://localhost:8000`を開くとアプリを使うことができます。
