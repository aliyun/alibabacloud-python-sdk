# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InputAudioBufferClear(DaraModel):
    def __init__(
        self,
        type: str = None,
        event_id: str = None,
    ):
        # 无额外业务入参。清理未处理缓冲，不撤回已下发结果；双向仅 manual 模式允许，server_vad 或存在待确认 commit 时拒绝。
        # 
        # This parameter is required.
        self.type = type
        # 可省略；提供时必须为非空、非纯空白字符串。
        self.event_id = event_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('event_id') is not None:
            self.event_id = m.get('event_id')

        return self

