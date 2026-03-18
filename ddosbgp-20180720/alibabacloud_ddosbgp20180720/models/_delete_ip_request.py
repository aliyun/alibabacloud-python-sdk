# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteIpRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        ip_list: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # The ID of the Anti-DDoS Origin instance.
        # 
        # >  You can call the [DescribeInstanceList](https://help.aliyun.com/document_detail/118698.html) operation to query the IDs of all Anti-DDoS Origin instances.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The IP addresses that you want to remove from the Anti-DDoS Origin instance. This parameter is a string that consists of JSON arrays. Each element in a JSON array is a JSON struct that contains the following fields:
        # 
        # *   **ip**: required. The IP address that you want to remove. Data type: string.
        # 
        #     **
        # 
        #     **Note** The IP addresses that you want to remove must be protected by the Anti-DDoS Origin instance.
        # 
        # This parameter is required.
        self.ip_list = ip_list
        # The ID of the region where the Anti-DDoS Origin instance resides.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/118703.html) operation to query the most recent region list.
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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.ip_list is not None:
            result['IpList'] = self.ip_list

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IpList') is not None:
            self.ip_list = m.get('IpList')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

