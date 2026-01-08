# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRiskEventPayloadResponseBody(DaraModel):
    def __init__(
        self,
        dst_ip: str = None,
        dst_port: int = None,
        dst_vpc_id: str = None,
        hit_content_type: int = None,
        hit_to: int = None,
        parsed_content: str = None,
        payload: str = None,
        payload_len: int = None,
        proto: str = None,
        real_ip: str = None,
        request_id: str = None,
        src_ip: str = None,
        src_port: int = None,
        src_vpc_id: str = None,
        xforward_for: str = None,
    ):
        # The destination IP address of the intrusion event.
        self.dst_ip = dst_ip
        # The destination port of the intrusion event.
        self.dst_port = dst_port
        # The destination VPC ID of the intrusion event.
        self.dst_vpc_id = dst_vpc_id
        # Type of the hit.
        self.hit_content_type = hit_content_type
        # The position where the hit ends.
        self.hit_to = hit_to
        # Hit payload.
        self.parsed_content = parsed_content
        # The attack payload of the intrusion event.
        self.payload = payload
        # The length of the attack payload of the intrusion event.
        self.payload_len = payload_len
        # The protocol type of intrusion event. Valid values:
        # 
        # *   **TCP**
        # *   **UDP**
        self.proto = proto
        # The HTTP X-Real-IP field.
        self.real_ip = real_ip
        # The request ID.
        self.request_id = request_id
        # The source IP address of the intrusion event.
        self.src_ip = src_ip
        # The source port of the intrusion event.
        self.src_port = src_port
        # The source VPC ID of the intrusion event.
        self.src_vpc_id = src_vpc_id
        # The HTTP X-Forwarded-For field.
        self.xforward_for = xforward_for

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dst_ip is not None:
            result['DstIP'] = self.dst_ip

        if self.dst_port is not None:
            result['DstPort'] = self.dst_port

        if self.dst_vpc_id is not None:
            result['DstVpcId'] = self.dst_vpc_id

        if self.hit_content_type is not None:
            result['HitContentType'] = self.hit_content_type

        if self.hit_to is not None:
            result['HitTo'] = self.hit_to

        if self.parsed_content is not None:
            result['ParsedContent'] = self.parsed_content

        if self.payload is not None:
            result['Payload'] = self.payload

        if self.payload_len is not None:
            result['PayloadLen'] = self.payload_len

        if self.proto is not None:
            result['Proto'] = self.proto

        if self.real_ip is not None:
            result['RealIp'] = self.real_ip

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.src_ip is not None:
            result['SrcIP'] = self.src_ip

        if self.src_port is not None:
            result['SrcPort'] = self.src_port

        if self.src_vpc_id is not None:
            result['SrcVpcId'] = self.src_vpc_id

        if self.xforward_for is not None:
            result['XForwardFor'] = self.xforward_for

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DstIP') is not None:
            self.dst_ip = m.get('DstIP')

        if m.get('DstPort') is not None:
            self.dst_port = m.get('DstPort')

        if m.get('DstVpcId') is not None:
            self.dst_vpc_id = m.get('DstVpcId')

        if m.get('HitContentType') is not None:
            self.hit_content_type = m.get('HitContentType')

        if m.get('HitTo') is not None:
            self.hit_to = m.get('HitTo')

        if m.get('ParsedContent') is not None:
            self.parsed_content = m.get('ParsedContent')

        if m.get('Payload') is not None:
            self.payload = m.get('Payload')

        if m.get('PayloadLen') is not None:
            self.payload_len = m.get('PayloadLen')

        if m.get('Proto') is not None:
            self.proto = m.get('Proto')

        if m.get('RealIp') is not None:
            self.real_ip = m.get('RealIp')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SrcIP') is not None:
            self.src_ip = m.get('SrcIP')

        if m.get('SrcPort') is not None:
            self.src_port = m.get('SrcPort')

        if m.get('SrcVpcId') is not None:
            self.src_vpc_id = m.get('SrcVpcId')

        if m.get('XForwardFor') is not None:
            self.xforward_for = m.get('XForwardFor')

        return self

