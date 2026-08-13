# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SendAsyncChatMessageResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        message_id: str = None,
        request_id: str = None,
        session_created: bool = None,
        session_id: str = None,
    ):
        # 业务状态码：成功为 200，失败为后端错误码（ERR.* / InvalidParameter.*）
        self.code = code
        # 错误描述，成功时为空
        self.message = message
        # 助手消息ID；用于随后调用 streamChatMessage 订阅生成结果
        self.message_id = message_id
        # 请求追踪 ID
        self.request_id = request_id
        # 本次调用是否新建了会话
        self.session_created = session_created
        # 会话ID；续写会话时与入参一致，新建会话时为服务端生成值
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        if self.message_id is not None:
            result['messageId'] = self.message_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.session_created is not None:
            result['sessionCreated'] = self.session_created

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('messageId') is not None:
            self.message_id = m.get('messageId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('sessionCreated') is not None:
            self.session_created = m.get('sessionCreated')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        return self

