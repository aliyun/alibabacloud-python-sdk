# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nis20211216 import models as main_models
from darabonba.model import DaraModel

class GetTransitRouterFlowTopNResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        transit_router_flow_top_n: List[main_models.GetTransitRouterFlowTopNResponseBodyTransitRouterFlowTopN] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The ranking result of inter-region traffic data.
        self.transit_router_flow_top_n = transit_router_flow_top_n

    def validate(self):
        if self.transit_router_flow_top_n:
            for v1 in self.transit_router_flow_top_n:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['TransitRouterFlowTopN'] = []
        if self.transit_router_flow_top_n is not None:
            for k1 in self.transit_router_flow_top_n:
                result['TransitRouterFlowTopN'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.transit_router_flow_top_n = []
        if m.get('TransitRouterFlowTopN') is not None:
            for k1 in m.get('TransitRouterFlowTopN'):
                temp_model = main_models.GetTransitRouterFlowTopNResponseBodyTransitRouterFlowTopN()
                self.transit_router_flow_top_n.append(temp_model.from_map(k1))

        return self

class GetTransitRouterFlowTopNResponseBodyTransitRouterFlowTopN(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        bandwith_package_id: str = None,
        bytes: float = None,
        cen_id: str = None,
        end_time: str = None,
        other_ip: str = None,
        other_port: str = None,
        other_region: str = None,
        packets: float = None,
        protocol: str = None,
        start_time: str = None,
        this_ip: str = None,
        this_port: str = None,
        this_region: str = None,
    ):
        # The account ID.
        self.account_id = account_id
        # The ID of the CEN bandwidth plan.
        self.bandwith_package_id = bandwith_package_id
        # The total volume of traffic in the specified time range.
        self.bytes = bytes
        # The CEN instance ID.
        self.cen_id = cen_id
        # The end of the time range that you queried. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.end_time = end_time
        # The remote IP address.
        self.other_ip = other_ip
        # The remote port.
        self.other_port = other_port
        # The remote region where the **remote IP address** resides.
        self.other_region = other_region
        # The total number of packets in the specified time range.
        self.packets = packets
        # The protocol number.
        self.protocol = protocol
        # The beginning of the time range that you queried. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.start_time = start_time
        # The local IP address.
        self.this_ip = this_ip
        # The local port.
        self.this_port = this_port
        # The local region where the **local IP address** resides.
        self.this_region = this_region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.bandwith_package_id is not None:
            result['BandwithPackageId'] = self.bandwith_package_id

        if self.bytes is not None:
            result['Bytes'] = self.bytes

        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.other_ip is not None:
            result['OtherIp'] = self.other_ip

        if self.other_port is not None:
            result['OtherPort'] = self.other_port

        if self.other_region is not None:
            result['OtherRegion'] = self.other_region

        if self.packets is not None:
            result['Packets'] = self.packets

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.this_ip is not None:
            result['ThisIp'] = self.this_ip

        if self.this_port is not None:
            result['ThisPort'] = self.this_port

        if self.this_region is not None:
            result['ThisRegion'] = self.this_region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('BandwithPackageId') is not None:
            self.bandwith_package_id = m.get('BandwithPackageId')

        if m.get('Bytes') is not None:
            self.bytes = m.get('Bytes')

        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('OtherIp') is not None:
            self.other_ip = m.get('OtherIp')

        if m.get('OtherPort') is not None:
            self.other_port = m.get('OtherPort')

        if m.get('OtherRegion') is not None:
            self.other_region = m.get('OtherRegion')

        if m.get('Packets') is not None:
            self.packets = m.get('Packets')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('ThisIp') is not None:
            self.this_ip = m.get('ThisIp')

        if m.get('ThisPort') is not None:
            self.this_port = m.get('ThisPort')

        if m.get('ThisRegion') is not None:
            self.this_region = m.get('ThisRegion')

        return self

