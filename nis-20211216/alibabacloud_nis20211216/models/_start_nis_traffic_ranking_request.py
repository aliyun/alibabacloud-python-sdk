# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nis20211216 import models as main_models
from darabonba.model import DaraModel

class StartNisTrafficRankingRequest(DaraModel):
    def __init__(
        self,
        begin_time: int = None,
        direction: str = None,
        end_time: int = None,
        filter: List[main_models.StartNisTrafficRankingRequestFilter] = None,
        group_by: List[str] = None,
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
        self.filter = filter
        # Specifies multiple traffic dimensions for aggregation and sorting.
        self.group_by = group_by
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
        if self.filter:
            for v1 in self.filter:
                 if v1:
                    v1.validate()

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

        result['Filter'] = []
        if self.filter is not None:
            for k1 in self.filter:
                result['Filter'].append(k1.to_map() if k1 else None)

        if self.group_by is not None:
            result['GroupBy'] = self.group_by

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

        self.filter = []
        if m.get('Filter') is not None:
            for k1 in m.get('Filter'):
                temp_model = main_models.StartNisTrafficRankingRequestFilter()
                self.filter.append(temp_model.from_map(k1))

        if m.get('GroupBy') is not None:
            self.group_by = m.get('GroupBy')

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

class StartNisTrafficRankingRequestFilter(DaraModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        value: List[str] = None,
    ):
        # Based on the `TupleDimension` and `TrafficScenario` fields, the following filter condition label keys are supported:
        # 
        # - `TrafficScenario = VpcFlowLogAll` / `VpcFlowLogInternet` (VPC flow log scenario):
        # 
        #   - When `TupleDimension` is 1-tuple, the following keys are supported:
        #     - `FlowAction`: The action type to execute on traffic after it matches a rule or policy (required, corresponding value does not support multiple selections)
        #     - `VpcId`: VPC ID (corresponding value supports multiple selections)
        #     - `VSwitchId`: vSwitch ID (corresponding value supports multiple selections)
        #     - `NetworkInterfaceId`: Network interface controller (NIC) ID (corresponding value supports multiple selections)
        #     - `EcsId`: ECS server ID (corresponding value supports multiple selections)
        #     - `CloudIp`: Cloud IP address (corresponding value supports multiple selections)
        # 
        #   - When `TupleDimension` is 2-tuple, the following keys are supported:
        #     - `FlowAction`: The action type to execute on traffic after it matches a rule or policy (required, corresponding value does not support multiple selections)
        #     - `VpcId`: VPC ID (corresponding value supports multiple selections)
        #     - `VSwitchId`: vSwitch ID (corresponding value supports multiple selections)
        #     - `NetworkInterfaceId`: Network interface controller (NIC) ID (corresponding value supports multiple selections)
        #     - `EcsId`: ECS server ID (corresponding value supports multiple selections)
        #     - `SourceIp`: Source IP address (corresponding value supports multiple selections)
        #     - `DestinationIp`: Destination IP address (corresponding value supports multiple selections)
        #     - `TrafficPath`: Traffic path (corresponding value supports multiple selections)
        # 
        #   - When `TupleDimension` is 5-tuple, the following keys are supported:
        #     - `FlowAction`: The action type to execute on traffic after it matches a rule or policy (required, corresponding value does not support multiple selections)
        #     - `VpcId`: VPC ID (corresponding value supports multiple selections)
        #     - `VSwitchId`: vSwitch ID (corresponding value supports multiple selections)
        #     - `NetworkInterfaceId`: Network interface controller (NIC) ID (corresponding value supports multiple selections)
        #     - `EcsId`: ECS server ID (corresponding value supports multiple selections)
        #     - `SourceIp`: Source IP address
        #     - `DestinationIp`: Destination IP address
        #     - `TrafficPath`: Traffic path (corresponding value supports multiple selections)
        #     - `SourcePort`: Source port (corresponding value supports multiple selections)
        #     - `DestinationPort`: Destination port (corresponding value supports multiple selections)
        #     - `Protocol`: Network protocol (corresponding value supports multiple selections)
        # 
        #   - For VPC public network scenarios (`TrafficScenario = VpcFlowLogInternet`), the following additional keys are supported for filtering by Internet location:
        #     - `ClientCountry`: Filter network traffic analysis scope by country (corresponding value supports multiple selections)
        #     - `ClientCity`: Filter network traffic analysis scope by city (corresponding value supports multiple selections)
        #     - `ClientAsn`: Filter network traffic analysis scope by ASN (corresponding value supports multiple selections)
        #     - `ClientIsp`: Filter network traffic analysis scope by client ISP (corresponding value supports multiple selections)
        # 
        #   - For all VPC scenarios, filtering by traffic metrics is supported:
        #     - `MinBytes`: Specifies the minimum traffic volume for sorting, in bytes (corresponding value does not support multiple selections)
        #     - `MaxBytes`: Specifies the maximum traffic volume for sorting, in bytes (corresponding value does not support multiple selections)
        #     - `MinRoundTripTime`: Specifies the minimum RTT for sorting, in ms (corresponding value does not support multiple selections)
        #     - `MaxRoundTripTime`: Specifies the maximum RTT for sorting, in ms (corresponding value does not support multiple selections)
        #     - `MinPackages`: Specifies the minimum number of packets for sorting (corresponding value does not support multiple selections)
        #     - `MaxPackages`: Specifies the maximum number of packets for sorting (corresponding value does not support multiple selections)
        # 
        # ---
        # 
        # - `TrafficScenario = TRFlowlog` (TR flow log scenario):
        # 
        #   - When querying 2-tuple or adaptive 2-tuple, the following keys are supported:
        #     - `TransitRouterAttachmentId`: Network instance connection ID (required, corresponding value does not support multiple selections)
        #     - `TransitRouterPairAttachmentId`: Peer TR connection ID (corresponding value supports multiple selections)
        #     - `TransitRouterId`: Forward router instance ID (corresponding value supports multiple selections)
        #     - `SourceIp`: Source IP address (corresponding value does not support multiple selections when Operator = like. Corresponding value supports multiple selections when Operator != like)
        #     - `DestinationIp`: Destination IP address (corresponding value does not support multiple selections when Operator = like. Corresponding value supports multiple selections when Operator != like)
        #     - `Dscp`: Differentiated Services Code Point (corresponding value supports multiple selections)
        # 
        #   - When querying 5-tuple or adaptive 5-tuple, the following additional keys are supported on top of 2-tuple:
        #     - `Protocol`: Network protocol (corresponding value supports multiple selections)
        #     - `SourcePort`: Source port (corresponding value supports multiple selections)
        #     - `DestinationPort`: Destination port (corresponding value supports multiple selections)
        #   - In `non-TR cross-region scenarios`, the following additional keys are supported:
        #     - `TransitRouterSourceResourceId`: Source network instance ID (corresponding value supports multiple selections)
        #     - `TransitRouterDestinationResourceId`: Destination network instance ID (corresponding value supports multiple selections)
        #   - In `VPC connection traffic scenarios`, the following additional keys are supported:
        #     - `TransitRouterSourceNetworkInterface`: Source TR ENI (corresponding value supports multiple selections)
        #     - `TransitRouterDestinationNetworkInterface`: Destination TR ENI (corresponding value supports multiple selections)
        # 
        #   - For all TR scenarios, filtering by traffic metrics is supported:
        #     - `MinBytes`: Specifies the minimum traffic volume for sorting, in bytes (corresponding value does not support multiple selections)
        #     - `MaxBytes`: Specifies the maximum traffic volume for sorting, in bytes (corresponding value does not support multiple selections)
        #     - `MinPackages`: Specifies the minimum number of packets for sorting (corresponding value does not support multiple selections)
        #     - `MaxPackages`: Specifies the maximum number of packets for sorting (corresponding value does not support multiple selections)
        #     - `MinPacketsLostNoRoute`: Minimum packet loss due to no routing (corresponding value does not support multiple selections)
        #     - `MinPacketsLostBlackhole`: Minimum packet loss due to blackhole routing (corresponding value does not support multiple selections)
        #     - `MinPacketsLostTTLExpired`: Minimum packet loss due to TTL timeout (corresponding value does not support multiple selections)
        #     - `MaxPacketsLostNoRoute`: Maximum packet loss due to no routing (corresponding value does not support multiple selections)
        #     - `MaxPacketsLostBlackhole`: Maximum packet loss due to blackhole routing (corresponding value does not support multiple selections)
        #     - `MaxPacketsLostTTLExpired`: Maximum packet loss due to TTL timeout (corresponding value does not support multiple selections)
        # 
        # ---
        # 
        # - `TrafficScenario = CbwpMetric` (Internet Shared Bandwidth metric analysis scenario):
        # 
        #   - Filtering by conditions supports:
        #     - `PublicIpAddress`: Public IP address of the bound EIP (corresponding value does not support multiple selections when Operator = like. Corresponding value supports multiple selections when Operator != like)
        #     - `BindingResourceType`: Resource type of the instance bound to the EIP (corresponding value supports multiple selections)
        #     - `BindingResourceId`: Resource ID of the instance bound to the EIP (corresponding value supports multiple selections)
        #     - `CbwpId`: Internet Shared Bandwidth ID (required, corresponding value does not support multiple selections)
        #     - `InstanceId`: EIP ID bound to the Internet Shared Bandwidth instance (corresponding value supports multiple selections)
        # 
        #   - For all CBWP scenarios, filtering by traffic metrics is supported:
        #     - `MinBytes`: Specifies the minimum traffic volume for sorting, in bytes (corresponding value does not support multiple selections)
        #     - `MaxBytes`: Specifies the maximum traffic volume for sorting, in bytes (corresponding value does not support multiple selections)
        #     - `MinPackages`: Specifies the minimum number of packets for sorting (corresponding value does not support multiple selections)
        #     - `MaxPackages`: Specifies the maximum number of packets for sorting (corresponding value does not support multiple selections)
        self.key = key
        # For specified key types, some support using operators to perform string matching on the passed value. Valid values (default value: `in`):
        # 
        # - `in`: Equal to.
        # - `not in`: Not equal to.
        # - `like`: Contains.
        # 
        # Based on the `TupleDimension` and `TrafficScenario` fields, `like` is supported as follows:
        # 
        # - `TrafficScenario = VpcFlowLogAll` / `VpcFlowLogInternet` (VPC flow log scenario):
        #   - The `like` operator is supported when the key is one of the following:
        #     - `CloudIp`
        #     - `SourceIp`
        #     - `DestinationIp`
        # 
        # - `TrafficScenario = TRFlowlog` (TR flow log scenario):
        #   - The `like` operator is supported when the key is one of the following:
        #     - `SourceIp`
        #     - `DestinationIp`
        # 
        # - `TrafficScenario = CbwpMetric` (Internet Shared Bandwidth metric analysis scenario):
        #   - The `like` operator is supported when the key is one of the following:
        #     - `PublicIpAddress`
        # 
        # For all other fields, only the `in` and `not in` operators are supported.
        self.operator = operator
        # The value of the filter condition.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

