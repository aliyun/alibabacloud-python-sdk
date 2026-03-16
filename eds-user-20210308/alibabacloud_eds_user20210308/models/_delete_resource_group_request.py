# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteResourceGroupRequest(DaraModel):
    def __init__(
        self,
        business_channel: str = None,
        resource_group_id: str = None,
        resource_group_ids: List[str] = None,
    ):
        self.business_channel = business_channel
        # >  The ID of the resource group that you want to delete.
        # 
        # *   If you also specify ResourceGroupIds, both parameters take effect.
        self.resource_group_id = resource_group_id
        # >  The IDs of the resource groups that you want to delete.
        # 
        # *   If you also specify ResourceGroupId, both parameters take effect.
        self.resource_group_ids = resource_group_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_channel is not None:
            result['BusinessChannel'] = self.business_channel

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_group_ids is not None:
            result['ResourceGroupIds'] = self.resource_group_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessChannel') is not None:
            self.business_channel = m.get('BusinessChannel')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceGroupIds') is not None:
            self.resource_group_ids = m.get('ResourceGroupIds')

        return self

