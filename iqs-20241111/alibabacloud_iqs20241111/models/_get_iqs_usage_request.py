# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetIqsUsageRequest(DaraModel):
    def __init__(
        self,
        caller_id: str = None,
        end_date: str = None,
        start_date: str = None,
    ):
        self.caller_id = caller_id
        self.end_date = end_date
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.caller_id is not None:
            result['callerId'] = self.caller_id

        if self.end_date is not None:
            result['endDate'] = self.end_date

        if self.start_date is not None:
            result['startDate'] = self.start_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('callerId') is not None:
            self.caller_id = m.get('callerId')

        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')

        if m.get('startDate') is not None:
            self.start_date = m.get('startDate')

        return self

