# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeUserApiRequestRequest(DaraModel):
    def __init__(
        self,
        api_format: str = None,
        api_id: str = None,
        cluster_id: str = None,
        domain: str = None,
        instance_id: str = None,
        region_id: str = None,
        resource_manager_resource_group_id: str = None,
        type: str = None,
    ):
        # The API.
        # >Notice: This parameter is deprecated, please use ApiId to query.
        self.api_format = api_format
        # The ID of the API.
        # 
        # This parameter is required.
        self.api_id = api_id
        # The ID of the hybrid cloud cluster.
        # >For hybrid cloud scenarios only, you can call the [DescribeHybridCloudClusters](https://help.aliyun.com/document_detail/2849376.html) operation to query the hybrid cloud clusters.
        self.cluster_id = cluster_id
        # The domain name or IP address of the API.
        # >Notice: This parameter is deprecated, please use ApiId to query.
        self.domain = domain
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
        # The type of the statistics. Valid values:
        # 
        # *   **api_ip**: total traffic
        # *   **api_cross_border_ip**: cross-border traffic
        # *   **api_bot_ip**: bot traffic
        # *   **remote_region**: geographical location
        # *   **client_id**: client type
        # *   **http_referer**: Referer
        # *   **api_cnt**: total number of calls
        # *   **bot_cnt**: number of bot calls
        # *   **cross_border_cnt**: number of cross-border requests
        # *   **api_freq**: call frequency
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_format is not None:
            result['ApiFormat'] = self.api_format

        if self.api_id is not None:
            result['ApiId'] = self.api_id

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiFormat') is not None:
            self.api_format = m.get('ApiFormat')

        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

