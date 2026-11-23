# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class ChatHeaders(DaraModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        accept: str = None,
        x_dash_scope_sse: str = None,
        x_gwaccess: str = None,
        x_gwnonce: str = None,
        x_gwprotocol: str = None,
        x_gwsignature: str = None,
        x_gwtimestamp: str = None,
        x_request_id: str = None,
    ):
        self.common_headers = common_headers
        # 可选。完整 JSON 可传 application/json，SSE 可传 text/event-stream。客户端必须在正文中以布尔值 params.responseStreaming 指定响应格式。
        self.accept = accept
        # 可选。enable 表示 SSE。每次请求须在正文中显式填写布尔参数 params.responseStreaming。本头不替代 X-GW-Protocol 或 X-GW 签名。
        self.x_dash_scope_sse = x_dash_scope_sse
        # 必填，服务方发放的业务网关 AK，用于识别租户和业务凭据，不是用于 POP 鉴权的阿里云 AK。每次只传一个非空值；业务 SK 只在客户端用于计算签名，不随请求发送。
        # 
        # This parameter is required.
        self.x_gwaccess = x_gwaccess
        # 必填，每次尝试唯一且非空的随机串，例如 UUID；不可重放旧签名。重试重新生成 nonce、时间戳及签名。
        # 
        # This parameter is required.
        self.x_gwnonce = x_gwnonce
        # 本文小驼峰请求与响应必须显式传 aliyun-roa，且只传一次。省略选择旧协议，不能直接照搬小驼峰正文。此头不参与业务 HMAC，不代替 POP 鉴权或 X-GW-* 业务签名。
        self.x_gwprotocol = x_gwprotocol
        # 必填，使用业务网关 SK 计算的 64 位小写十六进制 HMAC-SHA256。六段按 LF 连接且无末尾换行：METHOD、PATH、CANONICAL_QUERY、BODY_SHA256_HEX、TIMESTAMP、NONCE。原始 query 按 & 分项去空、字典序排序，不 decode/re-encode；正文按实际发送的 UTF-8 字节摘要。具体双签名示例见接口说明。
        # 
        # This parameter is required.
        self.x_gwsignature = x_gwsignature
        # 必填，当前 Unix 毫秒时间戳的数字字符串；有效时间窗按凭据配置。签名规范串与本头使用完全相同的字符串。每次重试重新生成时间戳、nonce 和签名。
        # 
        # This parameter is required.
        self.x_gwtimestamp = x_gwtimestamp
        # 必填，恰好一个，须与 communication.requestId 完全一致。格式 [A-Za-z0-9._:-]{1,128}，不得用保留前缀 gw-ingress-。例如 chat-20261118-001；这是业务关联号，不保证重复请求只执行一次。
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

        if self.accept is not None:
            result['Accept'] = self.accept

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

        if m.get('Accept') is not None:
            self.accept = m.get('Accept')

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

