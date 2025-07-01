# Incredibuild (IB) Windows サポート情報
- Current Version: 10
- %IB_DIR% は Incredibuild インストールディレクトリ（デフォルトは "C:\Program Files (x86)\Incredibuild"）

# 共通
## 古いバージョンのドキュメントとインストーラーの場所
https://docs.incredibuild.com/site_landing/download_docs_center.htm

# 開発者向け
## 詳細なログ付きビルドモニターの取得方法

1. 右下のタスクトレイにある Incredibuild のアイコンを右クリック > Agent Settings > Agent > General > Logging > Logging level: Detailed に設定
2. Incredibuild を使ってビルド
3. 右下のタスクトレイにある Incredibuild のアイコンを右クリック > Build History > 該当の Build をダブルクリック > File > Save Monitor File As... → 名前をつけた *.ib_mon を送付

## 個々のタスクの詳細なログ取得方法
ビルドモニター自体にはタスクごとの詳細なログは保存されないため、下記が必要なケースがあります

1. ビルドモニターを開く
2. タスクを一つ選択し、右クリック > Save Detailed Log...
3. _CPUX.{XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX}.ib_log を保存、送付

## PML ファイルの取得方法
ビルドモニターやログなどで解析が難しい場合、さらに Process Monitor ファイルが必要なケースがあります

