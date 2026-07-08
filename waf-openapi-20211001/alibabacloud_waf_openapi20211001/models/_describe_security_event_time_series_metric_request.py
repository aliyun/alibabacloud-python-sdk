# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeSecurityEventTimeSeriesMetricRequest(DaraModel):
    def __init__(
        self,
        filter: main_models.DescribeSecurityEventTimeSeriesMetricRequestFilter = None,
        instance_id: str = None,
        metric: str = None,
        region_id: str = None,
        resource_manager_resource_group_id: str = None,
    ):
        # The filter conditions for the query. Multiple filter conditions have a logical AND relationship.
        # 
        # This parameter is required.
        self.filter = filter
        # The ID of the Web Application Firewall (WAF) instance.
        # 
        # > Call [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) to query the ID of the WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Specifies the content of the returned data. Different metrics correspond to different data content. This operation supports the following metrics:
        # 
        # - mitigated_requests: Returns the time series statistics of blocked requests.
        # 
        # - monitored_requests: Returns the time series statistics of requests that hit only observation-type rules.
        # 
        # - mitigated_requests_group_by_defense_scene: Returns data grouped by module. It records a time series graph of the hit count for each module. A single request may hit multiple modules. Therefore, the hit count returned by this metric may not be consistent with the number of requests.
        # 
        # - mitigated_requests_group_by_block_defense_scene: Returns data grouped by module. It records a time series graph of the number of blocked requests for each module. A single request is blocked by only one module. Therefore, the count returned by this metric is consistent with the number of requests.
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
            temp_model = main_models.DescribeSecurityEventTimeSeriesMetricRequestFilter()
            self.filter = temp_model.from_map(m.get('Filter'))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Metric') is not None:
            self.metric = m.get('Metric')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        return self

class DescribeSecurityEventTimeSeriesMetricRequestFilter(DaraModel):
    def __init__(
        self,
        conditions: List[main_models.DescribeSecurityEventTimeSeriesMetricRequestFilterConditions] = None,
        date_range: main_models.DescribeSecurityEventTimeSeriesMetricRequestFilterDateRange = None,
    ):
        # A list of filter conditions. Each node describes one filter condition.
        self.conditions = conditions
        # The time range to query.
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
                temp_model = main_models.DescribeSecurityEventTimeSeriesMetricRequestFilterConditions()
                self.conditions.append(temp_model.from_map(k1))

        if m.get('DateRange') is not None:
            temp_model = main_models.DescribeSecurityEventTimeSeriesMetricRequestFilterDateRange()
            self.date_range = temp_model.from_map(m.get('DateRange'))

        return self

class DescribeSecurityEventTimeSeriesMetricRequestFilterDateRange(DaraModel):
    def __init__(
        self,
        end_date: int = None,
        start_date: int = None,
    ):
        # The end time of the query. This is a UNIX timestamp. Unit: seconds.
        # 
        # This parameter is required.
        self.end_date = end_date
        # You can query data from the last 30 days. The start time of the query. This is a UNIX timestamp. Unit: seconds.
        # 
        # > ## The start time must be within the last 30 days.
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

class DescribeSecurityEventTimeSeriesMetricRequestFilterConditions(DaraModel):
    def __init__(
        self,
        key: str = None,
        op_value: str = None,
        values: Any = None,
    ):
        # The name of the field to filter. This operation supports all fields.
        self.key = key
        # The operator.
        self.op_value = op_value
        # The filter value.
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

