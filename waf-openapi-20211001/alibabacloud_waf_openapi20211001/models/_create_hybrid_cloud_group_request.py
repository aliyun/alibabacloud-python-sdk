# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateHybridCloudGroupRequest(DaraModel):
    def __init__(
        self,
        back_source_mark: str = None,
        cluster_id: int = None,
        group_name: str = None,
        group_type: str = None,
        instance_id: str = None,
        load_balance_ip: str = None,
        location_code: str = None,
        region_id: str = None,
        remark: str = None,
        resource_manager_resource_group_id: str = None,
    ):
        # The region in which the node resides. Specify the parameter in the Carrier code-Continent code-City code format.
        self.back_source_mark = back_source_mark
        # The ID of the hybrid cloud cluster.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The name of the node group.
        # 
        # This parameter is required.
        self.group_name = group_name
        # The type of the node group. Valid values:
        # 
        # *   **protect**
        # *   **control**
        # *   **storage**
        # *   **controlStorage**
        # 
        # This parameter is required.
        self.group_type = group_type
        # The ID of the WAF instance.
        # 
        # >  You can call the [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) operation to query the ID of the WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The IP address of the server used for load balancing.
        # 
        # This parameter is required.
        self.load_balance_ip = load_balance_ip
        # The region in which the node resides. Specify the parameter in the Carrier code-Continent code-City code format.
        self.location_code = location_code
        # The region ID of the WAF instance. Valid values:
        # 
        # *   **cn-hangzhou**: Chinese mainland.
        # *   **ap-southeast-1**: outside the Chinese mainland.
        self.region_id = region_id
        # The remarks.
        self.remark = remark
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.back_source_mark is not None:
            result['BackSourceMark'] = self.back_source_mark

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.group_type is not None:
            result['GroupType'] = self.group_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.load_balance_ip is not None:
            result['LoadBalanceIp'] = self.load_balance_ip

        if self.location_code is not None:
            result['LocationCode'] = self.location_code

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackSourceMark') is not None:
            self.back_source_mark = m.get('BackSourceMark')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LoadBalanceIp') is not None:
            self.load_balance_ip = m.get('LoadBalanceIp')

        if m.get('LocationCode') is not None:
            self.location_code = m.get('LocationCode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        return self

