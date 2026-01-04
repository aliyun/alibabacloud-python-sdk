# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class CreateVpcRequest(DaraModel):
    def __init__(
        self,
        cidr_block: str = None,
        client_token: str = None,
        description: str = None,
        dry_run: bool = None,
        enable_dns_hostname: bool = None,
        enable_ipv_6: bool = None,
        ipv_4cidr_mask: int = None,
        ipv_4ipam_pool_id: str = None,
        ipv_6cidr_block: str = None,
        ipv_6cidr_mask: int = None,
        ipv_6ipam_pool_id: str = None,
        ipv_6isp: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tag: List[main_models.CreateVpcRequestTag] = None,
        user_cidr: str = None,
        vpc_name: str = None,
    ):
        # The CIDR block of the VPC.
        # 
        # *   We recommend using the private IPv4 address specified in RFC 1918 as the primary IPv4 CIDR block of the VPC with a recommended mask length of 16 to 28 bits. For example, 10.0.0.0/16, 172.16.0.0/16, and 192.168.0.0/16.
        # *   You can also use a custom CIDR block other than 100.64.0.0/10, 224.0.0.0/4, 127.0.0.0/8, 169.254.0.0/16, or their subnets as the primary IPv4 CIDR block.
        self.cidr_block = cidr_block
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # The description of the VPC.
        # 
        # The description must be 1 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # Specifies whether to perform a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error code is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # Whether to enable the DNS hostname feature. Values:
        # - **false** (default): Not enabled. 
        # - **true**: Enabled.
        self.enable_dns_hostname = enable_dns_hostname
        # Indicates whether IPv6 is enabled. Valid values:
        # 
        # *   **false** (default): disabled.
        # *   **true**: enabled.
        self.enable_ipv_6 = enable_ipv_6
        # Allocate VPC from the IPAM address pool by inputting a mask.
        # > When creating a VPC with a specified IPAM address pool, at least one of the parameters CidrBlock or Ipv4CidrMask must be provided.
        self.ipv_4cidr_mask = ipv_4cidr_mask
        # The ID of the IP Address Manager (IPAM) pool of the IPv4 type.
        self.ipv_4ipam_pool_id = ipv_4ipam_pool_id
        # The IPv6 CIDR block of the VPC. If you enable IPv6 for a VPC, the system allocates an IPv6 CIDR block. To specify an IPv6 CIDR block, you must call the [AllocateVpcIpv6Cidr](https://help.aliyun.com/document_detail/448916.html) operation to reserve the specified IPv6 CIDR block.
        self.ipv_6cidr_block = ipv_6cidr_block
        # Add an IPv6 CIDR block from the IPAM pool to the VPC by entering a mask.
        self.ipv_6cidr_mask = ipv_6cidr_mask
        # The ID of the IP Address Manager (IPAM) pool of the IPv6 type.
        self.ipv_6ipam_pool_id = ipv_6ipam_pool_id
        # The type of the IPv6 CIDR block of the VPC. Valid values:
        # 
        # *   **BGP** (default)
        # *   **ChinaMobile**
        # *   **ChinaUnicom**
        # *   **ChinaTelecom**
        # 
        # >  If you are allowed to use single-ISP bandwidth, you can set the value to **ChinaTelecom**, **ChinaUnicom**, or **ChinaMobile**.
        self.ipv_6isp = ipv_6isp
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region to which the VPC belongs.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        # 
        # For more information about resource groups, see [What is a resource group?](https://help.aliyun.com/document_detail/94475.html)
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tag of the resource.
        self.tag = tag
        # The user CIDR block. Separate user CIDR blocks with commas (,). You can specify up to three user CIDR blocks.
        # 
        # For more information about user CIDR blocks, see the `What is a user CIDR block?` section in [VPC FAQ](https://help.aliyun.com/document_detail/185311.html).
        self.user_cidr = user_cidr
        # The name of the VPC.
        # 
        # The name must be 1 to 128 characters in length and cannot start with `http://` or `https://`.
        self.vpc_name = vpc_name

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

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

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.enable_dns_hostname is not None:
            result['EnableDnsHostname'] = self.enable_dns_hostname

        if self.enable_ipv_6 is not None:
            result['EnableIpv6'] = self.enable_ipv_6

        if self.ipv_4cidr_mask is not None:
            result['Ipv4CidrMask'] = self.ipv_4cidr_mask

        if self.ipv_4ipam_pool_id is not None:
            result['Ipv4IpamPoolId'] = self.ipv_4ipam_pool_id

        if self.ipv_6cidr_block is not None:
            result['Ipv6CidrBlock'] = self.ipv_6cidr_block

        if self.ipv_6cidr_mask is not None:
            result['Ipv6CidrMask'] = self.ipv_6cidr_mask

        if self.ipv_6ipam_pool_id is not None:
            result['Ipv6IpamPoolId'] = self.ipv_6ipam_pool_id

        if self.ipv_6isp is not None:
            result['Ipv6Isp'] = self.ipv_6isp

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

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

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EnableDnsHostname') is not None:
            self.enable_dns_hostname = m.get('EnableDnsHostname')

        if m.get('EnableIpv6') is not None:
            self.enable_ipv_6 = m.get('EnableIpv6')

        if m.get('Ipv4CidrMask') is not None:
            self.ipv_4cidr_mask = m.get('Ipv4CidrMask')

        if m.get('Ipv4IpamPoolId') is not None:
            self.ipv_4ipam_pool_id = m.get('Ipv4IpamPoolId')

        if m.get('Ipv6CidrBlock') is not None:
            self.ipv_6cidr_block = m.get('Ipv6CidrBlock')

        if m.get('Ipv6CidrMask') is not None:
            self.ipv_6cidr_mask = m.get('Ipv6CidrMask')

        if m.get('Ipv6IpamPoolId') is not None:
            self.ipv_6ipam_pool_id = m.get('Ipv6IpamPoolId')

        if m.get('Ipv6Isp') is not None:
            self.ipv_6isp = m.get('Ipv6Isp')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateVpcRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('UserCidr') is not None:
            self.user_cidr = m.get('UserCidr')

        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')

        return self

class CreateVpcRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N to add to the resource. You can specify at most 20 tag keys. The tag key cannot be an empty string.
        # 
        # The tag key can be at most 128 characters in length. It cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
        self.key = key
        # The value of tag N to add to the resource. You can specify at most 20 tag values. The tag value can be an empty string.
        # 
        # The tag value can be up to 128 characters in length, but cannot contain `http://` or `https://`. The tag value cannot start with `aliyun` or `acs:`.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

