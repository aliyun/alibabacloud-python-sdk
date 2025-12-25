# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeUserAssetRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        data_type: str = None,
        days: str = None,
        instance_id: str = None,
        region_id: str = None,
        resource_manager_resource_group_id: str = None,
    ):
        # The ID of the hybrid cloud cluster.
        # >For hybrid cloud scenarios only, you can call the [DescribeHybridCloudClusters](https://help.aliyun.com/document_detail/2849376.html) operation to query the hybrid cloud clusters.
        self.cluster_id = cluster_id
        # The type of the statistics. Valid values:
        # 
        # *   **asset_num**: total number of APIs
        # *   **asset_active**: number of active APIs
        # *   **asset_newborn**: number of new APIs
        # *   **asset_offline**: number of deactivated APIs
        # *   **asset_bot**: number of APIs that are called by bots
        # *   **asset_cross_border**: number of APIs that are called for cross-border data transfer
        # *   **sensitive_api**: number of response-sensitive APIs
        # *   **sensitive_domain**: number of response-sensitive domain names
        # 
        # This parameter is required.
        self.data_type = data_type
        # The time at which the API was called. The value is a UNIX timestamp displayed in UTC. Unit: seconds.
        # >Notice: The parameter has been deprecated.
        self.days = days
        # The ID of the Web Application Firewall (WAF) instance.
        # 
        # >  You can call the [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) operation to query the ID of the WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region in which the WAF instance is deployed. Valid values:
        # 
        # *   **cn-hangzhou**: Chinese mainland
        # *   **ap-southeast-1**: outside the Chinese mainland
        self.region_id = region_id
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.days is not None:
            result['Days'] = self.days

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('Days') is not None:
            self.days = m.get('Days')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        return self

