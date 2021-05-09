# co2checker
二酸化炭素を測って通知し鯛

## Setup
### 前提
- LINE Notifyのアクセストークンが必要になります。
- [mh_z19](https://pypi.org/project/mh-z19/)が動く環境での実行を想定しています。
  - `sudo python3 -m mh_z19`が実行できること。
- [pipenv](https://github.com/pypa/pipenv)が必要です。

### リポジトリのクローン・環境変数の設定
```
$ git clone https://github.com/kterui9019/co2checker.git
$ cd co2checker
$ echo "LINE_API_KEY=XXXXXXXXXXXXXX" >> .env
$ echo "SUDO_PASSWD=XXXXXXXX" >> .env
```

### 依存関係の解決
```
$ pipenv install
```

### 実行
main.pyの第一引数にオペレーション名を入力して実行します。
```
$ python src/main.py check
```

|  operation  |  description  |
| ---- | ---- |
|  check  |  二酸化炭素濃度を測定して、しきい値を超えていればLINE Notifyに通知します。  |
