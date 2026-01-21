# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateUserRequest(DaraModel):
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
        source: str = None,
        source_user_id: str = None,
        two_factor_methods: str = None,
        two_factor_status: str = None,
        user_name: str = None,
    ):
        # The remarks of the user that you want to add. The remarks can be up to 500 characters in length.
        self.comment = comment
        # The display name of the user that you want to add. The display name can be up to 128 characters in length.
        # 
        # >  If you leave this parameter empty, the logon name is used as the display name.
        self.display_name = display_name
        # The end time of the validity period of the user. Specify a UNIX timestamp. Unit: seconds.
        self.effective_end_time = effective_end_time
        # The start time of the validity period of the user. Specify a UNIX timestamp. Unit: seconds.
        self.effective_start_time = effective_start_time
        # The email address of the user that you want to add.
        # 
        # > 
        # 
        # *   This parameter is required if TwoFactorStatus is set to Enable and TwoFactorMethods is set to email, or if TwoFactorStatus is set to Global and TwoFactorMethods is set to email in the global two-factor authentication settings.
        # 
        # *   You can call the [GetInstanceTwoFactor](https://help.aliyun.com/document_detail/462968.html) operation to query the global two-factor authentication settings.
        self.email = email
        # The ID of the bastion host to which you want to add a user.
        # 
        # > You can call the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to query the bastion host ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required if LanguageStatus is set to Custom. Valid values:
        # 
        # *   **zh-cn**: simplified Chinese.
        # *   **en**: English.
        self.language = language
        # Specifies whether to send notifications in the language specified in the global settings or a custom language.
        # 
        # *   **Global**
        # *   **Custom**
        # 
        # >  If you leave this parameter empty, the default value Global is used.
        self.language_status = language_status
        # The mobile phone number of the user that you want to add.
        # 
        # > 
        # 
        # *   This parameter is required if TwoFactorStatus is set to Enable and TwoFactorMethods is set to sms or dingtalk, or if TwoFactorStatus is set to Global and TwoFactorMethods is set to sms or dingtalk in the global two-factor authentication settings.
        # 
        # *   You can call the [GetInstanceTwoFactor](https://help.aliyun.com/document_detail/462968.html) operation to query the global two-factor authentication settings.
        self.mobile = mobile
        # The location where the mobile phone number of the user is registered. Default value: CN. Valid values:
        # 
        # *   **CN**: the Chinese mainland, whose international dialing code is +86.
        # *   **HK**: Hong Kong (China), whose international dialing code is +852.
        # *   **MO**: Macao (China), whose international dialing code is +853.
        # *   **TW**: Taiwan (China), whose international dialing code is +886.
        # *   **RU**: Russia, whose international dialing code is +7.
        # *   **SG**: Singapore, whose international dialing code is +65.
        # *   **MY**: Malaysia, whose international dialing code is +60.
        # *   **ID**: Indonesia, whose international dialing code is +62.
        # *   **DE**: Germany, whose international dialing code is +49.
        # *   **AU**: Australia, whose international dialing code is +61.
        # *   **US**: US, whose international dialing code is +1.
        # *   **AE**: United Arab Emirates, whose international dialing code is +971.
        # *   **JP**: Japan, whose international dialing code is +81.
        # *   **GB**: UK, whose international dialing code is +44.
        # *   **IN**: India, whose international dialing code is +91.
        # *   **KR**: Republic of Korea, whose international dialing code is +82.
        # *   **PH**: Philippines, whose international dialing code is +63.
        # *   **CH**: Switzerland, whose international dialing code is +41.
        # *   **SE:** Sweden, whose international dialing code is +46.
        # *   **SA:** Saudi Arabia, whose international dialing code is +966.
        self.mobile_country_code = mobile_country_code
        # Specifies whether password reset is required upon the next logon. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # >  If you leave this parameter empty, the default value false is used.
        self.need_reset_password = need_reset_password
        # The logon password of the user that you want to add. The logon password must be 8 to 128 characters in length. It must contain uppercase letters, lowercase letters, digits, and special characters.
        # 
        # > This parameter is required if Source is set to Local.
        self.password = password
        # The region ID of the bastion host to which you want to add a user.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id
        # The type of the user that you want to add. Valid values:
        # 
        # *   **Local**: a local user.
        # *   **Ram**: a RAM user.
        # *   **AD**: an AD-authenticated user.
        # *   **LDAP**: an LDAP-authenticated user.
        # 
        # This parameter is required.
        self.source = source
        # The unique ID of the user that you want to add.
        # 
        # > 
        # 
        # *   This parameter uniquely identifies a RAM user of the bastion host. This parameter is required if Source is set to Ram. You can call the [ListUsers](https://help.aliyun.com/document_detail/28684.html) operation in RAM to obtain the unique ID of the user from the UserId response parameter.
        # 
        # *   This parameter is required if Source is set to AD or LDAP. Specify the distinguished name (DN) of the Active Directory (AD)-authenticated user or Lightweight Directory Access Protocol (LDAP)-authenticated user that you want to add.
        self.source_user_id = source_user_id
        # The two-factor authentication method. You can select only one method. Valid values:
        # 
        # *   **sms**: text message-based two-factor authentication.
        # *   **email**: email-based two-factor authentication.
        # *   **dingtalk**: DingTalk-based two-factor authentication.
        # *   **totp OTP**: one-time password (OTP) token-based two-factor authentication.
        # 
        # >  If TwoFactorStatus is set to Enable, you must select one of the preceding values for TwoFactorMethods.
        self.two_factor_methods = two_factor_methods
        # Specifies whether two-factor authentication is enabled for the user. Valid values:
        # 
        # *   **Global**: The global settings apply.
        # *   **Disable**: Two-factor authentication is disabled.
        # *   **Enable**: Two-factor authentication is enabled and user-specific settings apply.
        # 
        # >  If you leave this parameter empty, the default value Global is used.
        self.two_factor_status = two_factor_status
        # The logon name of the user that you want to add. The logon name must be 1 to 128 characters in length and can contain only letters, digits, and underscores (_).
        # 
        # This parameter is required.
        self.user_name = user_name

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

        if self.source is not None:
            result['Source'] = self.source

        if self.source_user_id is not None:
            result['SourceUserId'] = self.source_user_id

        if self.two_factor_methods is not None:
            result['TwoFactorMethods'] = self.two_factor_methods

        if self.two_factor_status is not None:
            result['TwoFactorStatus'] = self.two_factor_status

        if self.user_name is not None:
            result['UserName'] = self.user_name

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

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SourceUserId') is not None:
            self.source_user_id = m.get('SourceUserId')

        if m.get('TwoFactorMethods') is not None:
            self.two_factor_methods = m.get('TwoFactorMethods')

        if m.get('TwoFactorStatus') is not None:
            self.two_factor_status = m.get('TwoFactorStatus')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

