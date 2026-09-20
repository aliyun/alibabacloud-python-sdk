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
        # The ID of the DataWorks workspace.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The role code of the DataWorks workspace. You can invoke the ListProjectRoles operation to obtain the list of role codes for a project.
        # The default preset roles are as follows:
        # 
        # - role_project_owner: Project owner.
        # - role_project_admin: Storage management administrator.
        # - role_project_dev: Developer.
        # - role_project_pe: O&M engineer.
        # - role_project_deploy: Deployment.
        # - role_project_guest: Visitor.
        # - role_project_security: Security administrator.
        # - role_project_tester: Experience user.
        # - role_project_erd: Model designer.
        # 
        # This parameter is required.
        self.role_code = role_code
        # The ID of the user.
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

