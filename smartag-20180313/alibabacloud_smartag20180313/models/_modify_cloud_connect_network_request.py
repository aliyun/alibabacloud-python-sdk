# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyCloudConnectNetworkRequest(DaraModel):
    def __init__(
        self,
        ccn_id: str = None,
        cidr_block: str = None,
        description: str = None,
        interworking_status: str = None,
        name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the CCN instance.
        # 
        # This parameter is required.
        self.ccn_id = ccn_id
        # The private CIDR block.
        self.cidr_block = cidr_block
        # The description of the CCN instance.
        # 
        # The description must be 2 to 256 characters in length. The description must start with a letter but cannot start with `http://` or `https://`.
        self.description = description
        # Specifies whether to allow the SAG instances associated with the same CCN instance to communicate with each other.
        # 
        # *   **enable**: yes
        # *   **disable**: no
        self.interworking_status = interworking_status
        # The name of the CCN instance.
        # 
        # The name must be 2 to 128 characters in length, and can contain digits, periods (.), underscores (_), and hyphens (-). The name must start with a letter and cannot start with `http://` or `https://`.
        self.name = name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where the CCN instance is deployed.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ccn_id is not None:
            result['CcnId'] = self.ccn_id

        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block

        if self.description is not None:
            result['Description'] = self.description

        if self.interworking_status is not None:
            result['InterworkingStatus'] = self.interworking_status

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CcnId') is not None:
            self.ccn_id = m.get('CcnId')

        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InterworkingStatus') is not None:
            self.interworking_status = m.get('InterworkingStatus')

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

        return self

