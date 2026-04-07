# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDataServiceFolderRequest(DaraModel):
    def __init__(
        self,
        folder_name: str = None,
        group_id: str = None,
        parent_id: int = None,
        project_id: int = None,
        tenant_id: int = None,
    ):
        # The name of the folder.
        # 
        # This parameter is required.
        self.folder_name = folder_name
        # The ID of the desired workflow to which the folder belongs.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The ID of the desired parent folder of the folder. The ID of the root folder in a workflow is 0. The ID of the folder created by users in a workflow is greater than 0.
        # 
        # This parameter is required.
        self.parent_id = parent_id
        # The ID of the workspace.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The tenant ID.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.folder_name is not None:
            result['FolderName'] = self.folder_name

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FolderName') is not None:
            self.folder_name = m.get('FolderName')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        return self

