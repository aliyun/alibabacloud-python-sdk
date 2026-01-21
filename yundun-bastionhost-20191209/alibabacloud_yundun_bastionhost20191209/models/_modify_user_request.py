# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyUserRequest(DaraModel):
    def __init__(
        self,
        comment: str = None,
        display_name: str = None,
        effective_end_time: int = None,
        effective_start_time: int = None,
        email: str = None,
        instance_id: str = None,
        language: str = None,
        language_status: str = None,
        mobile: str = None,
        mobile_country_code: str = None,
        need_reset_password: bool = None,
        password: str = None,
        region_id: str = None,
        two_factor_methods: str = None,
        two_factor_status: str = None,
        user_id: str = None,
    ):
        # The new remarks of the user. The remarks can be up to 500 characters in length.
        # 
        # >  Leave this parameter empty if you do not want to change the remarks of the user.
        self.comment = comment
        # The new display name of the user. The display name can be up to 128 characters in length.
        # 
        # >  Leave this parameter empty if you do not want to change the display name of the user.
        self.display_name = display_name
        # The end time of the validity period of the user. Specify a UNIX timestamp. Unit: seconds.
        # 
        # >  Leave this parameter empty if you do not want to change the end time of the validity period.
        self.effective_end_time = effective_end_time
        # The start time of the validity period of the user. Specify a UNIX timestamp. Unit: seconds.
        # 
        # >  Leave this parameter empty if you do not want to change the start time of the validity period.
        self.effective_start_time = effective_start_time
        # The new email address of the user.
        # 
        # > 
        # 
        # *   This parameter is required if TwoFactorStatus is set to Enable and TwoFactorMethods is set to email, or if TwoFactorStatus is set to Global and TwoFactorMethods is set to email in the global two-factor authentication settings.
        # 
        # *   You can call the [GetInstanceTwoFactor](https://help.aliyun.com/document_detail/462968.html) operation to query the global two-factor authentication settings.
        # 
        # *   Leave this parameter empty if you do not want to change the email address of the user.
        self.email = email
        # The ID of the bastion host on which you want to modify the information about the user.
        # 
        # >  You can call the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to query the bastion host ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required if LanguageStatus is set to Custom.
        # 
        # - **zh-cn**: simplified Chinese
        # - **en**: English
        self.language = language
        # Specifies whether to send notifications in the language specified in the global settings or a custom language.
        # 
        # *   **Global**
        # *   **Custom**
        # 
        # >  Leave this parameter empty if you do not want to change the natural language used to notify the user.
        self.language_status = language_status
        # The new mobile phone number of the user.
        # 
        # > 
        # 
        # *   This parameter is required if TwoFactorStatus is set to Enable and TwoFactorMethods is set to sms or dingtalk, or if TwoFactorStatus is set to Global and TwoFactorMethods is set to sms or dingtalk in the global two-factor authentication settings.
        # 
        # *   You can call the [GetInstanceTwoFactor](https://help.aliyun.com/document_detail/462968.html) operation to query the global two-factor authentication settings.
        # 
        # *   Leave this parameter empty if you do not want to change the mobile phone number of the user.
        self.mobile = mobile
        # The country where the new mobile number of the user is registered. Valid values:
        # 
        # *   **CN:** the Chinese mainland, whose country calling code is +86
        # *   **HK:** Hong Kong (China), whose country calling code is +852
        # *   **MO:** Macao (China), whose country calling code is +853
        # *   **TW:** Taiwan (China), whose country calling code is +886
        # *   **RU:** Russia, whose country calling code is +7
        # *   **SG:** Singapore, whose country calling code is +65
        # *   **MY:** Malaysia, whose country calling code is +60
        # *   **ID:** Indonesia, whose country calling code is +62
        # *   **DE:** Germany, whose country calling code is +49
        # *   **AU:** Australia, whose country calling code is +61
        # *   **US:** US, whose country calling code is +1
        # *   **AE:** United Arab Emirates, whose country calling code is +971
        # *   **JP:** Japan, whose country calling code is +81
        # *   **GB:** UK, whose country calling code is +44
        # *   **IN:** India, whose country calling code is +91
        # *   **KR:** Republic of Korea, whose country calling code is +82
        # *   **PH:** Philippines, whose country calling code is +63
        # *   **CH:** Switzerland, whose country calling code is +41
        # *   **SE:** Sweden, whose country calling code is +46
        # *   **SA:** Saudi Arabia, whose country calling code is +966
        self.mobile_country_code = mobile_country_code
        # Specifies whether password reset is required upon the next logon. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # >  Leave this parameter empty if you do not want to change the password reset settings for the user.
        self.need_reset_password = need_reset_password
        # The new password of the user. The password must be 8 to 128 characters in length. It must contain uppercase letters, lowercase letters, digits, and special characters.
        # 
        # > Leave this parameter empty if you do not want to change the password of the user.
        self.password = password
        # The region ID of the bastion host on which you want to modify the information about the user.
        # 
        # >  For more information about the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id
        # The two-factor authentication method. You can select only one method. Valid values:
        # 
        # *   **sms**: text message-based two-factor authentication.
        # *   **email**: email-based two-factor authentication.
        # *   **dingtalk**: DingTalk-based two-factor authentication.
        # *   **totp OTP:** one-time password (OTP) token-based two-factor authentication.
        # 
        # >  If TwoFactorStatus is set to Enable, you must specify one of the valid values as TwoFactorMethods.
        self.two_factor_methods = two_factor_methods
        # Specifies whether two-factor authentication is enabled for the user. Valid values:
        # 
        # *   **Global**: The global settings apply.
        # *   **Disable**: Two-factor authentication is disabled.
        # *   **Enable**: Two-factor authentication is enabled and user-specific settings apply.
        # 
        # >  Leave this parameter empty if you do not want to change the two-factory authentication settings for the user.
        self.two_factor_status = two_factor_status
        # The ID of the user whose information you want to modify.
        # 
        # >  You can call the [ListUsers](https://help.aliyun.com/document_detail/204522.html) operation to query the user ID.
        # 
        # This parameter is required.
        self.user_id = user_id

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

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

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

        if self.password is not None:
            result['Password'] = self.password

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.two_factor_methods is not None:
            result['TwoFactorMethods'] = self.two_factor_methods

        if self.two_factor_status is not None:
            result['TwoFactorStatus'] = self.two_factor_status

        if self.user_id is not None:
            result['UserId'] = self.user_id

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

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

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

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TwoFactorMethods') is not None:
            self.two_factor_methods = m.get('TwoFactorMethods')

        if m.get('TwoFactorStatus') is not None:
            self.two_factor_status = m.get('TwoFactorStatus')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

