# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aligeniessp_1_0 import models as main_models
from darabonba.model import DaraModel

class AddSubRequest(DaraModel):
    def __init__(
        self,
        add_subscription_info_request: main_models.AddSubRequestAddSubscriptionInfoRequest = None,
        device_info: main_models.AddSubRequestDeviceInfo = None,
        user_info: main_models.AddSubRequestUserInfo = None,
    ):
        # Subscribe to album request
        self.add_subscription_info_request = add_subscription_info_request
        # Device Information
        self.device_info = device_info
        # User Information
        self.user_info = user_info

    def validate(self):
        if self.add_subscription_info_request:
            self.add_subscription_info_request.validate()
        if self.device_info:
            self.device_info.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_subscription_info_request is not None:
            result['AddSubscriptionInfoRequest'] = self.add_subscription_info_request.to_map()

        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()

        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddSubscriptionInfoRequest') is not None:
            temp_model = main_models.AddSubRequestAddSubscriptionInfoRequest()
            self.add_subscription_info_request = temp_model.from_map(m.get('AddSubscriptionInfoRequest'))

        if m.get('DeviceInfo') is not None:
            temp_model = main_models.AddSubRequestDeviceInfo()
            self.device_info = temp_model.from_map(m.get('DeviceInfo'))

        if m.get('UserInfo') is not None:
            temp_model = main_models.AddSubRequestUserInfo()
            self.user_info = temp_model.from_map(m.get('UserInfo'))

        return self

class AddSubRequestUserInfo(DaraModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        self.encode_key = encode_key
        self.encode_type = encode_type
        self.id = id
        self.id_type = id_type
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key

        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type

        if self.id is not None:
            result['Id'] = self.id

        if self.id_type is not None:
            result['IdType'] = self.id_type

        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')

        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')

        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')

        return self

class AddSubRequestDeviceInfo(DaraModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        self.encode_key = encode_key
        self.encode_type = encode_type
        self.id = id
        self.id_type = id_type
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key

        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type

        if self.id is not None:
            result['Id'] = self.id

        if self.id_type is not None:
            result['IdType'] = self.id_type

        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')

        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')

        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')

        return self

class AddSubRequestAddSubscriptionInfoRequest(DaraModel):
    def __init__(
        self,
        album_id: str = None,
        daily_study_cnt: int = None,
        play_mode: str = None,
        schedule_info: main_models.AddSubRequestAddSubscriptionInfoRequestScheduleInfo = None,
    ):
        # Album ID
        self.album_id = album_id
        # Daily study quantity
        self.daily_study_cnt = daily_study_cnt
        # Playback pattern (currently only supports sequence)
        self.play_mode = play_mode
        # Schedule information
        self.schedule_info = schedule_info

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

        if self.play_mode is not None:
            result['PlayMode'] = self.play_mode

        if self.schedule_info is not None:
            result['ScheduleInfo'] = self.schedule_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlbumId') is not None:
            self.album_id = m.get('AlbumId')

        if m.get('DailyStudyCnt') is not None:
            self.daily_study_cnt = m.get('DailyStudyCnt')

        if m.get('PlayMode') is not None:
            self.play_mode = m.get('PlayMode')

        if m.get('ScheduleInfo') is not None:
            temp_model = main_models.AddSubRequestAddSubscriptionInfoRequestScheduleInfo()
            self.schedule_info = temp_model.from_map(m.get('ScheduleInfo'))

        return self

class AddSubRequestAddSubscriptionInfoRequestScheduleInfo(DaraModel):
    def __init__(
        self,
        days_of_week: List[int] = None,
        hour: int = None,
        minute: int = None,
    ):
        # The specific days of the week for weekly reminders. Valid values are 1 to 7.
        self.days_of_week = days_of_week
        # The hour of the clock when the reminder is triggered.
        self.hour = hour
        # The minute of the hour when the reminder is triggered.
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

