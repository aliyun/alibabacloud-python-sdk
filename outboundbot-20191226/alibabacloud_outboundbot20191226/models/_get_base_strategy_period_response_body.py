# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20191226 import models as main_models
from darabonba.model import DaraModel

class GetBaseStrategyPeriodResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        only_weekdays: bool = None,
        only_workdays: bool = None,
        request_id: str = None,
        success: bool = None,
        working_time: List[main_models.GetBaseStrategyPeriodResponseBodyWorkingTime] = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.only_weekdays = only_weekdays
        self.only_workdays = only_workdays
        self.request_id = request_id
        self.success = success
        self.working_time = working_time

    def validate(self):
        if self.working_time:
            for v1 in self.working_time:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.only_weekdays is not None:
            result['OnlyWeekdays'] = self.only_weekdays

        if self.only_workdays is not None:
            result['OnlyWorkdays'] = self.only_workdays

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        result['WorkingTime'] = []
        if self.working_time is not None:
            for k1 in self.working_time:
                result['WorkingTime'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('OnlyWeekdays') is not None:
            self.only_weekdays = m.get('OnlyWeekdays')

        if m.get('OnlyWorkdays') is not None:
            self.only_workdays = m.get('OnlyWorkdays')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        self.working_time = []
        if m.get('WorkingTime') is not None:
            for k1 in m.get('WorkingTime'):
                temp_model = main_models.GetBaseStrategyPeriodResponseBodyWorkingTime()
                self.working_time.append(temp_model.from_map(k1))

        return self

class GetBaseStrategyPeriodResponseBodyWorkingTime(DaraModel):
    def __init__(
        self,
        begin_time: str = None,
        begin_time_millis: int = None,
        end_time: str = None,
        end_time_millis: int = None,
    ):
        self.begin_time = begin_time
        self.begin_time_millis = begin_time_millis
        self.end_time = end_time
        self.end_time_millis = end_time_millis

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        if self.begin_time_millis is not None:
            result['BeginTimeMillis'] = self.begin_time_millis

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.end_time_millis is not None:
            result['EndTimeMillis'] = self.end_time_millis

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('BeginTimeMillis') is not None:
            self.begin_time_millis = m.get('BeginTimeMillis')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EndTimeMillis') is not None:
            self.end_time_millis = m.get('EndTimeMillis')

        return self

