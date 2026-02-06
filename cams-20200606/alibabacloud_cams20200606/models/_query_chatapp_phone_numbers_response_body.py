# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cams20200606 import models as main_models
from darabonba.model import DaraModel

class QueryChatappPhoneNumbersResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: str = None,
        message: str = None,
        phone_numbers: List[main_models.QueryChatappPhoneNumbersResponseBodyPhoneNumbers] = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        self.data = data
        # The message returned.
        self.message = message
        # The phone numbers.
        self.phone_numbers = phone_numbers
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success

    def validate(self):
        if self.phone_numbers:
            for v1 in self.phone_numbers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data

        if self.message is not None:
            result['Message'] = self.message

        result['PhoneNumbers'] = []
        if self.phone_numbers is not None:
            for k1 in self.phone_numbers:
                result['PhoneNumbers'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        self.phone_numbers = []
        if m.get('PhoneNumbers') is not None:
            for k1 in m.get('PhoneNumbers'):
                temp_model = main_models.QueryChatappPhoneNumbersResponseBodyPhoneNumbers()
                self.phone_numbers.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryChatappPhoneNumbersResponseBodyPhoneNumbers(DaraModel):
    def __init__(
        self,
        calling_configure: main_models.QueryChatappPhoneNumbersResponseBodyPhoneNumbersCallingConfigure = None,
        code_verification_status: str = None,
        is_official: str = None,
        messaging_limit_tier: str = None,
        name_status: str = None,
        new_name_status: str = None,
        phone_number: str = None,
        quality_rating: str = None,
        status: str = None,
        status_callback_url: str = None,
        status_queue: str = None,
        up_callback_url: str = None,
        up_queue: str = None,
        verified_name: str = None,
    ):
        self.calling_configure = calling_configure
        # The verification status of the phone number.
        # 
        # Valid values:
        # 
        # *   REVOKED: The review application is revoked.
        # *   MORE_INFORMATION_REQUESTED: More information needs to be provided.
        # *   VERIFIED: The phone number passes the verification.
        # *   REJECTED: The phone number fails to pass the verification.
        self.code_verification_status = code_verification_status
        # Indicates whether it is a WhatsApp Official Business Account (OBA).
        self.is_official = is_official
        # The number of phone numbers to which messages can be sent in a day.
        # 
        # Valid values:
        # 
        # *   TIER_100K: 100,000
        # *   TIER_UNLIMITED: unlimited
        # *   TIER_250: 250
        # *   TIER_1K: 1,000
        # *   TIER_50: 50
        # *   TIER_10K: 10,000
        self.messaging_limit_tier = messaging_limit_tier
        # The review status of the name.
        self.name_status = name_status
        # The review status of the new display name of the enterprise.
        self.new_name_status = new_name_status
        # The phone number.
        self.phone_number = phone_number
        # The quality rating of the phone number.
        # 
        # Valid values:
        # 
        # *   RED: low
        # *   YELLOW: medium
        # *   UNKNOWN: unknown
        # *   GREEN: high
        self.quality_rating = quality_rating
        # The state of the phone number.
        # 
        # Valid values:
        # 
        # *   MIGRATED
        # *   FLAGGED
        # *   DISCONNECTED
        # *   UNVERIFIED
        # *   BANNED
        # *   RATE_LIMITED
        # *   PENDING
        # *   CONNECTED
        # *   UNKNOWN
        # *   DELETED
        # *   RESTRICTED
        self.status = status
        # The URL that receives the status reports.
        self.status_callback_url = status_callback_url
        # The status report queue.
        self.status_queue = status_queue
        # The URL that receives the MO messages.
        self.up_callback_url = up_callback_url
        # The mobile originated (MO) message queue.
        self.up_queue = up_queue
        # The display name of the enterprise to which the phone number belongs.
        self.verified_name = verified_name

    def validate(self):
        if self.calling_configure:
            self.calling_configure.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.calling_configure is not None:
            result['CallingConfigure'] = self.calling_configure.to_map()

        if self.code_verification_status is not None:
            result['CodeVerificationStatus'] = self.code_verification_status

        if self.is_official is not None:
            result['IsOfficial'] = self.is_official

        if self.messaging_limit_tier is not None:
            result['MessagingLimitTier'] = self.messaging_limit_tier

        if self.name_status is not None:
            result['NameStatus'] = self.name_status

        if self.new_name_status is not None:
            result['NewNameStatus'] = self.new_name_status

        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        if self.quality_rating is not None:
            result['QualityRating'] = self.quality_rating

        if self.status is not None:
            result['Status'] = self.status

        if self.status_callback_url is not None:
            result['StatusCallbackUrl'] = self.status_callback_url

        if self.status_queue is not None:
            result['StatusQueue'] = self.status_queue

        if self.up_callback_url is not None:
            result['UpCallbackUrl'] = self.up_callback_url

        if self.up_queue is not None:
            result['UpQueue'] = self.up_queue

        if self.verified_name is not None:
            result['VerifiedName'] = self.verified_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallingConfigure') is not None:
            temp_model = main_models.QueryChatappPhoneNumbersResponseBodyPhoneNumbersCallingConfigure()
            self.calling_configure = temp_model.from_map(m.get('CallingConfigure'))

        if m.get('CodeVerificationStatus') is not None:
            self.code_verification_status = m.get('CodeVerificationStatus')

        if m.get('IsOfficial') is not None:
            self.is_official = m.get('IsOfficial')

        if m.get('MessagingLimitTier') is not None:
            self.messaging_limit_tier = m.get('MessagingLimitTier')

        if m.get('NameStatus') is not None:
            self.name_status = m.get('NameStatus')

        if m.get('NewNameStatus') is not None:
            self.new_name_status = m.get('NewNameStatus')

        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        if m.get('QualityRating') is not None:
            self.quality_rating = m.get('QualityRating')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusCallbackUrl') is not None:
            self.status_callback_url = m.get('StatusCallbackUrl')

        if m.get('StatusQueue') is not None:
            self.status_queue = m.get('StatusQueue')

        if m.get('UpCallbackUrl') is not None:
            self.up_callback_url = m.get('UpCallbackUrl')

        if m.get('UpQueue') is not None:
            self.up_queue = m.get('UpQueue')

        if m.get('VerifiedName') is not None:
            self.verified_name = m.get('VerifiedName')

        return self

class QueryChatappPhoneNumbersResponseBodyPhoneNumbersCallingConfigure(DaraModel):
    def __init__(
        self,
        calling: main_models.QueryChatappPhoneNumbersResponseBodyPhoneNumbersCallingConfigureCalling = None,
        calling_callback_url: str = None,
        max_talk_time: int = None,
    ):
        self.calling = calling
        self.calling_callback_url = calling_callback_url
        self.max_talk_time = max_talk_time

    def validate(self):
        if self.calling:
            self.calling.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.calling is not None:
            result['Calling'] = self.calling.to_map()

        if self.calling_callback_url is not None:
            result['CallingCallbackUrl'] = self.calling_callback_url

        if self.max_talk_time is not None:
            result['MaxTalkTime'] = self.max_talk_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Calling') is not None:
            temp_model = main_models.QueryChatappPhoneNumbersResponseBodyPhoneNumbersCallingConfigureCalling()
            self.calling = temp_model.from_map(m.get('Calling'))

        if m.get('CallingCallbackUrl') is not None:
            self.calling_callback_url = m.get('CallingCallbackUrl')

        if m.get('MaxTalkTime') is not None:
            self.max_talk_time = m.get('MaxTalkTime')

        return self

class QueryChatappPhoneNumbersResponseBodyPhoneNumbersCallingConfigureCalling(DaraModel):
    def __init__(
        self,
        call_hours: main_models.QueryChatappPhoneNumbersResponseBodyPhoneNumbersCallingConfigureCallingCallHours = None,
        status: str = None,
    ):
        self.call_hours = call_hours
        self.status = status

    def validate(self):
        if self.call_hours:
            self.call_hours.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_hours is not None:
            result['CallHours'] = self.call_hours.to_map()

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallHours') is not None:
            temp_model = main_models.QueryChatappPhoneNumbersResponseBodyPhoneNumbersCallingConfigureCallingCallHours()
            self.call_hours = temp_model.from_map(m.get('CallHours'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class QueryChatappPhoneNumbersResponseBodyPhoneNumbersCallingConfigureCallingCallHours(DaraModel):
    def __init__(
        self,
        call_icon_visibility: str = None,
        callback_permission_status: str = None,
        holiday_schedule: List[main_models.QueryChatappPhoneNumbersResponseBodyPhoneNumbersCallingConfigureCallingCallHoursHolidaySchedule] = None,
        status: str = None,
        timezone_id: str = None,
        weekly_operating_hours: List[main_models.QueryChatappPhoneNumbersResponseBodyPhoneNumbersCallingConfigureCallingCallHoursWeeklyOperatingHours] = None,
    ):
        self.call_icon_visibility = call_icon_visibility
        self.callback_permission_status = callback_permission_status
        self.holiday_schedule = holiday_schedule
        self.status = status
        self.timezone_id = timezone_id
        self.weekly_operating_hours = weekly_operating_hours

    def validate(self):
        if self.holiday_schedule:
            for v1 in self.holiday_schedule:
                 if v1:
                    v1.validate()
        if self.weekly_operating_hours:
            for v1 in self.weekly_operating_hours:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_icon_visibility is not None:
            result['CallIconVisibility'] = self.call_icon_visibility

        if self.callback_permission_status is not None:
            result['CallbackPermissionStatus'] = self.callback_permission_status

        result['HolidaySchedule'] = []
        if self.holiday_schedule is not None:
            for k1 in self.holiday_schedule:
                result['HolidaySchedule'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        if self.timezone_id is not None:
            result['TimezoneId'] = self.timezone_id

        result['WeeklyOperatingHours'] = []
        if self.weekly_operating_hours is not None:
            for k1 in self.weekly_operating_hours:
                result['WeeklyOperatingHours'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallIconVisibility') is not None:
            self.call_icon_visibility = m.get('CallIconVisibility')

        if m.get('CallbackPermissionStatus') is not None:
            self.callback_permission_status = m.get('CallbackPermissionStatus')

        self.holiday_schedule = []
        if m.get('HolidaySchedule') is not None:
            for k1 in m.get('HolidaySchedule'):
                temp_model = main_models.QueryChatappPhoneNumbersResponseBodyPhoneNumbersCallingConfigureCallingCallHoursHolidaySchedule()
                self.holiday_schedule.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TimezoneId') is not None:
            self.timezone_id = m.get('TimezoneId')

        self.weekly_operating_hours = []
        if m.get('WeeklyOperatingHours') is not None:
            for k1 in m.get('WeeklyOperatingHours'):
                temp_model = main_models.QueryChatappPhoneNumbersResponseBodyPhoneNumbersCallingConfigureCallingCallHoursWeeklyOperatingHours()
                self.weekly_operating_hours.append(temp_model.from_map(k1))

        return self

class QueryChatappPhoneNumbersResponseBodyPhoneNumbersCallingConfigureCallingCallHoursWeeklyOperatingHours(DaraModel):
    def __init__(
        self,
        close_time: str = None,
        day_of_week: str = None,
        open_time: str = None,
    ):
        self.close_time = close_time
        self.day_of_week = day_of_week
        self.open_time = open_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.close_time is not None:
            result['CloseTime'] = self.close_time

        if self.day_of_week is not None:
            result['DayOfWeek'] = self.day_of_week

        if self.open_time is not None:
            result['OpenTime'] = self.open_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloseTime') is not None:
            self.close_time = m.get('CloseTime')

        if m.get('DayOfWeek') is not None:
            self.day_of_week = m.get('DayOfWeek')

        if m.get('OpenTime') is not None:
            self.open_time = m.get('OpenTime')

        return self

class QueryChatappPhoneNumbersResponseBodyPhoneNumbersCallingConfigureCallingCallHoursHolidaySchedule(DaraModel):
    def __init__(
        self,
        date: str = None,
        end_time: str = None,
        start_time: str = None,
    ):
        self.date = date
        self.end_time = end_time
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date is not None:
            result['Date'] = self.date

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

