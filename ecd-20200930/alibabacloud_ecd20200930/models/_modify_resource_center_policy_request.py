# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyResourceCenterPolicyRequest(DaraModel):
    def __init__(
        self,
        policy_group_ids: List[str] = None,
        policy_group_type: str = None,
        product_type: str = None,
        resource_ids: List[str] = None,
        resource_region_id: str = None,
        resource_type: str = None,
    ):
        # The IDs of the cloud computer policies that you want to associate with cloud computers.
        # 
        # >  You can specify up to one cloud computer policy that takes effect globally, and up to four cloud computer policies that apply to specific IP addresses. If multiple cloud computer policies are configured for global enforcement, only the earliest-associated policy will take effect
        # 
        # This parameter is required.
        self.policy_group_ids = policy_group_ids
        # The policy type.
        # 
        # Valid values:
        # 
        # *   general: a general policy.
        # 
        # This parameter is required.
        self.policy_group_type = policy_group_type
        # The service type.
        # 
        # Valid values:
        # 
        # *   app: cloud applications.
        # *   resourceGroup: resource groups.
        # *   desktop: cloud computers.
        # *   desktopGroup: cloud computer shares.
        # 
        # This parameter is required.
        self.product_type = product_type
        # The resource IDs. You can specify up to 100 resource IDs.
        # 
        # This parameter is required.
        self.resource_ids = resource_ids
        # The region ID of the resource.
        # 
        # This parameter is required.
        self.resource_region_id = resource_region_id
        # The resource type.
        # 
        # Valid values:
        # 
        # *   app: cloud applications.
        # *   desktop: cloud computers.
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
        if self.policy_group_ids is not None:
            result['PolicyGroupIds'] = self.policy_group_ids

        if self.policy_group_type is not None:
            result['PolicyGroupType'] = self.policy_group_type

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids

        if self.resource_region_id is not None:
            result['ResourceRegionId'] = self.resource_region_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyGroupIds') is not None:
            self.policy_group_ids = m.get('PolicyGroupIds')

        if m.get('PolicyGroupType') is not None:
            self.policy_group_type = m.get('PolicyGroupType')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')

        if m.get('ResourceRegionId') is not None:
            self.resource_region_id = m.get('ResourceRegionId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

