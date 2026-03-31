# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeNetworkFlowTimeSeriesMetricShrinkRequest(DaraModel):
    def __init__(
        self,
        filter_shrink: str = None,
        instance_id: str = None,
        metric: str = None,
        region_id: str = None,
        resource_manager_resource_group_id: str = None,
    ):
        # Specifies filtering conditions. Multiple filter parameters use AND logic.
        # 
        # This parameter is required.
        self.filter_shrink = filter_shrink
        # The Web Application Firewall (WAF) instance ID.
        # > Call the [DescribeInstanceInfo](https://help.aliyun.com/document_detail/140857.html) operation to retrieve the WAF instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Specifies the data type to be returned. Valid values:
        # 
        # *   qps: Returns the queries per second (QPS) processed by WAF. This value is calculated using a peak detection method: QPS is measured every 10 seconds, and the highest value within the specified time range is returned.
        # *   total_requests: Returns the total number of requests processed by WAF.
        # *   top5_status: Returns the top 5 HTTP status codes returned by the WAF to clients, along with their corresponding time series statistics.
        # *   top 5_upstream_status: Returns the top 5 HTTP status codes returned by the origin server to clients, along with their corresponding time series data.
        # 
        # This parameter is required.
        self.metric = metric
        # The region ID of WAF instance. Valid values:
        # 
        # *   **cn-hangzhou**: The Chinese mainland.
        # *   **ap-southeast-1**: Outside the Chinese mainland.
        self.region_id = region_id
        # The resource group ID.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter_shrink is not None:
            result['Filter'] = self.filter_shrink

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
        if m.get('Filter') is not None:
            self.filter_shrink = m.get('Filter')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Metric') is not None:
            self.metric = m.get('Metric')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        return self

