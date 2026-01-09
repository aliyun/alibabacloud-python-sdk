# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Histogram(DaraModel):
    def __init__(
        self,
        count: int = None,
        from_: int = None,
        progress: str = None,
        to: int = None,
    ):
        self.count = count
        self.from_ = from_
        self.progress = progress
        self.to = to

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['count'] = self.count

        if self.from_ is not None:
            result['from'] = self.from_

        if self.progress is not None:
            result['progress'] = self.progress

        if self.to is not None:
            result['to'] = self.to

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')

        if m.get('from') is not None:
            self.from_ = m.get('from')

        if m.get('progress') is not None:
            self.progress = m.get('progress')

        if m.get('to') is not None:
            self.to = m.get('to')

        return self

