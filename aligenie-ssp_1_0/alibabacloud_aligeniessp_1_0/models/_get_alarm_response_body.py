# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aligeniessp_1_0 import models as main_models
from darabonba.model import DaraModel

class GetAlarmResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: main_models.GetAlarmResponseBodyResult = None,
    ):
        # Status code returned by the alarm service
        self.code = code
        # error message
        self.message = message
        # Request ID
        self.request_id = request_id
        # Alarm details
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.GetAlarmResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class GetAlarmResponseBodyResult(DaraModel):
    def __init__(
        self,
        alarm_id: int = None,
        music_info: main_models.GetAlarmResponseBodyResultMusicInfo = None,
        schedule_info: main_models.GetAlarmResponseBodyResultScheduleInfo = None,
        schedule_type_desc: str = None,
        status: int = None,
        trigger_date_desc: str = None,
        trigger_time_desc: str = None,
        volume: int = None,
    ):
        # Alarm ID
        self.alarm_id = alarm_id
        # Ringtone Information
        self.music_info = music_info
        # Schedule Information
        self.schedule_info = schedule_info
        # Chinese description of the loop type
        self.schedule_type_desc = schedule_type_desc
        # status: 0 Normal, 1 deleted, 2 shutdown
        self.status = status
        # Trigger date description (one-time)
        self.trigger_date_desc = trigger_date_desc
        # Trigger time description
        self.trigger_time_desc = trigger_time_desc
        # Ringtone volume
        self.volume = volume

    def validate(self):
        if self.music_info:
            self.music_info.validate()
        if self.schedule_info:
            self.schedule_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_id is not None:
            result['AlarmId'] = self.alarm_id

        if self.music_info is not None:
            result['MusicInfo'] = self.music_info.to_map()

        if self.schedule_info is not None:
            result['ScheduleInfo'] = self.schedule_info.to_map()

        if self.schedule_type_desc is not None:
            result['ScheduleTypeDesc'] = self.schedule_type_desc

        if self.status is not None:
            result['Status'] = self.status

        if self.trigger_date_desc is not None:
            result['TriggerDateDesc'] = self.trigger_date_desc

        if self.trigger_time_desc is not None:
            result['TriggerTimeDesc'] = self.trigger_time_desc

        if self.volume is not None:
            result['Volume'] = self.volume

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmId') is not None:
            self.alarm_id = m.get('AlarmId')

        if m.get('MusicInfo') is not None:
            temp_model = main_models.GetAlarmResponseBodyResultMusicInfo()
            self.music_info = temp_model.from_map(m.get('MusicInfo'))

        if m.get('ScheduleInfo') is not None:
            temp_model = main_models.GetAlarmResponseBodyResultScheduleInfo()
            self.schedule_info = temp_model.from_map(m.get('ScheduleInfo'))

        if m.get('ScheduleTypeDesc') is not None:
            self.schedule_type_desc = m.get('ScheduleTypeDesc')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TriggerDateDesc') is not None:
            self.trigger_date_desc = m.get('TriggerDateDesc')

        if m.get('TriggerTimeDesc') is not None:
            self.trigger_time_desc = m.get('TriggerTimeDesc')

        if m.get('Volume') is not None:
            self.volume = m.get('Volume')

        return self

