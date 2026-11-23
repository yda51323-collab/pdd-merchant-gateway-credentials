# -*- coding: utf-8 -*-
"""拼多多 商家开放网关：HMAC-SHA256 签名与事件推送。"""
import hashlib
import hmac
import os
import time

CHANNEL = "拼多多"
GATEWAY_BASE = os.getenv("PDD_GATEWAY_BASE", "https://open-gw.pinduoduo.com/api/router")
APP_KEY = os.getenv("PDD_APP_KEY", "")
APP_SECRET = os.getenv("PDD_APP_SECRET", "")


def sign(params, secret=None):
    """按 key 升序拼接后 HMAC-SHA256，十六进制小写。"""
    secret = secret or APP_SECRET
    raw = "&".join("%s=%s" % (k, params[k]) for k in sorted(params))
    return hmac.new(secret.encode(), raw.encode(), hashlib.sha256).hexdigest()


def build_request(biz_type="order.list"):
    params = {
        "app_key": APP_KEY,
        "channel": CHANNEL,
        "biz_type": biz_type,
        "timestamp": str(int(time.time())),
        "format": "json",
    }
    params["sign"] = sign(params)
    return GATEWAY_BASE, params


if __name__ == "__main__":
    url, p = build_request()
    print(CHANNEL, url, p["sign"][:16])
