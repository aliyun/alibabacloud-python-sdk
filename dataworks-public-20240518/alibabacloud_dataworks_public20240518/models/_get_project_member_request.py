# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetProjectMemberRequest(DaraModel):
    def __init__(
        self,
        project_id: int = None,
        user_id: str = None,
    ):
        # The ID of the DataWorks Workspace. You can sign in to the [DataWorks Console](https://dataworks.console.aliyun.com/workspace/list) and go to the Workspace Management page to obtain the Workspace ID.
        # 
        # This parameter is used to identify the DataWorks workspace that you want to access.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The ID of the user. To find the ID, sign in to the [DataWorks Console](https://dataworks.console.aliyun.com/product/ms_menu), go to the Management Center, select the target Workspace, and open the Tenant Members and Roles page.
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

