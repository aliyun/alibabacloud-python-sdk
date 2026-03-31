# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeHybridCloudGroupsRequest(DaraModel):
    def __init__(
        self,
        cluster_id: int = None,
        cluster_proxy_type: str = None,
        group_name: int = None,
        group_type: str = None,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_manager_resource_group_id: str = None,
    ):
        # The ID of the hybrid cloud cluster.
        self.cluster_id = cluster_id
        # The type of proxy cluster that is used. Valid values:
        # 
        # *   **service**: service-based traffic mirroring.
        # *   **cname**: reverse proxy.
        self.cluster_proxy_type = cluster_proxy_type
        # The name of the node group that you want to query.
        self.group_name = group_name
        # The type of the node group. Valid values:
        # 
        # *   **protect**
        # *   **control**
        # *   **storage**
        # *   **controlStorage**
        self.group_type = group_type
        # The ID of the WAF instance.
        # 
        # > You can call the [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) operation to obtain the ID of the WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The page number. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Default value: **10**.
        self.page_size = page_size
        # The region ID of the WAF instance. Valid values:
        # 
        # *   **cn-hangzhou:** the Chinese mainland.
        # *   **ap-southeast-1:** outside the Chinese mainland.
        self.region_id = region_id
        # The ID of the resource group.
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

        if self.cluster_proxy_type is not None:
            result['ClusterProxyType'] = self.cluster_proxy_type

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.group_type is not None:
            result['GroupType'] = self.group_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterProxyType') is not None:
            self.cluster_proxy_type = m.get('ClusterProxyType')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        return self

