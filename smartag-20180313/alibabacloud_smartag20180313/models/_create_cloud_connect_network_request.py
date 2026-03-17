# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCloudConnectNetworkRequest(DaraModel):
    def __init__(
        self,
        cidr_block: str = None,
        description: str = None,
        name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        snat_cidr_block: str = None,
    ):
        # The private CIDR block.
        self.cidr_block = cidr_block
        # The description of the CCN instance.
        # 
        # The description must be 2 to 128 characters in length and can contain letters, digits, underscores (_), and hyphens (-). The description must start with a letter.
        self.description = description
        # The name of the CCN instance.
        # 
        # The name must be 2 to 100 characters in length and can contain letters, digits, periods (.), underscores (_),and hyphens (-). The name must start with a letter.
        self.name = name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where the CCN instance is deployed.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The private CIDR block used for Source Network Address Translation (SNAT).
        self.snat_cidr_block = snat_cidr_block

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

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

        if self.snat_cidr_block is not None:
            result['SnatCidrBlock'] = self.snat_cidr_block

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

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

        if m.get('SnatCidrBlock') is not None:
            self.snat_cidr_block = m.get('SnatCidrBlock')

        return self

