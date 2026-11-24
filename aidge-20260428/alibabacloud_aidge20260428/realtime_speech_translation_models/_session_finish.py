# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SessionFinish(DaraModel):
    def __init__(
        self,
        type: str = None,
        event_id: str = None,
        reason: str = None,
    ):
        # This parameter is required.
        self.type = type
        # 可省略；提供时必须为非空、非纯空白字符串。
        self.event_id = event_id
        # 双向省略时后端按 completed 排空结果，cancelled 立即取消；clear 进行中拒绝结束。单向客户端省略本字段，等待 SessionFinished 后关闭连接。网关不补默认值。
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['type'] = self.type

        if self.event_id is not None:
            result['event_id'] = self.event_id

        if self.reason is not None:
            result['reason'] = self.reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('event_id') is not None:
            self.event_id = m.get('event_id')

        if m.get('reason') is not None:
            self.reason = m.get('reason')

        return self

