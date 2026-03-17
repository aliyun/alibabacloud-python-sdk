# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifySagRouteProtocolBgpRequest(DaraModel):
    def __init__(
        self,
        hold_time: int = None,
        keep_alive: int = None,
        local_as: int = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        router_id: str = None,
        smart_agid: str = None,
        smart_agsn: str = None,
    ):
        # The hold time.
        # 
        # Valid values: **3 to 65535**. Unit: seconds.
        # 
        # >  When the SAG device establishes a peering connection with a peer device, the hold time of both devices must be the same. If the SAG device does not receive a keepalive or update message from the peer device within the hold time, the connection between the BGP peers is closed.
        # 
        # This parameter is required.
        self.hold_time = hold_time
        # The time interval at which keep-alive packets are sent.
        # 
        # Valid values: **0 to 65535**. Unit: seconds.
        # 
        # This parameter is required.
        self.keep_alive = keep_alive
        # The autonomous system number (ASN) to which the SAG device belongs.
        # 
        # Valid values: **1 to 4294967295**.
        # 
        # This parameter is required.
        self.local_as = local_as
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where the SAG instance is deployed.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the BGP router.
        # 
        # Set the value to an IPv4 address.
        # 
        # This parameter is required.
        self.router_id = router_id
        # The ID of the SAG instance.
        # 
        # This parameter is required.
        self.smart_agid = smart_agid
        # The serial number of the SAG device.
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
        if self.hold_time is not None:
            result['HoldTime'] = self.hold_time

        if self.keep_alive is not None:
            result['KeepAlive'] = self.keep_alive

        if self.local_as is not None:
            result['LocalAs'] = self.local_as

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

        if self.router_id is not None:
            result['RouterId'] = self.router_id

        if self.smart_agid is not None:
            result['SmartAGId'] = self.smart_agid

        if self.smart_agsn is not None:
            result['SmartAGSn'] = self.smart_agsn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HoldTime') is not None:
            self.hold_time = m.get('HoldTime')

        if m.get('KeepAlive') is not None:
            self.keep_alive = m.get('KeepAlive')

        if m.get('LocalAs') is not None:
            self.local_as = m.get('LocalAs')

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

        if m.get('RouterId') is not None:
            self.router_id = m.get('RouterId')

        if m.get('SmartAGId') is not None:
            self.smart_agid = m.get('SmartAGId')

        if m.get('SmartAGSn') is not None:
            self.smart_agsn = m.get('SmartAGSn')

        return self

