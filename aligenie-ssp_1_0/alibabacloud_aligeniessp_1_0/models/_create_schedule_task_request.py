# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_aligeniessp_1_0 import models as main_models
from darabonba.model import DaraModel

class CreateScheduleTaskRequest(DaraModel):
    def __init__(
        self,
        device_info: main_models.CreateScheduleTaskRequestDeviceInfo = None,
        payload: main_models.CreateScheduleTaskRequestPayload = None,
        user_info: main_models.CreateScheduleTaskRequestUserInfo = None,
    ):
        # Device identity information
        # 
        # This parameter is required.
        self.device_info = device_info
        # Input parameters for the service request
        # 
        # This parameter is required.
        self.payload = payload
        # User Identifier Information
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
            temp_model = main_models.CreateScheduleTaskRequestDeviceInfo()
            self.device_info = temp_model.from_map(m.get('DeviceInfo'))

        if m.get('Payload') is not None:
            temp_model = main_models.CreateScheduleTaskRequestPayload()
            self.payload = temp_model.from_map(m.get('Payload'))

        if m.get('UserInfo') is not None:
            temp_model = main_models.CreateScheduleTaskRequestUserInfo()
            self.user_info = temp_model.from_map(m.get('UserInfo'))

        return self

class CreateScheduleTaskRequestUserInfo(DaraModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # The value corresponding to the encoding type. When the encoding type is SKILL_ID, the value is the application\\"s SkillID. When the encoding type is PACKAGE_NAME, the value is the packageName of the corresponding client app.
        self.encode_key = encode_key
        # Encoding Type. There are multiple ways to obtain the user identifier for Maojing, and each method corresponds to a different encoding type: PACKAGE_NAME: APK package name, used for Android application customer links; SKILL_ID: Skill ID, used for cloud-based links.
        self.encode_type = encode_type
        # User Identifier (userOpenId or userUnionId)
        self.id = id
        # Type of User ID:  
        # - OPEN_ID: The default User ID identity.  
        # - UNION_ID: The User ID identity at the organization dimension. This is available only after an organization has been requested on the Maojing Skill Application Open Platform.
        self.id_type = id_type
        # Organization ID; Required if IdType is UNION_ID
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

class CreateScheduleTaskRequestPayload(DaraModel):
    def __init__(
        self,
        action_dtos: List[main_models.CreateScheduleTaskRequestPayloadActionDTOs] = None,
        idempotent_id: str = None,
        schedule_dto: main_models.CreateScheduleTaskRequestPayloadScheduleDTO = None,
    ):
        # Scheduling action parameters
        # 
        # This parameter is required.
        self.action_dtos = action_dtos
        # Idempotent ID
        self.idempotent_id = idempotent_id
        # Scheduling information
        # 
        # This parameter is required.
        self.schedule_dto = schedule_dto

    def validate(self):
        if self.action_dtos:
            for v1 in self.action_dtos:
                 if v1:
                    v1.validate()
        if self.schedule_dto:
            self.schedule_dto.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ActionDTOs'] = []
        if self.action_dtos is not None:
            for k1 in self.action_dtos:
                result['ActionDTOs'].append(k1.to_map() if k1 else None)

        if self.idempotent_id is not None:
            result['IdempotentId'] = self.idempotent_id

        if self.schedule_dto is not None:
            result['ScheduleDTO'] = self.schedule_dto.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.action_dtos = []
        if m.get('ActionDTOs') is not None:
            for k1 in m.get('ActionDTOs'):
                temp_model = main_models.CreateScheduleTaskRequestPayloadActionDTOs()
                self.action_dtos.append(temp_model.from_map(k1))

        if m.get('IdempotentId') is not None:
            self.idempotent_id = m.get('IdempotentId')

        if m.get('ScheduleDTO') is not None:
            temp_model = main_models.CreateScheduleTaskRequestPayloadScheduleDTO()
            self.schedule_dto = temp_model.from_map(m.get('ScheduleDTO'))

        return self

class CreateScheduleTaskRequestPayloadScheduleDTO(DaraModel):
    def __init__(
        self,
        once: main_models.CreateScheduleTaskRequestPayloadScheduleDTOOnce = None,
        schedule_end_time: int = None,
        schedule_start_time: int = None,
        schedule_type: str = None,
        statutory_working_day: main_models.CreateScheduleTaskRequestPayloadScheduleDTOStatutoryWorkingDay = None,
        weekly: main_models.CreateScheduleTaskRequestPayloadScheduleDTOWeekly = None,
    ):
        # One-time Scan Configuration
        self.once = once
        # Schedule end time
        # 
        # This parameter is required.
        self.schedule_end_time = schedule_end_time
        # Schedule Start Time
        # 
        # This parameter is required.
        self.schedule_start_time = schedule_start_time
        # Schedule Type
        # 
        # This parameter is required.
        self.schedule_type = schedule_type
        # Statutory working day schedule configuration
        self.statutory_working_day = statutory_working_day
        # Loop schedule configuration
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

        if self.schedule_end_time is not None:
            result['ScheduleEndTime'] = self.schedule_end_time

        if self.schedule_start_time is not None:
            result['ScheduleStartTime'] = self.schedule_start_time

        if self.schedule_type is not None:
            result['ScheduleType'] = self.schedule_type

        if self.statutory_working_day is not None:
            result['StatutoryWorkingDay'] = self.statutory_working_day.to_map()

        if self.weekly is not None:
            result['Weekly'] = self.weekly.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Once') is not None:
            temp_model = main_models.CreateScheduleTaskRequestPayloadScheduleDTOOnce()
            self.once = temp_model.from_map(m.get('Once'))

        if m.get('ScheduleEndTime') is not None:
            self.schedule_end_time = m.get('ScheduleEndTime')

        if m.get('ScheduleStartTime') is not None:
            self.schedule_start_time = m.get('ScheduleStartTime')

        if m.get('ScheduleType') is not None:
            self.schedule_type = m.get('ScheduleType')

        if m.get('StatutoryWorkingDay') is not None:
            temp_model = main_models.CreateScheduleTaskRequestPayloadScheduleDTOStatutoryWorkingDay()
            self.statutory_working_day = temp_model.from_map(m.get('StatutoryWorkingDay'))

        if m.get('Weekly') is not None:
            temp_model = main_models.CreateScheduleTaskRequestPayloadScheduleDTOWeekly()
            self.weekly = temp_model.from_map(m.get('Weekly'))

        return self

class CreateScheduleTaskRequestPayloadScheduleDTOWeekly(DaraModel):
    def __init__(
        self,
        days_of_week: List[int] = None,
        hours: List[int] = None,
        minutes: List[int] = None,
    ):
        # Trigger days of the week, where 1–7 represent Monday through Sunday, respectively
        self.days_of_week = days_of_week
        # Trigger hour
        self.hours = hours
        # Trigger minute
        self.minutes = minutes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.days_of_week is not None:
            result['DaysOfWeek'] = self.days_of_week

        if self.hours is not None:
            result['Hours'] = self.hours

        if self.minutes is not None:
            result['Minutes'] = self.minutes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DaysOfWeek') is not None:
            self.days_of_week = m.get('DaysOfWeek')

        if m.get('Hours') is not None:
            self.hours = m.get('Hours')

        if m.get('Minutes') is not None:
            self.minutes = m.get('Minutes')

        return self

class CreateScheduleTaskRequestPayloadScheduleDTOStatutoryWorkingDay(DaraModel):
    def __init__(
        self,
        hours: List[int] = None,
        minutes: List[int] = None,
    ):
        # Trigger hour; Multiple Choice
        self.hours = hours
        # Trigger minute; Multiple Choice
        self.minutes = minutes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hours is not None:
            result['Hours'] = self.hours

        if self.minutes is not None:
            result['Minutes'] = self.minutes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Hours') is not None:
            self.hours = m.get('Hours')

        if m.get('Minutes') is not None:
            self.minutes = m.get('Minutes')

        return self

class CreateScheduleTaskRequestPayloadScheduleDTOOnce(DaraModel):
    def __init__(
        self,
        day: int = None,
        hour: int = None,
        minute: int = None,
        month: int = None,
        year: int = None,
    ):
        # Trigger day
        self.day = day
        # Trigger Hour
        self.hour = hour
        # Trigger Minute
        self.minute = minute
        # Trigger Month
        self.month = month
        # Trigger Year
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

class CreateScheduleTaskRequestPayloadActionDTOs(DaraModel):
    def __init__(
        self,
        custom_action: Dict[str, Any] = None,
    ):
        # Vendor-defined command
        self.custom_action = custom_action

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_action is not None:
            result['customAction'] = self.custom_action

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('customAction') is not None:
            self.custom_action = m.get('customAction')

        return self

class CreateScheduleTaskRequestDeviceInfo(DaraModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # The value corresponding to the encoding type. When the encoding type is SKILL_ID, the value is the SkillID of the application. When the encoding type is PACKAGE_NAME, the value is the packageName of the corresponding client application.
        self.encode_key = encode_key
        # Encoding type. There are multiple ways to obtain the device identity for Maojing, and each method corresponds to a different encoding type: PACKAGE_NAME: APK package name, used for Android application customer linkage; SKILL_ID: skill ID, used for cloud linkage.
        self.encode_type = encode_type
        # Device ID (deviceOpenId or deviceUnionId)
        self.id = id
        # Type of device ID: OPEN_ID: default device ID; UNION_ID: organization-level device ID, available only after applying for an organization in the Maojing Skill Application Open Platform.
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

