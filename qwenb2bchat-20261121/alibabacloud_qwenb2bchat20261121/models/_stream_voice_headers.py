# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class StreamVoiceHeaders(DaraModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_gwaccess: str = None,
        x_gwnonce: str = None,
        x_gwprotocol: str = None,
        x_gwsignature: str = None,
        x_gwtimestamp: str = None,
        x_request_id: str = None,
    ):
        self.common_headers = common_headers
        # 握手必填的业务网关 AK，用于识别租户和凭据；与阿里云 API AK 用途不同。业务网关 SK 仅在客户端用于计算签名，不发送。
        # 
        # This parameter is required.
        self.x_gwaccess = x_gwaccess
        # 握手必填，一次性随机串，原值参与业务签名；每次重新连接重新生成，不能重放原握手签名。
        # 
        # This parameter is required.
        self.x_gwnonce = x_gwnonce
        # 可选，当前公开小驼峰字段协议应传 aliyun-roa；省略时采用兼容旧协议，其字段命名不同。握手时选择后作用于本连接，不能在后续帧中切换。本头不参与 X-GW 签名。
        self.x_gwprotocol = x_gwprotocol
        # 握手必填，64 位小写十六进制 HMAC-SHA256。签名原文为 GET、实际路径、规范化实际 query、空请求体的 SHA-256 小写摘要、时间戳和 nonce，以换行符连接。对原文 UTF-8 字节使用业务网关 SK 签名；阿里云 API 签名另行生成。
        # 
        # This parameter is required.
        self.x_gwsignature = x_gwsignature
        # 握手必填，当前 Unix 毫秒时间戳的数字字符串，原值参与业务签名；每次重新连接更新后重新签名。
        # 
        # This parameter is required.
        self.x_gwtimestamp = x_gwtimestamp
        # 可选连接级关联号。省略时生成服务端诊断号。显式提供时只允许一个 1–128 位的 [A-Za-z0-9._:-] 字符串，gw-ingress- 前缀保留给服务。格式非法或提供多个值时返回 HTTP 400。每轮业务请求号使用 run-task.communication.requestId。
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

        if self.x_gwprotocol is not None:
            result['X-GW-Protocol'] = self.x_gwprotocol

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

        if m.get('X-GW-Protocol') is not None:
            self.x_gwprotocol = m.get('X-GW-Protocol')

        if m.get('X-GW-Signature') is not None:
            self.x_gwsignature = m.get('X-GW-Signature')

        if m.get('X-GW-Timestamp') is not None:
            self.x_gwtimestamp = m.get('X-GW-Timestamp')

        if m.get('X-Request-Id') is not None:
            self.x_request_id = m.get('X-Request-Id')

        return self

