# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyVSwitchCidrReservationAttributeRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        v_switch_cidr_reservation_description: str = None,
        v_switch_cidr_reservation_id: str = None,
        v_switch_cidr_reservation_name: str = None,
    ):
        self.client_token = client_token
        self.dry_run = dry_run
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where the vSwitch is deployed.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The new description of the reserved CIDR block. The default value is empty.
        # 
        # The description must be 2 to 256 characters in length. It must start with a letter and cannot start with `http://` or `https://`.
        self.v_switch_cidr_reservation_description = v_switch_cidr_reservation_description
        # The ID of the reserved CIDR block.
        # 
        # This parameter is required.
        self.v_switch_cidr_reservation_id = v_switch_cidr_reservation_id
        # The new name of the reserved CIDR block.
        # 
        # The name must be 2 to 128 characters in length and can contain letters, digits, underscores (_), and hyphens (-). It must start with a letter.
        self.v_switch_cidr_reservation_name = v_switch_cidr_reservation_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

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

        if self.v_switch_cidr_reservation_description is not None:
            result['VSwitchCidrReservationDescription'] = self.v_switch_cidr_reservation_description

        if self.v_switch_cidr_reservation_id is not None:
            result['VSwitchCidrReservationId'] = self.v_switch_cidr_reservation_id

        if self.v_switch_cidr_reservation_name is not None:
            result['VSwitchCidrReservationName'] = self.v_switch_cidr_reservation_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

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

        if m.get('VSwitchCidrReservationDescription') is not None:
            self.v_switch_cidr_reservation_description = m.get('VSwitchCidrReservationDescription')

        if m.get('VSwitchCidrReservationId') is not None:
            self.v_switch_cidr_reservation_id = m.get('VSwitchCidrReservationId')

        if m.get('VSwitchCidrReservationName') is not None:
            self.v_switch_cidr_reservation_name = m.get('VSwitchCidrReservationName')

        return self

