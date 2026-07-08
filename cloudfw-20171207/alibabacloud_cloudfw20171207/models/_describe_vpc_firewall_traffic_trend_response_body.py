# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeVpcFirewallTrafficTrendResponseBody(DaraModel):
    def __init__(
        self,
        avg_in_bps: int = None,
        avg_out_bps: int = None,
        avg_session: int = None,
        avg_total_bps: int = None,
        data_list: List[main_models.DescribeVpcFirewallTrafficTrendResponseBodyDataList] = None,
        max_bandwidth_time: int = None,
        max_in_bps: int = None,
        max_out_bps: int = None,
        max_session: int = None,
        max_total_bps: int = None,
        request_id: str = None,
        total_bytes: int = None,
        total_in_bytes: int = None,
        total_out_bytes: int = None,
        total_session: int = None,
    ):
        # The average inbound network throughput. Unit: bit/s.
        self.avg_in_bps = avg_in_bps
        # The average outbound network throughput. Unit: bit/s.
        self.avg_out_bps = avg_out_bps
        # The average number of requests.
        self.avg_session = avg_session
        # The average total network throughput in both the outbound and inbound directions. Unit: bit/s.
        self.avg_total_bps = avg_total_bps
        # The data list.
        self.data_list = data_list
        # The timestamp when the peak bandwidth occurred. The value is a UNIX timestamp. Unit: seconds.
        self.max_bandwidth_time = max_bandwidth_time
        # The peak inbound network throughput. Unit: bit/s.
        self.max_in_bps = max_in_bps
        # The peak outbound network throughput. Unit: bit/s.
        self.max_out_bps = max_out_bps
        # The peak number of requests.
        self.max_session = max_session
        # The peak total network throughput in both the outbound and inbound directions. Unit: bit/s.
        self.max_total_bps = max_total_bps
        # The request ID.
        self.request_id = request_id
        # The total traffic. Unit: bytes.
        self.total_bytes = total_bytes
        # The total inbound network throughput. Unit: bytes.
        self.total_in_bytes = total_in_bytes
        # The total outbound network throughput. Unit: bytes.
        self.total_out_bytes = total_out_bytes
        # The total number of requests.
        self.total_session = total_session

    def validate(self):
        if self.data_list:
            for v1 in self.data_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avg_in_bps is not None:
            result['AvgInBps'] = self.avg_in_bps

        if self.avg_out_bps is not None:
            result['AvgOutBps'] = self.avg_out_bps

        if self.avg_session is not None:
            result['AvgSession'] = self.avg_session

        if self.avg_total_bps is not None:
            result['AvgTotalBps'] = self.avg_total_bps

        result['DataList'] = []
        if self.data_list is not None:
            for k1 in self.data_list:
                result['DataList'].append(k1.to_map() if k1 else None)

        if self.max_bandwidth_time is not None:
            result['MaxBandwidthTime'] = self.max_bandwidth_time

        if self.max_in_bps is not None:
            result['MaxInBps'] = self.max_in_bps

        if self.max_out_bps is not None:
            result['MaxOutBps'] = self.max_out_bps

        if self.max_session is not None:
            result['MaxSession'] = self.max_session

        if self.max_total_bps is not None:
            result['MaxTotalBps'] = self.max_total_bps

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_bytes is not None:
            result['TotalBytes'] = self.total_bytes

        if self.total_in_bytes is not None:
            result['TotalInBytes'] = self.total_in_bytes

        if self.total_out_bytes is not None:
            result['TotalOutBytes'] = self.total_out_bytes

        if self.total_session is not None:
            result['TotalSession'] = self.total_session

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvgInBps') is not None:
            self.avg_in_bps = m.get('AvgInBps')

        if m.get('AvgOutBps') is not None:
            self.avg_out_bps = m.get('AvgOutBps')

        if m.get('AvgSession') is not None:
            self.avg_session = m.get('AvgSession')

        if m.get('AvgTotalBps') is not None:
            self.avg_total_bps = m.get('AvgTotalBps')

        self.data_list = []
        if m.get('DataList') is not None:
            for k1 in m.get('DataList'):
                temp_model = main_models.DescribeVpcFirewallTrafficTrendResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k1))

        if m.get('MaxBandwidthTime') is not None:
            self.max_bandwidth_time = m.get('MaxBandwidthTime')

        if m.get('MaxInBps') is not None:
            self.max_in_bps = m.get('MaxInBps')

        if m.get('MaxOutBps') is not None:
            self.max_out_bps = m.get('MaxOutBps')

        if m.get('MaxSession') is not None:
            self.max_session = m.get('MaxSession')

        if m.get('MaxTotalBps') is not None:
            self.max_total_bps = m.get('MaxTotalBps')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalBytes') is not None:
            self.total_bytes = m.get('TotalBytes')

        if m.get('TotalInBytes') is not None:
            self.total_in_bytes = m.get('TotalInBytes')

        if m.get('TotalOutBytes') is not None:
            self.total_out_bytes = m.get('TotalOutBytes')

        if m.get('TotalSession') is not None:
            self.total_session = m.get('TotalSession')

        return self

class DescribeVpcFirewallTrafficTrendResponseBodyDataList(DaraModel):
    def __init__(
        self,
        in_bps: int = None,
        in_bytes: int = None,
        in_pps: int = None,
        new_conn: int = None,
        out_bps: int = None,
        out_bytes: int = None,
        out_pps: int = None,
        session_count: int = None,
        time: int = None,
    ):
        # The inbound bandwidth. Unit: bit/s.
        self.in_bps = in_bps
        # The inbound traffic. Unit: bytes.
        self.in_bytes = in_bytes
        # The inbound packet forwarding rate. Unit: pps.
        self.in_pps = in_pps
        # The number of new connections.
        self.new_conn = new_conn
        # The outbound traffic. Unit: bytes.
        self.out_bps = out_bps
        # The total outbound network throughput. Unit: bytes.
        self.out_bytes = out_bytes
        # The outbound packet forwarding rate. Unit: pps.
        self.out_pps = out_pps
        # The number of sessions.
        self.session_count = session_count
        # The time when the traffic occurred. The value is a UNIX timestamp. Unit: seconds.
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.in_bps is not None:
            result['InBps'] = self.in_bps

        if self.in_bytes is not None:
            result['InBytes'] = self.in_bytes

        if self.in_pps is not None:
            result['InPps'] = self.in_pps

        if self.new_conn is not None:
            result['NewConn'] = self.new_conn

        if self.out_bps is not None:
            result['OutBps'] = self.out_bps

        if self.out_bytes is not None:
            result['OutBytes'] = self.out_bytes

        if self.out_pps is not None:
            result['OutPps'] = self.out_pps

        if self.session_count is not None:
            result['SessionCount'] = self.session_count

        if self.time is not None:
            result['Time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InBps') is not None:
            self.in_bps = m.get('InBps')

        if m.get('InBytes') is not None:
            self.in_bytes = m.get('InBytes')

        if m.get('InPps') is not None:
            self.in_pps = m.get('InPps')

        if m.get('NewConn') is not None:
            self.new_conn = m.get('NewConn')

        if m.get('OutBps') is not None:
            self.out_bps = m.get('OutBps')

        if m.get('OutBytes') is not None:
            self.out_bytes = m.get('OutBytes')

        if m.get('OutPps') is not None:
            self.out_pps = m.get('OutPps')

        if m.get('SessionCount') is not None:
            self.session_count = m.get('SessionCount')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        return self

