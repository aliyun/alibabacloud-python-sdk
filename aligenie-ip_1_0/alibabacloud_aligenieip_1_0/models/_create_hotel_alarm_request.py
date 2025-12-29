# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aligenieip_1_0 import models as main_models
from darabonba.model import DaraModel

class CreateHotelAlarmRequest(DaraModel):
    def __init__(
        self,
        hotel_id: str = None,
        music_type: str = None,
        rooms: List[str] = None,
        schedule_info: main_models.CreateHotelAlarmRequestScheduleInfo = None,
    ):
        # This parameter is required.
        self.hotel_id = hotel_id
        self.music_type = music_type
        # This parameter is required.
        self.rooms = rooms
        # This parameter is required.
        self.schedule_info = schedule_info

    def validate(self):
        if self.schedule_info:
            self.schedule_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id

        if self.music_type is not None:
            result['MusicType'] = self.music_type

        if self.rooms is not None:
            result['Rooms'] = self.rooms

        if self.schedule_info is not None:
            result['ScheduleInfo'] = self.schedule_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        if m.get('MusicType') is not None:
            self.music_type = m.get('MusicType')

        if m.get('Rooms') is not None:
            self.rooms = m.get('Rooms')

        if m.get('ScheduleInfo') is not None:
            temp_model = main_models.CreateHotelAlarmRequestScheduleInfo()
            self.schedule_info = temp_model.from_map(m.get('ScheduleInfo'))

        return self

class CreateHotelAlarmRequestScheduleInfo(DaraModel):
    def __init__(
        self,
        once: main_models.CreateHotelAlarmRequestScheduleInfoOnce = None,
        type: str = None,
        weekly: main_models.CreateHotelAlarmRequestScheduleInfoWeekly = None,
    ):
        self.once = once
        # ONCE, WEEKLY
        # 
        # This parameter is required.
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
            temp_model = main_models.CreateHotelAlarmRequestScheduleInfoOnce()
            self.once = temp_model.from_map(m.get('Once'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Weekly') is not None:
            temp_model = main_models.CreateHotelAlarmRequestScheduleInfoWeekly()
            self.weekly = temp_model.from_map(m.get('Weekly'))

        return self

class CreateHotelAlarmRequestScheduleInfoWeekly(DaraModel):
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

class CreateHotelAlarmRequestScheduleInfoOnce(DaraModel):
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

