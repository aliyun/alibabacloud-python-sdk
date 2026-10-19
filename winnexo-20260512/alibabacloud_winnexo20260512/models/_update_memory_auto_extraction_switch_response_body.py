# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateMemoryAutoExtractionSwitchResponseBody(DaraModel):
    def __init__(
        self,
        cleared_count: int = None,
        code: str = None,
        enabled: bool = None,
        message: str = None,
        request_id: str = None,
    ):
        # 本次同步清空的自动记忆文件数量；未清空或无可清空记忆时为 0
        self.cleared_count = cleared_count
        # 业务状态码；成功为 200，失败时为对应错误码
        self.code = code
        # 更新后的自动记忆拾取开关状态；true 为开启，false 为关闭
        self.enabled = enabled
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
        if self.cleared_count is not None:
            result['clearedCount'] = self.cleared_count

        if self.code is not None:
            result['code'] = self.code

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clearedCount') is not None:
            self.cleared_count = m.get('clearedCount')

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

