# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SessionFinished(DaraModel):
    def __init__(
        self,
        type: str = None,
        event_id: str = None,
        session_id: str = None,
        caused_by: str = None,
        reason: str = None,
        usage_complete: bool = None,
    ):
        self.type = type
        self.event_id = event_id
        self.session_id = session_id
        self.caused_by = caused_by
        self.reason = reason
        # true 表示结束时用量已完成 MQ 接收与通知写出；超时、取消、异常或用量不完整时为 false，不代表最终扣费结果。兼容旧版本时可省略，网关不补默认值。
        self.usage_complete = usage_complete

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

        if self.session_id is not None:
            result['session_id'] = self.session_id

        if self.caused_by is not None:
            result['caused_by'] = self.caused_by

        if self.reason is not None:
            result['reason'] = self.reason

        if self.usage_complete is not None:
            result['usage_complete'] = self.usage_complete

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('event_id') is not None:
            self.event_id = m.get('event_id')

        if m.get('session_id') is not None:
            self.session_id = m.get('session_id')

        if m.get('caused_by') is not None:
            self.caused_by = m.get('caused_by')

        if m.get('reason') is not None:
            self.reason = m.get('reason')

        if m.get('usage_complete') is not None:
            self.usage_complete = m.get('usage_complete')

        return self

