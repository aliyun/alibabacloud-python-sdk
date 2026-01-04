# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateForwardEntryRequest(DaraModel):
    def __init__(
        self,
        external_ip: str = None,
        external_port: str = None,
        forward_entry_name: str = None,
        health_check_port: int = None,
        internal_ip: str = None,
        internal_port: str = None,
        ip_protocol: str = None,
        nat_gateway_id: str = None,
        standby_external_ip: str = None,
    ):
        # The elastic IP address (EIP) that is used to access the Internet.
        # 
        # This parameter is required.
        self.external_ip = external_ip
        # The external port or port range that is used for port forwarding.
        # 
        # *   Valid values: 1 to 65535.
        # *   To specify a port range, separate the first port and the last port with a forward slash (/), such as 10/20.
        # *   If you set ExternalPort to a port range, you must also set InternalPort to a port range. The number of ports in the port ranges must be the same. For example, if you set ExternalPort to 10/20, you can set InternalPort to 80/90.
        # 
        # This parameter is required.
        self.external_port = external_port
        # The name of the DNAT entry. The name must be 2 to 128 characters in length. The name cannot start with `http://` or `https://`.
        self.forward_entry_name = forward_entry_name
        # The probe port. The port must be within the internal port range. By default, this parameter is left empty.
        self.health_check_port = health_check_port
        # The private IP address of the instance that uses the DNAT entry for Internet communication.
        # 
        # This parameter is required.
        self.internal_ip = internal_ip
        # The internal port or port range that is used for port forwarding.
        # 
        # *   Valid values: 1 to 65535.
        # *   To specify a port range, separate the first port and the last port with a forward slash (/), such as 10/20.
        # 
        # This parameter is required.
        self.internal_port = internal_port
        # The protocol. Valid values:
        # 
        # *   **TCP**: forwards TCP packets.
        # *   **UDP**: forwards UDP packets.
        # *   **Any** (default): forwards all packets.
        self.ip_protocol = ip_protocol
        # The ID of the Network Address Translation (NAT) gateway.
        # 
        # This parameter is required.
        self.nat_gateway_id = nat_gateway_id
        # The secondary EIP that is used to access the Internet. You need to select a secondary EIP that is bound to NAT. After the DNAT entry is created, the secondary EIP takes effect.
        self.standby_external_ip = standby_external_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.external_ip is not None:
            result['ExternalIp'] = self.external_ip

        if self.external_port is not None:
            result['ExternalPort'] = self.external_port

        if self.forward_entry_name is not None:
            result['ForwardEntryName'] = self.forward_entry_name

        if self.health_check_port is not None:
            result['HealthCheckPort'] = self.health_check_port

        if self.internal_ip is not None:
            result['InternalIp'] = self.internal_ip

        if self.internal_port is not None:
            result['InternalPort'] = self.internal_port

        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        if self.standby_external_ip is not None:
            result['StandbyExternalIp'] = self.standby_external_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternalIp') is not None:
            self.external_ip = m.get('ExternalIp')

        if m.get('ExternalPort') is not None:
            self.external_port = m.get('ExternalPort')

        if m.get('ForwardEntryName') is not None:
            self.forward_entry_name = m.get('ForwardEntryName')

        if m.get('HealthCheckPort') is not None:
            self.health_check_port = m.get('HealthCheckPort')

        if m.get('InternalIp') is not None:
            self.internal_ip = m.get('InternalIp')

        if m.get('InternalPort') is not None:
            self.internal_port = m.get('InternalPort')

        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        if m.get('StandbyExternalIp') is not None:
            self.standby_external_ip = m.get('StandbyExternalIp')

        return self

