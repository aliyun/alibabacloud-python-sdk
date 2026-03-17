# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifySmartAccessGatewayUpBandwidthRequest(DaraModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        smart_agid: str = None,
        up_bandwidth_4g: int = None,
        up_bandwidth_wan: int = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the SAG instance.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the SAG instance.
        # 
        # This parameter is required.
        self.smart_agid = smart_agid
        # The maximum upstream bandwidth of 4G network connections established by the SAG device. Unit: Mbit/s.
        self.up_bandwidth_4g = up_bandwidth_4g
        # The maximum upstream bandwidth of network connections established on the WAN port of the SAG device. Unit: Mbit/s.
        self.up_bandwidth_wan = up_bandwidth_wan

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.up_bandwidth_4g is not None:
            result['UpBandwidth4G'] = self.up_bandwidth_4g

        if self.up_bandwidth_wan is not None:
            result['UpBandwidthWan'] = self.up_bandwidth_wan

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        if m.get('UpBandwidth4G') is not None:
            self.up_bandwidth_4g = m.get('UpBandwidth4G')

        if m.get('UpBandwidthWan') is not None:
            self.up_bandwidth_wan = m.get('UpBandwidthWan')

        return self

