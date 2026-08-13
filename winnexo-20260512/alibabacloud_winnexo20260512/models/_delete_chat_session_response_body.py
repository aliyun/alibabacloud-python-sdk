# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteChatSessionResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        deleted: bool = None,
        hard_delete: bool = None,
        message: str = None,
        request_id: str = None,
        session_id: str = None,
    ):
        # 业务状态码：成功为 200，失败为后端错误码（ERR.* / InvalidParameter.*）
        self.code = code
        # 是否删除成功
        self.deleted = deleted
        # 是否硬删除
        self.hard_delete = hard_delete
        # 错误描述，成功时为空
        self.message = message
        # 请求追踪 ID
        self.request_id = request_id
        # 会话 ID
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

        if self.deleted is not None:
            result['deleted'] = self.deleted

        if self.hard_delete is not None:
            result['hardDelete'] = self.hard_delete

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('deleted') is not None:
            self.deleted = m.get('deleted')

        if m.get('hardDelete') is not None:
            self.hard_delete = m.get('hardDelete')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        return self

