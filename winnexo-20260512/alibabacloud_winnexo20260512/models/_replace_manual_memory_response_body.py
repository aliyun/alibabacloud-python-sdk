# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReplaceManualMemoryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        content: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # 业务状态码；成功为 200，失败时为对应错误码
        self.code = code
        # 保存后的手动记忆完整内容；清空成功时为空字符串
        self.content = content
        # 错误描述；成功时为空字符串，失败时返回具体原因
        self.message = message
        # 请求追踪 ID，用于定位本次调用
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.content is not None:
            result['content'] = self.content

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

