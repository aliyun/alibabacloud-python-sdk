# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeForwardTableEntriesRequest(DaraModel):
    def __init__(
        self,
        external_ip: str = None,
        forward_entry_id: str = None,
        forward_entry_name: str = None,
        internal_ip: str = None,
        ip_protocol: str = None,
        nat_gateway_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The EIP in the DNAT entry. The public IP address is used to access the Internet.
        self.external_ip = external_ip
        # The ID of the DNAT entry.
        self.forward_entry_id = forward_entry_id
        # The name of the DNAT entry.
        self.forward_entry_name = forward_entry_name
        # The private IP address of the instance that uses the DNAT entry for Internet communication.
        self.internal_ip = internal_ip
        # The protocol. Valid values:
        # 
        # *   **TCP**: forwards TCP packets.
        # *   **UDP**: forwards UDP packets.
        # *   **Any**: forwards all packets.
        self.ip_protocol = ip_protocol
        # The ID of the NAT gateway.
        # 
        # This parameter is required.
        self.nat_gateway_id = nat_gateway_id
        # The page number. Pages start from page **1**.
        # 
        # Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Maximum value: **100**.
        # 
        # Default value: **10**.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.external_ip is not None:
            result['ExternalIp'] = self.external_ip

        if self.forward_entry_id is not None:
            result['ForwardEntryId'] = self.forward_entry_id

        if self.forward_entry_name is not None:
            result['ForwardEntryName'] = self.forward_entry_name

        if self.internal_ip is not None:
            result['InternalIp'] = self.internal_ip

        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternalIp') is not None:
            self.external_ip = m.get('ExternalIp')

        if m.get('ForwardEntryId') is not None:
            self.forward_entry_id = m.get('ForwardEntryId')

        if m.get('ForwardEntryName') is not None:
            self.forward_entry_name = m.get('ForwardEntryName')

        if m.get('InternalIp') is not None:
            self.internal_ip = m.get('InternalIp')

        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

