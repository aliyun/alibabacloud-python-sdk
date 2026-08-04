# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aligeniessp_1_0 import models as main_models
from darabonba.model import DaraModel

class AddSubResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: main_models.AddSubResponseBodyResult = None,
    ):
        # Status code. A value of 200 indicates success.
        self.code = code
        # Additional information
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Return Result
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
            temp_model = main_models.AddSubResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class AddSubResponseBodyResult(DaraModel):
    def __init__(
        self,
        album_id: str = None,
        daily_study_cnt: int = None,
        device_id: str = None,
        id: int = None,
        play_mode: str = None,
        schedule_info: main_models.AddSubResponseBodyResultScheduleInfo = None,
        user_id: str = None,
    ):
        # Album ID
        self.album_id = album_id
        # Daily study quantity
        self.daily_study_cnt = daily_study_cnt
        # Device ID
        self.device_id = device_id
        # Subscription record ID
        self.id = id
        # Playback mode
        self.play_mode = play_mode
        # Schedule information
        self.schedule_info = schedule_info
        # User ID
        self.user_id = user_id

    def validate(self):
        if self.schedule_info:
            self.schedule_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.album_id is not None:
            result['AlbumId'] = self.album_id

        if self.daily_study_cnt is not None:
            result['DailyStudyCnt'] = self.daily_study_cnt

        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        if self.id is not None:
            result['Id'] = self.id

        if self.play_mode is not None:
            result['PlayMode'] = self.play_mode

        if self.schedule_info is not None:
            result['ScheduleInfo'] = self.schedule_info.to_map()

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlbumId') is not None:
            self.album_id = m.get('AlbumId')

        if m.get('DailyStudyCnt') is not None:
            self.daily_study_cnt = m.get('DailyStudyCnt')

        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('PlayMode') is not None:
            self.play_mode = m.get('PlayMode')

        if m.get('ScheduleInfo') is not None:
            temp_model = main_models.AddSubResponseBodyResultScheduleInfo()
            self.schedule_info = temp_model.from_map(m.get('ScheduleInfo'))

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class AddSubResponseBodyResultScheduleInfo(DaraModel):
    def __init__(
        self,
        days_of_week: List[int] = None,
        hour: int = None,
        minute: int = None,
    ):
        # The epoch for trigger
        self.days_of_week = days_of_week
        # The hour of the clock when the trigger occurs.
        self.hour = hour
        # The minute of the Time when the trigger occurs.
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

