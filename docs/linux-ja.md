# Incredibuild (IB) Linux サポート情報
Updated for Version 4

# 開発者向け
## プロファイルの args と type の組み合わせ
- “exclude_args” は type=“local_only” でのみ使用可能です
  - "exclude_args" 内に定義された引数を持つプロセスは “allow_remote” となります
- "include_args" は type="intercepted" でのみ使用可能です
  - "include_args" 内に定義された引数を持つプロセスは "intercepted" となり、それ以外のプロセスは "local_only" となります

# 管理者向け
## IB Cloud 利用時 Helper が割り当てられない問題が起こった場合の解析手順

1. ロギングを有効にしておく（次回問題発生に備えて）
```
$ sudo /opt/incredibuild/management/set_debug_level.sh coordinator info
```
このコマンドの一環で Coordinator が自動的に再起動されます。これによるパフォーマンスへの影響はありませんが 10GB ほどディスク領域を余分に使います。

2. 問題が実際に発生した時、以下のコマンドを実行する
```
$ sudo /opt/incredibuild/management/ib_dump_process $(pidof ib_coordinator)
```
このコマンドを実行すると /etc/incredibuild/log/ib_coordinator_<pid>.crash.log.tgz が作成されます。これを送付ください。
この後 Coordinator Service を再起動ください
```
sudo /opt/incredibuild/etc/init.d/incredibuild restart
```
この段階で Coordinator が Helper を利用できる（問題が解決している）かどうかご確認ください。そうでない場合 IB Cloud を "pause and delete" と "start" して下さい。また下記のログを送付ください。
- /etc/incredibuild/log/ib_coorinator.log
- /etc/incredibuild/log/ib_coordinator.log.1
- /etc/incredibuild/log/ib_cloud.log
- /etc/incredibuild/log/ib_cloud.log.1 /etc/incredibuild/log/ib_coordinator_<pid>.crash.log.tgz

## Coordinator ID の調べ方
```
$ sudo /opt/incredibuild/bin/sqlite3 /etc/incredibuild/db/incredibuildCoordinatorReport.db "select LicenseId from LicenseDesc"
```

## IBC 接続用の Secret の場所（Activate 後のタイムスタンプが更新されているかチェック）
```
$ ls -l /opt/incredibuild/settings/secret
```

## 共有（リモート）ビルドキャッシュを Read Only で利用する方法
[ビルドキャッシュのマニュアル](https://docs.incredibuild.com/lin/latest/linux/build_avoidance.htm) ”Build Examples" の２つ目 "Run local and shared cache" で実現できます。ローカルと共有（リモート）ビルドキャッシュを両方併用することで、共有（リモート）ビルドキャッシュへは書き込みをしにいかないようになるため、結果 Read Only となります。詳細は同じページの "Local + Remote Cache Deployment" に記載があります。
