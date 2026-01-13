# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChangeResourceGroupRequest(DaraModel):
    def __init__(
        self,
        new_resource_group_id: str = None,
        resource_id: str = None,
    ):
        # The ID of the new resource group.
        # 
        # This parameter is required.
        self.new_resource_group_id = new_resource_group_id
        # The resource ID, which is the instance name.
        # 
        # This parameter is required.
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.new_resource_group_id is not None:
            result['NewResourceGroupId'] = self.new_resource_group_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewResourceGroupId') is not None:
            self.new_resource_group_id = m.get('NewResourceGroupId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        return self

