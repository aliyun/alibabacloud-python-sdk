# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RLProgressBufferDetail(DaraModel):
    def __init__(
        self,
        consumed: int = None,
        finished: int = None,
        ready: int = None,
        tag: int = None,
        total: int = None,
    ):
        # 已被 trainer 消费的样本数
        self.consumed = consumed
        # 已完成样本数
        self.finished = finished
        # 已就绪样本数
        self.ready = ready
        # buffer 标签，即 global batch 序号
        self.tag = tag
        # 目标样本数
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consumed is not None:
            result['Consumed'] = self.consumed

        if self.finished is not None:
            result['Finished'] = self.finished

        if self.ready is not None:
            result['Ready'] = self.ready

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Consumed') is not None:
            self.consumed = m.get('Consumed')

        if m.get('Finished') is not None:
            self.finished = m.get('Finished')

        if m.get('Ready') is not None:
            self.ready = m.get('Ready')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