class GetAlarmResponseBodyResultScheduleInfo(DaraModel):
    def __init__(
        self,
        once: main_models.GetAlarmResponseBodyResultScheduleInfoOnce = None,
        statutory_working_day: main_models.GetAlarmResponseBodyResultScheduleInfoStatutoryWorkingDay = None,
        type: str = None,
        weekly: main_models.GetAlarmResponseBodyResultScheduleInfoWeekly = None,
    ):
        # One-time: This property is active when the loop type is ONCE.
        self.once = once
        # Statutory working day: This property is active when the loop Type is STATUTORYWORKINGDAY.
        self.statutory_working_day = statutory_working_day
        # Schedule Type / Loop Type: ONCE -> One-time, WEEKLY -> Weekly loop, STATUTORYWORKINGDAY -> Statutory working day
        self.type = type
        # Weekly loop: This property is active when the loop Type is WEEKLY.
        self.weekly = weekly

    def validate(self):
        if self.once:
            self.once.validate()
        if self.statutory_working_day:
            self.statutory_working_day.validate()
        if self.weekly:
            self.weekly.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.once is not None:
            result['Once'] = self.once.to_map()

        if self.statutory_working_day is not None:
            result['StatutoryWorkingDay'] = self.statutory_working_day.to_map()

        if self.type is not None:
            result['Type'] = self.type

        if self.weekly is not None:
            result['Weekly'] = self.weekly.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Once') is not None:
            temp_model = main_models.GetAlarmResponseBodyResultScheduleInfoOnce()
            self.once = temp_model.from_map(m.get('Once'))

        if m.get('StatutoryWorkingDay') is not None:
            temp_model = main_models.GetAlarmResponseBodyResultScheduleInfoStatutoryWorkingDay()
            self.statutory_working_day = temp_model.from_map(m.get('StatutoryWorkingDay'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Weekly') is not None:
            temp_model = main_models.GetAlarmResponseBodyResultScheduleInfoWeekly()
            self.weekly = temp_model.from_map(m.get('Weekly'))

        return self

class GetAlarmResponseBodyResultScheduleInfoWeekly(DaraModel):
    def __init__(
        self,
        days_of_week: List[int] = None,
        hour: int = None,
        minute: int = None,
    ):
        # Collection of days of the week to trigger: Numeric values between 1 and 7, where each number corresponds to a specific day of the week. If triggered every day, include all numbers.
        self.days_of_week = days_of_week
        # Trigger time: Hour
        self.hour = hour
        # Trigger time: Minute
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

class GetAlarmResponseBodyResultScheduleInfoStatutoryWorkingDay(DaraModel):
    def __init__(
        self,
        hour: int = None,
        minute: int = None,
    ):
        # Trigger Time: Hour
        self.hour = hour
        # Trigger Time: Minute
        self.minute = minute

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hour is not None:
            result['Hour'] = self.hour

        if self.minute is not None:
            result['Minute'] = self.minute

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')

        if m.get('Minute') is not None:
            self.minute = m.get('Minute')

        return self

class GetAlarmResponseBodyResultScheduleInfoOnce(DaraModel):
    def __init__(
        self,
        day: int = None,
        hour: int = None,
        minute: int = None,
        month: int = None,
        year: int = None,
    ):
        # Trigger time: Day
        self.day = day
        # Trigger Time: Hour
        self.hour = hour
        # Trigger Time: Minute
        self.minute = minute
        # Trigger Time: Month
        self.month = month
        # Trigger Time: Year
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

class GetAlarmResponseBodyResultMusicInfo(DaraModel):
    def __init__(
        self,
        music_id: int = None,
        music_name: str = None,
        music_type: int = None,
        music_type_name: str = None,
        music_url: str = None,
    ):
        # Ringtone ID
        self.music_id = music_id
        # Ringtone Name
        self.music_name = music_name
        # Ringtone Category ID
        self.music_type = music_type
        # Ringtone Category Name
        self.music_type_name = music_type_name
        # Ringtone URL
        self.music_url = music_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.music_id is not None:
            result['MusicId'] = self.music_id

        if self.music_name is not None:
            result['MusicName'] = self.music_name

        if self.music_type is not None:
            result['MusicType'] = self.music_type

        if self.music_type_name is not None:
            result['MusicTypeName'] = self.music_type_name

        if self.music_url is not None:
            result['MusicUrl'] = self.music_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MusicId') is not None:
            self.music_id = m.get('MusicId')

        if m.get('MusicName') is not None:
            self.music_name = m.get('MusicName')

        if m.get('MusicType') is not None:
            self.music_type = m.get('MusicType')

        if m.get('MusicTypeName') is not None:
            self.music_type_name = m.get('MusicTypeName')

        if m.get('MusicUrl') is not None:
            self.music_url = m.get('MusicUrl')

        return self

