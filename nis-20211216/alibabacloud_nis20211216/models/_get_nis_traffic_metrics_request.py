# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nis20211216 import models as main_models
from darabonba.model import DaraModel

class GetNisTrafficMetricsRequest(DaraModel):
    def __init__(
        self,
        begin_time: int = None,
        direction: str = None,
        end_time: int = None,
        filter: List[main_models.GetNisTrafficMetricsRequestFilter] = None,
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
        self.filter = filter
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

        self.filter = []
        if m.get('Filter') is not None:
            for k1 in m.get('Filter'):
                temp_model = main_models.GetNisTrafficMetricsRequestFilter()
                self.filter.append(temp_model.from_map(k1))

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

class GetNisTrafficMetricsRequestFilter(DaraModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        value: List[str] = None,
    ):
        # Based on the TupleDimension field and TrafficScenario field, the supported filter condition label keys are as follows:
        # 
        # - `TrafficScenario = VpcFlowLogAll` / `VpcFlowLogInternet` (VPC flow log scenario):
        # 
        #   - When `TupleDimension` is a 1-tuple, the following keys are supported:
        #     - `FlowAction`: the action type to execute on traffic after it matches the corresponding rule or policy (required, the corresponding value does not support multiple selections)
        #     - `VpcId`: VPC ID (the corresponding value supports multiple selections)
        #     - `VSwitchId`: vSwitch ID (the corresponding value supports multiple selections)
        #     - `NetworkInterfaceId`: elastic network interfaces (ENIs) ID (the corresponding value supports multiple selections)
        #     - `EcsId`: ECS instance ID (the corresponding value supports multiple selections)
        #     - `CloudIp`: cloud IP address (the corresponding value supports multiple selections)
        # 
        #   - When `TupleDimension` is a 2-tuple, the following keys are supported:
        #     - `FlowAction`: the action type to execute on traffic after it matches the corresponding rule or policy (required, the corresponding value does not support multiple selections)
        #     - `VpcId`: VPC ID (the corresponding value supports multiple selections)
        #     - `VSwitchId`: vSwitch ID (the corresponding value supports multiple selections)
        #     - `NetworkInterfaceId`: elastic network interfaces (ENIs) ID (the corresponding value supports multiple selections)
        #     - `EcsId`: ECS instance ID (the corresponding value supports multiple selections)
        #     - `SourceIp`: source IP address (the corresponding value supports multiple selections)
        #     - `DestinationIp`: destination IP address (the corresponding value supports multiple selections)
        #     - `TrafficPath`: traffic path (the corresponding value supports multiple selections)
        # 
        #   - When `TupleDimension` is a 5-tuple, the following keys are supported:
        #     - `FlowAction`: the action type to execute on traffic after it matches the corresponding rule or policy (required, the corresponding value does not support multiple selections)
        #     - `VpcId`: VPC ID (the corresponding value supports multiple selections)
        #     - `VSwitchId`: vSwitch ID (the corresponding value supports multiple selections)
        #     - `NetworkInterfaceId`: elastic network interfaces (ENIs) ID (the corresponding value supports multiple selections)
        #     - `EcsId`: ECS instance ID (the corresponding value supports multiple selections)
        #     - `SourceIp`: source IP address
        #     - `DestinationIp`: destination IP address
        #     - `TrafficPath`: traffic path (the corresponding value supports multiple selections)
        #     - `SourcePort`: source port (the corresponding value supports multiple selections)
        #     - `DestinationPort`: destination port (the corresponding value supports multiple selections)
        #     - `Protocol`: network protocol (the corresponding value supports multiple selections)
        # 
        #   - In the VPC Internet scenario (`TrafficScenario = VpcFlowLogInternet`), the following additional keys are supported for filtering by Internet location:
        #     - `ClientCountry`: filters network traffic analysis scope by country (the corresponding value supports multiple selections)
        #     - `ClientCity`: filters network traffic analysis scope by city (the corresponding value supports multiple selections)
        #     - `ClientAsn`: filters network traffic analysis scope by ASN (the corresponding value supports multiple selections)
        #     - `ClientIsp`: filters network traffic analysis scope by client ISP (the corresponding value supports multiple selections)
        # 
        #   - In VPC scenarios, the following traffic metrics filters are supported:
        #     - `MinBytes`: specifies the minimum traffic volume for sorting, in bytes (the corresponding value does not support multiple selections)
        #     - `MaxBytes`: specifies the maximum traffic volume for sorting, in bytes (the corresponding value does not support multiple selections)
        #     - `MinRoundTripTime`: specifies the minimum RTT for sorting, in ms (the corresponding value does not support multiple selections)
        #     - `MaxRoundTripTime`: specifies the maximum RTT for sorting, in ms (the corresponding value does not support multiple selections)
        #     - `MinPackages`: specifies the minimum number of packets for sorting (the corresponding value does not support multiple selections)
        #     - `MaxPackages`: specifies the maximum number of packets for sorting (the corresponding value does not support multiple selections)
        # 
        # ---
        # 
        # - `TrafficScenario = TRFlowlog` (TR flow log scenario):
        # 
        #   - When querying 2-tuples or adaptively using 2-tuples, the following keys are supported:
        #     - `TransitRouterAttachmentId`: network instance connection ID (required, the corresponding value does not support multiple selections)
        #     - `TransitRouterPairAttachmentId`: peer TR connection ID (the corresponding value supports multiple selections)
        #     - `TransitRouterId`: transit router instance ID (the corresponding value supports multiple selections)
        #     - `SourceIp`: source IP address (the corresponding value does not support multiple selections when Operator is like, and supports multiple selections when Operator is not like)
        #     - `DestinationIp`: destination IP address (the corresponding value does not support multiple selections when Operator is like, and supports multiple selections when Operator is not like)
        #     - `Dscp`: Differentiated Services Code Point (the corresponding value supports multiple selections)
        # 
        #   - When querying 5-tuples or adaptively using 5-tuples, the following additional keys are supported in addition to the 2-tuple keys:
        #     - `Protocol`: network protocol (the corresponding value supports multiple selections)
        #     - `SourcePort`: source port (the corresponding value supports multiple selections)
        #     - `DestinationPort`: destination port (the corresponding value supports multiple selections)
        #   - In `non-TR cross-region scenarios`, the following additional keys are supported:
        #     - `TransitRouterSourceResourceId`: source network instance ID (the corresponding value supports multiple selections)
        #     - `TransitRouterDestinationResourceId`: destination network instance ID (the corresponding value supports multiple selections)
        #   - In `VPC connection traffic scenarios`, the following additional keys are supported:
        #     - `TransitRouterSourceNetworkInterface`: source TR network interface controller (NIC) (the corresponding value supports multiple selections)
        #     - `TransitRouterDestinationNetworkInterface`: destination TR network interface controller (NIC) (the corresponding value supports multiple selections)
        # 
        #   - In TR scenarios, the following traffic metrics filters are supported:
        #     - `MinBytes`: specifies the minimum traffic volume for sorting, in bytes (the corresponding value does not support multiple selections)
        #     - `MaxBytes`: specifies the maximum traffic volume for sorting, in bytes (the corresponding value does not support multiple selections)
        #     - `MinPackages`: specifies the minimum number of packets for sorting (the corresponding value does not support multiple selections)
        #     - `MaxPackages`: specifies the maximum number of packets for sorting (the corresponding value does not support multiple selections)
        #     - `MinPacketsLostNoRoute`: minimum number of packets dropped due to no route (the corresponding value does not support multiple selections)
        #     - `MinPacketsLostBlackhole`: minimum number of packets dropped due to blackhole route (the corresponding value does not support multiple selections)
        #     - `MinPacketsLostTTLExpired`: minimum number of packets dropped due to TTL timeout (the corresponding value does not support multiple selections)
        #     - `MaxPacketsLostNoRoute`: maximum number of packets dropped due to no route (the corresponding value does not support multiple selections)
        #     - `MaxPacketsLostBlackhole`: maximum number of packets dropped due to blackhole route (the corresponding value does not support multiple selections)
        #     - `MaxPacketsLostTTLExpired`: maximum number of packets dropped due to TTL timeout (the corresponding value does not support multiple selections)
        # 
        # ---
        # 
        # - `TrafficScenario = CbwpMetric` (Internet Shared Bandwidth metric analysis scenario):
        # 
        #   - The following filter condition keys are supported:
        #     - `PublicIpAddress`: the public IP address of the associated EIP (the corresponding value does not support multiple selections when Operator is like, and supports multiple selections when Operator is not like)
        #     - `BindingResourceType`: the type of the instance resource to which the EIP is bound (the corresponding value supports multiple selections)
        #     - `BindingResourceId`: the ID of the instance resource to which the EIP is bound (the corresponding value supports multiple selections)
        #     - `CbwpId`: the Internet Shared Bandwidth instance ID (required, the corresponding value does not support multiple selections)
        #     - `InstanceId`: the EIP ID bound to the Internet Shared Bandwidth instance (the corresponding value supports multiple selections)
        # 
        #   - In CBWP scenarios, the following traffic metrics filters are supported:
        #     - `MinBytes`: specifies the minimum traffic volume for sorting, in bytes (the corresponding value does not support multiple selections)
        #     - `MaxBytes`: specifies the maximum traffic volume for sorting, in bytes (the corresponding value does not support multiple selections)
        #     - `MinPackages`: specifies the minimum number of packets for sorting (the corresponding value does not support multiple selections)
        #     - `MaxPackages`: specifies the maximum number of packets for sorting (the corresponding value does not support multiple selections)
        self.key = key
        # The filter operator.
        # - TR and Internet Shared Bandwidth scenarios:
        #   - Defaults to in if not specified.
        #   - like performs prefix matching and only one Value can be specified.
        # - VPC scenarios currently ignore this parameter and uniformly process it as IN.
        self.operator = operator
        # The filter value corresponding to the specified key type.
        # 
        # Based on the `TupleDimension` field and `TrafficScenario` field, the supported values are as follows:
        # 
        # - `TrafficScenario = VpcFlowLogAll` / `VpcFlowLogInternet` (VPC flow log scenario)
        # 
        #   - When the key is `FlowAction`, the valid values are:
        #     - `ACCEPT` (pass `Accept` by default): traffic allowed by security groups and network ACLs
        #     - `REJECT`: traffic denied by security groups and network ACLs
        # 
        # - `TrafficScenario = TRFlowlog` (TR flow log scenario)
        # 
        #   - When the key is `TransitRouterAttachmentId`, this is a required field, and the corresponding value is also required (specify the specific VPC connection / VPN connection / VBR connection / ECR connection / inter-region connection or network instance connection ID).
        # 
        # - `TrafficScenario = CbwpMetric` (shared bandwidth metric analysis scenario)
        # 
        #   - When the key is `CbwpId`, this is a required field, and the corresponding value is also required (specify the specific Internet Shared Bandwidth instance ID).
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

