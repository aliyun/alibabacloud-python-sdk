# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class MedicalAgentChatHeaders(DaraModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_dash_scope_sse: str = None,
        x_gwaccess: str = None,
        x_gwnonce: str = None,
        x_gwprotocol: str = None,
        x_gwsignature: str = None,
        x_gwtimestamp: str = None,
        x_request_id: str = None,
    ):
        self.common_headers = common_headers
        # 可选。请求 SSE 时可填 enable。正文中必须显式填写 JSON 布尔值 params.responseStreaming；true 返回 SSE，false 返回完整 JSON。
        self.x_dash_scope_sse = x_dash_scope_sse
        # 接入时领取的业务 Access Key ID，用于识别调用方。阿里云调用凭证按 SDK 的要求单独配置。
        # 
        # This parameter is required.
        self.x_gwaccess = x_gwaccess
        # 每次发送时重新生成的随机串，例如 UUID。重试时也要重新生成 nonce、时间戳和签名。
        # 
        # This parameter is required.
        self.x_gwnonce = x_gwnonce
        # 本文示例固定传 aliyun-roa，使用小驼峰格式的请求和响应。此请求头不参与业务签名。
        self.x_gwprotocol = x_gwprotocol
        # 使用接入时领取的业务签名密钥（SK）对六段内容计算 HMAC-SHA256。依次为 HTTP 方法（大写）、请求路径、规范化查询串、实际发送正文的 SHA-256 小写十六进制、X-GW-Timestamp、X-GW-Nonce。以换行连接，末尾不加换行；无查询参数时第三段保留为空。查询串按 & 拆分并去除空项，按原始参数项字典序排序后以 & 拼接，不解码。签名传 64 个小写十六进制字符。正文用 UTF-8 序列化一次，用同一份字节签名和发送，SK 仅用于本地计算。
        # 
        # This parameter is required.
        self.x_gwsignature = x_gwsignature
        # 发送请求时的 Unix 毫秒时间戳，使用十进制字符串。签名和请求头使用同一个值。
        # 
        # This parameter is required.
        self.x_gwtimestamp = x_gwtimestamp
        # 本次业务请求的关联号，单值，与 communication.requestId 完全相同。允许 1 至 128 个字母、数字或 . _ : - 字符，gw-ingress- 前缀保留给服务诊断。
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

        if self.x_dash_scope_sse is not None:
            result['X-DashScope-SSE'] = self.x_dash_scope_sse

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

        if m.get('X-DashScope-SSE') is not None:
            self.x_dash_scope_sse = m.get('X-DashScope-SSE')

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

