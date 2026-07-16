# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateVpcRequest(DaraModel):
    def __init__(
        self,
        cidr_block: str = None,
        client_token: str = None,
        description: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        user_cidr: str = None,
        vpc_name: str = None,
    ):
        # The IPv4 CIDR block of the VPC. You can use one of the following standard IPv4 CIDR blocks or their subnets:
        # 
        # - `10.0.0.0/8`
        # - `172.16.0.0/12`
        # - `192.168.0.0/16`
        self.cidr_block = cidr_block
        # A client-generated token that ensures the idempotence of the request. The token must be unique across requests, contain only ASCII characters, and not exceed 64 characters. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The VPC description. The description must be 2 to 256 characters long and cannot start with `http://` or `https://`.
        self.description = description
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where the VPC will be created. You can call the `DescribeRegions` operation to query the latest list of regions.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The user CIDR block. You can specify a user CIDR block as an alternative to the standard CIDR blocks. This lets you use a private IP address range other than `10.0.0.0/8`, `172.16.0.0/12`, or `192.168.0.0/16` as the CIDR block for the VPC.
        self.user_cidr = user_cidr
        # The VPC name. It must be 2 to 128 characters long, start with a letter, and contain only letters, digits, underscores (_), and hyphens (-).
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

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

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

        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

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

        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')

        return self

