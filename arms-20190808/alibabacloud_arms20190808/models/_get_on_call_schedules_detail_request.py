# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetOnCallSchedulesDetailRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        id: int = None,
        start_time: str = None,
    ):
        # The date on which the shift ends. Format: `yyyy-MM-dd`.
        self.end_time = end_time
        # The ID of the scheduling policy.
        # 
        # This parameter is required.
        self.id = id
        # The date from which the shift starts. Format: `yyyy-MM-dd`.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.id is not None:
            result['Id'] = self.id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

