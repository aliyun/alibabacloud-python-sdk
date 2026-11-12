# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSagExpressConnectInterfaceRequest(DaraModel):
    def __init__(
        self,
        ip: str = None,
        mask: str = None,
        owner_account: str = None,
        owner_id: int = None,
        port_name: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        smart_agid: str = None,
        smart_agsn: str = None,
        vlan: str = None,
    ):
        # The IP address.
        # 
        # This parameter is required.
        self.ip = ip
        # The IP address mask.
        # 
        # This parameter is required.
        self.mask = mask
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The name of the dedicated connection port.
        # 
        # This parameter is required.
        self.port_name = port_name
        # The region ID of the Smart Access Gateway instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The instance ID of the Smart Access Gateway.
        # 
        # This parameter is required.
        self.smart_agid = smart_agid
        # The serial number of the bound Smart Access Gateway device.
        # 
        # This parameter is required.
        self.smart_agsn = smart_agsn
        # The VLAN ID of the dedicated connection sub-interface.
        # 
        # Valid values: **0 to 4094**.
        # 
        # > - If the VLAN ID is 0, the port is a physical port and the VLAN sub-interface mode is not used.
        # - If the VLAN ID is 1 to 4094, the port uses a VLAN-based Layer 3 sub-interface.
        # - You can create up to 5 VLANs.
        self.vlan = vlan

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip is not None:
            result['IP'] = self.ip

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

        if self.vlan is not None:
            result['Vlan'] = self.vlan

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IP') is not None:
            self.ip = m.get('IP')

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

        if m.get('Vlan') is not None:
            self.vlan = m.get('Vlan')

        return self

