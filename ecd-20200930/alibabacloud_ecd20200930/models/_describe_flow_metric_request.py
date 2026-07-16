# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeFlowMetricRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        instance_id: str = None,
        instance_type: str = None,
        metric_type: str = None,
        period: int = None,
        region_id: str = None,
        start_time: str = None,
    ):
        # End Time. Supported formats:
        # 
        # - UNIX timestamp: the number of milliseconds elapsed since January 1, 1970.
        # 
        # - Format: YYYY-MM-DDThh:mm:ssZ.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The instance ID, which can be either a cloud computr ID or a premium public bandwidth plan ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The instance type. You can select either cloud computer type or premium public bandwidth type. If you select cloud computer type, the `InstanceId` and `MetricType` must be filled in with a cloud computer ID and its corresponding traffic type. The same applies to premium public bandwidth.
        # 
        # This parameter is required.
        self.instance_type = instance_type
        # The type of monitoring metric. Supports monitoring data for inbound and outbound bandwidth of cloud computers, as well as inbound and outbound bandwidth for public network access of premium public bandwidth.
        # 
        # This parameter is required.
        self.metric_type = metric_type
        # The statistic period of monitoring data. Unit: seconds.
        # 
        # This parameter is required.
        self.period = period
        # The Region ID. You can call [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) to obtain the list of Regions supported by Elastic Desktop Service (EDS).
        # 
        # This parameter is required.
        self.region_id = region_id
        # Start Time. Supported formats:
        # 
        # - UNIX timestamp: the number of milliseconds elapsed since January 1, 1970.
        # 
        # - Format: YYYY-MM-DDThh:mm:ssZ.
        # 
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.metric_type is not None:
            result['MetricType'] = self.metric_type

        if self.period is not None:
            result['Period'] = self.period

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

