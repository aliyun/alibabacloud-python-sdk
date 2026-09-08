# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RLProgressProcessed(DaraModel):
    def __init__(
        self,
        done: int = None,
        total: int = None,
    ):
        # 已处理条数
        self.done = done
        # 总条数
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.done is not None:
            result['Done'] = self.done

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Done') is not None:
            self.done = m.get('Done')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

