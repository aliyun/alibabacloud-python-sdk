# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AuthorizeResourceGroupRequest(DaraModel):
    def __init__(
        self,
        resource_group_ids: str = None,
        target_user_id: str = None,
    ):
        # The ID of the resource group. You can call the ListResourceGroup operation to query the resource group ID. For more information, see [ListResourceGroup](https://help.aliyun.com/document_detail/62055.html).
        # 
        # You can specify multiple resource group IDs. Separate multiple resource group IDs with semicolons (;).
        # 
        # This parameter is required.
        self.resource_group_ids = resource_group_ids
        # The ID of the RAM user to be authorized.
        # 
        # This parameter is required.
        self.target_user_id = target_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_group_ids is not None:
            result['ResourceGroupIds'] = self.resource_group_ids

        if self.target_user_id is not None:
            result['TargetUserId'] = self.target_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupIds') is not None:
            self.resource_group_ids = m.get('ResourceGroupIds')

        if m.get('TargetUserId') is not None:
            self.target_user_id = m.get('TargetUserId')

        return self

