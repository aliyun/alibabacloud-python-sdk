# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AllocateVpcIpv6CidrRequest(DaraModel):
    def __init__(
        self,
        address_pool_type: str = None,
        client_token: str = None,
        ipv_6cidr_block: str = None,
        ipv_6isp: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The type of the IPv6 address pool. Valid values:
        # - **aliyun** (default): The system assigns an IPv6 CIDR block.
        # - **custom**: A user-defined IPv6 CIDR block.
        self.address_pool_type = address_pool_type
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The ClientToken value can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** of each API request may be different.
        self.client_token = client_token
        # The IPv6 CIDR block to reserve.
        self.ipv_6cidr_block = ipv_6cidr_block
        # The type of the IPv6 CIDR block of the VPC. Valid values:
        # 
        # - **BGP** (default): BGP (multi-ISP).
        # - **BGP_International**: BGP (multi-ISP)_International.
        # - **ChinaMobile**: China Mobile (single-ISP).
        # - **ChinaUnicom**: China Unicom (single-ISP).
        # - **ChinaTelecom**: China Telecom (single-ISP).
        # - **ChinaMobile_L2**: China Mobile (single-ISP)_L2.
        # - **ChinaUnicom_L2**: China Unicom (single-ISP)_L2.
        # - **ChinaTelecom_L2**: China Telecom (single-ISP)_L2.
        # 
        # > - If you are a user whose whitelist is activated, you can set this parameter to **ChinaTelecom** (China Telecom), **ChinaUnicom** (China Unicom), **ChinaMobile** (China Mobile), **ChinaTelecom_L2** (China L2 Telecom), **ChinaUnicom_L2** (China L2 Unicom), **ChinaMobile_L2** (China L2 Mobile), or **BGP_International** (BGP multi-ISP International).
        # > - You can reserve only one IPv6 CIDR block of each type. You can reserve the next one only after the current one is assigned to a VPC.
        self.ipv_6isp = ipv_6isp
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the VPC.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the region ID.
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
        if self.address_pool_type is not None:
            result['AddressPoolType'] = self.address_pool_type

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.ipv_6cidr_block is not None:
            result['Ipv6CidrBlock'] = self.ipv_6cidr_block

        if self.ipv_6isp is not None:
            result['Ipv6Isp'] = self.ipv_6isp

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
        if m.get('AddressPoolType') is not None:
            self.address_pool_type = m.get('AddressPoolType')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Ipv6CidrBlock') is not None:
            self.ipv_6cidr_block = m.get('Ipv6CidrBlock')

        if m.get('Ipv6Isp') is not None:
            self.ipv_6isp = m.get('Ipv6Isp')

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

