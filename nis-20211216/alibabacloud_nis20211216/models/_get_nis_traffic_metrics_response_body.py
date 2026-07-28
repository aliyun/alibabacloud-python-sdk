# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nis20211216 import models as main_models
from darabonba.model import DaraModel

class GetNisTrafficMetricsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        metric_statics: List[main_models.GetNisTrafficMetricsResponseBodyMetricStatics] = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
        unit: str = None,
    ):
        # The maximum number of entries returned per page or per query. In VPC scenarios, this represents the paging size. In TR and Internet Shared Bandwidth scenarios, this represents the SQL query limit.
        self.max_results = max_results
        # The list of time series metric data points. Each element represents an aggregated time point and its corresponding metric value.
        self.metric_statics = metric_statics
        # The paging token for the next page. Paging is supported only in VPC scenarios. An empty value indicates that no more pages exist. This field is typically not returned in TR and Internet Shared Bandwidth scenarios.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The number of data points in the query result.
        self.total_count = total_count
        # **Unit and MetricName mapping**
        # 
        # - Bandwidth  
        #   - Unit: Bits/Second  
        #   - Description: bits per second.
        # 
        # - PacketsRate  
        #   - Unit: Packets/Second  
        #   - Description: packets per second.
        # 
        # - RoundTripTime  
        #   - Unit: MicroSecond  
        #   - Description: TCP round-trip time.
        # 
        # - BandwidthUtilization  
        #   - Unit: Percent  
        #   - Description: bandwidth utilization.
        # 
        # - PacketsLostNoRouteRate  
        #   - Unit: PacketsLostNoRouteRate  
        #   - Description: rate of packets dropped due to no route.
        # 
        # - PacketsLostBlackholeRate  
        #   - Unit: PacketsLostBlackholeRate  
        #   - Description: rate of packets dropped due to blackhole routing.
        # 
        # - PacketsLostTTLExpiredRate  
        #   - Unit: PacketsLostTTLExpiredRate  
        #   - Description: rate of packets dropped due to TTL expiration.
        self.unit = unit

    def validate(self):
        if self.metric_statics:
            for v1 in self.metric_statics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        result['MetricStatics'] = []
        if self.metric_statics is not None:
            for k1 in self.metric_statics:
                result['MetricStatics'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.unit is not None:
            result['Unit'] = self.unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        self.metric_statics = []
        if m.get('MetricStatics') is not None:
            for k1 in m.get('MetricStatics'):
                temp_model = main_models.GetNisTrafficMetricsResponseBodyMetricStatics()
                self.metric_statics.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        return self

class GetNisTrafficMetricsResponseBodyMetricStatics(DaraModel):
    def __init__(
        self,
        time_stamp: int = None,
        value: float = None,
    ):
        # The timestamp of the data point, in milliseconds.
        self.time_stamp = time_stamp
        # The metric value at the current time point. The specific meaning and unit are determined by the MetricName in the request.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

