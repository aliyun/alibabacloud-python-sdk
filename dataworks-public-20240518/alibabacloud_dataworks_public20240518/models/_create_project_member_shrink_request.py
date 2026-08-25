# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateProjectMemberShrinkRequest(DaraModel):
    def __init__(
        self,
        project_id: int = None,
        role_codes_shrink: str = None,
        user_id: str = None,
    ):
        # The ID of the DataWorks workspace. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace Management page to obtain the ID.
        # 
        # This parameter specifies the DataWorks workspace for this API call operation.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The list of workspace role codes. You can call [ListProjectRoles](https://help.aliyun.com/document_detail/2853930.html) to obtain the role codes.
        # 
        # This parameter is used to grant workspace roles to the member when adding the member to the workspace.
        # 
        # This parameter is required.
        self.role_codes_shrink = role_codes_shrink
        # The ID of the DataWorks account. You can log on to the [DataWorks console - Management Center](https://dataworks.console.aliyun.com/product/ms_menu), select the workspace to which you want to add a member, go to the Management Center page, and then navigate to the **Tenant Members and Roles** page to view the account ID of the user you want to add to the workspace.
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

        if self.role_codes_shrink is not None:
            result['RoleCodes'] = self.role_codes_shrink

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RoleCodes') is not None:
            self.role_codes_shrink = m.get('RoleCodes')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

