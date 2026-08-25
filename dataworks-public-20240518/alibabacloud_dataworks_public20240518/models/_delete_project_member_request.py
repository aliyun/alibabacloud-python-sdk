# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteProjectMemberRequest(DaraModel):
    def __init__(
        self,
        project_id: int = None,
        user_id: str = None,
    ):
        # The ID of the DataWorks workspace. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the workspace configuration page to obtain the workspace ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The ID of the DataWorks account. You can log on to the [DataWorks console - Management Center](https://dataworks.console.aliyun.com/product/ms_menu), select the workspace from which you want to remove the member, go to the **Tenant Members and Roles** page, and view the account ID of the member to be removed from the workspace.
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

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

