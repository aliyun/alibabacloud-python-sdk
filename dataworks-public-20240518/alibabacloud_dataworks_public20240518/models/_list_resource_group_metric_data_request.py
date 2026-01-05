# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListResourceGroupMetricDataRequest(DaraModel):
    def __init__(
        self,
        begin_time: int = None,
        end_time: int = None,
        length: int = None,
        metric_name: str = None,
        next_token: str = None,
        period: str = None,
        resource_group_id: str = None,
    ):
        # The start time.
        # 
        # Supported format: Unix timestamp in milliseconds (the number of milliseconds that have elapsed since January 1, 1970).
        # 
        # The interval between BeginTime and EndTime must be less than or equal to 31 days.
        # 
        # Default: The current time minus 2 hours, expressed as a millisecond Unix timestamp.
        self.begin_time = begin_time
        # The end time.
        # 
        # Supported format: Unix timestamp in milliseconds (the number of milliseconds that have elapsed since January 1, 1970).
        # 
        # The interval between BeginTime and EndTime must be less than or equal to 31 days.
        # 
        # Default: The current time, expressed as a millisecond Unix timestamp.
        self.end_time = end_time
        # The number of records to display on each page for paginated queries.
        # 
        # >  The maximum value of Length for a single request is 1440.
        self.length = length
        # The metric name. Valid values:
        # 
        # *   CUSpec: Maximum CU capacity of the resource group, in CUs.
        # *   CUUsage: CU usage of the resource group, in CUs.
        # *   CUUtilization: CU utilization of the resource group, in %.
        # *   SlotSpec: Maximum number of concurrent slots for resource group scheduling, in slots.
        # *   SlotUsage: Used concurrency for resource group scheduling, in slots.
        # *   SchedulerCUMaxSpec: Maximum CU quota for data computing, in CUs.
        # *   SchedulerCUUsage: CU usage for data computing, in CUs.
        # *   SchedulerCUMinSpec: Minimum guaranteed CUs for data computing, in CUs.
        # *   DataIntegrationCUMaxSpec: Maximum CU quota for Data Integration, in CUs.
        # *   DataIntegrationCUUsage: CU usage for Data Integration, in CUs.
        # *   DataIntegrationCUMinSpec: Minimum guaranteed CUs for Data Integration, in CUs.
        # *   DataServiceCUMaxSpec: Maximum CU quota for DataService Studio, in CUs.
        # *   DataServiceCUUsage: CU usage for DataService Studio, in CUs.
        # *   DataServiceCUMinSpec: Minimum guaranteed CUs for DataService Studio, in CUs.
        # *   ServerIdeCUMaxSpec: Maximum CU quota for personal development environment, in CUs.
        # *   ServerIdeCUUsage: CU usage for personal development environment, in CUs.
        # *   ServerIdeCUMinSpec: Minimum guaranteed CUs for personal development environment, in CUs.
        # 
        # This parameter is required.
        self.metric_name = metric_name
        # The pagination cursor.
        # 
        # >  If this parameter is not set, the first page of data is retrieved. If a value is returned for this parameter, it indicates that there is a next page. You can use the returned NextToken as a parameter to request the next page of data until it returns Null, which means all data has been retrieved.
        self.next_token = next_token
        # The statistical period for monitoring data.
        # 
        # Value: A multiple of 60.
        # 
        # Unit: Seconds.
        # 
        # Default: 60.
        self.period = period
        # The unique identifier for the general-purpose resource group.
        # 
        # This parameter is required.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.length is not None:
            result['Length'] = self.length

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.period is not None:
            result['Period'] = self.period

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Length') is not None:
            self.length = m.get('Length')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

