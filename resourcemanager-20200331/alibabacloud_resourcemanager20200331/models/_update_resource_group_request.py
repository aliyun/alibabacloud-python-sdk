# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateResourceGroupRequest(DaraModel):
    def __init__(
        self,
        new_display_name: str = None,
        resource_group_id: str = None,
    ):
        # The display name of the resource group.
        # 
        # The name must be 1 to 50 characters in length.
        # 
        # This parameter is required.
        self.new_display_name = new_display_name
        # The ID of the resource group.
        # 
        # You can call the [ListResourceGroups](https://help.aliyun.com/document_detail/158855.html) operation to obtain the ID.
        # 
        # This parameter is required.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.new_display_name is not None:
            result['NewDisplayName'] = self.new_display_name

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewDisplayName') is not None:
            self.new_display_name = m.get('NewDisplayName')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

