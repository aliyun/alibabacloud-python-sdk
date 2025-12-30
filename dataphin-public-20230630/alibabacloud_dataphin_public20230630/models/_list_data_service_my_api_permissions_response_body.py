# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListDataServiceMyApiPermissionsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        page_result: main_models.ListDataServiceMyApiPermissionsResponseBodyPageResult = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.page_result = page_result
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.page_result:
            self.page_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.page_result is not None:
            result['PageResult'] = self.page_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageResult') is not None:
            temp_model = main_models.ListDataServiceMyApiPermissionsResponseBodyPageResult()
            self.page_result = temp_model.from_map(m.get('PageResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListDataServiceMyApiPermissionsResponseBodyPageResult(DaraModel):
    def __init__(
        self,
        permission_list: List[main_models.ListDataServiceMyApiPermissionsResponseBodyPageResultPermissionList] = None,
        total_count: int = None,
    ):
        self.permission_list = permission_list
        self.total_count = total_count

    def validate(self):
        if self.permission_list:
            for v1 in self.permission_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PermissionList'] = []
        if self.permission_list is not None:
            for k1 in self.permission_list:
                result['PermissionList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.permission_list = []
        if m.get('PermissionList') is not None:
            for k1 in m.get('PermissionList'):
                temp_model = main_models.ListDataServiceMyApiPermissionsResponseBodyPageResultPermissionList()
                self.permission_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListDataServiceMyApiPermissionsResponseBodyPageResultPermissionList(DaraModel):
    def __init__(
        self,
        api_id: int = None,
        api_name: str = None,
        create_user_name: str = None,
        creator: str = None,
        owner: str = None,
        owner_user_name: str = None,
        privilege_belong_to: str = None,
        privilege_from: int = None,
        project_id: int = None,
        project_name: str = None,
        role: int = None,
    ):
        self.api_id = api_id
        self.api_name = api_name
        self.create_user_name = create_user_name
        self.creator = creator
        self.owner = owner
        self.owner_user_name = owner_user_name
        self.privilege_belong_to = privilege_belong_to
        self.privilege_from = privilege_from
        self.project_id = project_id
        self.project_name = project_name
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_id is not None:
            result['ApiId'] = self.api_id

        if self.api_name is not None:
            result['ApiName'] = self.api_name

        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.owner_user_name is not None:
            result['OwnerUserName'] = self.owner_user_name

        if self.privilege_belong_to is not None:
            result['PrivilegeBelongTo'] = self.privilege_belong_to

        if self.privilege_from is not None:
            result['PrivilegeFrom'] = self.privilege_from

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.role is not None:
            result['Role'] = self.role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')

        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')

        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('OwnerUserName') is not None:
            self.owner_user_name = m.get('OwnerUserName')

        if m.get('PrivilegeBelongTo') is not None:
            self.privilege_belong_to = m.get('PrivilegeBelongTo')

        if m.get('PrivilegeFrom') is not None:
            self.privilege_from = m.get('PrivilegeFrom')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        return self

