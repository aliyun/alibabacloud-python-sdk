# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quickbi_public20220101 import models as main_models
from darabonba.model import DaraModel

class QueryUserListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.QueryUserListResponseBodyResult = None,
        success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The paginated list of users. The `Data` parameter contains the details of each organization member.
        self.result = result
        # Indicates whether the request was successful. Valid values:
        # 
        # - `true`: The request was successful.
        # 
        # - `false`: The request failed.
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
            temp_model = main_models.QueryUserListResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryUserListResponseBodyResult(DaraModel):
    def __init__(
        self,
        data: List[main_models.QueryUserListResponseBodyResultData] = None,
        page_num: int = None,
        page_size: int = None,
        total_num: int = None,
        total_pages: int = None,
    ):
        # The list of users.
        self.data = data
        # The page number.
        self.page_num = page_num
        # The number of entries per page.
        self.page_size = page_size
        # The total number of matching users.
        self.total_num = total_num
        # The total number of pages.
        self.total_pages = total_pages

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
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_num is not None:
            result['TotalNum'] = self.total_num

        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.QueryUserListResponseBodyResultData()
                self.data.append(temp_model.from_map(k1))

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')

        return self

class QueryUserListResponseBodyResultData(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        account_name: str = None,
        admin_user: bool = None,
        auth_admin_user: bool = None,
        copilot_modules: List[str] = None,
        is_deleted: bool = None,
        joined_date: int = None,
        last_login_time: int = None,
        nick_name: str = None,
        role_id_list: List[int] = None,
        user_id: str = None,
        user_type: int = None,
    ):
        # The Alibaba Cloud account ID. For users not added through RAM, this ID is available only after they log in.
        self.account_id = account_id
        # The Alibaba Cloud account name.
        self.account_name = account_name
        # Indicates whether the user is an organization administrator. Valid values:
        # 
        # - `true`: Yes
        # 
        # - `false`: No
        # 
        # >Notice: 
        # 
        # This parameter is deprecated. Use the `RoleIdList` parameter instead.
        self.admin_user = admin_user
        # Indicates whether the user is a permission administrator. Valid values:
        # 
        # - `true`: Yes
        # 
        # - `false`: No
        # 
        # >Notice: 
        # 
        # This parameter is deprecated. Use the `RoleIdList` parameter instead.
        self.auth_admin_user = auth_admin_user
        self.copilot_modules = copilot_modules
        # Indicates whether the user is inactive.
        # 
        # - `false`: Active
        # 
        # - `true`: Inactive
        self.is_deleted = is_deleted
        # The Unix timestamp (in milliseconds) that indicates when the user joined the organization.
        self.joined_date = joined_date
        # The Unix timestamp (in milliseconds) of the user\\"s last login.
        self.last_login_time = last_login_time
        # The nickname of the user.
        self.nick_name = nick_name
        # The IDs of the organization roles assigned to the user.
        self.role_id_list = role_id_list
        # The user ID in Quick BI.
        self.user_id = user_id
        # The user type of the organization member. Valid values:
        # 
        # - `1`: developer
        # 
        # - `2`: viewer
        # 
        # - `3`: analyst
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

        if self.copilot_modules is not None:
            result['CopilotModules'] = self.copilot_modules

        if self.is_deleted is not None:
            result['IsDeleted'] = self.is_deleted

        if self.joined_date is not None:
            result['JoinedDate'] = self.joined_date

        if self.last_login_time is not None:
            result['LastLoginTime'] = self.last_login_time

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
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('AdminUser') is not None:
            self.admin_user = m.get('AdminUser')

        if m.get('AuthAdminUser') is not None:
            self.auth_admin_user = m.get('AuthAdminUser')

        if m.get('CopilotModules') is not None:
            self.copilot_modules = m.get('CopilotModules')

        if m.get('IsDeleted') is not None:
            self.is_deleted = m.get('IsDeleted')

        if m.get('JoinedDate') is not None:
            self.joined_date = m.get('JoinedDate')

        if m.get('LastLoginTime') is not None:
            self.last_login_time = m.get('LastLoginTime')

        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')

        if m.get('RoleIdList') is not None:
            self.role_id_list = m.get('RoleIdList')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')

        return self

