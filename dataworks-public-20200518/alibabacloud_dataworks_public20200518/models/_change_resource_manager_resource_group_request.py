# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChangeResourceManagerResourceGroupRequest(DaraModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_manager_resource_group_id: str = None,
        resource_type: str = None,
    ):
        # The ID of the resource. The value of this parameter depends on the value of the ResourceType parameter:
        # 
        # - If ResourceType is set to project, this parameter specifies the name of the workspace (ProjectIdentifier). You can call the [ListProjects](https://help.aliyun.com/document_detail/2780068.html) operation to obtain the workspace name.
        # 
        # - If ResourceType is set to tenantresourcegroup, this parameter specifies the identifier of the exclusive resource group (Identifier). You can call the [ListResourceGroups](https://help.aliyun.com/document_detail/2780075.html) operation to obtain the identifier. This applies only to resource groups of type 7, 8, or 9.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The ID of the destination resource group.
        # 
        # This parameter is required.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # The resource type. Valid values:
        # 
        # - project: a workspace. Select this value to change the resource group for a DataWorks edition.
        # 
        # - tenantresourcegroup: an exclusive resource group. Select this value to change the resource group for a DataWorks exclusive resource group.
        # 
        # This parameter is required.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

