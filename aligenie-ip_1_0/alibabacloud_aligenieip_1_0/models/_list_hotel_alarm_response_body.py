# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_aligenieip_1_0 import models as main_models
from darabonba.model import DaraModel

class ListHotelAlarmResponseBody(DaraModel):
    def __init__(
        self,
        extentions: Dict[str, Any] = None,
        message: str = None,
        request_id: str = None,
        result: List[main_models.ListHotelAlarmResponseBodyResult] = None,
        status_code: int = None,
    ):
        self.extentions = extentions
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extentions is not None:
            result['Extentions'] = self.extentions

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.status_code is not None:
            result['StatusCode'] = self.status_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extentions') is not None:
            self.extentions = m.get('Extentions')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListHotelAlarmResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')

        return self

class ListHotelAlarmResponseBodyResult(DaraModel):
    def __init__(
        self,
        alarm_id: int = None,
        device_open_id: str = None,
        schedule_info: main_models.ListHotelAlarmResponseBodyResultScheduleInfo = None,
        user_open_id: str = None,
    ):
        self.alarm_id = alarm_id
        self.device_open_id = device_open_id
        self.schedule_info = schedule_info
        self.user_open_id = user_open_id

    def validate(self):
        if self.schedule_info:
            self.schedule_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_id is not None:
            result['AlarmId'] = self.alarm_id

        if self.device_open_id is not None:
            result['DeviceOpenId'] = self.device_open_id

        if self.schedule_info is not None:
            result['ScheduleInfo'] = self.schedule_info.to_map()

        if self.user_open_id is not None:
            result['UserOpenId'] = self.user_open_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmId') is not None:
            self.alarm_id = m.get('AlarmId')

        if m.get('DeviceOpenId') is not None:
            self.device_open_id = m.get('DeviceOpenId')

        if m.get('ScheduleInfo') is not None:
            temp_model = main_models.ListHotelAlarmResponseBodyResultScheduleInfo()
            self.schedule_info = temp_model.from_map(m.get('ScheduleInfo'))

        if m.get('UserOpenId') is not None:
            self.user_open_id = m.get('UserOpenId')

        return self

class ListHotelAlarmResponseBodyResultScheduleInfo(DaraModel):
    def __init__(
        self,
        once: main_models.ListHotelAlarmResponseBodyResultScheduleInfoOnce = None,
        type: str = None,
        weekly: main_models.ListHotelAlarmResponseBodyResultScheduleInfoWeekly = None,
    ):
        self.once = once
        # ONCE, WEEKLY
        self.type = type
        self.weekly = weekly

    def validate(self):
        if self.once:
            self.once.validate()
        if self.weekly:
            self.weekly.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.once is not None:
            result['Once'] = self.once.to_map()

        if self.type is not None:
            result['Type'] = self.type

        if self.weekly is not None:
            result['Weekly'] = self.weekly.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Once') is not None:
            temp_model = main_models.ListHotelAlarmResponseBodyResultScheduleInfoOnce()
            self.once = temp_model.from_map(m.get('Once'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Weekly') is not None:
            temp_model = main_models.ListHotelAlarmResponseBodyResultScheduleInfoWeekly()
            self.weekly = temp_model.from_map(m.get('Weekly'))

        return self

class ListHotelAlarmResponseBodyResultScheduleInfoWeekly(DaraModel):
    def __init__(
        self,
        days_of_week: List[int] = None,
        hour: int = None,
        minute: int = None,
    ):
        self.days_of_week = days_of_week
        self.hour = hour
        self.minute = minute

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.days_of_week is not None:
            result['DaysOfWeek'] = self.days_of_week

        if self.hour is not None:
            result['Hour'] = self.hour

        if self.minute is not None:
            result['Minute'] = self.minute

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DaysOfWeek') is not None:
            self.days_of_week = m.get('DaysOfWeek')

        if m.get('Hour') is not None:
            self.hour = m.get('Hour')

        if m.get('Minute') is not None:
            self.minute = m.get('Minute')

        return self

class ListHotelAlarmResponseBodyResultScheduleInfoOnce(DaraModel):
    def __init__(
        self,
        day: int = None,
        hour: int = None,
        minute: int = None,
        month: int = None,
        year: int = None,
    ):
        self.day = day
        self.hour = hour
        self.minute = minute
        self.month = month
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.day is not None:
            result['Day'] = self.day

        if self.hour is not None:
            result['Hour'] = self.hour

        if self.minute is not None:
            result['Minute'] = self.minute

        if self.month is not None:
            result['Month'] = self.month

        if self.year is not None:
            result['Year'] = self.year

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Day') is not None:
            self.day = m.get('Day')

        if m.get('Hour') is not None:
            self.hour = m.get('Hour')

        if m.get('Minute') is not None:
            self.minute = m.get('Minute')

        if m.get('Month') is not None:
            self.month = m.get('Month')

        if m.get('Year') is not None:
            self.year = m.get('Year')

        return self

