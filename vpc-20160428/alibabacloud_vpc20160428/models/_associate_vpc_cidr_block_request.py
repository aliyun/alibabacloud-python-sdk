# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AssociateVpcCidrBlockRequest(DaraModel):
    def __init__(
        self,
        ipv_6cidr_block: str = None,
        ip_version: str = None,
        ipam_pool_id: str = None,
        ipv_6cidr_mask: int = None,
        ipv_6isp: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        secondary_cidr_block: str = None,
        secondary_cidr_mask: int = None,
        vpc_id: str = None,
    ):
        # The specified IPv6 CIDR block of the VPC.
        # 
        # > You cannot specify both **SecondaryCidrBlock** and **Ipv6CidrBlock**.
        self.ipv_6cidr_block = ipv_6cidr_block
        # The version of the IP address. Valid values:
        # 
        # - **IPV4**: IPv4 address.
        # - **IPV6**: IPv6 address. When **IpVersion** is set to **IPV6** and **SecondaryCidrBlock** is not specified, a secondary IPv6 CIDR block is added to the VPC.
        self.ip_version = ip_version
        # The instance ID of the IPAM pool.
        self.ipam_pool_id = ipam_pool_id
        # The subnet mask used to add an IPv6 CIDR block from an IPAM pool to the VPC.
        # 
        # > When you use an IPAM pool to add a secondary IPv6 CIDR block to the VPC, you must specify at least one of IPv6CidrBlock and Ipv6CidrMask.
        self.ipv_6cidr_mask = ipv_6cidr_mask
        # The type of the IPv6 CIDR block of the VPC. Valid values:
        # 
        # - **BGP** (default): Alibaba Cloud BGP IPv6.
        # - **ChinaMobile**: China Mobile (single ISP).
        # - **ChinaUnicom**: China Unicom (single ISP).
        # - **ChinaTelecom**: China Telecom (single ISP).
        # 
        # > If your account is included in the China single-ISP bandwidth whitelist, you can set this parameter to **ChinaTelecom** (China Telecom), **ChinaUnicom** (China Unicom), or **ChinaMobile** (China Mobile).
        self.ipv_6isp = ipv_6isp
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the VPC to which you want to add a secondary CIDR block. 
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The secondary IPv4 CIDR block to add. The CIDR block must meet the following requirements:
        # 
        # - Use a private IPv4 address specified in RFC 1918 as the secondary IPv4 CIDR block of the VPC. The subnet mask is recommended to be 16 to 28 bits in length. Examples: 10.0.0.0/16, 172.16.0.0/16, and 192.168.0.0/16.
        # - You can use a custom CIDR block other than 100.64.0.0/10, 224.0.0.0/4, 127.0.0.0/8, 169.254.0.0/16, or their subnets as the secondary IPv4 CIDR block of the virtual private cloud (VPC).
        # 
        # Configuration limits:
        # 
        # - The CIDR block cannot start with 0. The subnet mask is recommended to be 16 to 28 bits in length.
        # 
        # - The secondary CIDR block cannot overlap with the primary CIDR block or existing secondary CIDR blocks of the VPC.
        # 
        # > If you do not use an IPAM pool to add a secondary CIDR block to the VPC, you must specify either the **SecondaryCidrBlock** parameter or the **Ipv6CidrBlock** parameter, but not both.
        self.secondary_cidr_block = secondary_cidr_block
        # The subnet mask used to add a secondary IPv4 CIDR block from an IPAM pool to the VPC.
        # 
        # > When you use an IPAM pool to add a secondary IPv4 CIDR block to the VPC, you must specify at least one of SecondaryCidrBlock and SecondaryCidrMask.
        self.secondary_cidr_mask = secondary_cidr_mask
        # The ID of the VPC to which you want to add a secondary CIDR block.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipv_6cidr_block is not None:
            result['IPv6CidrBlock'] = self.ipv_6cidr_block

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        if self.ipam_pool_id is not None:
            result['IpamPoolId'] = self.ipam_pool_id

        if self.ipv_6cidr_mask is not None:
            result['Ipv6CidrMask'] = self.ipv_6cidr_mask

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

        if self.secondary_cidr_block is not None:
            result['SecondaryCidrBlock'] = self.secondary_cidr_block

        if self.secondary_cidr_mask is not None:
            result['SecondaryCidrMask'] = self.secondary_cidr_mask

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IPv6CidrBlock') is not None:
            self.ipv_6cidr_block = m.get('IPv6CidrBlock')

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        if m.get('IpamPoolId') is not None:
            self.ipam_pool_id = m.get('IpamPoolId')

        if m.get('Ipv6CidrMask') is not None:
            self.ipv_6cidr_mask = m.get('Ipv6CidrMask')

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

        if m.get('SecondaryCidrBlock') is not None:
            self.secondary_cidr_block = m.get('SecondaryCidrBlock')

        if m.get('SecondaryCidrMask') is not None:
            self.secondary_cidr_mask = m.get('SecondaryCidrMask')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

