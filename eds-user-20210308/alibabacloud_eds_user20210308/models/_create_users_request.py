# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_user20210308 import models as main_models
from darabonba.model import DaraModel

class CreateUsersRequest(DaraModel):
    def __init__(
        self,
        auto_lock_time: str = None,
        business_channel: str = None,
        is_local_admin: bool = None,
        password: str = None,
        password_expire_days: str = None,
        users: List[main_models.CreateUsersRequestUsers] = None,
    ):
        # The date on which the convenience users are automatically locked.
        self.auto_lock_time = auto_lock_time
        self.business_channel = business_channel
        self.is_local_admin = is_local_admin
        # The initial password. If this parameter is left empty, an email for password reset is sent to the specified email address.
        self.password = password
        self.password_expire_days = password_expire_days
        # The information about the convenience user.
        # 
        # This parameter is required.
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
        if self.auto_lock_time is not None:
            result['AutoLockTime'] = self.auto_lock_time

        if self.business_channel is not None:
            result['BusinessChannel'] = self.business_channel

        if self.is_local_admin is not None:
            result['IsLocalAdmin'] = self.is_local_admin

        if self.password is not None:
            result['Password'] = self.password

        if self.password_expire_days is not None:
            result['PasswordExpireDays'] = self.password_expire_days

        result['Users'] = []
        if self.users is not None:
            for k1 in self.users:
                result['Users'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoLockTime') is not None:
            self.auto_lock_time = m.get('AutoLockTime')

        if m.get('BusinessChannel') is not None:
            self.business_channel = m.get('BusinessChannel')

        if m.get('IsLocalAdmin') is not None:
            self.is_local_admin = m.get('IsLocalAdmin')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('PasswordExpireDays') is not None:
            self.password_expire_days = m.get('PasswordExpireDays')

        self.users = []
        if m.get('Users') is not None:
            for k1 in m.get('Users'):
                temp_model = main_models.CreateUsersRequestUsers()
                self.users.append(temp_model.from_map(k1))

        return self

class CreateUsersRequestUsers(DaraModel):
    def __init__(
        self,
        email: str = None,
        end_user_id: str = None,
        group_id_list: List[str] = None,
        org_id: str = None,
        owner_type: str = None,
        password: str = None,
        phone: str = None,
        real_nick_name: str = None,
        remark: str = None,
    ):
        # The email address of the convenience user. The email address is used to receive notifications about events such as desktop assignment. You must specify an email address or a mobile number to receive notifications.
        self.email = email
        # The username of the convenience user. The name can contain lowercase letters, digits, and underscores (_), and must be 3 to 24 characters in length.
        # 
        # This parameter is required.
        self.end_user_id = end_user_id
        self.group_id_list = group_id_list
        # The organization to which the convenience user belongs.
        self.org_id = org_id
        # The type of the account ownership.
        # 
        # Valid values:
        # 
        # *   CreateFromManager: administrator-activated
        # *   Normal: user-activated
        self.owner_type = owner_type
        # The user password.
        # 
        # >  The password must be at least 10 characters in length and contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters (excluding spaces).
        self.password = password
        # Mobile numbers are not supported on the international site (alibabacloud.com).
        self.phone = phone
        # The display name of the end user.
        self.real_nick_name = real_nick_name
        # The remarks on the convenience user.
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.email is not None:
            result['Email'] = self.email

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.group_id_list is not None:
            result['GroupIdList'] = self.group_id_list

        if self.org_id is not None:
            result['OrgId'] = self.org_id

        if self.owner_type is not None:
            result['OwnerType'] = self.owner_type

        if self.password is not None:
            result['Password'] = self.password

        if self.phone is not None:
            result['Phone'] = self.phone

        if self.real_nick_name is not None:
            result['RealNickName'] = self.real_nick_name

        if self.remark is not None:
            result['Remark'] = self.remark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('GroupIdList') is not None:
            self.group_id_list = m.get('GroupIdList')

        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')

        if m.get('OwnerType') is not None:
            self.owner_type = m.get('OwnerType')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('Phone') is not None:
            self.phone = m.get('Phone')

        if m.get('RealNickName') is not None:
            self.real_nick_name = m.get('RealNickName')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        return self

