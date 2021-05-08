# co2checker
二酸化炭素を測って通知し鯛

## Setup
### 前提
- LINE Notifyのアクセストークンが必要になります。
- [mh_z19](https://pypi.org/project/mh-z19/)が動く環境での実行を想定しています。
- [pipenv](https://github.com/pypa/pipenv)が必要です。

### リポジトリのクローン・環境変数の設定
```
$ git clone https://github.com/kterui9019/co2checker.git
$ cd co2checker
$ echo "LINE_API_KEY=XXXXXXXXXXXXXX" >> .env
```

### 依存関係の解決
```
$ pipenv install
```
