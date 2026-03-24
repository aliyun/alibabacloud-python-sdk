# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeApisecUserOperationsRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        instance_id: str = None,
        object_id: str = None,
        region_id: str = None,
        resource_manager_resource_group_id: str = None,
        type: str = None,
    ):
        # The ID of the Hybrid Cloud WAF cluster.
        # 
        # > This parameter is required only when WAF is deployed in hybrid cloud mode. Call the [DescribeHybridCloudClusters](https://help.aliyun.com/document_detail/2849376.html) operation to query the IDs of Hybrid Cloud WAF clusters.
        self.cluster_id = cluster_id
        # The ID of the WAF instance.
        # 
        # > Call the [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) operation to query the ID of the WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the threat detection or security event for which you want to query operation records.
        # 
        # This parameter is required.
        self.object_id = object_id
        # The region in which the WAF instance resides. Valid values:
        # 
        # - **cn-hangzhou**: the Chinese mainland.
        # 
        # - **ap-southeast-1**: outside the Chinese mainland.
        self.region_id = region_id
        # The ID of the Alibaba Cloud resource group to which the WAF instance belongs.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # The type of the operation record. Valid values:
        # 
        # - **abnormal**: threat detection.
        # 
        # - **event**: security event.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.object_id is not None:
            result['ObjectId'] = self.object_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

