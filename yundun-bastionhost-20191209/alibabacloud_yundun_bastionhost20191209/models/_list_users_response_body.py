# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yundun_bastionhost20191209 import models as main_models
from darabonba.model import DaraModel

class ListUsersResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        users: List[main_models.ListUsersResponseBodyUsers] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The total number of users returned.
        self.total_count = total_count
        # The list of users returned.
        self.users = users

    def validate(self):
        if self.users:
            for v1 in self.users:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['Users'] = []
        if self.users is not None:
            for k1 in self.users:
                result['Users'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.users = []
        if m.get('Users') is not None:
            for k1 in m.get('Users'):
                temp_model = main_models.ListUsersResponseBodyUsers()
                self.users.append(temp_model.from_map(k1))

        return self

class ListUsersResponseBodyUsers(DaraModel):
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
        # The remarks of the user.
        self.comment = comment
        # The display name of the user.
        self.display_name = display_name
        # The end time of the validity period of the user, in seconds (UNIX timestamp format).
        self.effective_end_time = effective_end_time
        # The start time of the validity period of the user, in seconds (UNIX timestamp format).
        self.effective_start_time = effective_start_time
        # The email address of the user.
        self.email = email
        # The language for message notifications. This parameter is required when LanguageStatus is set to Custom. Valid values:
        # 
        # - **zh-cn**: Simplified Chinese
        # - **en**: English
        self.language = language
        # The language setting for message notifications. Valid values:
        # 
        # - **Global**: follows the global settings
        # - **Custom**: custom
        self.language_status = language_status
        # The mobile phone number of the user.
        self.mobile = mobile
        # The country code of the mobile phone number of the user. Valid values:
        # - **CN**: the Chinese mainland (+86)
        # - **HK**: Hong Kong (China) (+852)
        # - **MO**: Macao (China) (+853)
        # - **TW**: Taiwan (China) (+886)
        # - **RU**: Russia (+7)
        # - **SG**: Singapore (+65)
        # - **MY**: Malaysia (+60)
        # - **ID**: Indonesia (+62)
        # - **DE**: Germany (+49)
        # - **AU**: Australia (+61)
        # - **US**: United States (+1)
        # - **AE**: Dubai (+971)
        # - **JP**: Japan (+81)
        # - **GB**: United Kingdom (+44)
        # - **IN**: India (+91)
        # - **KR**: South Korea (+82)
        # - **PH**: Philippines (+63)
        # - **CH**: Switzerland (+41)
        # - **SE**: Sweden (+46)
        self.mobile_country_code = mobile_country_code
        # Indicates whether the password must be reset upon next logon. Valid values:
        # 
        # - **true**: The password must be reset.
        # - **false**: The password does not need to be reset.
        self.need_reset_password = need_reset_password
        # The source of the user. Valid values:
        # - **Local**: local user
        # - **Ram**: Resource Access Management (RAM) user
        # - **AD**: AD user
        # - **LDAP**: LDAP user
        self.source = source
        # The unique identity of the user.
        # > This parameter is the unique identity of the Resource Access Management (RAM) user that corresponds to the bastion host user. This parameter is returned when the user source is a RAM user (that is, **Source** is set to **Ram**). If the user source is a local user (that is, **Source** is set to **Local**), this parameter is empty.
        self.source_user_id = source_user_id
        # The array of enabled two-factor authentication methods.
        self.two_factor_methods = two_factor_methods
        # The two-factor authentication status of the user. Valid values:
        # 
        # - **Global**: follows the global settings
        # - **Disable**: two-factor authentication disabled
        # - **Enable**: two-factor authentication enabled, follows individual user settings
        self.two_factor_status = two_factor_status
        # The user ID.
        self.user_id = user_id
        # The logon name of the user.
        self.user_name = user_name
        # The user status array.
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

