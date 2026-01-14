# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quickbi_public20220101 import models as main_models
from darabonba.model import DaraModel

class AddUserResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.AddUserResponseBodyResult = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Returns detailed information about the newly added Aliyun user.
        self.result = result
        # Indicates whether the request was successful. Possible values:
        # 
        # - true: The request was successful.
        # - false: The request failed.
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
            temp_model = main_models.AddUserResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self



class AddUserResponseBodyResult(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        admin_user: bool = None,
        auth_admin_user: bool = None,
        nick_name: str = None,
        role_id_list: List[int] = None,
        user_id: str = None,
        user_type: int = None,
    ):
        # Aliyun account.
        self.account_name = account_name
        # Whether the organization administrator role is assigned. Value range: 
        # 
        # - true: Yes
        # - false: No
        # 
        # <notice>This parameter is deprecated and not recommended for use. It is invalid when RoleIdList is provided.</notice>
        self.admin_user = admin_user
        # Whether the permission administrator role is assigned. Value range: 
        # 
        # - true: Yes
        # - false: No
        # 
        # <notice>This parameter is deprecated and not recommended for use. It is invalid when RoleIdList is provided.</notice>
        self.auth_admin_user = auth_admin_user
        # Aliyun account nickname.
        self.nick_name = nick_name
        # List of organization role IDs bound to the user.
        self.role_id_list = role_id_list
        # UserID in Quick BI.
        self.user_id = user_id
        # User type of the organization member. Value range: 
        # - 1: Developer 
        # - 2: Visitor 
        # - 3: Analyst
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.admin_user is not None:
            result['AdminUser'] = self.admin_user

        if self.auth_admin_user is not None:
            result['AuthAdminUser'] = self.auth_admin_user

        if self.nick_name is not None:
            result['NickName'] = self.nick_name

        if self.role_id_list is not None:
            result['RoleIdList'] = self.role_id_list

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_type is not None:
            result['UserType'] = self.user_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('AdminUser') is not None:
            self.admin_user = m.get('AdminUser')

        if m.get('AuthAdminUser') is not None:
            self.auth_admin_user = m.get('AuthAdminUser')

        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')

        if m.get('RoleIdList') is not None:
            self.role_id_list = m.get('RoleIdList')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')

        return self

