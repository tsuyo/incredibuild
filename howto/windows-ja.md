# Incredibuild (IB) 10 質問集

## 詳細なログ付きビルドモニターの取得方法

1. 右下のタスクトレイにある Incredibuild のアイコンを右クリック > Agent Settings > Agent > General > Logging > Logging level: Detailed に設定
2. Incredibuild を使ってビルド
3. 右下のタスクトレイにある Incredibuild のアイコンを右クリック > Build History > 該当の Build をダブルクリック > File > Save Monitor File As... → 名前をつけた *.ib_mon を送付

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
