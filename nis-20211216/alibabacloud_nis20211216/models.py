# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class GetNatTopNRequest(TeaModel):
    def __init__(
        self,
        begin_time: int = None,
        end_time: int = None,
        ip: str = None,
        nat_gateway_id: str = None,
        order_by: str = None,
        region_id: str = None,
        top_n: int = None,
    ):
        # The beginning of the time range to query in milliseconds. If you do not specify **EndTime**, the point in time specified by **BeginTime** is queried.
        self.begin_time = begin_time
        # The end of the time range to query in milliseconds. The time range specified by **BeginTime** and **EndTime** cannot exceed **86400000** milliseconds (24 hours).
        self.end_time = end_time
        # Query ranking statistics for a specific IP address. If you specify this parameter, you do not need to specify **TopN** or **OrderBy**.
        self.ip = ip
        # The ID of the NAT gateway.
        self.nat_gateway_id = nat_gateway_id
        # The metric that is used for real-time SNAT performance ranking. Valid values:
        # 
        # *   **InBps**: inbound data transfer. Unit: bit/s.
        # *   **OutBps**: outbound data transfer. Unit: bit/s.
        # *   **InPps**: inbound packet forwarding rate. Unit: packets per second.
        # *   **OutPps**: outbound packet forwarding rate. Unit: packets per second.
        # *   **NewSessionPerSecond**: new connection creation rate. Unit: connections per second.
        # *   **ActiveSessionCount**: number of concurrent connections. Unit: connections.
        self.order_by = order_by
        # The ID of the region in which the NAT gateway is deployed.
        self.region_id = region_id
        # The number of entries to return for real-time SNAT performance ranking. Valid values: **1 to 100**. Default value: **10**.
        self.top_n = top_n

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.top_n is not None:
            result['TopN'] = self.top_n
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TopN') is not None:
            self.top_n = m.get('TopN')
        return self


class GetNatTopNResponseBodyNatGatewayTopN(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetNatTopNResponseBody(TeaModel):
    def __init__(
        self,
        is_top_nopen: bool = None,
        nat_gateway_top_n: List[GetNatTopNResponseBodyNatGatewayTopN] = None,
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
            for k in self.nat_gateway_top_n:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_top_nopen is not None:
            result['IsTopNOpen'] = self.is_top_nopen
        result['NatGatewayTopN'] = []
        if self.nat_gateway_top_n is not None:
            for k in self.nat_gateway_top_n:
                result['NatGatewayTopN'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsTopNOpen') is not None:
            self.is_top_nopen = m.get('IsTopNOpen')
        self.nat_gateway_top_n = []
        if m.get('NatGatewayTopN') is not None:
            for k in m.get('NatGatewayTopN'):
                temp_model = GetNatTopNResponseBodyNatGatewayTopN()
                self.nat_gateway_top_n.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetNatTopNResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetNatTopNResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetNatTopNResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


