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
        # The IPv6 CIDR block that you want to add to the VPC.
        # 
        # >  You can specify only one of **SecondaryCidrBlock** and **Ipv6CidrBlock**.
        self.ipv_6cidr_block = ipv_6cidr_block
        # The version of the IP address. Valid values:
        # 
        # *   **IPV4**: the IPv4 address.
        # *   **IPV6**: the IPv6 address. If you set **IpVersion** to **IPV6** and do not specify **SecondaryCidrBlock**, you can add a secondary IPv6 CIDR block to the VPC.
        self.ip_version = ip_version
        # The ID of the IPAM pool.
        self.ipam_pool_id = ipam_pool_id
        # Add an IPv6 CIDR block from the IPAM pool to the VPC by entering a mask.
        # 
        # >  To add an IPv6 CIDR block to a VPC, specify at least one of the IPv6CidrBlock and Ipv6CidrMask parameters.
        self.ipv_6cidr_mask = ipv_6cidr_mask
        # The type of the IPv6 CIDR block. Valid values:
        # 
        # *   **BGP** (default)
        # *   **ChinaMobile**
        # *   **ChinaUnicom**
        # *   **ChinaTelecom**
        # 
        # >  If your Alibaba Cloud account is allowed to activate single-ISP bandwidth, you can set this parameter to **ChinaTelecom**, **ChinaUnicom**, or **ChinaMobile**.
        self.ipv_6isp = ipv_6isp
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the VPC to which you want to add a secondary CIDR block.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the region ID.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The IPv4 CIDR block to be added. Take note of the following requirements:
        # 
        # *   You can specify one of the following standard IPv4 CIDR blocks or their subnets as the secondary IPv4 CIDR block of the VPC: 192.168.0.0/16, 172.16.0.0/12, and 10.0.0.0/8.
        # *   You can also use a custom CIDR block other than 100.64.0.0/10, 224.0.0.0/4, 127.0.0.0/8, 169.254.0.0/16, or their subnets as the secondary IPv4 CIDR block of the VPC.
        # 
        # The CIDR block must meet the following requirements:
        # 
        # *   The CIDR block cannot start with 0. The subnet mask must be 8 to 28 bits in length.
        # *   The CIDR block cannot overlap with the primary CIDR block or an existing secondary CIDR block of the VPC.
        # 
        # >  You must and can specify only one of **SecondaryCidrBlock** and **Ipv6CidrBlock**.
        self.secondary_cidr_block = secondary_cidr_block
        # Add an IPv4 CIDR block from the IPAM pool to the VPC by specifying a mask.
        # 
        # >  If you use an IPAM pool, you must specify at least one of SecondaryCidrBlock and SecondaryCidrMask.
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

