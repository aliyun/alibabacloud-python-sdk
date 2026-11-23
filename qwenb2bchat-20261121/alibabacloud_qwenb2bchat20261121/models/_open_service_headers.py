# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class OpenServiceHeaders(DaraModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_gwaccess: str = None,
        x_gwnonce: str = None,
        x_gwsignature: str = None,
        x_gwtimestamp: str = None,
        x_request_id: str = None,
    ):
        self.common_headers = common_headers
        # 必填的业务网关 AK，由服务接入方签发，用于识别租户和凭据；与阿里云 API 鉴权凭据用途不同，不发送业务网关 SK。
        # 
        # This parameter is required.
        self.x_gwaccess = x_gwaccess
        # 必填的一次性随机串，原值参与业务网关签名；每次请求和重试重新生成，不能重放原签名。
        # 
        # This parameter is required.
        self.x_gwnonce = x_gwnonce
        # 必填的业务网关 HMAC-SHA256 签名，64 位小写十六进制。签名原文为方法、路径、空查询串、实际请求体字节的 SHA-256 小写摘要、时间戳、nonce 六段，以换行符连接。签名后不得改变请求体字节；阿里云 API 签名另行生成。
        # 
        # This parameter is required.
        self.x_gwsignature = x_gwsignature
        # 必填的当前 Unix 毫秒时间戳，用数字字符串表示，原值参与业务网关签名；重试时更新并重新签名。
        # 
        # This parameter is required.
        self.x_gwtimestamp = x_gwtimestamp
        # 必填的客户请求关联号，恰好一个，匹配 [A-Za-z0-9._:-]{1,128}；不能使用 gw-ingress- 保留前缀。仅用于关联本次调用，不是订单号或幂等令牌。
        # 
        # This parameter is required.
        self.x_request_id = x_request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers

        if self.x_gwaccess is not None:
            result['X-GW-Access'] = self.x_gwaccess

        if self.x_gwnonce is not None:
            result['X-GW-Nonce'] = self.x_gwnonce

        if self.x_gwsignature is not None:
            result['X-GW-Signature'] = self.x_gwsignature

        if self.x_gwtimestamp is not None:
            result['X-GW-Timestamp'] = self.x_gwtimestamp

        if self.x_request_id is not None:
            result['X-Request-Id'] = self.x_request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')

        if m.get('X-GW-Access') is not None:
            self.x_gwaccess = m.get('X-GW-Access')

        if m.get('X-GW-Nonce') is not None:
            self.x_gwnonce = m.get('X-GW-Nonce')

        if m.get('X-GW-Signature') is not None:
            self.x_gwsignature = m.get('X-GW-Signature')

        if m.get('X-GW-Timestamp') is not None:
            self.x_gwtimestamp = m.get('X-GW-Timestamp')

        if m.get('X-Request-Id') is not None:
            self.x_request_id = m.get('X-Request-Id')

        return self

