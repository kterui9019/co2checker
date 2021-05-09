# co2checker
二酸化炭素を測って通知し鯛

## Setup
### 前提
- LINE Notifyのアクセストークンが必要になります。
- [mh_z19](https://pypi.org/project/mh-z19/)が動く環境での実行を想定しています。
  - `sudo python3 -m mh_z19`が実行できること。
- [pipenv](https://github.com/pypa/pipenv)が必要です。
- (loggingを使う場合)spreadsheet, drive APIのサービスアカウントが必要です。

### リポジトリのクローン・環境変数の設定
```
$ git clone https://github.com/kterui9019/co2checker.git
$ cd co2checker
$ echo "LINE_API_KEY=XXXXXXXXXXXXXX" >> .env
$ echo "SUDO_PASSWD=XXXXXXXX" >> .env
```

### サービスアカウントの認証情報
サービスアカウントの鍵を`service.json`という名前でプロジェクト直下に配備します。

参考
[ラズパイで取得したIoTデータをグーグルスプレッドシートに自動記録](https://jorublog.site/raspi-google-sheet/)

### 依存関係の解決
```
$ pipenv install
```

### 実行
オペレーション名を指定して`pipenv run`を実行します。
```
$ pipenv run check
```

|  operation  |  description  |
| ---- | ---- |
|  check  |  二酸化炭素濃度を測定して、しきい値を超えていればLINE Notifyに通知します。  |
| logging | 二酸化炭素濃度を測定して、日時と値をスプレッドシートに記録します。 |

### UnitTest
```
$ pipenv run test
```
