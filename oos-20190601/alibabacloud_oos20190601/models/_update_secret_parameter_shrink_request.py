# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateSecretParameterShrinkRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        tags_shrink: str = None,
        value: str = None,
    ):
        # The description of the parameter. The description must be 1 to 200 characters in length.
        self.description = description
        # The name of the parameter. The name must be 1 to 180 characters in length, and can contain letters, digits, hyphens (-), and underscores (_). It cannot start with ALIYUN, ACS, ALIBABA, ALICLOUD, or OOS.
        # 
        # This parameter is required.
        self.name = name
        # The ID of the region.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The tags of the parameter.
        self.tags_shrink = tags_shrink
        # The value of the parameter. The value must be 1 to 4096 characters in length.
        # 
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

