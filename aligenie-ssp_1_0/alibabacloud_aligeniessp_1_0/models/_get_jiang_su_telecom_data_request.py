# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetJiangSuTelecomDataRequest(DaraModel):
    def __init__(
        self,
        date: str = None,
    ):
        # Date in the format yyyy-MM-dd. This refers to the data timestamp when the data becomes available, not the date when the data was generated. Data is always produced on a T+1 basis.
        self.date = date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date is not None:
            result['Date'] = self.date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')

        return self

