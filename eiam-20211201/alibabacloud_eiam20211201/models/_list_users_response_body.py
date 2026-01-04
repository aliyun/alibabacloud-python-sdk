# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class ListUsersResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        users: List[main_models.ListUsersResponseBodyUsers] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The number of entries in the list.
        self.total_count = total_count
        # The list of data objects of accounts.
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
        account_expire_time: int = None,
        create_time: int = None,
        description: str = None,
        display_name: str = None,
        email: str = None,
        email_verified: bool = None,
        instance_id: str = None,
        lock_expire_time: int = None,
        password_expire_time: int = None,
        password_set: bool = None,
        phone_number: str = None,
        phone_number_verified: bool = None,
        phone_region: str = None,
        register_time: int = None,
        status: str = None,
        update_time: int = None,
        user_external_id: str = None,
        user_id: str = None,
        user_source_id: str = None,
        user_source_type: str = None,
        username: str = None,
    ):
        # The time when the account expires. This value is a UNIX timestamp. Unit: milliseconds.
        self.account_expire_time = account_expire_time
        # The time when the account was created. This value is a UNIX timestamp. Unit: milliseconds.
        self.create_time = create_time
        # The description of the account.
        self.description = description
        # The display name of the account.
        self.display_name = display_name
        # The email address of the user who owns the account.
        self.email = email
        # Indicates whether the email address has been verified. A value of true indicates that the email address has been verified by the user or has been set to the verified status by the administrator. A value of false indicates that the email address has not been verified.
        self.email_verified = email_verified
        # The ID of the instance
        self.instance_id = instance_id
        # The time when the account lock expires. This value is a UNIX timestamp. Unit: milliseconds.
        self.lock_expire_time = lock_expire_time
        # Time When Password Expires
        self.password_expire_time = password_expire_time
        # Indicates whether a password is set.
        self.password_set = password_set
        # The mobile number of the user who owns the account.
        self.phone_number = phone_number
        # Indicates whether the mobile number has been verified. A value of true indicates that the mobile number has been verified by the user or has been set to the verified status by the administrator. A value of false indicates that the mobile number has not been verified.
        self.phone_number_verified = phone_number_verified
        # The country code of the mobile number. For example, the country code of China is 86 without 00 or +.
        self.phone_region = phone_region
        # The time when the account was registered. This value is a UNIX timestamp. Unit: milliseconds.
        self.register_time = register_time
        # The status of the account. Valid values:
        # 
        # *   enabled: The account is enabled.
        # *   disabled: The account is disabled.
        self.status = status
        # The time when the account was last updated. The value is a UNIX timestamp. Unit: milliseconds.
        self.update_time = update_time
        # The external ID of the account. The external ID can be used by external data to map the data of the account in IDaaS EIAM. By default, the external ID is the account ID.
        # 
        # For accounts with the same source type and source ID, each account has a unique external ID.
        self.user_external_id = user_external_id
        # The ID of the account.
        self.user_id = user_id
        # The source ID of the account.
        # 
        # If the account was created in IDaaS, its source ID is the ID of the IDaaS instance. If the account was imported, its source ID is the enterprise ID in the source. For example, if the account was imported from DingTalk, its source ID is the corpId value of the enterprise in DingTalk.
        self.user_source_id = user_source_id
        # The source type of the account. Valid values:
        # 
        # *   build_in: The account was created in IDaaS.
        # *   ding_talk: The account was imported from DingTalk.
        # *   ad: The account was imported from Microsoft Active Directory (AD).
        # *   ldap: The account was imported from a Lightweight Directory Access Protocol (LDAP) service.
        self.user_source_type = user_source_type
        # The username of the account.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_expire_time is not None:
            result['AccountExpireTime'] = self.account_expire_time

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.email is not None:
            result['Email'] = self.email

        if self.email_verified is not None:
            result['EmailVerified'] = self.email_verified

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.lock_expire_time is not None:
            result['LockExpireTime'] = self.lock_expire_time

        if self.password_expire_time is not None:
            result['PasswordExpireTime'] = self.password_expire_time

        if self.password_set is not None:
            result['PasswordSet'] = self.password_set

        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        if self.phone_number_verified is not None:
            result['PhoneNumberVerified'] = self.phone_number_verified

        if self.phone_region is not None:
            result['PhoneRegion'] = self.phone_region

        if self.register_time is not None:
            result['RegisterTime'] = self.register_time

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.user_external_id is not None:
            result['UserExternalId'] = self.user_external_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_source_id is not None:
            result['UserSourceId'] = self.user_source_id

        if self.user_source_type is not None:
            result['UserSourceType'] = self.user_source_type

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountExpireTime') is not None:
            self.account_expire_time = m.get('AccountExpireTime')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('EmailVerified') is not None:
            self.email_verified = m.get('EmailVerified')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LockExpireTime') is not None:
            self.lock_expire_time = m.get('LockExpireTime')

        if m.get('PasswordExpireTime') is not None:
            self.password_expire_time = m.get('PasswordExpireTime')

        if m.get('PasswordSet') is not None:
            self.password_set = m.get('PasswordSet')

        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        if m.get('PhoneNumberVerified') is not None:
            self.phone_number_verified = m.get('PhoneNumberVerified')

        if m.get('PhoneRegion') is not None:
            self.phone_region = m.get('PhoneRegion')

        if m.get('RegisterTime') is not None:
            self.register_time = m.get('RegisterTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UserExternalId') is not None:
            self.user_external_id = m.get('UserExternalId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserSourceId') is not None:
            self.user_source_id = m.get('UserSourceId')

        if m.get('UserSourceType') is not None:
            self.user_source_type = m.get('UserSourceType')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

