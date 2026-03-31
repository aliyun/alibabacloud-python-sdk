# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeNetworkFlowTopNMetricRequest(DaraModel):
    def __init__(
        self,
        filter: main_models.DescribeNetworkFlowTopNMetricRequestFilter = None,
        instance_id: str = None,
        limit: int = None,
        metric: str = None,
        region_id: str = None,
        resource_manager_resource_group_id: str = None,
    ):
        # An array of filter conditions. Multiple filter parameters use AND logic.
        # 
        # This parameter is required.
        self.filter = filter
        # The Web Application Firewall (WAF) instance ID.
        # 
        # >  Call the [DescribeInstanceInfo](https://help.aliyun.com/document_detail/140857.html) operation to retrieve the WAF instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Returns up to 10 data entries, sorted in descending order.
        # 
        # This parameter is required.
        self.limit = limit
        # Specifies the data type to be returned. Valid values:
        # 
        # *   real_client_ip: The top N requests, sorted in descending order by source IP address, aggregated from all the current user\\"s WAF requests.
        # *   request_path: The top N requests, sorted in descending order by user-agent, aggregated from all the current user\\"s WAF requests.
        # *   request_path: The top N requests, sorted in descending order by request URL, aggregated from all the current user\\"s WAF requests.
        # *   matched_host_by_total_requests: The top N protected objects and their request counts for the current user.
        # *   matched_host_by_qps: The top N protected objects and their queries per second (QPS) values.
        # *   matched_host_by_status: When using it, you must specify status in the Conditions field of the Filter parameter. If the HTTP response code returned by WAF matches the status specified in the Conditions, then the top N data is returned, sorted in descending order by protected objects. The format for specifying the status is as follows:\\
        #     {"Key":"status","OpValue":"eq","Values":"200"}
        # *   matched_host_by_upstream_status: When using it, you must specify upstream_status in the Conditions field of the Filter parameter. If the HTTP response code returned by the origin server matches the upstream_status specified, the top N data is returned, sorted in descending order by protected objects. The format for specifying the upstream_status is as follows:\\
        #     {"Key":"upstream_status","OpValue":"eq","Values":"200"}
        # 
        # This parameter is required.
        self.metric = metric
        # The region ID of the WAF instance. Valid values:
        # 
        # *   **cn-hangzhou**: The Chinese mainland.
        # *   **ap-southeast-1**: Outside the Chinese mainland.
        self.region_id = region_id
        # The resource group ID.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id

    def validate(self):
        if self.filter:
            self.filter.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter is not None:
            result['Filter'] = self.filter.to_map()

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
            temp_model = main_models.DescribeNetworkFlowTopNMetricRequestFilter()
            self.filter = temp_model.from_map(m.get('Filter'))

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

class DescribeNetworkFlowTopNMetricRequestFilter(DaraModel):
    def __init__(
        self,
        conditions: List[main_models.DescribeNetworkFlowTopNMetricRequestFilterConditions] = None,
        date_range: main_models.DescribeNetworkFlowTopNMetricRequestFilterDateRange = None,
    ):
        # The list of filter conditions. Each node describes a filter condition.
        self.conditions = conditions
        # Specifies the date range for the query.
        # 
        # This parameter is required.
        self.date_range = date_range

    def validate(self):
        if self.conditions:
            for v1 in self.conditions:
                 if v1:
                    v1.validate()
        if self.date_range:
            self.date_range.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Conditions'] = []
        if self.conditions is not None:
            for k1 in self.conditions:
                result['Conditions'].append(k1.to_map() if k1 else None)

        if self.date_range is not None:
            result['DateRange'] = self.date_range.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conditions = []
        if m.get('Conditions') is not None:
            for k1 in m.get('Conditions'):
                temp_model = main_models.DescribeNetworkFlowTopNMetricRequestFilterConditions()
                self.conditions.append(temp_model.from_map(k1))

        if m.get('DateRange') is not None:
            temp_model = main_models.DescribeNetworkFlowTopNMetricRequestFilterDateRange()
            self.date_range = temp_model.from_map(m.get('DateRange'))

        return self

class DescribeNetworkFlowTopNMetricRequestFilterDateRange(DaraModel):
    def __init__(
        self,
        end_date: int = None,
        start_date: int = None,
    ):
        # End time of the query range (Unix timestamp, seconds).
        # 
        # This parameter is required.
        self.end_date = end_date
        # Start time of the query range (Unix timestamp, seconds).
        # 
        # This parameter is required.
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        return self

class DescribeNetworkFlowTopNMetricRequestFilterConditions(DaraModel):
    def __init__(
        self,
        key: str = None,
        op_value: str = None,
        values: Any = None,
    ):
        # The filter fields. Valid values:
        # 
        # *   matched_host
        # *   cluster
        # 
        # For details, see the **Filter fields (Key)** section below.
        self.key = key
        # The filter operator.
        # For details, see the **Filter operators (OpValue)** section below.
        self.op_value = op_value
        # The filter content.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.op_value is not None:
            result['OpValue'] = self.op_value

        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('OpValue') is not None:
            self.op_value = m.get('OpValue')

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

