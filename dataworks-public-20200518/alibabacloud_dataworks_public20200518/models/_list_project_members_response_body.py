# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class ListProjectMembersResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListProjectMembersResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned results.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ListProjectMembersResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListProjectMembersResponseBodyData(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        project_member_list: List[main_models.ListProjectMembersResponseBodyDataProjectMemberList] = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The information about members in the DataWorks workspace.
        self.project_member_list = project_member_list
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.project_member_list:
            for v1 in self.project_member_list:
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

        result['ProjectMemberList'] = []
        if self.project_member_list is not None:
            for k1 in self.project_member_list:
                result['ProjectMemberList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.project_member_list = []
        if m.get('ProjectMemberList') is not None:
            for k1 in m.get('ProjectMemberList'):
                temp_model = main_models.ListProjectMembersResponseBodyDataProjectMemberList()
                self.project_member_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListProjectMembersResponseBodyDataProjectMemberList(DaraModel):
    def __init__(
        self,
        nick: str = None,
        project_member_id: str = None,
        project_member_name: str = None,
        project_member_type: str = None,
        project_role_list: List[main_models.ListProjectMembersResponseBodyDataProjectMemberListProjectRoleList] = None,
        status: str = None,
    ):
        # The nickname of the member.
        self.nick = nick
        # The member ID.
        self.project_member_id = project_member_id
        # The name of the member.
        self.project_member_name = project_member_name
        # The type of the member. Valid values:
        # 
        # *   1: USER_ALIYUN, which indicates that the member is an Alibaba Cloud account.
        # *   5: USER_UBACCOUNT, which indicates that the member is a RAM user.
        # *   6: USER_STS_ROLE, which indicates that the member is a RAM role.
        self.project_member_type = project_member_type
        # The roles that are assigned to the member.
        self.project_role_list = project_role_list
        # The status of the member. Valid values:
        # 
        # *   0: NORMAL, which indicates that the member is in a normal state.
        # *   1: FORBIDDEN, which indicates that the member is disabled.
        # *   2: DELETED, which indicates that the member is deleted.
        self.status = status

    def validate(self):
        if self.project_role_list:
            for v1 in self.project_role_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.nick is not None:
            result['Nick'] = self.nick

        if self.project_member_id is not None:
            result['ProjectMemberId'] = self.project_member_id

        if self.project_member_name is not None:
            result['ProjectMemberName'] = self.project_member_name

        if self.project_member_type is not None:
            result['ProjectMemberType'] = self.project_member_type

        result['ProjectRoleList'] = []
        if self.project_role_list is not None:
            for k1 in self.project_role_list:
                result['ProjectRoleList'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Nick') is not None:
            self.nick = m.get('Nick')

        if m.get('ProjectMemberId') is not None:
            self.project_member_id = m.get('ProjectMemberId')

        if m.get('ProjectMemberName') is not None:
            self.project_member_name = m.get('ProjectMemberName')

        if m.get('ProjectMemberType') is not None:
            self.project_member_type = m.get('ProjectMemberType')

        self.project_role_list = []
        if m.get('ProjectRoleList') is not None:
            for k1 in m.get('ProjectRoleList'):
                temp_model = main_models.ListProjectMembersResponseBodyDataProjectMemberListProjectRoleList()
                self.project_role_list.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class ListProjectMembersResponseBodyDataProjectMemberListProjectRoleList(DaraModel):
    def __init__(
        self,
        project_role_code: str = None,
        project_role_id: int = None,
        project_role_name: str = None,
        project_role_type: str = None,
    ):
        # The code of the role. DataWorks provides built-in roles and allows you to create custom roles based on your business requirements. For more information about roles, see [Overview of users, roles, and permissions](https://help.aliyun.com/document_detail/295463.html).
        self.project_role_code = project_role_code
        # The role ID.
        self.project_role_id = project_role_id
        # The name of the role. DataWorks provides built-in roles and allows you to create custom roles based on your business requirements. For more information about roles, see [Overview of users, roles, and permissions](https://help.aliyun.com/document_detail/295463.html).
        self.project_role_name = project_role_name
        # The type of the role. Valid values:
        # 
        # *   0: SYSTEM, which indicates that the role is a built-in role.
        # *   2: USER_CUSTOM, which indicates that the role is a custom role.
        self.project_role_type = project_role_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.project_role_code is not None:
            result['ProjectRoleCode'] = self.project_role_code

        if self.project_role_id is not None:
            result['ProjectRoleId'] = self.project_role_id

        if self.project_role_name is not None:
            result['ProjectRoleName'] = self.project_role_name

        if self.project_role_type is not None:
            result['ProjectRoleType'] = self.project_role_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectRoleCode') is not None:
            self.project_role_code = m.get('ProjectRoleCode')

        if m.get('ProjectRoleId') is not None:
            self.project_role_id = m.get('ProjectRoleId')

        if m.get('ProjectRoleName') is not None:
            self.project_role_name = m.get('ProjectRoleName')

        if m.get('ProjectRoleType') is not None:
            self.project_role_type = m.get('ProjectRoleType')

        return self

