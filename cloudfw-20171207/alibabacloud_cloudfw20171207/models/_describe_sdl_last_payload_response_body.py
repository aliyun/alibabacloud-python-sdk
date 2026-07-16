# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSdlLastPayloadResponseBody(DaraModel):
    def __init__(
        self,
        dst_port_list: str = None,
        payload: str = None,
        proto_list: str = None,
        request_id: str = None,
        src_port_list: str = None,
    ):
        # The destination port.
        self.dst_port_list = dst_port_list
        # The attack payload of the intrusion prevention event.
        self.payload = payload
        # The protocol.
        self.proto_list = proto_list
        # Id of the request
        self.request_id = request_id
        # The source port.
        self.src_port_list = src_port_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dst_port_list is not None:
            result['DstPortList'] = self.dst_port_list

        if self.payload is not None:
            result['Payload'] = self.payload

        if self.proto_list is not None:
            result['ProtoList'] = self.proto_list

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.src_port_list is not None:
            result['SrcPortList'] = self.src_port_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DstPortList') is not None:
            self.dst_port_list = m.get('DstPortList')

        if m.get('Payload') is not None:
            self.payload = m.get('Payload')

        if m.get('ProtoList') is not None:
            self.proto_list = m.get('ProtoList')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SrcPortList') is not None:
            self.src_port_list = m.get('SrcPortList')

        return self

