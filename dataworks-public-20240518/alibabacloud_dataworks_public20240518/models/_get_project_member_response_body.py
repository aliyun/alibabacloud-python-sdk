# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetProjectMemberResponseBody(DaraModel):
    def __init__(
        self,
        project_member: main_models.GetProjectMemberResponseBodyProjectMember = None,
        request_id: str = None,
    ):
        # The details about the member in the workspace.
        self.project_member = project_member
        # The request ID. You can use the ID to query logs and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.project_member:
            self.project_member.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.project_member is not None:
            result['ProjectMember'] = self.project_member.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectMember') is not None:
            temp_model = main_models.GetProjectMemberResponseBodyProjectMember()
            self.project_member = temp_model.from_map(m.get('ProjectMember'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetProjectMemberResponseBodyProjectMember(DaraModel):
    def __init__(
        self,
        project_id: int = None,
        roles: List[main_models.GetProjectMemberResponseBodyProjectMemberRoles] = None,
        status: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        # The DataWorks workspace ID.
        self.project_id = project_id
        # The roles that are assigned to the member in the workspace.
        self.roles = roles
        # The status of the member.
        # 
        # *   Normal
        # *   Forbidden
        self.status = status
        # The ID of the account used by the member in the workspace.
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
                temp_model = main_models.GetProjectMemberResponseBodyProjectMemberRoles()
                self.roles.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

class GetProjectMemberResponseBodyProjectMemberRoles(DaraModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
        type: str = None,
    ):
        # The code of the role. Valid values:
        # 
        # *   role_project_admin: Workspace Administrator
        # *   role_project_dev: Develop
        # *   role_project_dg_admin: Data Governance Administrator
        # *   role_project_guest: Visitor
        # *   role_project_security: Security Administrator
        # *   role_project_deploy: Deploy
        # *   role_project_owner: Workspace Owner
        # *   role_project_data_analyst: Data Analyst
        # *   role_project_pe: O\\&M
        # *   role_project_erd: Model Designer
        self.code = code
        # The name of the role.
        self.name = name
        # The type of the role. Valid values:
        # 
        # *   UserCustom: custom role
        # *   System: built-in role
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

