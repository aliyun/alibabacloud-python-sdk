# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetProjectRoleRequest(DaraModel):
    def __init__(
        self,
        code: str = None,
        project_id: int = None,
    ):
        # The code of the role in the DataWorks workspace. Valid values:
        # 
        # *   role_project_admin: workspace administrator
        # *   role_project_dev: developer
        # *   role_project_dg_admin: data governance administrator
        # *   role_project_guest: visitor
        # *   role_project_security: security administrator
        # *   role_project_deploy: deployer
        # *   role_project_owner: workspace owner
        # *   role_project_data_analyst: data analyst
        # *   role_project_pe: O\\&M engineer
        # *   role_project_erd: model designer
        # 
        # This parameter is required.
        self.code = code
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to query the ID.
        # 
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

