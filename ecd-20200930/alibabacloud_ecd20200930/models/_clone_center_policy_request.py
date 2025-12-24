# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CloneCenterPolicyRequest(DaraModel):
    def __init__(
        self,
        business_type: int = None,
        name: str = None,
        policy_group_id: str = None,
        region_id: str = None,
        resource_type: str = None,
    ):
        # The business type.
        # 
        # Valid values:
        # 
        # *   1: public cloud
        # *   8: commercial edition.
        # 
        # This parameter is required.
        self.business_type = business_type
        # The name of the cloud computer policy that you want to clone.
        # 
        # This parameter is required.
        self.name = name
        # The ID of the cloud computer policy that you want to clone.
        # 
        # This parameter is required.
        self.policy_group_id = policy_group_id
        # The region ID. Set the value to cn-shanghai.
        # 
        # This parameter is required.
        self.region_id = region_id
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
        if self.business_type is not None:
            result['BusinessType'] = self.business_type

        if self.name is not None:
            result['Name'] = self.name

        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