1. マイクロソフトの専用ツール Process Monitor を[ダウンロード](https://download.sysinternals.com/files/ProcessMonitor.zip)する
2. ProcessMonitor.zip ファイルを解凍する
3. タスクバーに表示されているすべてのアプリケーションを閉じ（可能であれば）、以下のステップで追加のアクションを取らないようにする
4. Procmon.exe を実行する
5. Edit > Clear Display
6. File > "Capture Events" がチェックされていることを確認する
7. 問題を再現する
8. File > Save in Process Monitor を選択し、ネイティブ PML 形式でログファイルを保存する

## Predictive Execution (PE) のオン・オフの仕方
### オン
Agent Settings > Visual Studio Builds > Advanced > Predicrtive execution (Visual Studio 2010 and higher) > "Enhance throughput using out-of-order tasks spawning" をチェック

### オフ
Agent Settings > Visual Studio Builds > Advanced > Predicrtive execution (Visual Studio 2010 and higher) > "Enhance throughput using out-of-order tasks spawning" をアンチェック

## ビルドが Helper でのみ失敗する時（ビルドモニター上「白いバー」になる時）
- アンチウイルスソフトのスキャン対象フォルダから IB を外す（[System Requirements > Antivirus](https://docs.incredibuild.com/win/latest/windows/system_requirements.html)）
- Agent Settings > Initiator > Advanced > Recovery: Distributed tasks should only fail on local machine をアンチェック、ビルドし原因を確認

## Visual Studio の出力ウィンドウで日本語が文字化けする
- レジストリ `HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Xoreax\IncrediBuild\Builder` 下に `ForceEnglishMSBuildOutput = 0` のエントリーを追加（もしくは値が 1 なら 0 に修正）して再度ビルドを確認

# 管理者向け
## SSL 証明書の使われ方
- Coordinator SSL Certificate（インストール時の名称）
  - Coordinator と Browser の通信暗号化
  - Coordinator と Agent の通信暗号化
- Agent SSL Certificate（インストール時の名称）
  - Agent と Agent の通信暗号化

## SSL 証明書の更新手順（>= IB10.24）
コマンドプロンプト
```
C:\Users\Administrator>cd "C:\Program Files (x86)\Incredibuild\Manager"

C:\Program Files (x86)\Incredibuild\Manager>Manager.exe updateCertificate -c "C:\Users\Administrator\certs\tsuyo-aws-win2022-1.crt" -k "C:\Users\Administrator\certs\tsuyo-aws-win2022-1.key"

Certificate and Key validation passed successfully.
Stopping Incredibuild Services
Services Stopped
Updating Certificate
Certificate copied successfully
Starting Incredibuild Services
Services Started
Certificate updated successfully
```
WSL
```
$ cd "/mnt/c/Program Files (x86)/Incredibuild/Manager"
$ ./Manager.exe updateCertificate -c "$(wslpath -w /mnt/c/Users/Administrator/certs/tsuyo-aws-win2022-1.crt)" -k "$(wslpath -w /mnt/c/Users/Administrator/certs/tsuyo-aws-win2022-1.key)"
```

## ビルドが一部の Helper でしか実行されない時
Coordinator > Settings > Agents > Helper Participation Threshold の設定（特に "Available CPU" を見直す）
- Available CPU は「Helper の CPU リソースが 30% 以上空いていない時、この Helper を利用しない」という意味
- Available CPU のデフォルトは 30%、増やすと Helper が割り当てられる可能性が**低く**なっていく

## インストール・アップグレード不具合時の送付ファイル
- %IB_DIR%\Logs
- %IB_DIR%\Manager\logs
- %TEMP%\IB_Setup_Log*

## ライセンスとビルドグループ設定のバックアップとリストア
### バックアップ
1. Coordinator を停止する（Services > Incredibuild CoordinatorService を右クリック > Stop）
2. インストールフォルダ（デフォルト "C:\Program Files (x86)\Incredibuild"）直下の CoordService.sbd をバックアップ（このファイルにライセンスとビルドグループの情報が保存されている）
3. Coordinator を開始する（Services > Incredibuild CoordinatorService を右クリック > Start）

### リストア
1. Coordinator を停止する（Services > Incredibuild CoordinatorService を右クリック > Stop）
2. インストールフォルダ（デフォルト "C:\Program Files (x86)\Incredibuild"）直下に CoordService.sbd をリストア
3. Coordinator を開始する（Services > Incredibuild CoordinatorService を右クリック > Start）

## Coordinator Service 不具合時の必要データ取得方法

下記手順を実行し、2, 3, 4 のファイルを送付ください

1. CrashDump の取得準備
- C:\\CoordinatorServiceDumpFiles フォルダを作成後、EnableCoordinatorDump.reg を実行

  [EnableCoordinatorDump.reg]
  ```
  Windows Registry Editor Version 5.00

  [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\Windows Error Reporting\LocalDumps\CoordinatorService.exe]
  "DumpFolder"="C:\\CoordinatorServiceDumpFiles"
  "DumpCount"=dword:00000003
  "DumpType"=dword:00000000
  "CustomDumpFlags"=dword:00041826
  ```
- C:\\LicenseServiceDumpFiles フォルダを作成後、EnableLicenseServerDump.reg を実行

  [EnableLicenseServerDump.reg]
  ```
  Windows Registry Editor Version 5.00

  [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\Windows Error Reporting\LocalDumps\LicenseService.exe]
  "DumpFolder"="C:\\LicenseServiceDumpFiles"
  "DumpCount"=dword:00000003
  "DumpType"=dword:00000000
  "CustomDumpFlags"=dword:00041826
  ```

2. CrashDump の収集
- 1 の設定後、実際に Coordinator に問題があった際、"DumpFolder" で指定したフォルダにダンプファイルが生成される

3. ログの収集

- Coordinator
  - C:\Program Files (x86)\Incredibuild\Logs
  - C:\Program Files (x86)\Incredibuild\Manager\logs

- Backup Coordinator（あれば）
  - C:\Program Files (x86)\Incredibuild\Logs
  - （Manager ログはない）

4. Coordinator Persistent Data の収集
- Coordinator
  - C:\Program Files (x86)\Incredibuild\CoordService.sbd
  - C:\Program Files (x86)\Incredibuild\resources\coordinator_service_config.json
  - `xgCoordConsole.exe /ExportStatus=output.xml` の出力（output.xml）

- Backup Coordinator（あれば）
  - C:\Program Files (x86)\Incredibuild\CoordService.sbd.backup
  - C:\Program Files (x86)\Incredibuild\resources\coordinator_service_config.json

## Coordinator の再起動時間の確認方法
1. %IB_DIR%\Logs\CoordinatorService.log の下記ライン
```
grep -a "============= Incredibuild Version" CoordinatorService*.log
[2024-09-24 13:48:51.026] [info] [coordinator_service] [3252] [main.cpp:72] ============= Incredibuild Version 10.17.0 (Build 13843) =============
[....]
```
2. %IB_DIR%\Logs\CoordinatorCore.log の下記ライン
```
$ grep -a "Coordinator ID" CoordinatorCore.log
24-09-2024 13:48:52.317 Coordinator ID: XXXXXXXXXX
[....]
```

## VPN などで Agent の内部 IP と外部向け IP (Routing IP) が変わってしまう場合の対応
Coordinator のレジストリ `Computer\HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Xoreax\Incredibuild\Coordinator` 内にエントリ `Key: UseRoutingIP, Value: 0` を設定する
- Value: 1 (default) → Agent の IP として Routing IP を使う
- Value: 0 → Agent の IP として内部 IP を使う

## Incredibuild 関連のイベントログを抑止する方法（IB10.20 以降）
1. 下記内容の `coordinator_service_config.json` ファイルを作成
```
{
  "logger": {
    "sink": {
      "logToEventViewer": false
    }
  }
}
```
2. `C:\ProgramData\Incredibuild\Coordinator` フォルダを作成（存在しない場合）
3. `1.` のファイルを `2.` のフォルダ以下にコピー (`C:\ProgramData\Incredibuild\Coordinator\coordinator_service_config.json`)
4. Coordinator を再起動

## Incredibuild 各ファイルのバージョンの調べ方
ファイルを右クリック（例: BuildAddInVC17.dll） > Properties > Details > Product version

![Screenshot 2025-01-06 at 20 02 45](https://github.com/user-attachments/assets/e8db1add-31a0-45d5-8f2f-9cd7f5cbf0f0)

## Floating Initiator ライセンスの割り当て状況の確認
[floating-initiator-checker.py](../tools/floating-initiator-checker.py) を利用して、下記を実行して下さい。"Available Floating Initiators" で表示される数がその時点で利用可能な Floating Initiator の数です
```
$ python3 floating-initiator-checker.py %IB_DIR%\LicenseService.log
[2024-12-09 08:16:17.551] Available Floating Initiators: 36
[2024-12-09 08:16:17.559] Available Floating Initiators: 35
[2024-12-09 08:16:17.580] Available Floating Initiators: 35
[....]
```
