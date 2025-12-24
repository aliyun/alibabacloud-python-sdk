# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyDesktopsPolicyGroupRequest(DaraModel):
    def __init__(
        self,
        desktop_id: List[str] = None,
        policy_group_id: str = None,
        policy_group_ids: List[str] = None,
        region_id: str = None,
    ):
        # The cloud computer IDs. You can specify one or more cloud computers IDs. The value is a JSON array.
        # 
        # This parameter is required.
        self.desktop_id = desktop_id
        # The ID of the cloud computer policy that you want to associate with cloud computers.
        # 
        # >  If the `PolicyGroupIds` parameter is used, ignore the current parameter.
        self.policy_group_id = policy_group_id
        # The IDs of the cloud computer policies that you want to associate with cloud computers.
        # 
        # >  You can specify up to one cloud computer policy that takes effect globally, and up to four cloud computer policies that apply to specific IP addresses. If you specify more than one cloud computer policy that takes effect globally, only the policy first associate with the cloud computer can take effect.
        self.policy_group_ids = policy_group_ids
        # The region ID. You can call the [DescribeRegions](~~DescribeRegions~~) operation to query the regions supported by Elastic Desktop Service (EDS).
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id

        if self.policy_group_ids is not None:
            result['PolicyGroupIds'] = self.policy_group_ids

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')

        if m.get('PolicyGroupIds') is not None:
            self.policy_group_ids = m.get('PolicyGroupIds')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

