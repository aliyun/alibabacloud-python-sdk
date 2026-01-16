# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetEmonAlarmRecordStatisticsDistributeRequest(DaraModel):
    def __init__(
        self,
        body: str = None,
        group_id: str = None,
        time_end: int = None,
        time_start: int = None,
    ):
        self.body = body
        self.group_id = group_id
        self.time_end = time_end
        self.time_start = time_start

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body

        if self.group_id is not None:
            result['groupId'] = self.group_id

        if self.time_end is not None:
            result['timeEnd'] = self.time_end

        if self.time_start is not None:
            result['timeStart'] = self.time_start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')

        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')

        if m.get('timeEnd') is not None:
            self.time_end = m.get('timeEnd')

        if m.get('timeStart') is not None:
            self.time_start = m.get('timeStart')

        return self

