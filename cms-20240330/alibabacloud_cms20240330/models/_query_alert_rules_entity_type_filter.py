# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class QueryAlertRulesEntityTypeFilter(DaraModel):
    def __init__(
        self,
        in_: List[str] = None,
        not_in: List[str] = None,
    ):
        self.in_ = in_
        self.not_in = not_in

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.in_ is not None:
            result['in'] = self.in_

        if self.not_in is not None:
            result['notIn'] = self.not_in

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('in') is not None:
            self.in_ = m.get('in')

        if m.get('notIn') is not None:
            self.not_in = m.get('notIn')

        return self

