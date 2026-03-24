# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeThreatEventTopMetricRequest(DaraModel):
    def __init__(
        self,
        event_id: str = None,
        instance_id: str = None,
        metric: str = None,
        region_id: str = None,
        resource_manager_resource_group_id: str = None,
    ):
        # The ID of the security event.
        # 
        # This parameter is required.
        self.event_id = event_id
        # The ID of the Web Application Firewall (WAF) instance.
        # 
        # > Call the [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) operation to query the ID of the WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The metric that you want to use for statistics. Each metric corresponds to a different statistical object. Valid values:
        # 
        # - **time**: Aggregates statistics by attack time and returns the top 5 entries in descending order.
        # 
        # - **src**: Aggregates statistics by the source IP address of attack requests and returns the top 5 entries in descending order.
        # 
        # - **target**: Aggregates statistics by the URL of attack requests, excluding the query string, and returns the top 5 entries in descending order.
        # 
        # - **type**: Aggregates statistics by attack type and returns the top 5 entries in descending order.
        # 
        # - **tools**: Aggregates statistics by attack tool and returns the top 5 entries in descending order.
        # 
        # This parameter is required.
        self.metric = metric
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
        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.metric is not None:
            result['Metric'] = self.metric

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Metric') is not None:
            self.metric = m.get('Metric')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        return self

