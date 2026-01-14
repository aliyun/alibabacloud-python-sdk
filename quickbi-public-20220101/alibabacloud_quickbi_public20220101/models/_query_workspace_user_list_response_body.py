# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quickbi_public20220101 import models as main_models
from darabonba.model import DaraModel

class QueryWorkspaceUserListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.QueryWorkspaceUserListResponseBodyResult = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Returns the paginated result of the member list, with detailed information about the members stored in the Data parameter of the response.
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
            temp_model = main_models.QueryWorkspaceUserListResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryWorkspaceUserListResponseBodyResult(DaraModel):
    def __init__(
        self,
        data: List[main_models.QueryWorkspaceUserListResponseBodyResultData] = None,
        page_num: int = None,
        page_size: int = None,
        total_num: int = None,
        total_pages: int = None,
    ):
        # Information about the workspace members.
        self.data = data
        # Page number.
        self.page_num = page_num
        # Number of rows per page as set in the request.
        self.page_size = page_size
        # Total number of rows.
        self.total_num = total_num
        # Total number of pages.
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
                temp_model = main_models.QueryWorkspaceUserListResponseBodyResultData()
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

class QueryWorkspaceUserListResponseBodyResultData(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        account_name: str = None,
        nick_name: str = None,
        role: main_models.QueryWorkspaceUserListResponseBodyResultDataRole = None,
        user_id: str = None,
    ):
        # Alibaba Cloud account ID.
        self.account_id = account_id
        # Alibaba Cloud account name.
        self.account_name = account_name
        # Nickname.
        self.nick_name = nick_name
        # Preset role information for the workspace member.
        self.role = role
        # Quick BI user ID.
        self.user_id = user_id

    def validate(self):
        if self.role:
            self.role.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.nick_name is not None:
            result['NickName'] = self.nick_name

        if self.role is not None:
            result['Role'] = self.role.to_map()

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')

        if m.get('Role') is not None:
            temp_model = main_models.QueryWorkspaceUserListResponseBodyResultDataRole()
            self.role = temp_model.from_map(m.get('Role'))

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class QueryWorkspaceUserListResponseBodyResultDataRole(DaraModel):
    def __init__(
        self,
        role_code: str = None,
        role_id: int = None,
        role_name: str = None,
    ):
        # Code corresponding to the preset role.
        self.role_code = role_code
        # Preset role ID. Possible values:
        # 
        # - 25: Workspace Administrator
        # - 26: Workspace Developer
        # - 27: Workspace Analyst
        # - 30: Workspace Viewer
        self.role_id = role_id
        # Name of the preset role.
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.role_code is not None:
            result['RoleCode'] = self.role_code

        if self.role_id is not None:
            result['RoleId'] = self.role_id

        if self.role_name is not None:
            result['RoleName'] = self.role_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleCode') is not None:
            self.role_code = m.get('RoleCode')

        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')

        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')

        return self

