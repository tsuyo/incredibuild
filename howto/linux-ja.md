# Incredibuild Linux 4.x 質問集
## Coordinator ID の調べ方
```
$ sudo /opt/incredibuild/bin/sqlite3 /etc/incredibuild/db/incredibuildCoordinatorReport.db "select LicenseId from LicenseDesc"
```
