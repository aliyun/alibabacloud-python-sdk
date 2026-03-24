# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeNetworkFlowTopNMetricShrinkRequest(DaraModel):
    def __init__(
        self,
        filter_shrink: str = None,
        instance_id: str = None,
        limit: int = None,
        metric: str = None,
        region_id: str = None,
        resource_manager_resource_group_id: str = None,
    ):
        # The filter conditions for the query. If you specify multiple filter conditions, all conditions must be met (logical AND).
        # 
        # This parameter is required.
        self.filter_shrink = filter_shrink
        # The ID of the WAF instance.
        # 
        # > You can call the [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) operation to query the ID of the WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The maximum number of entries to return. Results are sorted in descending order. Maximum value: 10.
        # 
        # This parameter is required.
        self.limit = limit
        # The metric by which to query and rank data. Valid values:
        # 
        # - real_client_ip: Returns the top N source IP addresses of requests that are sent to WAF. The data is aggregated by source IP address and sorted in descending order.
        # 
        # - http_user_agent: Returns the top N user agents of requests that are sent to WAF. The data is aggregated by user agent and sorted in descending order.
        # 
        # - request_path: Returns the top N request URLs. The data is aggregated by URL and sorted in descending order.
        # 
        # - matched_host_by_total_requests: Returns the top N protected objects by total number of requests received.
        # 
        # - matched_host_by_qps: Returns the top N protected objects by queries per second (QPS).
        # 
        # - matched_host_by_status: Returns the top N protected objects based on a specific WAF-returned HTTP status code. The data is aggregated by protected object and sorted in descending order. If you set Metric to this value, you must specify the status field in the Conditions parameter of Filter. The format is as follows:<br> {"Key":"status","OpValue":"eq","Values":"200"}<br>
        # 
        # - matched_host_by_upstream_status: Returns the top N protected objects based on a specific origin server-returned HTTP status code. The data is aggregated by protected object and sorted in descending order. If you set Metric to this value, you must specify the upstream_status field in the Conditions parameter of Filter. The format is as follows:<br> {"Key":"upstream_status","OpValue":"eq","Values":"200"}<br>
        # 
        # This parameter is required.
        self.metric = metric
        # The region in which the WAF instance resides. Valid values:
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
        if self.filter_shrink is not None:
            result['Filter'] = self.filter_shrink

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.limit is not None:
            result['Limit'] = self.limit

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

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('Metric') is not None:
            self.metric = m.get('Metric')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        return self

