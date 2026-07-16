# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpcipam20230228 import models as main_models
from darabonba.model import DaraModel

class CreateIpamPoolRequest(DaraModel):
    def __init__(
        self,
        allocation_default_cidr_mask: int = None,
        allocation_max_cidr_mask: int = None,
        allocation_min_cidr_mask: int = None,
        auto_import: bool = None,
        client_token: str = None,
        dry_run: bool = None,
        ip_version: str = None,
        ipam_pool_description: str = None,
        ipam_pool_name: str = None,
        ipam_scope_id: str = None,
        ipv_6isp: str = None,
        owner_account: str = None,
        owner_id: int = None,
        pool_region_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        source_ipam_pool_id: str = None,
        tag: List[main_models.CreateIpamPoolRequestTag] = None,
    ):
        # The default CIDR mask for allocations from the IPAM address pool.
        # 
        # > The IPv4 CIDR mask ranges from **0** to **32** bits. The IPv6 CIDR mask ranges from **0** to **128** bits.
        self.allocation_default_cidr_mask = allocation_default_cidr_mask
        # The maximum CIDR mask for allocations from the IPAM address pool.
        # 
        # > The IPv4 CIDR mask ranges from **0** to **32** bits. The IPv6 CIDR mask ranges from **0** to **128** bits.
        self.allocation_max_cidr_mask = allocation_max_cidr_mask
        # The minimum CIDR mask for allocations from the IPAM address pool.
        # 
        # > The IPv4 CIDR mask ranges from **0** to **32** bits. The IPv6 CIDR mask ranges from **0** to **128** bits.
        self.allocation_min_cidr_mask = allocation_min_cidr_mask
        # Specifies whether to enable the auto-import feature for the address pool.
        self.auto_import = auto_import
        # The client token that is used to ensure the idempotency of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the RequestId of the API request as the ClientToken. The RequestId may be different for each API request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # - **true**: performs only a dry run. The system checks the request for potential issues, including missing required parameters, request format, and instance status. If the request fails the dry run, an error message is returned. If the request passes the dry run, DryRunOperation is returned.
        # - **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, an HTTP 2xx status code is returned and the operation is directly performed.
        self.dry_run = dry_run
        # The IP address protocol version. Valid values:
        # 
        # - **IPv4**: IPv4.
        # 
        # - **IPv6**: IPv6.
        self.ip_version = ip_version
        # The description of the IPAM address pool.
        # 
        # The description must be 1 to 256 characters in length and must start with an uppercase or lowercase English letter or a Chinese character. It cannot start with `http://` or `https://`. If this parameter is not specified, the description is empty by default.
        self.ipam_pool_description = ipam_pool_description
        # The name of the IPAM address pool.
        # 
        # The name must be 1 to 128 characters in length and cannot start with `http://` or `https://`.
        self.ipam_pool_name = ipam_pool_name
        # The instance ID of the IPAM scope.
        # 
        # This parameter is required.
        self.ipam_scope_id = ipam_scope_id
        # The type of IPv6 CIDR block. This parameter takes effect only for public IPv6 address pools. Valid values:
        # 
        # - **BGP** (default): Alibaba Cloud BGP IPv6.
        # - **ChinaMobile**: China Mobile (single-line).
        # - **ChinaUnicom**: China Unicom (single-line).
        # - **ChinaTelecom**: China Telecom (single-line).
        # 
        # > If you are a user who has activated the single-line bandwidth whitelist, this field can be set to **ChinaTelecom** (China Telecom), **ChinaUnicom** (China Unicom), or **ChinaMobile** (China Mobile).
        self.ipv_6isp = ipv_6isp
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region where the IPAM address pool takes effect.
        self.pool_region_id = pool_region_id
        # The region ID of the IPAM. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) API to obtain the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID of the IPAM address pool.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The instance ID of the source IPAM address pool.
        # 
        # > If this parameter is not specified, the created address pool is a parent address pool.
        self.source_ipam_pool_id = source_ipam_pool_id
        # The tag list.
        self.tag = tag

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
        if self.allocation_default_cidr_mask is not None:
            result['AllocationDefaultCidrMask'] = self.allocation_default_cidr_mask

        if self.allocation_max_cidr_mask is not None:
            result['AllocationMaxCidrMask'] = self.allocation_max_cidr_mask

        if self.allocation_min_cidr_mask is not None:
            result['AllocationMinCidrMask'] = self.allocation_min_cidr_mask

        if self.auto_import is not None:
            result['AutoImport'] = self.auto_import

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        if self.ipam_pool_description is not None:
            result['IpamPoolDescription'] = self.ipam_pool_description

        if self.ipam_pool_name is not None:
            result['IpamPoolName'] = self.ipam_pool_name

        if self.ipam_scope_id is not None:
            result['IpamScopeId'] = self.ipam_scope_id

        if self.ipv_6isp is not None:
            result['Ipv6Isp'] = self.ipv_6isp

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.pool_region_id is not None:
            result['PoolRegionId'] = self.pool_region_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.source_ipam_pool_id is not None:
            result['SourceIpamPoolId'] = self.source_ipam_pool_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationDefaultCidrMask') is not None:
            self.allocation_default_cidr_mask = m.get('AllocationDefaultCidrMask')

        if m.get('AllocationMaxCidrMask') is not None:
            self.allocation_max_cidr_mask = m.get('AllocationMaxCidrMask')

        if m.get('AllocationMinCidrMask') is not None:
            self.allocation_min_cidr_mask = m.get('AllocationMinCidrMask')

        if m.get('AutoImport') is not None:
            self.auto_import = m.get('AutoImport')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        if m.get('IpamPoolDescription') is not None:
            self.ipam_pool_description = m.get('IpamPoolDescription')

        if m.get('IpamPoolName') is not None:
            self.ipam_pool_name = m.get('IpamPoolName')

        if m.get('IpamScopeId') is not None:
            self.ipam_scope_id = m.get('IpamScopeId')

        if m.get('Ipv6Isp') is not None:
            self.ipv_6isp = m.get('Ipv6Isp')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PoolRegionId') is not None:
            self.pool_region_id = m.get('PoolRegionId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SourceIpamPoolId') is not None:
            self.source_ipam_pool_id = m.get('SourceIpamPoolId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateIpamPoolRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class CreateIpamPoolRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the resource. A maximum of 20 tag keys are supported. Once this value is specified, it cannot be an empty string.
        # 
        # The tag key can be up to 64 characters in length and must start with a letter or Chinese character. It can contain digits, periods (.), underscores (_), and hyphens (-). It cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
        # 
        # > You must specify at least one of the **ResourceId.N** and **Tag.N** (**Tag.N.Key** and **Tag.N.Value**) parameters.
        self.key = key
        # The tag value of the resource. A maximum of 20 tag values are supported. Once this value is specified, it can be an empty string.
        # 
        # The tag value can be up to 128 characters in length and cannot contain `http://` or `https://`.
        # 
        # > You must specify at least one of the **ResourceId.N** and **Tag.N** (**Tag.N.Key** and **Tag.N.Value**) parameters.
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

