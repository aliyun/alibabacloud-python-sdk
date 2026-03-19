# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20171228 import models as main_models
from darabonba.model import DaraModel

class DescribeIpTrafficResponseBody(DaraModel):
    def __init__(
        self,
        avg_in_bps: int = None,
        avg_out_bps: int = None,
        ip_traffic_points: List[main_models.DescribeIpTrafficResponseBodyIpTrafficPoints] = None,
        max_in_bps: int = None,
        max_out_bps: int = None,
        request_id: str = None,
    ):
        self.avg_in_bps = avg_in_bps
        self.avg_out_bps = avg_out_bps
        self.ip_traffic_points = ip_traffic_points
        self.max_in_bps = max_in_bps
        self.max_out_bps = max_out_bps
        self.request_id = request_id

    def validate(self):
        if self.ip_traffic_points:
            for v1 in self.ip_traffic_points:
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

        result['IpTrafficPoints'] = []
        if self.ip_traffic_points is not None:
            for k1 in self.ip_traffic_points:
                result['IpTrafficPoints'].append(k1.to_map() if k1 else None)

        if self.max_in_bps is not None:
            result['MaxInBps'] = self.max_in_bps

        if self.max_out_bps is not None:
            result['MaxOutBps'] = self.max_out_bps

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvgInBps') is not None:
            self.avg_in_bps = m.get('AvgInBps')

        if m.get('AvgOutBps') is not None:
            self.avg_out_bps = m.get('AvgOutBps')

        self.ip_traffic_points = []
        if m.get('IpTrafficPoints') is not None:
            for k1 in m.get('IpTrafficPoints'):
                temp_model = main_models.DescribeIpTrafficResponseBodyIpTrafficPoints()
                self.ip_traffic_points.append(temp_model.from_map(k1))

        if m.get('MaxInBps') is not None:
            self.max_in_bps = m.get('MaxInBps')

        if m.get('MaxOutBps') is not None:
            self.max_out_bps = m.get('MaxOutBps')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeIpTrafficResponseBodyIpTrafficPoints(DaraModel):
    def __init__(
        self,
        act_conns: int = None,
        cps: int = None,
        inact_conns: int = None,
        max_inbps: int = None,
        max_outbps: int = None,
        time: int = None,
    ):
        self.act_conns = act_conns
        self.cps = cps
        self.inact_conns = inact_conns
        self.max_inbps = max_inbps
        self.max_outbps = max_outbps
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.act_conns is not None:
            result['ActConns'] = self.act_conns

        if self.cps is not None:
            result['Cps'] = self.cps

        if self.inact_conns is not None:
            result['InactConns'] = self.inact_conns

        if self.max_inbps is not None:
            result['MaxInbps'] = self.max_inbps

        if self.max_outbps is not None:
            result['MaxOutbps'] = self.max_outbps

        if self.time is not None:
            result['Time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActConns') is not None:
            self.act_conns = m.get('ActConns')

        if m.get('Cps') is not None:
            self.cps = m.get('Cps')

        if m.get('InactConns') is not None:
            self.inact_conns = m.get('InactConns')

        if m.get('MaxInbps') is not None:
            self.max_inbps = m.get('MaxInbps')

        if m.get('MaxOutbps') is not None:
            self.max_outbps = m.get('MaxOutbps')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        return self

