# Incredibuild Linux 4.x 質問集

## Coordinator ID の調べ方
```
$ sudo /opt/incredibuild/bin/sqlite3 /etc/incredibuild/db/incredibuildCoordinatorReport.db "select LicenseId from LicenseDesc"
```

## 共有（リモート）ビルドキャッシュを Read Only で利用する方法
[ビルドキャッシュのマニュアル](https://docs.incredibuild.com/lin/latest/linux/build_avoidance.htm) ”Build Examples" の２つ目 "Run local and shared cache" で実現できます。ローカルと共有（リモート）ビルドキャッシュを両方併用することで、共有（リモート）ビルドキャッシュへは書き込みをしにいかないようになるため、結果 Read Only となります。詳細は同じページの "Local + Remote Cache Deployment" に記載があります。
