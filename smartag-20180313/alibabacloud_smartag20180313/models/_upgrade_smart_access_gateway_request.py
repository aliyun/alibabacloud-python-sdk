# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpgradeSmartAccessGatewayRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        band_width_spec: int = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        restore_time: str = None,
        smart_agid: str = None,
    ):
        # Specifies whether automatic payment is enabled for the bills of upfront instances. Valid values:
        # 
        # - **true**: Yes.
        # 
        # - **false**: No.
        # 
        # This parameter is required.
        self.auto_pay = auto_pay
        # The bandwidth of the Smart Access Gateway instance. 
        # 
        # - If the device specification is sag-100wm, the value ranges from 2 to 50 Mbit/s.
        #           
        # - If the device specification is sag-1000, the value ranges from 10 to 500 Mbit/s.
        self.band_width_spec = band_width_spec
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the Smart Access Gateway.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The revert epoch for a temporary upgrade. This parameter specifies the expiration epoch of the temporary bandwidth upgrade. By default, if this parameter is left empty, the upgrade remains effective until the end-of-life (EOL) of the instance. If a specific epoch is specified, the bandwidth automatically reverts to the pre-upgrade configuration at the specified epoch.
        self.restore_time = restore_time
        # The Smart Access Gateway instance ID.
        # 
        # This parameter is required.
        self.smart_agid = smart_agid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.band_width_spec is not None:
            result['BandWidthSpec'] = self.band_width_spec

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

        if self.restore_time is not None:
            result['RestoreTime'] = self.restore_time

        if self.smart_agid is not None:
            result['SmartAGId'] = self.smart_agid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('BandWidthSpec') is not None:
            self.band_width_spec = m.get('BandWidthSpec')

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

        if m.get('RestoreTime') is not None:
            self.restore_time = m.get('RestoreTime')

        if m.get('SmartAGId') is not None:
            self.smart_agid = m.get('SmartAGId')

        return self

