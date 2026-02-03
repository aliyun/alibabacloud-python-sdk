# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nis20211216 import models as main_models
from darabonba.model import DaraModel

class GetVbrFlowTopNResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        virtual_border_router_flowlog_top_n: List[main_models.GetVbrFlowTopNResponseBodyVirtualBorderRouterFlowlogTopN] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The ranking result of hybrid cloud traffic data.
        self.virtual_border_router_flowlog_top_n = virtual_border_router_flowlog_top_n

    def validate(self):
        if self.virtual_border_router_flowlog_top_n:
            for v1 in self.virtual_border_router_flowlog_top_n:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['VirtualBorderRouterFlowlogTopN'] = []
        if self.virtual_border_router_flowlog_top_n is not None:
            for k1 in self.virtual_border_router_flowlog_top_n:
                result['VirtualBorderRouterFlowlogTopN'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.virtual_border_router_flowlog_top_n = []
        if m.get('VirtualBorderRouterFlowlogTopN') is not None:
            for k1 in m.get('VirtualBorderRouterFlowlogTopN'):
                temp_model = main_models.GetVbrFlowTopNResponseBodyVirtualBorderRouterFlowlogTopN()
                self.virtual_border_router_flowlog_top_n.append(temp_model.from_map(k1))

        return self

class GetVbrFlowTopNResponseBodyVirtualBorderRouterFlowlogTopN(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        attachment_id: str = None,
        bytes: float = None,
        cloud_ip: str = None,
        cloud_port: str = None,
        cloud_region: str = None,
        other_ip: str = None,
        other_port: str = None,
        packets: float = None,
        protocol: str = None,
        virtual_border_router_id: str = None,
    ):
        # The account ID.
        self.account_id = account_id
        # The CEN connection ID.
        self.attachment_id = attachment_id
        # The total volume of traffic in the specified time range.
        self.bytes = bytes
        # The local IP address.
        self.cloud_ip = cloud_ip
        # The local port.
        self.cloud_port = cloud_port
        # The local region where the local IP address resides.
        self.cloud_region = cloud_region
        # The remote IP address.
        self.other_ip = other_ip
        # The remote port.
        self.other_port = other_port
        # The total number of packets in the specified time range.
        self.packets = packets
        # The protocol number.
        self.protocol = protocol
        # The ID of the VBR that is associated with the Express Connect circuit.
        self.virtual_border_router_id = virtual_border_router_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.attachment_id is not None:
            result['AttachmentId'] = self.attachment_id

        if self.bytes is not None:
            result['Bytes'] = self.bytes

        if self.cloud_ip is not None:
            result['CloudIp'] = self.cloud_ip

        if self.cloud_port is not None:
            result['CloudPort'] = self.cloud_port

        if self.cloud_region is not None:
            result['CloudRegion'] = self.cloud_region

        if self.other_ip is not None:
            result['OtherIp'] = self.other_ip

        if self.other_port is not None:
            result['OtherPort'] = self.other_port

        if self.packets is not None:
            result['Packets'] = self.packets

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.virtual_border_router_id is not None:
            result['VirtualBorderRouterId'] = self.virtual_border_router_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('AttachmentId') is not None:
            self.attachment_id = m.get('AttachmentId')

        if m.get('Bytes') is not None:
            self.bytes = m.get('Bytes')

        if m.get('CloudIp') is not None:
            self.cloud_ip = m.get('CloudIp')

        if m.get('CloudPort') is not None:
            self.cloud_port = m.get('CloudPort')

        if m.get('CloudRegion') is not None:
            self.cloud_region = m.get('CloudRegion')

        if m.get('OtherIp') is not None:
            self.other_ip = m.get('OtherIp')

        if m.get('OtherPort') is not None:
            self.other_port = m.get('OtherPort')

        if m.get('Packets') is not None:
            self.packets = m.get('Packets')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('VirtualBorderRouterId') is not None:
            self.virtual_border_router_id = m.get('VirtualBorderRouterId')

        return self

