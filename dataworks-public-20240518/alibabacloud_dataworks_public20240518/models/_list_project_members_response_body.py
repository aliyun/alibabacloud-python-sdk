# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListProjectMembersResponseBody(DaraModel):
    def __init__(
        self,
        paging_info: main_models.ListProjectMembersResponseBodyPagingInfo = None,
        request_id: str = None,
    ):
        # The pagination information.
        self.paging_info = paging_info
        # The request ID. You can use the ID to query logs and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.paging_info:
            self.paging_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.paging_info is not None:
            result['PagingInfo'] = self.paging_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PagingInfo') is not None:
            temp_model = main_models.ListProjectMembersResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m.get('PagingInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListProjectMembersResponseBodyPagingInfo(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        project_members: List[main_models.ListProjectMembersResponseBodyPagingInfoProjectMembers] = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The members in the workspace.
        self.project_members = project_members
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.project_members:
            for v1 in self.project_members:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['ProjectMembers'] = []
        if self.project_members is not None:
            for k1 in self.project_members:
                result['ProjectMembers'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.project_members = []
        if m.get('ProjectMembers') is not None:
            for k1 in m.get('ProjectMembers'):
                temp_model = main_models.ListProjectMembersResponseBodyPagingInfoProjectMembers()
                self.project_members.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListProjectMembersResponseBodyPagingInfoProjectMembers(DaraModel):
    def __init__(
        self,
        project_id: int = None,
        roles: List[main_models.ListProjectMembersResponseBodyPagingInfoProjectMembersRoles] = None,
        status: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        # The ID of the DataWorks workspace.
        self.project_id = project_id
        # The roles that are assigned to the member.
        self.roles = roles
        # The status of the member. Valid values:
        # 
        # *   Normal
        # *   Forbidden
        self.status = status
        # The ID of the account used by the member.
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        if self.roles:
            for v1 in self.roles:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        result['Roles'] = []
        if self.roles is not None:
            for k1 in self.roles:
                result['Roles'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        self.roles = []
        if m.get('Roles') is not None:
            for k1 in m.get('Roles'):
                temp_model = main_models.ListProjectMembersResponseBodyPagingInfoProjectMembersRoles()
                self.roles.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

class ListProjectMembersResponseBodyPagingInfoProjectMembersRoles(DaraModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
        type: str = None,
    ):
        # The code of the role.
        self.code = code
        # The name of the role.
        self.name = name
        # The type of the role. Valid values:
        # 
        # *   UserCustom: user-defined role
        # *   System: system role
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

