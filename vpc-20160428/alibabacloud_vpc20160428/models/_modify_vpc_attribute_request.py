# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyVpcAttributeRequest(DaraModel):
    def __init__(
        self,
        cidr_block: str = None,
        description: str = None,
        enable_dns_hostname: bool = None,
        enable_ipv_6: bool = None,
        ipv_6cidr_block: str = None,
        ipv_6isp: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        vpc_id: str = None,
        vpc_name: str = None,
    ):
        # The new IPv4 CIDR block of the VPC.
        # 
        # You can expand or shrink the CIDR block within the original IPv4 CIDR block of the VPC. The recommended subnet mask is 16 to 28 bits. If you shrink the IPv4 CIDR block of the VPC and IP addresses that are already in use fall outside the target CIDR block, the modification fails.
        # 
        # > Modifying the IPv4 CIDR block of a VPC does not affect existing services.
        self.cidr_block = cidr_block
        # The new description of the VPC.
        # 
        # The description must be 1 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # Specifies whether to enable the DNS hostname feature. Valid values:
        # 
        # - **false** (default): Disabled.
        # - **true**: Enabled.
        self.enable_dns_hostname = enable_dns_hostname
        # Specifies whether to enable IPv6. Valid values:
        # - **false** (default): Disabled.
        # - **true**: Enabled.
        self.enable_ipv_6 = enable_ipv_6
        # The IPv6 CIDR block of the VPC.
        # When you enable IPv6 for a VPC, the system will assign an IPv6 CIDR block. To specify an IPv6 CIDR block, invoke the [AllocateVpcIpv6Cidr](https://help.aliyun.com/document_detail/448916.html) operation to reserve a specific IPv6 CIDR block first, and then pass it in.
        # > For a VPC that already has IPv6 enabled, you cannot modify the IPv6 CIDR block by passing in this parameter.
        self.ipv_6cidr_block = ipv_6cidr_block
        # The type of the IPv6 CIDR block of the VPC. Valid values:
        # 
        # - **BGP** (default): Alibaba Cloud BGP IPv6.
        # - **ChinaMobile**: China Mobile (single ISP).
        # - **ChinaUnicom**: China Unicom (single ISP).
        # - **ChinaTelecom**: China Telecom (single ISP).
        # 
        # > If you are a user who has the single-ISP bandwidth whitelist enabled, you can set this parameter to **ChinaTelecom** (China Telecom), **ChinaUnicom** (China Unicom), or **ChinaMobile** (China Mobile).
        self.ipv_6isp = ipv_6isp
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the VPC.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the VPC that you want to modify.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id
        # The new name of the VPC.
        # 
        # The name must be 1 to 128 characters in length and cannot start with `http://` or `https://`.
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

        if self.enable_dns_hostname is not None:
            result['EnableDnsHostname'] = self.enable_dns_hostname

        if self.enable_ipv_6 is not None:
            result['EnableIPv6'] = self.enable_ipv_6

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

        if m.get('EnableDnsHostname') is not None:
            self.enable_dns_hostname = m.get('EnableDnsHostname')

        if m.get('EnableIPv6') is not None:
            self.enable_ipv_6 = m.get('EnableIPv6')

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

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')

        return self

