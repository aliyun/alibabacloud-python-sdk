# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class ListUsersResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
        users: List[main_models.ListUsersResponseBodyUsers] = None,
    ):
        # The number of entries returned per page.
        self.max_results = max_results
        # The token used to retrieve the next page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count
        # The list of users.
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
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

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
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

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
        # The account expiration time. This is a Unix timestamp in milliseconds.
        self.account_expire_time = account_expire_time
        # The creation time. This is a Unix timestamp in milliseconds.
        self.create_time = create_time
        # The user description.
        self.description = description
        # The display name.
        self.display_name = display_name
        # The email address.
        self.email = email
        # Indicates whether the email address is verified. `true` means the user has verified the email address or an administrator has marked it as verified. `false` means the email address is not verified.
        self.email_verified = email_verified
        # The instance ID.
        self.instance_id = instance_id
        # The account lock expiration time. This is a Unix timestamp in milliseconds.
        self.lock_expire_time = lock_expire_time
        # The password expiration time. This is a Unix timestamp in milliseconds.
        self.password_expire_time = password_expire_time
        # Indicates whether a password is set.
        self.password_set = password_set
        # The phone number.
        self.phone_number = phone_number
        # Indicates whether the phone number is verified. `true` means the user has verified the phone number or an administrator has marked it as verified. `false` means the phone number is not verified.
        self.phone_number_verified = phone_number_verified
        # The country calling code. For example, specify `86` for Chinese mainland. Do not include `00` or a plus sign (+).
        self.phone_region = phone_region
        # The registration time. This is a Unix timestamp in milliseconds.
        self.register_time = register_time
        # The status. Valid values:
        # 
        # - `enabled`: The user is enabled.
        # 
        # - `disabled`: The user is disabled.
        self.status = status
        # The last update time. This is a Unix timestamp in milliseconds.
        self.update_time = update_time
        # The external user ID. This ID maps data from an external system to a user in IDaaS. It defaults to the user ID.
        # 
        # Note: The external user ID must be unique for the same source type and source ID.
        self.user_external_id = user_external_id
        # The user ID.
        self.user_id = user_id
        # The user source ID.
        # 
        # If the user is built-in, this is the instance ID. For users from other sources, this is the enterprise ID from the source, such as the `corpId` for a DingTalk organization.
        self.user_source_id = user_source_id
        # The user source type. Valid values:
        # 
        # - `build_in`: The user is a built-in user.
        # 
        # - `ding_talk`: The user is imported from DingTalk.
        # 
        # - `ad`: The user is imported from AD.
        # 
        # - `ldap`: The user is imported from LDAP.
        self.user_source_type = user_source_type
        # The user name.
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

