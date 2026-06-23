# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateProjectRoleShrinkRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        module_permissions_shrink: str = None,
        name: str = None,
        project_id: int = None,
    ):
        # The client token.
        self.client_token = client_token
        # The list of DataWorks module permissions.
        self.module_permissions_shrink = module_permissions_shrink
        # The role name.
        # 
        # This parameter is required.
        self.name = name
        # The ID of the DataWorks workspace. You can log on to the [DataWorks console](https://dataworks.console.aliyun.com/workspace/list) and go to the workspace management page to obtain the ID.
        # 
        # This parameter specifies the DataWorks workspace on which the API operation is performed.
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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.module_permissions_shrink is not None:
            result['ModulePermissions'] = self.module_permissions_shrink

        if self.name is not None:
            result['Name'] = self.name

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ModulePermissions') is not None:
            self.module_permissions_shrink = m.get('ModulePermissions')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

