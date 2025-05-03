# Sirene コントロールパネル

このアプリケーションは、リコーダー自動演奏装置「Sirene」を操作するためのものです。

> [!IMPORTANT]
> このアプリケーションは現在のところWindows上でしか動作しません。 
> WSLとの互換性もありません。注意してください。

## 目次
1. [Sirene コントロールパネル](#sirene-コントロールパネル)
   1. [目次](#目次)
   2. [インストール](#インストール)
   3. [起動](#起動)
   4. [MIDIファイルを配置するディレクトリ](#midiファイルを配置するディレクトリ)
   5. [設定について](#設定について)
      1. [experimentals](#experimentals)
      2. [frontend](#frontend)
      3. [midi\_dir](#midi_dir)
      4. [time\_resolution](#time_resolution)

## インストール
必要なソフトウェアは以下の通りです：

- uv
  - [インストール方法](https://docs.astral.sh/uv/getting-started/installation/)
- node 15.10.0

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
$ uv sync
```

これで準備は完了です。

## 起動
起動には`uvicorn`というASGIサーバーを利用します。
これは、先のインストールステップでインストールされるものです。

以下のコマンドで起動できます。
```sh
$ uv run main.py
```

起動コマンド実行後、2秒ほど待つとブラウザが自動で立ち上がります。

## MIDIファイルを配置するディレクトリ

MIDIファイルは、このリポジトリをクローンしたディレクトリの直下にある`midis`ディレクトリの中に配置してください。
上記のインストールステップで最初にいたディレクトリが`C:\Users\frodo`だとすると、MIDIファイルを配置するディレクトリは`C:\Users\frodo\sirene\midis`になります。

このディレクトリは、リポジトリをクローンした段階で作られるため、新しく作る必要はありません。
また、最初から`midis`の中に入っている`.gitkeep`という名前の空ファイルを削除する必要はありません。

## 設定について
サーバーの初回起動後、このファイル(`README.md`)と同じディレクトリに `config.yml` という名前で設定ファイルが生成されます。
デフォルトの設定は以下のとおりです。

```yaml
experimentals:
  debugging_devices: 0
  next_gen_arduino_driver: true
frontend:
  base_path: <project_root>/frontend/public
midi_dir: <project_root>/midis
time_resolution: 128
```

それぞれの設定内容について説明します。

### experimentals
- `debugging_devices`: いくつデバッグ用のデバイスを使用するか指定します。`0`以上の整数を受け入れます。デフォルトは`0`で、デバッグ用のデバイスは使用しません。
- `next_gen_arduino_driver`: 新しいArduinoドライバを使用するかどうかを指定します。`true`または`false`を受け入れます。デフォルトは`true`で、新しいArduinoドライバを使用します。

これらのArduinoドライバは、`arduino`ディレクトリに格納されています。このディレクトリには、スケッチが3つ格納されています。

- `driver`: 簡易版のドライバです。Arduinoと接続されたシリアルポートを使って、ASCIIで送信された数値を受け取ります。
- `driver_nexgen`: より高機能なドライバです。Arduinoと接続されたシリアルポートを使って、2バイト単位のコマンド列を受け取ります。
- `dutyTester`: 電磁弁のデューティー比を調整するためのスケッチです。Arduino IDEのシリアルモニタを利用して最適なデューティー比を探索することができます。

### frontend
- `base_path`: フロントエンドの静的ファイルが格納されているディレクトリのパスを指定します。デフォルトは`<project_root>/frontend/public`です。フロントエンドアプリケーションを別の場所に配置した場合は、ここを変更してください。

### midi_dir
この設定は、MIDIファイルを配置するディレクトリのパスを指定します。デフォルトは`<project_root>/midis`です。MIDIファイルを別の場所に配置した場合は、ここを変更してください。

### time_resolution
この設定は、時間解像度を指定します。デフォルトは`128`で、これは1/128秒を意味します。ただしWindowsの仕様上、短い時間に設定しても時間精度は上がりません。
