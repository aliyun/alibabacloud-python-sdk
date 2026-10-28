# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetQuotaAlarmRequest(DaraModel):
    def __init__(
        self,
        alarm_id: str = None,
    ):
        # The ID of the quota alert.
        # 
        # For more information about how to obtain the ID of a quota alert, see [ListQuotaAlarms](https://help.aliyun.com/document_detail/184348.html).
        self.alarm_id = alarm_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_id is not None:
            result['AlarmId'] = self.alarm_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmId') is not None:
            self.alarm_id = m.get('AlarmId')

        return self

