# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aligeniessp_1_0 import models as main_models
from darabonba.model import DaraModel

class CreateAlarmRequest(DaraModel):
    def __init__(
        self,
        device_info: main_models.CreateAlarmRequestDeviceInfo = None,
        payload: main_models.CreateAlarmRequestPayload = None,
        user_info: main_models.CreateAlarmRequestUserInfo = None,
    ):
        # Device identity information
        # 
        # This parameter is required.
        self.device_info = device_info
        # Input parameters for the service request
        # 
        # This parameter is required.
        self.payload = payload
        # User Identifier information
        # 
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.payload:
            self.payload.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()

        if self.payload is not None:
            result['Payload'] = self.payload.to_map()

        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = main_models.CreateAlarmRequestDeviceInfo()
            self.device_info = temp_model.from_map(m.get('DeviceInfo'))

        if m.get('Payload') is not None:
            temp_model = main_models.CreateAlarmRequestPayload()
            self.payload = temp_model.from_map(m.get('Payload'))

        if m.get('UserInfo') is not None:
            temp_model = main_models.CreateAlarmRequestUserInfo()
            self.user_info = temp_model.from_map(m.get('UserInfo'))

        return self

class CreateAlarmRequestUserInfo(DaraModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # Value corresponding to the encoding type. When the encoding type is SKILL_ID, the value is the application\\"s Skill ID. When the encoding type is PACKAGE_NAME, the value is the packageName of the corresponding client app.
        # 
        # This parameter is required.
        self.encode_key = encode_key
        # Encoding Type. There are multiple ways to obtain the User Identifier for Maojing, and each way corresponds to a different encoding Type: PACKAGE_NAME: APK package name, used for the Android application Customer link; SKILL_ID: Skill ID, used for the cloud link.
        # 
        # This parameter is required.
        self.encode_type = encode_type
        # User Identifier (userOpenId or userUnionId)
        # 
        # This parameter is required.
        self.id = id
        # Type of User ID: OPEN_ID: default User ID identifier; UNION_ID: organization-dimension User ID identifier, available only after an organization has been requested on the Maojing Skill Application Open Platform.
        # 
        # This parameter is required.
        self.id_type = id_type
        # Organization ID. Required when IdType is UNION_ID.
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

class CreateAlarmRequestPayload(DaraModel):
    def __init__(
        self,
        music_info: main_models.CreateAlarmRequestPayloadMusicInfo = None,
        schedule_info: main_models.CreateAlarmRequestPayloadScheduleInfo = None,
        volume: int = None,
    ):
        # Ringtone information
        # 
        # This parameter is required.
        self.music_info = music_info
        # Schedule information
        # 
        # This parameter is required.
        self.schedule_info = schedule_info
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
        if self.music_info is not None:
            result['MusicInfo'] = self.music_info.to_map()

        if self.schedule_info is not None:
            result['ScheduleInfo'] = self.schedule_info.to_map()

        if self.volume is not None:
            result['Volume'] = self.volume

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MusicInfo') is not None:
            temp_model = main_models.CreateAlarmRequestPayloadMusicInfo()
            self.music_info = temp_model.from_map(m.get('MusicInfo'))

        if m.get('ScheduleInfo') is not None:
            temp_model = main_models.CreateAlarmRequestPayloadScheduleInfo()
            self.schedule_info = temp_model.from_map(m.get('ScheduleInfo'))

        if m.get('Volume') is not None:
            self.volume = m.get('Volume')

        return self

class CreateAlarmRequestPayloadScheduleInfo(DaraModel):
    def __init__(
        self,
        once: main_models.CreateAlarmRequestPayloadScheduleInfoOnce = None,
        statutory_working_day: main_models.CreateAlarmRequestPayloadScheduleInfoStatutoryWorkingDay = None,
        type: str = None,
        weekly: main_models.CreateAlarmRequestPayloadScheduleInfoWeekly = None,
    ):
        # One-time: This property is active when the loop type is ONCE.
        self.once = once
        # Statutory working day: This property is active when the loop Type is STATUTORY_WORKING_DAY.
        self.statutory_working_day = statutory_working_day
        # Schedule Type / Loop Type:  
        # ONCE -> One-time, WEEKLY -> Weekly loop, STATUTORY_WORKING_DAY -> Statutory working day
        # 
        # This parameter is required.
        self.type = type
        # Weekly Loop: This property is active when the loop Type is WEEKLY.
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
            temp_model = main_models.CreateAlarmRequestPayloadScheduleInfoOnce()
            self.once = temp_model.from_map(m.get('Once'))

        if m.get('StatutoryWorkingDay') is not None:
            temp_model = main_models.CreateAlarmRequestPayloadScheduleInfoStatutoryWorkingDay()
            self.statutory_working_day = temp_model.from_map(m.get('StatutoryWorkingDay'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Weekly') is not None:
            temp_model = main_models.CreateAlarmRequestPayloadScheduleInfoWeekly()
            self.weekly = temp_model.from_map(m.get('Weekly'))

        return self

class CreateAlarmRequestPayloadScheduleInfoWeekly(DaraModel):
    def __init__(
        self,
        days_of_week: List[int] = None,
        hour: int = None,
        minute: int = None,
    ):
        # Collection of Days of the Week to Trigger
        self.days_of_week = days_of_week
        # Trigger time: hour
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

class CreateAlarmRequestPayloadScheduleInfoStatutoryWorkingDay(DaraModel):
    def __init__(
        self,
        hour: int = None,
        minute: int = None,
    ):
        # Trigger time: hour
        self.hour = hour
        # Trigger time: minute
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

class CreateAlarmRequestPayloadScheduleInfoOnce(DaraModel):
    def __init__(
        self,
        day: int = None,
        hour: int = None,
        minute: int = None,
        month: int = None,
        year: int = None,
    ):
        # Trigger Time: Day
        self.day = day
        # Trigger Time: Hour
        self.hour = hour
        # Trigger time: Minute
        self.minute = minute
        # Trigger time: Month
        self.month = month
        # Trigger time: Year
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

class CreateAlarmRequestPayloadMusicInfo(DaraModel):
    def __init__(
        self,
        music_id: int = None,
        music_name: str = None,
        music_type: int = None,
        music_type_name: str = None,
        music_url: str = None,
    ):
        # Ringtone ID
        # 
        # This parameter is required.
        self.music_id = music_id
        # Ringtone name
        # 
        # This parameter is required.
        self.music_name = music_name
        # Ringtone category ID
        # 
        # This parameter is required.
        self.music_type = music_type
        # Ringtone category name
        # 
        # This parameter is required.
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

class CreateAlarmRequestDeviceInfo(DaraModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # The value corresponding to the encoding type. When the encoding type is SKILL_ID, the value is the Skill ID of the application; when the encoding type is PACKAGE_NAME, the value is the packageName of the corresponding client app.
        # 
        # This parameter is required.
        self.encode_key = encode_key
        # Encoding type. There are multiple ways to obtain the device identity for Maojing, and each method corresponds to a different encoding type: PACKAGE_NAME: APK package name, used in the Android application customer link; SKILL_ID: skill ID, used in the cloud link.
        # 
        # This parameter is required.
        self.encode_type = encode_type
        # Device ID (deviceOpenId or deviceUnionId)
        # 
        # This parameter is required.
        self.id = id
        # Type of device ID: OPEN_ID: default device ID; UNION_ID: organization-dimension device ID, available only after applying for an organization on the Maojing Skill Application Open Platform.
        # 
        # This parameter is required.
        self.id_type = id_type
        # Organization ID. Required if IdType is UNION_ID.
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

