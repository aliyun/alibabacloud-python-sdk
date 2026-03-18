# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeInstanceSpecsRequest(DaraModel):
    def __init__(
        self,
        instance_id_list: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # The ID of the Anti-DDoS Origin instance. This parameter is a string that consists of JSON arrays. Each element in a JSON array indicates an instance ID. If you want to query more than one instance, separate instance IDs with commas (,).
        # 
        # >  You can call the [DescribeInstanceList](https://help.aliyun.com/document_detail/118698.html) operation to query the IDs of all Anti-DDoS Origin instances in a specific region.
        # 
        # This parameter is required.
        self.instance_id_list = instance_id_list
        # The region ID of the Anti-DDoS Origin instance. Default value: **cn-hangzhou**, which indicates the China (Hangzhou) region.
        # 
        # >  If your instance does not reside in the China (Hangzhou) region, you must set this parameter to the region ID of your instance. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/118703.html) operation to query the regions of assets that can be protected by Anti-DDoS Origin in a specific region.
        self.region_id = region_id
        # The ID of the resource group to which the Anti-DDoS Origin instance belongs in Resource Management. This parameter is empty by default, which indicates that the Anti-DDoS Origin instance belongs to the default resource group.
        # 
        # For information about resource groups, see [Create a resource group](https://help.aliyun.com/document_detail/94485.html).
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id_list is not None:
            result['InstanceIdList'] = self.instance_id_list

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIdList') is not None:
            self.instance_id_list = m.get('InstanceIdList')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

