# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yundun_dbaudit20180320 import models as main_models
from darabonba.model import DaraModel

class ListSystemAlarmsResponseBody(DaraModel):
    def __init__(
        self,
        alarms: List[main_models.ListSystemAlarmsResponseBodyAlarms] = None,
        request_id: str = None,
    ):
        self.alarms = alarms
        self.request_id = request_id

    def validate(self):
        if self.alarms:
            for v1 in self.alarms:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Alarms'] = []
        if self.alarms is not None:
            for k1 in self.alarms:
                result['Alarms'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alarms = []
        if m.get('Alarms') is not None:
            for k1 in m.get('Alarms'):
                temp_model = main_models.ListSystemAlarmsResponseBodyAlarms()
                self.alarms.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListSystemAlarmsResponseBodyAlarms(DaraModel):
    def __init__(
        self,
        alarm_detail: str = None,
        alarm_id: int = None,
        alarm_type: str = None,
        create_time: str = None,
        read_mark: int = None,
    ):
        self.alarm_detail = alarm_detail
        self.alarm_id = alarm_id
        self.alarm_type = alarm_type
        self.create_time = create_time
        self.read_mark = read_mark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_detail is not None:
            result['AlarmDetail'] = self.alarm_detail

        if self.alarm_id is not None:
            result['AlarmId'] = self.alarm_id

        if self.alarm_type is not None:
            result['AlarmType'] = self.alarm_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.read_mark is not None:
            result['ReadMark'] = self.read_mark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmDetail') is not None:
            self.alarm_detail = m.get('AlarmDetail')

        if m.get('AlarmId') is not None:
            self.alarm_id = m.get('AlarmId')

        if m.get('AlarmType') is not None:
            self.alarm_type = m.get('AlarmType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ReadMark') is not None:
            self.read_mark = m.get('ReadMark')

        return self

