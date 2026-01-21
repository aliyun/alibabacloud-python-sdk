# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yundun_bastionhost20191209 import models as main_models
from darabonba.model import DaraModel

class GetUserResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        user: main_models.GetUserResponseBodyUser = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The detailed information about the queried user.
        self.user = user

    def validate(self):
        if self.user:
            self.user.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.user is not None:
            result['User'] = self.user.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('User') is not None:
            temp_model = main_models.GetUserResponseBodyUser()
            self.user = temp_model.from_map(m.get('User'))

        return self

class GetUserResponseBodyUser(DaraModel):
    def __init__(
        self,
        comment: str = None,
        display_name: str = None,
        effective_end_time: int = None,
        effective_start_time: int = None,
        email: str = None,
        language: str = None,
        language_status: str = None,
        mobile: str = None,
        mobile_country_code: str = None,
        need_reset_password: bool = None,
        source: str = None,
        source_user_id: str = None,
        two_factor_methods: List[str] = None,
        two_factor_status: str = None,
        user_id: str = None,
        user_name: str = None,
        user_state: List[str] = None,
    ):
        # The description of the user.
        self.comment = comment
        # The display name of the user.
        self.display_name = display_name
        # The end of the validity period of the user. The value is a UNIX timestamp. Unit: seconds.
        self.effective_end_time = effective_end_time
        # The beginning of the validity period of the user. The value is a UNIX timestamp. Unit: seconds.
        self.effective_start_time = effective_start_time
        # The email address of the user.
        self.email = email
        # This parameter is required if LanguageStatus is set to Custom.
        # 
        # - **zh-cn**: simplified Chinese.
        # - **en**: English.
        self.language = language
        # Indicates whether notifications are sent in the language specified in the global settings or a custom language.
        # 
        # *   **Global**: Global
        # *   **Custom**: Custom
        self.language_status = language_status
        # The mobile phone number of the user.
        self.mobile = mobile
        # The location in which the mobile number of the user is registered. Valid values:
        # 
        # *   **CN**: the Chinese mainland, whose country calling code is +86
        # *   **HK**: Hong Kong (China), whose country calling code is +852
        # *   **MO**: Macao (China), whose country calling code is +853
        # *   **TW**: Taiwan (China), whose country calling code is +886
        # *   **RU**: Russia, whose country calling code is +7
        # *   **SG**: Singapore, whose country calling code is +65
        # *   **MY**: Malaysia, whose country calling code is +60
        # *   **ID**: Indonesia, whose country calling code is +62
        # *   **DE**: Germany, whose country calling code is +49
        # *   **AU**: Australia, whose country calling code is +61
        # *   **US**: US, whose country calling code is +1
        # *   **AE**: United Arab Emirates, whose country calling code is +971
        # *   **JP:** Japan, whose country calling code is +81
        # *   **GB**: UK, whose country calling code is +44
        # *   **IN**: India, whose country calling code is +91
        # *   **KR**: Republic of Korea, whose country calling code is +82
        # *   **PH**: Philippines, whose country calling code is +63
        # *   **CH**: Switzerland, whose country calling code is +41
        # *   **SE**: Sweden, whose country calling code is +46
        self.mobile_country_code = mobile_country_code
        # Specifies whether password reset is required upon the next logon. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.need_reset_password = need_reset_password
        # The source of the user. Valid values:
        # 
        # *   **Local**: a local user
        # *   **Ram**: a RAM user
        self.source = source
        # The unique ID of the user.
        # 
        # > This parameter uniquely identifies a RAM user of the bastion host. A value is returned for this parameter if the **Source** parameter is set to **Ram**. No value is returned for this parameter if the **Source** parameter is set to **Local**.
        self.source_user_id = source_user_id
        # An array that consists of the details of the two-factor authentication method.
        self.two_factor_methods = two_factor_methods
        # The two-factor authentication status of the user. Valid values:
        # 
        # *   **Global**: The global settings are used.
        # *   **Disable**: The two-factor authentication is disabled.
        # *   **Enable**: The two-factor authentication is enabled and the user-specific setting is used.
        self.two_factor_status = two_factor_status
        # The ID of the user.
        self.user_id = user_id
        # The logon name of the user.
        self.user_name = user_name
        # An array that consists of the details of the user status.
        self.user_state = user_state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.effective_end_time is not None:
            result['EffectiveEndTime'] = self.effective_end_time

        if self.effective_start_time is not None:
            result['EffectiveStartTime'] = self.effective_start_time

        if self.email is not None:
            result['Email'] = self.email

        if self.language is not None:
            result['Language'] = self.language

        if self.language_status is not None:
            result['LanguageStatus'] = self.language_status

        if self.mobile is not None:
            result['Mobile'] = self.mobile

        if self.mobile_country_code is not None:
            result['MobileCountryCode'] = self.mobile_country_code

        if self.need_reset_password is not None:
            result['NeedResetPassword'] = self.need_reset_password

        if self.source is not None:
            result['Source'] = self.source

        if self.source_user_id is not None:
            result['SourceUserId'] = self.source_user_id

        if self.two_factor_methods is not None:
            result['TwoFactorMethods'] = self.two_factor_methods

        if self.two_factor_status is not None:
            result['TwoFactorStatus'] = self.two_factor_status

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_name is not None:
            result['UserName'] = self.user_name

        if self.user_state is not None:
            result['UserState'] = self.user_state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('EffectiveEndTime') is not None:
            self.effective_end_time = m.get('EffectiveEndTime')

        if m.get('EffectiveStartTime') is not None:
            self.effective_start_time = m.get('EffectiveStartTime')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('LanguageStatus') is not None:
            self.language_status = m.get('LanguageStatus')

        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')

        if m.get('MobileCountryCode') is not None:
            self.mobile_country_code = m.get('MobileCountryCode')

        if m.get('NeedResetPassword') is not None:
            self.need_reset_password = m.get('NeedResetPassword')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SourceUserId') is not None:
            self.source_user_id = m.get('SourceUserId')

        if m.get('TwoFactorMethods') is not None:
            self.two_factor_methods = m.get('TwoFactorMethods')

        if m.get('TwoFactorStatus') is not None:
            self.two_factor_status = m.get('TwoFactorStatus')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        if m.get('UserState') is not None:
            self.user_state = m.get('UserState')

        return self

