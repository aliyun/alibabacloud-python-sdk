# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddIpRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        ip_list: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # The ID of the Anti-DDoS Origin instance to manage.
        # 
        # > Call [DescribeInstanceList](https://help.aliyun.com/document_detail/118698.html) to query the IDs of all Anti-DDoS Origin instances.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The list of IP addresses to add to the Anti-DDoS Origin instance for protection. The value is a string that is converted from a JSON array. Each element in the JSON array is a struct that contains the following fields:
        # 
        # - **ip**: The IP address to add. This parameter is of the String type and is required.
        # 
        # - **member_uid**: The ID of the member account that owns the asset. This parameter is of the String type and is optional. Specify this parameter only when you add an asset that belongs to a member account. For example: [{"ip":"121.41.XX.XX","member_uid":"120100811162\\*\\*\\*\\*"}]
        # 
        # This parameter is required.
        self.ip_list = ip_list
        # The region ID of the Anti-DDoS Origin instance.
        # 
        # > Call [DescribeRegions](https://help.aliyun.com/document_detail/118703.html) to query information about all regions that Anti-DDoS Origin supports.
        self.region_id = region_id
        # The ID of the resource group in Resource Management to which the Anti-DDoS Origin instance belongs. If you leave this parameter empty, the instance is added to the default resource group.
        # 
        # For more information about resource groups, see [Create a resource group](https://help.aliyun.com/document_detail/94485.html).
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

