# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetNisTrafficMetricsShrinkRequest(DaraModel):
    def __init__(
        self,
        begin_time: int = None,
        direction: str = None,
        end_time: int = None,
        filter_shrink: str = None,
        max_results: int = None,
        metric_name: str = None,
        next_token: str = None,
        region_no: str = None,
        scan_by: str = None,
        step_minutes: int = None,
        storage_interval: int = None,
        traffic_analyzer_id: str = None,
        traffic_scenario: str = None,
        tuple_dimension: str = None,
    ):
        # The start timestamp, in milliseconds. If not specified, the most recent 1 hour is queried by default.
        # 
        # This parameter is required.
        self.begin_time = begin_time
        # The network traffic direction based on Alibaba Cloud resources.
        # 
        # In: traffic flowing into the target resource.
        # Out: traffic flowing out of the target resource.
        # 
        # This parameter is required.
        self.direction = direction
        # The end timestamp, in milliseconds. If not specified, the most recent 1 hour is queried by default. If only BeginTime is specified, the 1 hour after BeginTime is queried.
        # 
        # This parameter is required.
        self.end_time = end_time
        # Specifies additional filter conditions for the traffic to perform focused network traffic analysis.
        self.filter_shrink = filter_shrink
        # In VPC scenarios, this parameter specifies the paging size. In TR and Internet Shared Bandwidth scenarios, this parameter specifies the SQL query limit. If not specified, the backend defaults to 1440.
        self.max_results = max_results
        # The metric name.
        # Common parameters supported in network traffic analysis scenarios:
        #   bps: bits per second.
        #   pps: packets per second.
        # Parameters specific to the Internet scenario:
        #   rtt: round-trip time when establishing a TCP protocol connection.
        #   RetransmitRate: retransmission rate.
        # Parameters specific to the area-level bandwidth scenario:
        #   RatelimitDropPps: rate of packet loss due to rate limiting.
        #   BandwidthUtilization: bandwidth utilization.
        # Parameters specific to the NAT scenario:
        #   ActiveSessionCount: number of concurrent sessions.
        #   NewSessionPerSecond: number of new sessions per second.
        # 
        # This parameter is required.
        self.metric_name = metric_name
        # The token for the next query. You do not need to specify this parameter for the first query or when no more results exist. If a next page exists, set this parameter to the NextToken value returned by the previous API invoke. This parameter is valid only in VPC scenarios. TR and Internet Shared Bandwidth scenarios do not use this parameter.
        self.next_token = next_token
        # The region ID.
        # 
        # This parameter is required.
        self.region_no = region_no
        # The sort order. Valid values:
        # TimestampAscending: sorts by time in ascending order.
        # TimestampDescending: sorts by time in descending order.
        self.scan_by = scan_by
        # The aggregation step for time series data, in minutes. The final query granularity is the larger value between StepMinutes and the underlying storage granularity. The number of data points calculated by (EndTime-BeginTime)/StepMinutes cannot exceed 1440.
        self.step_minutes = step_minutes
        # The storage bucket precision property.
        # 
        # The storage bucket precision specifies the storage aggregation epoch to query. Two precision levels are supported: high precision (such as 1 minute) or long epoch (such as 1 day). The specific precision is determined by the network traffic analysis sampling interval configured for high-precision traffic statistics or long-epoch traffic statistics when creating or editing the network traffic analysis analyzer.
        # 
        # - The storage precisions active for the corresponding tuples of the network traffic analysis analyzer are:
        #   - `1`: in minutes (1 minute)
        #   - `10`: in minutes (10 minutes)
        #   - `60`: in minutes (60 minutes, i.e., 1 hour)
        #   - `1440`: in minutes (1440 minutes, i.e., 1 day)
        # 
        # - The storage bucket precision can be used for two typical purposes:
        #   - High-precision traffic statistics: such as 1-minute, 10-minute, or 60-minute aggregation
        #   - Long-epoch traffic statistics: such as 1440-minute (1-day) aggregation
        # 
        # - Specify a value for this field during the query to select the storage aggregation epoch. For example:
        #   - Pass `10`: queries short-epoch data with a 10-minute aggregation granularity
        #   - Pass `1440`: queries long-epoch data with a 1-day aggregation granularity
        self.storage_interval = storage_interval
        # The ID of the network traffic analysis analyzer.
        # 
        # This parameter is required.
        self.traffic_analyzer_id = traffic_analyzer_id
        # The supported analysis scenarios: 
        # 
        # - All VPC flow log analysis
        # - Internet VPC flow log analysis
        # - All TR flow log analysis
        # - Internet Shared Bandwidth metric analysis
        # 
        # This parameter is required.
        self.traffic_scenario = traffic_scenario
        # The traffic storage aggregation dimension.
        # 
        # Based on the TrafficScenario:
        # 
        # - VpcFlowLogAll/VpcFlowLog: required. Specifies the storage aggregation view to query, which corresponds to the storage aggregation property configured in the network traffic analysis analyzer.
        # 
        # - TRFlowLog/CbwpMetric: optional. Automatically adapts based on the storage aggregation property of the network traffic analysis analyzer.
        self.tuple_dimension = tuple_dimension

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        if self.direction is not None:
            result['Direction'] = self.direction

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.filter_shrink is not None:
            result['Filter'] = self.filter_shrink

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        if self.scan_by is not None:
            result['ScanBy'] = self.scan_by

        if self.step_minutes is not None:
            result['StepMinutes'] = self.step_minutes

        if self.storage_interval is not None:
            result['StorageInterval'] = self.storage_interval

        if self.traffic_analyzer_id is not None:
            result['TrafficAnalyzerId'] = self.traffic_analyzer_id

        if self.traffic_scenario is not None:
            result['TrafficScenario'] = self.traffic_scenario

        if self.tuple_dimension is not None:
            result['TupleDimension'] = self.tuple_dimension

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Filter') is not None:
            self.filter_shrink = m.get('Filter')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        if m.get('ScanBy') is not None:
            self.scan_by = m.get('ScanBy')

        if m.get('StepMinutes') is not None:
            self.step_minutes = m.get('StepMinutes')

        if m.get('StorageInterval') is not None:
            self.storage_interval = m.get('StorageInterval')

        if m.get('TrafficAnalyzerId') is not None:
            self.traffic_analyzer_id = m.get('TrafficAnalyzerId')

        if m.get('TrafficScenario') is not None:
            self.traffic_scenario = m.get('TrafficScenario')

        if m.get('TupleDimension') is not None:
            self.tuple_dimension = m.get('TupleDimension')

        return self

