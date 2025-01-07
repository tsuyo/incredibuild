# Incredibuild Cloud (IBC) サポート情報

# 管理者向け
## クラウドベンダーのコア数制限について
Resource Management > Max Number of Cores 設定時 "Vendor account allows up to xxx cores" という注釈が表示されます。xxx は下記に基づいて表示されます。
- Spot Instance オン
  - Region Spot vCPU Quota
- Spot Instance オフ（下記の最小値）
  - Total Regional vCPU Quota (1st tier)
  - VM-family vCPU Quota (2nd tier)
