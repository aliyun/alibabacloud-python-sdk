# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CountTodosResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        pending_count: int = None,
        request_id: str = None,
        unread_count: int = None,
    ):
        # 业务状态码；成功为200
        self.code = code
        # 错误描述
        self.message = message
        # 待处理数量（PENDING 主状态）
        self.pending_count = pending_count
        # 请求追踪ID
        self.request_id = request_id
        # 未读数量（处理人 readAt 为空）
        self.unread_count = unread_count

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

        if self.pending_count is not None:
            result['pendingCount'] = self.pending_count

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.unread_count is not None:
            result['unreadCount'] = self.unread_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('pendingCount') is not None:
            self.pending_count = m.get('pendingCount')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('unreadCount') is not None:
            self.unread_count = m.get('unreadCount')

        return self

