# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MigrateAvailableZoneRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        effective_time: str = None,
        hidden_zone_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        secondary_zone_id: str = None,
        vswitch: str = None,
        zone_id: str = None,
    ):
        # The ID of the instance.
        # 
        # > If the instance is deployed in a VPC, you must specify the **Vswitch** parameter.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The time when the instance is migrated to the destination zone. Valid values:
        # 
        # *   **Immediately**: The instance is immediately migrated to the destination zone.
        # *   **MaintainTime**: The instance is migrated to the destination zone during the maintenance window of the instance.
        # 
        # Default value: **Immediately**.
        self.effective_time = effective_time
        # The ID of the destination hidden zone.
        self.hidden_zone_id = hidden_zone_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the destination secondary zone.
        self.secondary_zone_id = secondary_zone_id
        # The ID of the vSwitch in the destination zone.
        # 
        # > If the instance is deployed in a VPC, you must specify this parameter.
        self.vswitch = vswitch
        # The ID of the destination zone.
        # 
        # > 
        # 
        # *   The source zone and the destination zone belong to the same region.
        # 
        # *   You can call the [DescribeRegions](https://help.aliyun.com/document_detail/61933.html) operation to query the zone ID.
        # 
        # This parameter is required.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time

        if self.hidden_zone_id is not None:
            result['HiddenZoneId'] = self.hidden_zone_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.secondary_zone_id is not None:
            result['SecondaryZoneId'] = self.secondary_zone_id

        if self.vswitch is not None:
            result['Vswitch'] = self.vswitch

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')

        if m.get('HiddenZoneId') is not None:
            self.hidden_zone_id = m.get('HiddenZoneId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecondaryZoneId') is not None:
            self.secondary_zone_id = m.get('SecondaryZoneId')

        if m.get('Vswitch') is not None:
            self.vswitch = m.get('Vswitch')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

