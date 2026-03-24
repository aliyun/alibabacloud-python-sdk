# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeApisecEventDetailRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        detail_type: str = None,
        event_id: str = None,
        event_scope: str = None,
        instance_id: str = None,
        region_id: str = None,
        resource_manager_resource_group_id: str = None,
    ):
        # The ID of the Hybrid Cloud WAF cluster.
        # 
        # > This parameter applies only to hybrid cloud scenarios. You can call the [DescribeHybridCloudClusters](https://help.aliyun.com/document_detail/2849376.html) operation to query information about hybrid cloud WAF clusters.
        self.cluster_id = cluster_id
        # The type of the detailed information about the security event. Valid values:
        # 
        # - **event_info** (default): attack details.
        # 
        # - **api_info**: API information.
        # 
        # - **cnt_info**: attack trend.
        # 
        # - **ip_info**: attacker IP information.
        # 
        # - **sensitive_info**: information about access to sensitive data.
        # 
        # - **request_data**: request information.
        # 
        # - **response_data**: response information.
        self.detail_type = detail_type
        # The ID of the API security event.
        # 
        # This parameter is required.
        self.event_id = event_id
        # The dimension of the security event. Valid values:
        # 
        # - **ip** (default): IP security event.
        # 
        # - **account**: account security event.
        self.event_scope = event_scope
        # The ID of the Web Application Firewall (WAF) instance.
        # 
        # > You can call the [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) operation to query the ID of the WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region where the WAF instance resides. Valid values:
        # 
        # - **cn-hangzhou**: the Chinese mainland.
        # 
        # - **ap-southeast-1**: outside the Chinese mainland.
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

        if self.detail_type is not None:
            result['DetailType'] = self.detail_type

        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.event_scope is not None:
            result['EventScope'] = self.event_scope

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

        if m.get('DetailType') is not None:
            self.detail_type = m.get('DetailType')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('EventScope') is not None:
            self.event_scope = m.get('EventScope')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        return self

