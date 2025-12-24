# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeLifecycleHooksRequest(DaraModel):
    def __init__(
        self,
        lifecycle_hook_ids: List[str] = None,
        lifecycle_hook_name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        scaling_group_id: str = None,
    ):
        # The IDs of the lifecycle hooks that you want to query.
        self.lifecycle_hook_ids = lifecycle_hook_ids
        # The name of the lifecycle hook.
        self.lifecycle_hook_name = lifecycle_hook_name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The number of the page to return. Pages start from page 1.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Maximum value: 50.
        # 
        # Default value: 50.
        self.page_size = page_size
        # The region ID of the scaling group.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        # The ID of the scaling group.
        self.scaling_group_id = scaling_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lifecycle_hook_ids is not None:
            result['LifecycleHookIds'] = self.lifecycle_hook_ids

        if self.lifecycle_hook_name is not None:
            result['LifecycleHookName'] = self.lifecycle_hook_name

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LifecycleHookIds') is not None:
            self.lifecycle_hook_ids = m.get('LifecycleHookIds')

        if m.get('LifecycleHookName') is not None:
            self.lifecycle_hook_name = m.get('LifecycleHookName')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')

        return self

