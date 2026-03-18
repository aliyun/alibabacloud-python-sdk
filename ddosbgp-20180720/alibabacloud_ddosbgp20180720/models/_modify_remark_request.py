# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyRemarkRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        remark: str = None,
        resource_group_id: str = None,
    ):
        # The ID of the Anti-DDoS Origin instance for which you want to add remarks.
        # 
        # >  You can call the [DescribeInstanceList](https://help.aliyun.com/document_detail/118698.html) operation to query the IDs of all Anti-DDoS Origin instances.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the region where the Anti-DDoS Origin instance resides.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/118703.html) operation to query the most recent region list.
        self.region_id = region_id
        # The remarks for the Anti-DDoS Origin instance.
        # 
        # This parameter is required.
        self.remark = remark
        # The ID of the resource group to which the Anti-DDoS Origin instance belongs in Resource Management.
        # 
        # If you do not specify this parameter, the instance belongs to the default resource group.
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

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

