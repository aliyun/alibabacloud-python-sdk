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
        # Indicates whether the request was successful.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # ChangeResourceManagerResourceGroup
        # 
        # This parameter is required.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # The HTTP status code.
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

