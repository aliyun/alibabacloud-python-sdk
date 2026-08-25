# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RevokeMemberProjectRolesRequest(DaraModel):
    def __init__(
        self,
        project_id: int = None,
        role_codes: List[str] = None,
        user_id: str = None,
    ):
        # The ID of the DataWorks workspace. You can log on to the [DataWorks console](https://dataworks.console.aliyun.com/workspace/list) and go to the workspace settings page to obtain the workspace ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The list of workspace role codes. You can call [ListProjectRoles](https://help.aliyun.com/document_detail/2853930.html) to obtain the role codes. 
        # 
        # This parameter specifies the workspace roles to be revoked by this API call.
        # 
        # This parameter is required.
        self.role_codes = role_codes
        # The ID of the DataWorks account. You can log on to the [DataWorks console - Management Center](https://dataworks.console.aliyun.com/product/ms_menu), select the workspace that you want to manage, go to the Tenant Members and Roles page, and view the account ID of the member whose roles you want to revoke.
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

        if self.role_codes is not None:
            result['RoleCodes'] = self.role_codes

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RoleCodes') is not None:
            self.role_codes = m.get('RoleCodes')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

