## 開発コンテナの起動

- vscode 起動時にコンテナで起動する
- Dev Containers(ms-vscode-remote.remote-containers)が必要
- .devcontainer ディレクトリ内に開発コンテナ適用時の vscode の設定が格納されている
- 開発コンテナ起動時の Docker の設定も内包している
- .vscode ディレクトリにはデバッガーの設定がある
- src ディレクトリに Python のコードを記述する

## 依存関係整理

`pipenv sync` -- dev 以外の依存ライブラリを install する
`pipenv sync --dev` -- 依存ライブラリをすべて install する
`pipenv shell` -- 仮想環境に入る

- Pipfile で依存関係を管理している
- requirements.txt は使用しない

## 構文チェック・整形ツール

- flake8 (.flake8 ファイルに black とバッティングしないよう抑制設定を入れている)
- black
- [参考](https://zenn.dev/yamaden/articles/23d3805fc85d99#flake8)

```
(workspace) root@08693bafdfa0:/workspace# flake8 --version
7.2.0 (mccabe: 0.7.0, pycodestyle: 2.13.0, pyflakes: 3.3.2) CPython 3.13.2 on Linux
(workspace) root@08693bafdfa0:/workspace# black --version
black, 25.1.0 (compiled: no)
Python (CPython) 3.13.2
```
