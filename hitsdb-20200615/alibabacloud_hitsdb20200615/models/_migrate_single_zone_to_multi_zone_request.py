# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MigrateSingleZoneToMultiZoneRequest(DaraModel):
    def __init__(
        self,
        arbitrary_vswitch_id: str = None,
        arbitrary_zone_id: str = None,
        dry_run: bool = None,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
        standby_vswitch_id: str = None,
        standby_zone_id: str = None,
    ):
        self.arbitrary_vswitch_id = arbitrary_vswitch_id
        self.arbitrary_zone_id = arbitrary_zone_id
        self.dry_run = dry_run
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token
        self.standby_vswitch_id = standby_vswitch_id
        self.standby_zone_id = standby_zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arbitrary_vswitch_id is not None:
            result['ArbitraryVSwitchId'] = self.arbitrary_vswitch_id

        if self.arbitrary_zone_id is not None:
            result['ArbitraryZoneId'] = self.arbitrary_zone_id

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.standby_vswitch_id is not None:
            result['StandbyVSwitchId'] = self.standby_vswitch_id

        if self.standby_zone_id is not None:
            result['StandbyZoneId'] = self.standby_zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArbitraryVSwitchId') is not None:
            self.arbitrary_vswitch_id = m.get('ArbitraryVSwitchId')

        if m.get('ArbitraryZoneId') is not None:
            self.arbitrary_zone_id = m.get('ArbitraryZoneId')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('StandbyVSwitchId') is not None:
            self.standby_vswitch_id = m.get('StandbyVSwitchId')

        if m.get('StandbyZoneId') is not None:
            self.standby_zone_id = m.get('StandbyZoneId')

        return self

