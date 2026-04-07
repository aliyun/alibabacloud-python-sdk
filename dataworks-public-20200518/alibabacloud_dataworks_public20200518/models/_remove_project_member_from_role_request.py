# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RemoveProjectMemberFromRoleRequest(DaraModel):
    def __init__(
        self,
        project_id: int = None,
        role_code: str = None,
        user_id: str = None,
    ):
        # The DataWorks workspace ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The code of the role in the DataWorks workspace. You can call the ListProjectRoles operation to query the codes of all roles in a DataWorks workspace. Valid values:
        # 
        # *   role_project_owner: workspace owner
        # *   role_project_admin: workspace administrator
        # *   role_project_dev: developer
        # *   role_project_pe: O\\&M engineer
        # *   role_project_deploy: deployment expert
        # *   role_project_guest: visitor
        # *   role_project_security: security administrator
        # *   role_project_tester: experiencer
        # *   role_project_erd: model designer
        # 
        # This parameter is required.
        self.role_code = role_code
        # The user ID.
        # 
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.role_code is not None:
            result['RoleCode'] = self.role_code

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RoleCode') is not None:
            self.role_code = m.get('RoleCode')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

