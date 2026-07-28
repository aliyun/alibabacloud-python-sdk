# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartNisTrafficRankingShrinkRequest(DaraModel):
    def __init__(
        self,
        begin_time: int = None,
        direction: str = None,
        end_time: int = None,
        filter_shrink: str = None,
        group_by_shrink: str = None,
        language: str = None,
        max_results: int = None,
        next_token: str = None,
        order_by: str = None,
        region_no: str = None,
        sort: str = None,
        storage_interval: int = None,
        top_n: int = None,
        traffic_analyzer_id: str = None,
        traffic_scenario: str = None,
        tuple_dimension: str = None,
    ):
        # The start timestamp of the query, in milliseconds.
        # 
        # This parameter is required.
        self.begin_time = begin_time
        # The network traffic direction based on Alibaba Cloud resources.
        # 
        # In: Traffic flowing into the target resource.
        # Out: Traffic flowing out of the target resource.
        # 
        # - VPC flow log scenario (`TraffficScenario = VpcFlowLogAll` / `VpcFlowLogInternet`):
        #   - In: Traffic flowing into the ENI.
        #   - Out: Traffic flowing out of the ENI.
        # 
        # - TR flow log scenario (`TraffficScenario = TRFlowlog`):
        #   - In: Traffic flowing into the TR.
        #   - Out: Traffic flowing out of the TR.
        # 
        # - Internet Shared Bandwidth metric analysis scenario (`TraffficScenario = CbwpMetric`):
        #   - In: Traffic flowing into the EIP.
        #   - Out: Traffic flowing out of the EIP.
        # 
        # This parameter is required.
        self.direction = direction
        # The end timestamp of the query, in milliseconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # Specifies additional filter conditions for focused network traffic analysis.
        self.filter_shrink = filter_shrink
        # Specifies multiple traffic dimensions for aggregation and sorting.
        self.group_by_shrink = group_by_shrink
        # The language. Valid values: zh-CN, en-US.
        self.language = language
        # The page size. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # The pagination token for the next query. Leave this parameter empty for the first query or when no more results are available. If a next query exists, set this value to the NextToken value returned by the previous API call.
        self.next_token = next_token
        # Based on the `TrafficScenario` field, the following metrics are supported for ranking traffic:
        # 
        # - `TrafficScenario = VpcFlowLogAll` / `VpcFlowLogInternet` (VPC flow log scenario):
        #   - `Bytes`: Bandwidth
        #   - `Packets`: Packets
        #   - `RoundTripTime`: TCP RTT
        # 
        # - `TrafficScenario = TRFlowlog` (TR flow log scenario):
        #   - `Bytes`: Bandwidth
        #   - `Packets`: Packets
        #   - `PacketsLostNoRoute`: Packet loss due to no routing
        #   - `PacketsLostBlackhole`: Packet loss due to blackhole routing
        #   - `PacketsLostTTLExpired`: Packet loss due to TTL timeout
        #   - `BytesIncrease`: Bandwidth increase
        #   - `BytesIncreaseRatio`: Bandwidth increase ratio
        # 
        # - `TrafficScenario = CbwpMetric` (Internet Shared Bandwidth metric analysis scenario):
        #   - `Bytes`: Bandwidth
        #   - `Packets`: Packets
        # 
        # This parameter is required.
        self.order_by = order_by
        # The region where the resource resides.
        # 
        # This parameter is required.
        self.region_no = region_no
        # The sorting method for network traffic analysis. Valid values:
        # - ASC: Sorts in ascending order.
        # - DESC: Sorts in descending order.
        self.sort = sort
        # The storage bucket precision property.
        # 
        # The storage bucket precision specifies the storage aggregation epoch to query. Two precision levels are supported: high precision (such as 1 minute) and long epoch (such as 1 day). The specific precision is determined by the network traffic analysis sampling interval configured for high-precision traffic statistics or long-epoch traffic statistics when creating or editing the network traffic analysis instance.
        # 
        # - The storage precision supported by the corresponding tuple of the network traffic analysis instance:
        #   - `1`: In minutes (1 minute)
        #   - `10`: In minutes (10 minutes)
        #   - `60`: In minutes (60 minutes, or 1 hour)
        #   - `1440`: In minutes (1440 minutes, or 1 day)
        # 
        # - The storage bucket precision can be used for two typical purposes:
        #   - High-precision traffic statistics: Aggregation at 1-minute, 10-minute, or 60-minute intervals.
        #   - Long-epoch traffic statistics: Aggregation at 1440-minute (1-day) intervals.
        # 
        # - Pass a value for this field during the query to specify the storage aggregation epoch. For example:
        #   - Pass `10`: Queries short-epoch data aggregated at 10-minute granularity.
        #   - Pass `1440`: Queries long-epoch data aggregated at 1-day granularity.
        # 
        # Note: The active storage precision values depend on the configuration of the network traffic analysis instance.
        self.storage_interval = storage_interval
        # The number of entries for the network traffic analysis sorting query.
        # 
        # You can specify a custom number. If this field is not specified, all traffic data that meets the specified conditions is sorted and analyzed within the performance capacity of the network traffic analysis feature.
        self.top_n = top_n
        # The ID of the network traffic analysis instance.
        # 
        # This parameter is required.
        self.traffic_analyzer_id = traffic_analyzer_id
        # Supported analysis scenarios: 
        # 
        # - All VPC flow log analysis
        # - Public VPC flow log analysis
        # - All TR flow log analysis
        # - Internet Shared Bandwidth metric analysis
        # 
        # This parameter is required.
        self.traffic_scenario = traffic_scenario
        # The storage aggregation dimension of the network traffic analysis instance.
        # 
        # Based on the TraffficScenario:
        # 
        # - VpcFlowLogAll/VpcFlowLog: Required. Specifies the storage aggregation view to query, which corresponds to the storage aggregation property configured in the network traffic analysis instance.
        # 
        # - TRFlowLog/CbwpMetric: Optional. Automatically adapts based on the storage aggregation property of the network traffic analysis instance.
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

        if self.group_by_shrink is not None:
            result['GroupBy'] = self.group_by_shrink

        if self.language is not None:
            result['Language'] = self.language

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        if self.sort is not None:
            result['Sort'] = self.sort

        if self.storage_interval is not None:
            result['StorageInterval'] = self.storage_interval

        if self.top_n is not None:
            result['TopN'] = self.top_n

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

        if m.get('GroupBy') is not None:
            self.group_by_shrink = m.get('GroupBy')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        if m.get('Sort') is not None:
            self.sort = m.get('Sort')

        if m.get('StorageInterval') is not None:
            self.storage_interval = m.get('StorageInterval')

        if m.get('TopN') is not None:
            self.top_n = m.get('TopN')

        if m.get('TrafficAnalyzerId') is not None:
            self.traffic_analyzer_id = m.get('TrafficAnalyzerId')

        if m.get('TrafficScenario') is not None:
            self.traffic_scenario = m.get('TrafficScenario')

        if m.get('TupleDimension') is not None:
            self.tuple_dimension = m.get('TupleDimension')

        return self

