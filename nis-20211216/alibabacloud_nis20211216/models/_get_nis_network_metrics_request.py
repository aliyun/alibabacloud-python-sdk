# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nis20211216 import models as main_models
from darabonba.model import DaraModel

class GetNisNetworkMetricsRequest(DaraModel):
    def __init__(
        self,
        account_ids: List[str] = None,
        begin_time: int = None,
        dimensions: List[main_models.GetNisNetworkMetricsRequestDimensions] = None,
        end_time: int = None,
        metric_name: str = None,
        region_no: str = None,
        resource_type: str = None,
        scan_by: str = None,
        step_minutes: int = None,
        use_cross_account: bool = None,
    ):
        # Explicitly passes sub-account IDs.
        self.account_ids = account_ids
        # The start time, in **ms**, in **UNIX** timestamp format. If not specified, the most recent 1 hour is queried by default. The earliest start time is 7 days ago.
        self.begin_time = begin_time
        # The collection of metric query parameters for specific business scenarios. For metric description of each scenario, see [GetNisNetworkMetrics](https://help.aliyun.com/document_detail/2833348.html).
        # 
        # This parameter is required.
        self.dimensions = dimensions
        # The end time, in **ms**, in **UNIX** timestamp format. If not specified, the most recent 1 hour is queried by default. If only BeginTime is specified, the 1 hour after BeginTime is queried. The maximum time span between the end time and start time is 24 hours.
        self.end_time = end_time
        # The metric name. Valid values:
        # 
        # -   bps: bits per second.
        # -   pps: packets per second.
        # -   rtt: round-trip time when establishing a TCP connection.
        # -   RetransmitRate: retransmission rate.
        # -   RatelimitDropPps: rate of packets dropped due to throttling.
        # -   ActiveSessionCount: concurrent sessions.
        # -   NewSessionPerSecond: new sessions per second.
        # -   BandwidthUtilization: bandwidth utilization.
        # -   passRate: inspection pass rate.
        # > If no RTT data is available within the selected time range, the connection is a persistent connection and no initial connection was established during that period.
        # 
        # This parameter is required.
        self.metric_name = metric_name
        # The region ID.
        # 
        # This parameter is required.
        self.region_no = region_no
        # Analyzes traffic by the Alibaba Cloud network resource type used for traffic forwarding. Valid values:
        # 
        # - AccessInternetIpV4: all Alibaba Cloud public IPv4 addresses.
        # - AccessInternetIpV4Limited: all region-throttled Alibaba Cloud public IPv4 addresses.
        # - ElasticIP: Elastic IP Address (EIP) (IPv4).
        # - PublicIpEcs: static public IP address bound to an ECS instance (IPv4).
        # - PublicIpClb: static public IP address bound to a CLB instance (IPv4).
        # - NAT: public traffic through SNAT.
        # - TR: traffic through Cloud Enterprise Network (CEN) transit routers.
        # - TRAttachment: traffic through CEN connection instances, including intra-region and inter-region connections. Intra-region connections have inbound and outbound directions. Inter-region connections have only the outbound direction.
        # - VBR: traffic through virtual border routers.
        # - GA: traffic through Global Accelerator.
        # - InternetProbing: Internet quality probing data.
        # - IntranetProbing: internal network quality probing data.
        # - NisInspectionHistoryReportScore: inspection history scores.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The sort order. Default value: TimestampAscending. Valid values:
        # 
        # - TimestampAscending: sorts by time in ascending order.
        # - TimestampDescending: sorts by time in descending order.
        self.scan_by = scan_by
        self.step_minutes = step_minutes
        # Specifies whether to use cross-account access mode. This is a reserved parameter and is not currently supported.
        self.use_cross_account = use_cross_account

    def validate(self):
        if self.dimensions:
            for v1 in self.dimensions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids

        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        result['Dimensions'] = []
        if self.dimensions is not None:
            for k1 in self.dimensions:
                result['Dimensions'].append(k1.to_map() if k1 else None)

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.scan_by is not None:
            result['ScanBy'] = self.scan_by

        if self.step_minutes is not None:
            result['StepMinutes'] = self.step_minutes

        if self.use_cross_account is not None:
            result['UseCrossAccount'] = self.use_cross_account

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')

        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        self.dimensions = []
        if m.get('Dimensions') is not None:
            for k1 in m.get('Dimensions'):
                temp_model = main_models.GetNisNetworkMetricsRequestDimensions()
                self.dimensions.append(temp_model.from_map(k1))

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('ScanBy') is not None:
            self.scan_by = m.get('ScanBy')

        if m.get('StepMinutes') is not None:
            self.step_minutes = m.get('StepMinutes')

        if m.get('UseCrossAccount') is not None:
            self.use_cross_account = m.get('UseCrossAccount')

        return self

class GetNisNetworkMetricsRequestDimensions(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name of the filter condition.
        self.name = name
        # The value of the filter condition.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

