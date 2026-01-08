# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeUserAssetIPTrafficInfoResponseBody(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        in_bps: int = None,
        in_pps: int = None,
        new_conn: int = None,
        out_bps: int = None,
        out_pps: int = None,
        request_id: str = None,
        session_count: int = None,
        start_time: int = None,
    ):
        # The end of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        self.end_time = end_time
        # The network throughput, which indicates the inbound traffic rate. Unit: bit/s.
        self.in_bps = in_bps
        # The inbound network throughput, which indicates the number of packets that are sent inbound per second. Unit: packets per second (pps).
        self.in_pps = in_pps
        # The new connection creation rate.
        self.new_conn = new_conn
        # The network throughput, which indicates the outbound traffic rate. Unit: bit/s.
        self.out_bps = out_bps
        # The outbound network throughput, which indicates the number of packets that are sent outbound per second. Unit: pps.
        self.out_pps = out_pps
        # The request ID.
        self.request_id = request_id
        # The number of requests.
        self.session_count = session_count
        # The beginning of the time range to query. The value is a UNIX timestamp. Unit: seconds.
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

        if self.in_bps is not None:
            result['InBps'] = self.in_bps

        if self.in_pps is not None:
            result['InPps'] = self.in_pps

        if self.new_conn is not None:
            result['NewConn'] = self.new_conn

        if self.out_bps is not None:
            result['OutBps'] = self.out_bps

        if self.out_pps is not None:
            result['OutPps'] = self.out_pps

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.session_count is not None:
            result['SessionCount'] = self.session_count

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InBps') is not None:
            self.in_bps = m.get('InBps')

        if m.get('InPps') is not None:
            self.in_pps = m.get('InPps')

        if m.get('NewConn') is not None:
            self.new_conn = m.get('NewConn')

        if m.get('OutBps') is not None:
            self.out_bps = m.get('OutBps')

        if m.get('OutPps') is not None:
            self.out_pps = m.get('OutPps')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SessionCount') is not None:
            self.session_count = m.get('SessionCount')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

