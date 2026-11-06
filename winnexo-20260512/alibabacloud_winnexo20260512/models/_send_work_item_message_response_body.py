# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SendWorkItemMessageResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        message_id: str = None,
        request_id: str = None,
        session_id: str = None,
        user_message_id: str = None,
        work_item_id: str = None,
    ):
        # 公共业务状态码；成功为200，失败为后端错误码。
        self.code = code
        # 公共状态说明；成功时为success，失败时描述具体原因。
        self.message = message
        # 本轮助手消息ID；回复在后台异步生成，取得该ID不表示AI已开始或已完成回复。
        self.message_id = message_id
        # 请求追踪ID，可用于定位本次调用及排查失败原因。
        self.request_id = request_id
        # 本次消息发送到的已有话题会话ID，不是新建会话ID。
        self.session_id = session_id
        # 本次提交的用户消息ID。
        self.user_message_id = user_message_id
        # 请求传入的工作项ID；仅传conversationId时返回legacy-topic:<conversationId>形式的兼容ID。
        self.work_item_id = work_item_id

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

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.user_message_id is not None:
            result['userMessageId'] = self.user_message_id

        if self.work_item_id is not None:
            result['workItemId'] = self.work_item_id

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

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('userMessageId') is not None:
            self.user_message_id = m.get('userMessageId')

        if m.get('workItemId') is not None:
            self.work_item_id = m.get('workItemId')

        return self

