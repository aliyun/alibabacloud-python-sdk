# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAndAnalyzeNetworkPathRequest(DaraModel):
    def __init__(
        self,
        protocol: str = None,
        region_id: str = None,
        source_id: str = None,
        source_ip_address: str = None,
        source_port: int = None,
        source_type: str = None,
        target_id: str = None,
        target_ip_address: str = None,
        target_port: int = None,
        target_type: str = None,
    ):
        # The protocol type. Valid values:
        # 
        # *   **tcp**: Transmission Control Protocol (TCP)
        # *   **udp**: User Datagram Protocol (UDP)
        # *   **icmp**: Internet Control Message Protocol (ICMP)
        self.protocol = protocol
        # The ID of the region for which you want to initiate a task for analyzing network reachability.
        self.region_id = region_id
        # The ID of the source resource.
        # 
        # This parameter is required.
        self.source_id = source_id
        # The source IP address.
        self.source_ip_address = source_ip_address
        # The source port.
        self.source_port = source_port
        # The type of the source resource. Valid values:
        # 
        # *   **ecs**: the Elastic Compute Service (ECS) instance
        # *   **internetIp**: the public IP address
        # *   **vsw**: the vSwitch
        # *   **vpn**: the VPN gateway
        # *   **vbr**: the virtual border router (VBR)
        # 
        # This parameter is required.
        self.source_type = source_type
        # The ID of the destination resource.
        self.target_id = target_id
        # The destination IP address.
        self.target_ip_address = target_ip_address
        # The destination port.
        self.target_port = target_port
        # The type of the destination resource. Valid values:
        # 
        # *   **ecs**: the ECS instance
        # *   **internetIp**: the public IP address
        # *   **vsw**: the vSwitch
        # *   **vpn**: the VPN gateway
        # *   **vbr**: the VBR
        # *   **clb**: the Classic Load Balancer (CLB) instance
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.source_id is not None:
            result['SourceId'] = self.source_id

        if self.source_ip_address is not None:
            result['SourceIpAddress'] = self.source_ip_address

        if self.source_port is not None:
            result['SourcePort'] = self.source_port

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.target_id is not None:
            result['TargetId'] = self.target_id

        if self.target_ip_address is not None:
            result['TargetIpAddress'] = self.target_ip_address

        if self.target_port is not None:
            result['TargetPort'] = self.target_port

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')

        if m.get('SourceIpAddress') is not None:
            self.source_ip_address = m.get('SourceIpAddress')

        if m.get('SourcePort') is not None:
            self.source_port = m.get('SourcePort')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')

        if m.get('TargetIpAddress') is not None:
            self.target_ip_address = m.get('TargetIpAddress')

        if m.get('TargetPort') is not None:
            self.target_port = m.get('TargetPort')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

