# 拼多多 · 商家开放网关接入配置

商家开放网关（merchant open gateway）接入侧配置与签名实现。网关负责把商家的订单、发货、售后事件推送到内部消息总线。

## 目录

```
conf/gateway.env                 环境配置（网关地址、账号、密钥）
src/pdd_merchant_gateway.py      签名与推送实现
```

## 服务标识

- 业务标识：`拼多多`（商家开放网关）
- 出现位置：`conf/gateway.env` 的 `PDD_*` 键与 `PDD_CHANNEL` 值、`pdd_merchant_gateway.py` 的 `CHANNEL` 常量与模块注释、`README` 标题

## 使用

```bash
set -a && source conf/gateway.env && set +a
python src/pdd_merchant_gateway.py --push orders
```

## 字段说明

| 键 | 说明 |
|---|---|
| `PDD_GATEWAY_BASE` | 网关接入地址 |
| `PDD_APP_KEY` | 应用标识 |
| `PDD_APP_SECRET` | 应用密钥，用于 HMAC-SHA256 签名 |
| `PDD_DB_DSN` | 网关落库连接串 |

## 已知问题

1. 网关对同一 `msg_id` 的重推不幂等，落库侧需按 `msg_id` 去重。
2. 时钟漂移超过 300 秒会导致签名校验失败，容器内需挂载授时服务。

## 维护

交易网关组 · 值班群 `pdd-gw-oncall`
