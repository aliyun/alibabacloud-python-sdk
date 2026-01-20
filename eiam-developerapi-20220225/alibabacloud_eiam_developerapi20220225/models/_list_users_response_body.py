# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam_developerapi20220225 import models as main_models
from darabonba.model import DaraModel

class ListUsersResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListUsersResponseBodyData] = None,
        total_count: int = None,
    ):
        # The queried EIAM accounts.
        self.data = data
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.ListUsersResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListUsersResponseBodyData(DaraModel):
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
        # The time when the account expires. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.account_expire_time = account_expire_time
        # The time when the account was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_time = create_time
        self.description = description
        # The display name of the account.
        self.display_name = display_name
        # The email address of the user who owns the account.
        self.email = email
        # Indicates whether the email address has been verified. A value of true indicates that the email address has been verified by the user or has been set to the verified status by the administrator. A value of false indicates that the email address has not been verified.
        self.email_verified = email_verified
        # The instance ID.
        self.instance_id = instance_id
        # The time when the account lock expires. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.lock_expire_time = lock_expire_time
        self.password_set = password_set
        # The mobile number of the user who owns the account.
        self.phone_number = phone_number
        # Indicates whether the mobile number has been verified. A value of true indicates that the mobile number has been verified by the user or has been set to the verified status by the administrator. A value of false indicates that the mobile number has not been verified.
        self.phone_number_verified = phone_number_verified
        # The country code of the mobile number. For example, the country code of China is 86 without 00 or +.
        self.phone_region = phone_region
        # The time when the account was registered. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.register_time = register_time
        # The status of the account. Valid values: enabled disabled
        self.status = status
        # The time when the account was last modified. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.update_time = update_time
        # The external ID of the account. The external ID can be used to map external data to the data of the account in EIAM of Identity as a Service (IDaaS). By default, the external ID is the account ID.
        # 
        # Note: For accounts with the same source type and source ID, each account has a unique external ID.
        self.user_external_id = user_external_id
        # The account ID.
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
            result['accountExpireTime'] = self.account_expire_time

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.description is not None:
            result['description'] = self.description

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.email is not None:
            result['email'] = self.email

        if self.email_verified is not None:
            result['emailVerified'] = self.email_verified

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.lock_expire_time is not None:
            result['lockExpireTime'] = self.lock_expire_time

        if self.password_set is not None:
            result['passwordSet'] = self.password_set

        if self.phone_number is not None:
            result['phoneNumber'] = self.phone_number

        if self.phone_number_verified is not None:
            result['phoneNumberVerified'] = self.phone_number_verified

        if self.phone_region is not None:
            result['phoneRegion'] = self.phone_region

        if self.register_time is not None:
            result['registerTime'] = self.register_time

        if self.status is not None:
            result['status'] = self.status

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        if self.user_external_id is not None:
            result['userExternalId'] = self.user_external_id

        if self.user_id is not None:
            result['userId'] = self.user_id

        if self.user_source_id is not None:
            result['userSourceId'] = self.user_source_id

        if self.user_source_type is not None:
            result['userSourceType'] = self.user_source_type

        if self.username is not None:
            result['username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountExpireTime') is not None:
            self.account_expire_time = m.get('accountExpireTime')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('email') is not None:
            self.email = m.get('email')

        if m.get('emailVerified') is not None:
            self.email_verified = m.get('emailVerified')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('lockExpireTime') is not None:
            self.lock_expire_time = m.get('lockExpireTime')

        if m.get('passwordSet') is not None:
            self.password_set = m.get('passwordSet')

        if m.get('phoneNumber') is not None:
            self.phone_number = m.get('phoneNumber')

        if m.get('phoneNumberVerified') is not None:
            self.phone_number_verified = m.get('phoneNumberVerified')

        if m.get('phoneRegion') is not None:
            self.phone_region = m.get('phoneRegion')

        if m.get('registerTime') is not None:
            self.register_time = m.get('registerTime')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        if m.get('userExternalId') is not None:
            self.user_external_id = m.get('userExternalId')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        if m.get('userSourceId') is not None:
            self.user_source_id = m.get('userSourceId')

        if m.get('userSourceType') is not None:
            self.user_source_type = m.get('userSourceType')

        if m.get('username') is not None:
            self.username = m.get('username')

        return self

