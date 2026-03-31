# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeAlarmListResponseBody(DaraModel):
    def __init__(
        self,
        alarms: List[main_models.DescribeAlarmListResponseBodyAlarms] = None,
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
                temp_model = main_models.DescribeAlarmListResponseBodyAlarms()
                self.alarms.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeAlarmListResponseBodyAlarms(DaraModel):
    def __init__(
        self,
        cause: str = None,
        end_time: int = None,
        max_qps: int = None,
        spec: int = None,
        start_time: int = None,
        status: int = None,
        type: str = None,
    ):
        self.cause = cause
        self.end_time = end_time
        self.max_qps = max_qps
        self.spec = spec
        self.start_time = start_time
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cause is not None:
            result['Cause'] = self.cause

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.max_qps is not None:
            result['MaxQps'] = self.max_qps

        if self.spec is not None:
            result['Spec'] = self.spec

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cause') is not None:
            self.cause = m.get('Cause')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('MaxQps') is not None:
            self.max_qps = m.get('MaxQps')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

