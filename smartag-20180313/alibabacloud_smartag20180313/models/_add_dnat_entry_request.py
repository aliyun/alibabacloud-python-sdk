# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddDnatEntryRequest(DaraModel):
    def __init__(
        self,
        external_ip: str = None,
        external_port: str = None,
        internal_ip: str = None,
        internal_port: str = None,
        ip_protocol: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sag_id: str = None,
        type: str = None,
    ):
        # The public IP address.
        # 
        # >  If the DNAT entry is used to forward packets transmitted over the Internet, the DNAT entry automatically recognizes the current public IP address.
        self.external_ip = external_ip
        # The public port.
        # 
        # Valid values: **1 to 65535**.
        # 
        # This parameter is required.
        self.external_port = external_port
        # The destination private IP address.
        # 
        # This parameter is required.
        self.internal_ip = internal_ip
        # The destination private port.
        # 
        # Valid values: **1 to 65535**.
        # 
        # This parameter is required.
        self.internal_port = internal_port
        # The protocol used in DNAT. Valid values:
        # 
        # *   **TCP**: forwards TCP packets.
        # *   **UDP**: The NAT gateway forwards UDP packets.
        # *   **Any**: forwards packets of all protocols.
        # 
        # This parameter is required.
        self.ip_protocol = ip_protocol
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where the SAG instance is deployed.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the SAG instance.
        # 
        # >  Only SAG instances used to manage SAG devices support DNAT.
        # 
        # This parameter is required.
        self.sag_id = sag_id
        # The type of the DNAT entry. Valid values:
        # 
        # *   **Intranet**: translates the destination IP address to a specific internal IP address. This is the default value.
        # *   **Internet**: translates the destination IP address to a specific public IP address.
        self.type = type

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

        if self.internal_ip is not None:
            result['InternalIp'] = self.internal_ip

        if self.internal_port is not None:
            result['InternalPort'] = self.internal_port

        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.sag_id is not None:
            result['SagId'] = self.sag_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternalIp') is not None:
            self.external_ip = m.get('ExternalIp')

        if m.get('ExternalPort') is not None:
            self.external_port = m.get('ExternalPort')

        if m.get('InternalIp') is not None:
            self.internal_ip = m.get('InternalIp')

        if m.get('InternalPort') is not None:
            self.internal_port = m.get('InternalPort')

        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SagId') is not None:
            self.sag_id = m.get('SagId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

