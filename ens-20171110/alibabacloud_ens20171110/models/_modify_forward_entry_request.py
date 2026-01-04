# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyForwardEntryRequest(DaraModel):
    def __init__(
        self,
        external_ip: str = None,
        external_port: str = None,
        forward_entry_id: str = None,
        forward_entry_name: str = None,
        health_check_port: int = None,
        internal_ip: str = None,
        internal_port: str = None,
        ip_protocol: str = None,
    ):
        # The EIP in the DNAT entry. The public IP address is used to access the Internet.
        self.external_ip = external_ip
        # The external port or port range that is used for port forwarding.
        # 
        # *   Valid values: 1 to 65535.
        # *   To specify a port range, separate the first port and the last port with a forward slash (/), such as 10/20. The first port and the last port are included.
        # *   If you set ExternalPort to a port range, you must also set InternalPort to a port range. The number of ports in the port ranges must be the same. For example, if you set ExternalPort to 10/20, you can set InternalPort to 80/90.
        # *   The maximum port range is 1000.
        self.external_port = external_port
        # The ID of the DNAT entry.
        # 
        # This parameter is required.
        self.forward_entry_id = forward_entry_id
        # The name of the DNAT entry. The name must be 2 to 128 characters in length. It cannot start with `http://` or `https://`.
        self.forward_entry_name = forward_entry_name
        # The probe port. The port must be within the internal port range. By default, this parameter is left empty.
        self.health_check_port = health_check_port
        # The private IP address of the instance that uses the DNAT entry for Internet communication.
        self.internal_ip = internal_ip
        # The private port or port range that is used in port forwarding.
        # 
        # *   Valid values: 1 to 65535.
        # *   To specify a port range, separate the first port and the last port with a forward slash (/), such as 10/20. The first port and the last port are included.
        # *   If you set InternalPort to a port range, you must also set ExternalPort to a port range. The number of ports in the port ranges must be the same. For example, if you set ExternalPort to 10/20, you can set InternalPort to 80/90.
        # *   The maximum port range is 1000.
        self.internal_port = internal_port
        # The protocol. Valid values:
        # 
        # *   **TCP**: forwards TCP packets.
        # *   **UDP**: forwards UDP packets.
        # *   **Any** (default): forwards all packets.
        self.ip_protocol = ip_protocol

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

        if self.forward_entry_id is not None:
            result['ForwardEntryId'] = self.forward_entry_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternalIp') is not None:
            self.external_ip = m.get('ExternalIp')

        if m.get('ExternalPort') is not None:
            self.external_port = m.get('ExternalPort')

        if m.get('ForwardEntryId') is not None:
            self.forward_entry_id = m.get('ForwardEntryId')

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

        return self

