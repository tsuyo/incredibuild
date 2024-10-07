# Incredibuild (IB) Windows 質問集
Updated for Version 10

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

## Predictive Execution (PE) のオン・オフの仕方
### オン
Agent Settings > Visual Studio Builds > Advanced > Predicrtive execution (Visual Studio 2010 and higher) > "Enhance throughput using out-of-order tasks spawning" をチェック

### オフ
Agent Settings > Visual Studio Builds > Advanced > Predicrtive execution (Visual Studio 2010 and higher) > "Enhance throughput using out-of-order tasks spawning" をアンチェック

# 管理者向け
## インストール・アップグレード不具合時の送付ファイル
%IB_DIR% は Incredibuild インストールディレクトリ（デフォルトは "C:\Program Files (x86)\Incredibuild"）
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
