# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyVpcAttributeRequest(DaraModel):
    def __init__(
        self,
        cidr_block: str = None,
        description: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        user_cidr: str = None,
        vpc_id: str = None,
        vpc_name: str = None,
    ):
        self.cidr_block = cidr_block
        self.description = description
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.user_cidr = user_cidr
        # This parameter is required.
        self.vpc_id = vpc_id
        self.vpc_name = vpc_name

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

        if self.user_cidr is not None:
            result['UserCidr'] = self.user_cidr

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')

        if m.get('Description') is not None:
            self.description = m.get('Description')

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

        if m.get('UserCidr') is not None:
            self.user_cidr = m.get('UserCidr')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')

        return self

