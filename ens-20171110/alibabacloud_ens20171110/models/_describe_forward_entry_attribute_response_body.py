# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeForwardEntryAttributeResponseBody(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        external_ip: str = None,
        external_port: str = None,
        forward_entry_id: str = None,
        forward_entry_name: str = None,
        health_check_port: str = None,
        internal_ip: str = None,
        internal_port: str = None,
        ip_protocol: str = None,
        nat_gateway_id: str = None,
        request_id: str = None,
        standby_external_ip: str = None,
        standby_status: str = None,
        status: str = None,
    ):
        # The creation time in UTC.
        self.creation_time = creation_time
        # The Elastic IP Address (EIP) that provides public network access in the DNAT entry.
        self.external_ip = external_ip
        # The external port or port range for port forwarding.
        # 
        # - The port range must be between 1 and 65535.
        # 
        # - To forward a port range, separate the start and end ports with a forward slash (/), such as 10/20.
        self.external_port = external_port
        # The ID of the DNAT entry.
        self.forward_entry_id = forward_entry_id
        # The name of the DNAT entry.
        self.forward_entry_name = forward_entry_name
        # The probe port for DNAT. It must fall within the internal port range. The default value is empty.
        self.health_check_port = health_check_port
        # The private IP address of the instance that communicates over the public network through the DNAT entry.
        self.internal_ip = internal_ip
        # The internal port or port range for port forwarding.
        # 
        # - The port range must be between 1 and 65535.
        # 
        # - To forward a port range, separate the start and end ports with a forward slash (/), such as 10/20.
        self.internal_port = internal_port
        # The protocol type. Valid values:
        # 
        # - **TCP**: Forwards TCP messages.
        # 
        # - **UDP**: Forwards UDP messages.
        # 
        # - **Any**: Forwards messages of all protocols.
        self.ip_protocol = ip_protocol
        # The ID of the NAT Gateway.
        self.nat_gateway_id = nat_gateway_id
        # The request ID.
        self.request_id = request_id
        # The standby Elastic IP Address (EIP) that provides public network access. You must select a standby EIP attached to the NAT Gateway. The standby public IP becomes active after the DNAT entry is created.
        self.standby_external_ip = standby_external_ip
        # The status of the standby EIP.
        # 
        # - Running: Enabled.
        # 
        # - Stopping: Being disabled.
        # 
        # - Stopped: Disabled.
        # 
        # - Starting: Being enabled.
        self.standby_status = standby_status
        # The status of the DNAT entry.
        # 
        # - Pending: The configuration is in progress, such as during creation or modification.
        # 
        # - Available: The entry is active.
        # 
        # - Deleting: The entry is being deleted.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

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

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.standby_external_ip is not None:
            result['StandbyExternalIp'] = self.standby_external_ip

        if self.standby_status is not None:
            result['StandbyStatus'] = self.standby_status

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

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

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StandbyExternalIp') is not None:
            self.standby_external_ip = m.get('StandbyExternalIp')

        if m.get('StandbyStatus') is not None:
            self.standby_status = m.get('StandbyStatus')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

