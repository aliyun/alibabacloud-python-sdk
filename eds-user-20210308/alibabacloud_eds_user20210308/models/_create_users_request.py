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
        # The date and time when the system automatically locks the convenience user\\"s account. The value must be in the `yyyy-MM-dd HH:mm:ss` format.
        self.auto_lock_time = auto_lock_time
        # The business channel.
        self.business_channel = business_channel
        # Specifies whether to set the convenience user as a local administrator.
        self.is_local_admin = is_local_admin
        # The initial password. If you do not specify this parameter, the system sends a password reset email to the convenience user\\"s email address.
        self.password = password
        # By default, a convenience user\\"s password does not expire. You can use this parameter to specify a password validity period of 30 to 365 days. After the password expires, the user must reset it to log in again.
        # 
        # > This feature is in invited preview. To use this feature, submit a ticket.
        self.password_expire_days = password_expire_days
        # Details about the convenience users.
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
        # The email address of the convenience user. This email address is used for notifications, such as an alert when a cloud computer is assigned. You must specify either this parameter or the `Phone` parameter.
        self.email = email
        # The user name. The user name must be 3 to 24 characters long and can contain lowercase letters, digits, and underscores (_).
        # 
        # This parameter is required.
        self.end_user_id = end_user_id
        self.group_id_list = group_id_list
        # The ID of the organization to which the convenience user belongs.
        self.org_id = org_id
        # The account activation type.
        self.owner_type = owner_type
        # The password for the convenience user.
        # 
        # > The password must be at least 10 characters long and contain characters from at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters (excluding spaces).
        self.password = password
        # <props="china">
        # 
        # The phone number of the convenience user. This phone number is used for notifications, such as a text message when a cloud computer is assigned. You must specify either this parameter or the `Email` parameter.
        # 
        # 
        # 
        # <props="intl">
        # 
        # Phone numbers are not supported on the international site.
        self.phone = phone
        # The display name of the convenience user.
        self.real_nick_name = real_nick_name
        # A remark for the convenience user.
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

