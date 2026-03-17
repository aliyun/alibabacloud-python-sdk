# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifySagManagementPortRequest(DaraModel):
    def __init__(
        self,
        gateway: str = None,
        ip: str = None,
        mask: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        smart_agid: str = None,
        smart_agsn: str = None,
    ):
        # The IP address of the management port gateway.
        self.gateway = gateway
        # The IP address of the management port.
        # 
        # This parameter is required.
        self.ip = ip
        # The subnet mask for the IP address of the management port.
        # 
        # This parameter is required.
        self.mask = mask
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
        # This parameter is required.
        self.smart_agid = smart_agid
        # The serial number of the SAG device associated with the SAG instance.
        # 
        # This parameter is required.
        self.smart_agsn = smart_agsn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gateway is not None:
            result['Gateway'] = self.gateway

        if self.ip is not None:
            result['IP'] = self.ip

        if self.mask is not None:
            result['Mask'] = self.mask

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

        if self.smart_agid is not None:
            result['SmartAGId'] = self.smart_agid

        if self.smart_agsn is not None:
            result['SmartAGSn'] = self.smart_agsn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Gateway') is not None:
            self.gateway = m.get('Gateway')

        if m.get('IP') is not None:
            self.ip = m.get('IP')

        if m.get('Mask') is not None:
            self.mask = m.get('Mask')

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

        if m.get('SmartAGId') is not None:
            self.smart_agid = m.get('SmartAGId')

        if m.get('SmartAGSn') is not None:
            self.smart_agsn = m.get('SmartAGSn')

        return self

