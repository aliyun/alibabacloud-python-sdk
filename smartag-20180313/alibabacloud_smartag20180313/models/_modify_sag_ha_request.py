# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifySagHaRequest(DaraModel):
    def __init__(
        self,
        mode: str = None,
        owner_account: str = None,
        owner_id: int = None,
        port_name: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        smart_agid: str = None,
        smart_agsn: str = None,
        virtual_ip: str = None,
    ):
        # The HA mode. Valid values:
        # 
        # *   **NONE**: disables HA.
        # *   **STATIC**: enables static HA.
        # *   **DYNAMIC**: enables dynamic HA.
        # 
        # This parameter is required.
        self.mode = mode
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The port name.
        # 
        # >  If Mode is set to STATIC, you must specify a port name.
        self.port_name = port_name
        # The region ID of the SAG instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The SAG instance ID.
        # 
        # This parameter is required.
        self.smart_agid = smart_agid
        # The serial number of the SAG device associated with the SAG instance.
        # 
        # This parameter is required.
        self.smart_agsn = smart_agsn
        # The virtual IP address.
        # 
        # >  If Mode is set to STATIC, you must specify a virtual IP address.
        self.virtual_ip = virtual_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mode is not None:
            result['Mode'] = self.mode

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

        if self.virtual_ip is not None:
            result['VirtualIp'] = self.virtual_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

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

        if m.get('VirtualIp') is not None:
            self.virtual_ip = m.get('VirtualIp')

        return self

