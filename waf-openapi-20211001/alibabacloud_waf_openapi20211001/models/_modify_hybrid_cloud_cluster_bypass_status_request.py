# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyHybridCloudClusterBypassStatusRequest(DaraModel):
    def __init__(
        self,
        cluster_resource_id: str = None,
        instance_id: str = None,
        region_id: str = None,
        resource_manager_resource_group_id: str = None,
        rule_status: str = None,
    ):
        # The ID of the hybrid cloud cluster.
        # 
        # This parameter is required.
        self.cluster_resource_id = cluster_resource_id
        # The ID of the Web Application Firewall (WAF) instance.
        # 
        # **
        # 
        # **You can call the **DescribeInstanceInfo[ operation to obtain the ID of the WAF instance.](https://help.aliyun.com/document_detail/140857.html)
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID of the WAF instance. Valid values:
        # 
        # *   **cn-hangzhou**: Chinese mainland
        # *   **ap-southeast-1**: outside the Chinese mainland.
        self.region_id = region_id
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # The status of manual bypass. Valid values:
        # 
        # *   **on**: enabled.
        # *   **off**: disabled. This is the default value.
        # 
        # This parameter is required.
        self.rule_status = rule_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_resource_id is not None:
            result['ClusterResourceId'] = self.cluster_resource_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        if self.rule_status is not None:
            result['RuleStatus'] = self.rule_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterResourceId') is not None:
            self.cluster_resource_id = m.get('ClusterResourceId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        if m.get('RuleStatus') is not None:
            self.rule_status = m.get('RuleStatus')

        return self

