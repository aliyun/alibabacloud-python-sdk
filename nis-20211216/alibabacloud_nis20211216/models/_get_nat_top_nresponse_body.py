# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nis20211216 import models as main_models
from darabonba.model import DaraModel

class GetNatTopNResponseBody(DaraModel):
    def __init__(
        self,
        is_top_nopen: bool = None,
        nat_gateway_top_n: List[main_models.GetNatTopNResponseBodyNatGatewayTopN] = None,
        request_id: str = None,
    ):
        # Indicates whether Network Intelligence Service (NIS) is activated. The NatGatewayTopN parameter returns an empty array when NIS is not activated.
        # 
        # *   **true**: activated
        # *   **false**: not activated
        self.is_top_nopen = is_top_nopen
        # An array of statistics about real-time SNAT performance ranking.
        self.nat_gateway_top_n = nat_gateway_top_n
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.nat_gateway_top_n:
            for v1 in self.nat_gateway_top_n:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_top_nopen is not None:
            result['IsTopNOpen'] = self.is_top_nopen

        result['NatGatewayTopN'] = []
        if self.nat_gateway_top_n is not None:
            for k1 in self.nat_gateway_top_n:
                result['NatGatewayTopN'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsTopNOpen') is not None:
            self.is_top_nopen = m.get('IsTopNOpen')

        self.nat_gateway_top_n = []
        if m.get('NatGatewayTopN') is not None:
            for k1 in m.get('NatGatewayTopN'):
                temp_model = main_models.GetNatTopNResponseBodyNatGatewayTopN()
                self.nat_gateway_top_n.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetNatTopNResponseBodyNatGatewayTopN(DaraModel):
    def __init__(
        self,
        active_session_count: float = None,
        in_bps: float = None,
        in_flow_per_minute: float = None,
        in_pps: float = None,
        ip: str = None,
        new_session_per_second: float = None,
        out_bps: float = None,
        out_flow_per_minute: float = None,
        out_pps: float = None,
    ):
        # The number of concurrent connections. Unit: connections.
        self.active_session_count = active_session_count
        # The inbound data transfer. Unit: bit/s.
        self.in_bps = in_bps
        # This field is reserved and not in use.
        self.in_flow_per_minute = in_flow_per_minute
        # The inbound packet forwarding rate. Unit: packets per second.
        self.in_pps = in_pps
        # The IP address.
        self.ip = ip
        # The new connection creation rate. Unit: connections per second.
        self.new_session_per_second = new_session_per_second
        # The outbound data transfer. Unit: bit/s.
        self.out_bps = out_bps
        # This field is reserved and not in use.
        self.out_flow_per_minute = out_flow_per_minute
        # The outbound packet forwarding rate. Unit: packets per second.
        self.out_pps = out_pps

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_session_count is not None:
            result['ActiveSessionCount'] = self.active_session_count

        if self.in_bps is not None:
            result['InBps'] = self.in_bps

        if self.in_flow_per_minute is not None:
            result['InFlowPerMinute'] = self.in_flow_per_minute

        if self.in_pps is not None:
            result['InPps'] = self.in_pps

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.new_session_per_second is not None:
            result['NewSessionPerSecond'] = self.new_session_per_second

        if self.out_bps is not None:
            result['OutBps'] = self.out_bps

        if self.out_flow_per_minute is not None:
            result['OutFlowPerMinute'] = self.out_flow_per_minute

        if self.out_pps is not None:
            result['OutPps'] = self.out_pps

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveSessionCount') is not None:
            self.active_session_count = m.get('ActiveSessionCount')

        if m.get('InBps') is not None:
            self.in_bps = m.get('InBps')

        if m.get('InFlowPerMinute') is not None:
            self.in_flow_per_minute = m.get('InFlowPerMinute')

        if m.get('InPps') is not None:
            self.in_pps = m.get('InPps')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('NewSessionPerSecond') is not None:
            self.new_session_per_second = m.get('NewSessionPerSecond')

        if m.get('OutBps') is not None:
            self.out_bps = m.get('OutBps')

        if m.get('OutFlowPerMinute') is not None:
            self.out_flow_per_minute = m.get('OutFlowPerMinute')

        if m.get('OutPps') is not None:
            self.out_pps = m.get('OutPps')

        return self

