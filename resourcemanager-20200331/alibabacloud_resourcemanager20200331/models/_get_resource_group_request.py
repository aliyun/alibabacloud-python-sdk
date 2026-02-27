# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetResourceGroupRequest(DaraModel):
    def __init__(
        self,
        include_tags: bool = None,
        resource_group_id: str = None,
    ):
        # Specifies whether to return the information of tags. Valid values:
        # 
        # *   false (default value)
        # *   true
        self.include_tags = include_tags
        # The ID of the resource group.
        # 
        # You can call the [ListResourceGroups](https://help.aliyun.com/document_detail/158855.html) operation to obtain the ID of the resource group.
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
        if self.include_tags is not None:
            result['IncludeTags'] = self.include_tags

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IncludeTags') is not None:
            self.include_tags = m.get('IncludeTags')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

