# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quickbi_public20220101 import models as main_models
from darabonba.model import DaraModel

class QueryUserInfoByAccountResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.QueryUserInfoByAccountResponseBodyResult = None,
        success: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The returned organization user information.
        self.result = result
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.QueryUserInfoByAccountResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryUserInfoByAccountResponseBodyResult(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        account_name: str = None,
        admin_user: bool = None,
        auth_admin_user: bool = None,
        email: str = None,
        nick_name: str = None,
        phone: str = None,
        role_id_list: List[int] = None,
        user_id: str = None,
        user_type: int = None,
    ):
        # The ID of the Alibaba Cloud account.
        self.account_id = account_id
        # The name of the Alibaba Cloud account that corresponds to the member. (If you use a RAM user, the domain name information that follows @ is removed. For example, if you use a <test@test.com>, test is returned.)
        self.account_name = account_name
        # Whether you are an administrator of the organization. Valid values:
        # 
        # *   true
        # *   false
        self.admin_user = admin_user
        # Whether you are a permission administrator. Valid values:
        # 
        # *   true
        # *   false
        self.auth_admin_user = auth_admin_user
        # The email address of the user.
        self.email = email
        # The nickname of the account.
        self.nick_name = nick_name
        # The phone number of the alert contact.
        self.phone = phone
        # List of organization role IDs bound to the user.
        self.role_id_list = role_id_list
        # The UserID in the Quick BI.
        self.user_id = user_id
        # The role type of the organization member. Valid values:
        # 
        # *   1 : developer
        # *   2 : visitors
        # *   3 : Analyst
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.admin_user is not None:
            result['AdminUser'] = self.admin_user

        if self.auth_admin_user is not None:
            result['AuthAdminUser'] = self.auth_admin_user

        if self.email is not None:
            result['Email'] = self.email

        if self.nick_name is not None:
            result['NickName'] = self.nick_name

        if self.phone is not None:
            result['Phone'] = self.phone

        if self.role_id_list is not None:
            result['RoleIdList'] = self.role_id_list

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_type is not None:
            result['UserType'] = self.user_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('AdminUser') is not None:
            self.admin_user = m.get('AdminUser')

        if m.get('AuthAdminUser') is not None:
            self.auth_admin_user = m.get('AuthAdminUser')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')

        if m.get('Phone') is not None:
            self.phone = m.get('Phone')

        if m.get('RoleIdList') is not None:
            self.role_id_list = m.get('RoleIdList')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')

        return self

