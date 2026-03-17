# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifySagLanRequest(DaraModel):
    def __init__(
        self,
        end_ip: str = None,
        ip: str = None,
        iptype: str = None,
        lease: str = None,
        mask: str = None,
        owner_account: str = None,
        owner_id: int = None,
        port_name: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        smart_agid: str = None,
        smart_agsn: str = None,
        start_ip: str = None,
    ):
        # The last IP address of the DHCP pool.
        self.end_ip = end_ip
        # The IP address of the LAN port.
        # 
        # This parameter is required.
        self.ip = ip
        # The connection type of the LAN port. Valid values:
        # 
        # *   **DHCP**: a dynamic IP address. Uses the Dynamic Host Configuration Protocol (DHCP) to dynamically assign an IP address to a connected device.
        # *   **STATIC**: a static IP address. Specifies a static IP address for the LAN port.
        # 
        # This parameter is required.
        self.iptype = iptype
        # The time duration that the IP address is retained after it is assigned through DHCP. Unit: minute.
        # 
        # Valid values: **1 to 43200**.
        self.lease = lease
        # The subnet mask of the LAN port IP address.
        # 
        # This parameter is required.
        self.mask = mask
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The name of the LAN port.
        # 
        # This parameter is required.
        self.port_name = port_name
        # The ID of the region where the SAG instance is deployed.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the SAG instance.
        # 
        # This parameter is required.
        self.smart_agid = smart_agid
        # The serial number of the SAG device that is associated with the SAG instance.
        # 
        # This parameter is required.
        self.smart_agsn = smart_agsn
        # The first IP address of the DHCP pool.
        self.start_ip = start_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_ip is not None:
            result['EndIp'] = self.end_ip

        if self.ip is not None:
            result['IP'] = self.ip

        if self.iptype is not None:
            result['IPType'] = self.iptype

        if self.lease is not None:
            result['Lease'] = self.lease

        if self.mask is not None:
            result['Mask'] = self.mask

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.port_name is not None:
            result['PortName'] = self.port_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.smart_agid is not None:
            result['SmartAGId'] = self.smart_agid

        if self.smart_agsn is not None:
            result['SmartAGSn'] = self.smart_agsn

        if self.start_ip is not None:
            result['StartIp'] = self.start_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndIp') is not None:
            self.end_ip = m.get('EndIp')

        if m.get('IP') is not None:
            self.ip = m.get('IP')

        if m.get('IPType') is not None:
            self.iptype = m.get('IPType')

        if m.get('Lease') is not None:
            self.lease = m.get('Lease')

        if m.get('Mask') is not None:
            self.mask = m.get('Mask')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PortName') is not None:
            self.port_name = m.get('PortName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SmartAGId') is not None:
            self.smart_agid = m.get('SmartAGId')

        if m.get('SmartAGSn') is not None:
            self.smart_agsn = m.get('SmartAGSn')

        if m.get('StartIp') is not None:
            self.start_ip = m.get('StartIp')

        return self

