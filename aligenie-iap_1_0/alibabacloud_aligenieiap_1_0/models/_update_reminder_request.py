# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aligenieiap_1_0 import models as main_models
from darabonba.model import DaraModel

class UpdateReminderRequest(DaraModel):
    def __init__(
        self,
        device_info: main_models.UpdateReminderRequestDeviceInfo = None,
        payload: main_models.UpdateReminderRequestPayload = None,
        user_info: main_models.UpdateReminderRequestUserInfo = None,
    ):
        # Device identity information.
        # 
        # This parameter is required.
        self.device_info = device_info
        # The input parameters for this service request.
        # 
        # This parameter is required.
        self.payload = payload
        # User identifier information.
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
            temp_model = main_models.UpdateReminderRequestDeviceInfo()
            self.device_info = temp_model.from_map(m.get('DeviceInfo'))

        if m.get('Payload') is not None:
            temp_model = main_models.UpdateReminderRequestPayload()
            self.payload = temp_model.from_map(m.get('Payload'))

        if m.get('UserInfo') is not None:
            temp_model = main_models.UpdateReminderRequestUserInfo()
            self.user_info = temp_model.from_map(m.get('UserInfo'))

        return self

class UpdateReminderRequestUserInfo(DaraModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # Value corresponding to the encoding type.  
        # 
        # - When the encoding type is set to SKILL_ID, the value is the application\\"s Skill ID.  
        # - When the encoding type is set to PACKAGE_NAME, the value is the packageName of the corresponding client app.
        # 
        # This parameter is required.
        self.encode_key = encode_key
        # Encoding type. There are multiple ways to obtain the user identifier for Maojing, and each method corresponds to a different encoding type.  
        # - PACKAGE_NAME: APK package name, used in the Android application customer link.  
        # - SKILL_ID: Skill ID, used in the cloud link.
        # 
        # This parameter is required.
        self.encode_type = encode_type
        # User identifier, set to either userOpenId or userUnionId.
        # 
        # This parameter is required.
        self.id = id
        # Type of User ID  
        # - OPEN_ID: The default User ID identifier.  
        # - UNION_ID: The organization-dimension User ID identifier. This value is available only after an organization has been requested on the Tmall Genie Skill Application Open Platform.
        # 
        # This parameter is required.
        self.id_type = id_type
        # Organization ID. This parameter is required when **IdType** is set to **UNION_ID**.
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

class UpdateReminderRequestPayload(DaraModel):
    def __init__(
        self,
        content: str = None,
        id: int = None,
        is_debug: bool = None,
        recurrence_rule: main_models.UpdateReminderRequestPayloadRecurrenceRule = None,
    ):
        # The detailed content of the reminder message.
        # 
        # This parameter is required.
        self.content = content
        # The ID of the reminder to update.
        # 
        # This parameter is required.
        self.id = id
        # Indicates whether this invocation is for debugging.
        # 
        # This parameter is required.
        self.is_debug = is_debug
        # Scheduling information for the reminder.
        # 
        # This parameter is required.
        self.recurrence_rule = recurrence_rule

    def validate(self):
        if self.recurrence_rule:
            self.recurrence_rule.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.id is not None:
            result['Id'] = self.id

        if self.is_debug is not None:
            result['IsDebug'] = self.is_debug

        if self.recurrence_rule is not None:
            result['RecurrenceRule'] = self.recurrence_rule.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IsDebug') is not None:
            self.is_debug = m.get('IsDebug')

        if m.get('RecurrenceRule') is not None:
            temp_model = main_models.UpdateReminderRequestPayloadRecurrenceRule()
            self.recurrence_rule = temp_model.from_map(m.get('RecurrenceRule'))

        return self

class UpdateReminderRequestPayloadRecurrenceRule(DaraModel):
    def __init__(
        self,
        day: int = None,
        days_of_month: List[int] = None,
        days_of_week: List[int] = None,
        end_date_time: int = None,
        freq: str = None,
        hour: int = None,
        minute: int = None,
        month: int = None,
        second: int = None,
        start_date_time: int = None,
        year: int = None,
    ):
        # The date on which the reminder is triggered.
        self.day = day
        # Configure monthly reminders, specifying on which day(s) of each month the reminder is triggered.
        self.days_of_month = days_of_month
        # Configure weekly reminders, indicating on which days of the week the reminder is triggered.
        self.days_of_week = days_of_week
        # The expiration time when the reminder ends, in milliseconds as a UNIX timestamp.
        # 
        # This parameter is required.
        self.end_date_time = end_date_time
        # Recurrence type:
        # 
        # - ONCE: One-time
        # - DAILY: Daily
        # - WEEKLY: Weekly
        # - MONTHLY: Monthly
        # 
        # This parameter is required.
        self.freq = freq
        # The hour of the time when the reminder is triggered.
        # 
        # This parameter is required.
        self.hour = hour
        # The minute of the time when the reminder is triggered.
        self.minute = minute
        # The month in which the reminder is triggered.
        self.month = month
        # The second of the time when the reminder is triggered.
        self.second = second
        # The effective start time of the reminder, in milliseconds as a UNIX timestamp.
        # 
        # This parameter is required.
        self.start_date_time = start_date_time
        # The year of the time when the reminder is triggered.
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

        if self.days_of_month is not None:
            result['DaysOfMonth'] = self.days_of_month

        if self.days_of_week is not None:
            result['DaysOfWeek'] = self.days_of_week

        if self.end_date_time is not None:
            result['EndDateTime'] = self.end_date_time

        if self.freq is not None:
            result['Freq'] = self.freq

        if self.hour is not None:
            result['Hour'] = self.hour

        if self.minute is not None:
            result['Minute'] = self.minute

        if self.month is not None:
            result['Month'] = self.month

        if self.second is not None:
            result['Second'] = self.second

        if self.start_date_time is not None:
            result['StartDateTime'] = self.start_date_time

        if self.year is not None:
            result['Year'] = self.year

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Day') is not None:
            self.day = m.get('Day')

        if m.get('DaysOfMonth') is not None:
            self.days_of_month = m.get('DaysOfMonth')

        if m.get('DaysOfWeek') is not None:
            self.days_of_week = m.get('DaysOfWeek')

        if m.get('EndDateTime') is not None:
            self.end_date_time = m.get('EndDateTime')

        if m.get('Freq') is not None:
            self.freq = m.get('Freq')

        if m.get('Hour') is not None:
            self.hour = m.get('Hour')

        if m.get('Minute') is not None:
            self.minute = m.get('Minute')

        if m.get('Month') is not None:
            self.month = m.get('Month')

        if m.get('Second') is not None:
            self.second = m.get('Second')

        if m.get('StartDateTime') is not None:
            self.start_date_time = m.get('StartDateTime')

        if m.get('Year') is not None:
            self.year = m.get('Year')

        return self

class UpdateReminderRequestDeviceInfo(DaraModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # The value corresponding to the encoding type.
        # 
        # - When the encoding type is set to SKILL_ID, the value is the application\\"s Skill ID.
        # - When the encoding type is set to PACKAGE_NAME, the value is the packageName of the corresponding client app.
        # 
        # This parameter is required.
        self.encode_key = encode_key
        # Encoding type. There are multiple ways to obtain the device identity for Tmall Genie, and each method corresponds to a different encoding type.  
        # - PACKAGE_NAME: APK package name, used in the Android application customer flow.  
        # - SKILL_ID: Skill ID, used in the cloud-based flow.
        # 
        # This parameter is required.
        self.encode_type = encode_type
        # Device ID, set to either deviceOpenId or deviceUnionId.
        # 
        # This parameter is required.
        self.id = id
        # Type of the device ID.  
        # - OPEN_ID: Default device ID.  
        # - UNION_ID: Organization-level device ID. This value is available only after an organization has been registered on the Tmall Genie skill application platform.
        # 
        # This parameter is required.
        self.id_type = id_type
        # Organization ID. This parameter is required when **IdType** is set to **UNION_ID**.
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

