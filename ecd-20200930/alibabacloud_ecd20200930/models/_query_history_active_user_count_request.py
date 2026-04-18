# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryHistoryActiveUserCountRequest(DaraModel):
    def __init__(
        self,
        data_date: str = None,
    ):
        self.data_date = data_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_date is not None:
            result['DataDate'] = self.data_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataDate') is not None:
            self.data_date = m.get('DataDate')

        return self

