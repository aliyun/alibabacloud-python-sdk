# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class CreateUserRequest(DaraModel):
    def __init__(
        self,
        avatar: str = None,
        description: str = None,
        email: str = None,
        group_info_list: List[main_models.CreateUserRequestGroupInfoList] = None,
        nick_name: str = None,
        phone: str = None,
        role: str = None,
        status: str = None,
        user_data: Dict[str, Any] = None,
        user_id: str = None,
        user_name: str = None,
    ):
        # The URL of the profile picture.
        # 
        # If you specify the parameter in the HTTP URL format, the URL must start with http:// or https:// and can be up to 4 KB in size.
        # 
        # If you specify the parameter in the data URL format, the URL must start with data:// and be encoded in Base64. The URL can be up to 300 KB in size.
        self.avatar = avatar
        # The description of the user. The description can be up to 1,024 characters in length.
        self.description = description
        # The email address.
        self.email = email
        # The information about the group.
        self.group_info_list = group_info_list
        # The nickname of the user. The nickname can be up to 128 characters in length.
        self.nick_name = nick_name
        # The phone number.
        self.phone = phone
        # The role of the user. Default value: user. Valid values:
        # 
        # *   superadmin
        # *   admin
        # *   user
        # 
        # If the domain can be divided into subdomains, the subdomain_super_admin and subdomain_admin roles are also supported.
        # 
        # Valid values:
        # 
        # *   subdomain_super_admin
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   subdomain_admin
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   superadmin
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   admin
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   user
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.role = role
        # The state of the user. Default value: enabled. Valid values:
        # 
        # *   enabled: The user is in a normal state.
        # *   disabled: The user is prohibited from logon.
        self.status = status
        # The custom data. The data can be up to 1,024 characters in length.
        self.user_data = user_data
        # The user ID. The ID can be up to 64 characters in length and cannot contain number signs (#).
        # 
        # This parameter is required.
        self.user_id = user_id
        # The username. The username can be up to 128 characters in length.
        self.user_name = user_name

    def validate(self):
        if self.group_info_list:
            for v1 in self.group_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avatar is not None:
            result['avatar'] = self.avatar

        if self.description is not None:
            result['description'] = self.description

        if self.email is not None:
            result['email'] = self.email

        result['group_info_list'] = []
        if self.group_info_list is not None:
            for k1 in self.group_info_list:
                result['group_info_list'].append(k1.to_map() if k1 else None)

        if self.nick_name is not None:
            result['nick_name'] = self.nick_name

        if self.phone is not None:
            result['phone'] = self.phone

        if self.role is not None:
            result['role'] = self.role

        if self.status is not None:
            result['status'] = self.status

        if self.user_data is not None:
            result['user_data'] = self.user_data

        if self.user_id is not None:
            result['user_id'] = self.user_id

        if self.user_name is not None:
            result['user_name'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('avatar') is not None:
            self.avatar = m.get('avatar')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('email') is not None:
            self.email = m.get('email')

        self.group_info_list = []
        if m.get('group_info_list') is not None:
            for k1 in m.get('group_info_list'):
                temp_model = main_models.CreateUserRequestGroupInfoList()
                self.group_info_list.append(temp_model.from_map(k1))

        if m.get('nick_name') is not None:
            self.nick_name = m.get('nick_name')

        if m.get('phone') is not None:
            self.phone = m.get('phone')

        if m.get('role') is not None:
            self.role = m.get('role')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('user_data') is not None:
            self.user_data = m.get('user_data')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')

        return self

class CreateUserRequestGroupInfoList(DaraModel):
    def __init__(
        self,
        group_id: str = None,
    ):
        # The group ID.
        self.group_id = group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['group_id'] = self.group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')

        return self

