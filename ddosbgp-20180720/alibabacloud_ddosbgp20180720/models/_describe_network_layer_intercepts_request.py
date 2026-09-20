# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeNetworkLayerInterceptsRequest(DaraModel):
    def __init__(
        self,
        destination_ip: str = None,
        destination_port: int = None,
        end_time: int = None,
        instance_id: str = None,
        intercept_module: str = None,
        network_protocol: str = None,
        page: int = None,
        page_size: int = None,
        protocol_number: int = None,
        source_port: int = None,
        src_ip: str = None,
        start_time: int = None,
    ):
        # The destination IP address.
        self.destination_ip = destination_ip
        # The destination port.
        self.destination_port = destination_port
        # The end time of the DDoS attack event to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The instance ID of the Anti-DDoS Origin instance to query.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The interception module.
        self.intercept_module = intercept_module
        # The network protocol.
        self.network_protocol = network_protocol
        # The page number.
        self.page = page
        # The number of interception log entries per page in a paged query.
        self.page_size = page_size
        # The network protocol number. This is a standard network protocol number.
        self.protocol_number = protocol_number
        # The source port.
        self.source_port = source_port
        # The source IP address.
        self.src_ip = src_ip
        # The start time of the DDoS attack event to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination_ip is not None:
            result['DestinationIp'] = self.destination_ip

        if self.destination_port is not None:
            result['DestinationPort'] = self.destination_port

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.intercept_module is not None:
            result['InterceptModule'] = self.intercept_module

        if self.network_protocol is not None:
            result['NetworkProtocol'] = self.network_protocol

        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.protocol_number is not None:
            result['ProtocolNumber'] = self.protocol_number

        if self.source_port is not None:
            result['SourcePort'] = self.source_port

        if self.src_ip is not None:
            result['SrcIp'] = self.src_ip

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationIp') is not None:
            self.destination_ip = m.get('DestinationIp')

        if m.get('DestinationPort') is not None:
            self.destination_port = m.get('DestinationPort')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InterceptModule') is not None:
            self.intercept_module = m.get('InterceptModule')

        if m.get('NetworkProtocol') is not None:
            self.network_protocol = m.get('NetworkProtocol')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProtocolNumber') is not None:
            self.protocol_number = m.get('ProtocolNumber')

        if m.get('SourcePort') is not None:
            self.source_port = m.get('SourcePort')

        if m.get('SrcIp') is not None:
            self.src_ip = m.get('SrcIp')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

