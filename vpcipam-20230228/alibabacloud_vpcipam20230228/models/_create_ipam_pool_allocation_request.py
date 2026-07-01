# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateIpamPoolAllocationRequest(DaraModel):
    def __init__(
        self,
        cidr: str = None,
        cidr_mask: int = None,
        client_token: str = None,
        dry_run: bool = None,
        ipam_pool_allocation_description: str = None,
        ipam_pool_allocation_name: str = None,
        ipam_pool_id: str = None,
        region_id: str = None,
    ):
        # The CIDR block to allocate from the IPAM pool.
        # 
        # > You must specify either the **Cidr** or **CidrMask** parameter.
        self.cidr = cidr
        # The mask of the CIDR block to allocate from the IPAM pool.
        # 
        # > You must specify either the **Cidr** or **CidrMask** parameter.
        self.cidr_mask = cidr_mask
        # The client token that is used to ensure the idempotence of the request. Generate a value on your client to make sure that the value is unique among different requests. The token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the RequestId of the request as the ClientToken. The RequestId may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform a dry run. Valid values:
        # 
        # - **true**: Sends a check request. The custom reserved CIDR block is not created. The system checks for required parameters, request format, and service limits. If the check fails, an error is returned. If the check passes, the DryRunOperation error code is returned.
        # 
        # - **false** (default): Sends a normal request. After the request passes the check, a 2xx HTTP status code is returned and the custom reserved CIDR block is created.
        self.dry_run = dry_run
        # The description of the custom reserved CIDR block.
        # 
        # The description must be 1 to 256 characters in length. It must start with a letter or a Chinese character and cannot start with `http://` or `https://`. The default value is an empty string.
        self.ipam_pool_allocation_description = ipam_pool_allocation_description
        # The name of the custom reserved CIDR block.
        # 
        # The name must be 1 to 128 characters in length and cannot start with `http://` or `https://`.
        self.ipam_pool_allocation_name = ipam_pool_allocation_name
        # The ID of the IPAM pool.
        # 
        # This parameter is required.
        self.ipam_pool_id = ipam_pool_id
        # The ID of the region where you want to create the custom reserved CIDR block.
        # 
        # You can call [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) to obtain the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr is not None:
            result['Cidr'] = self.cidr

        if self.cidr_mask is not None:
            result['CidrMask'] = self.cidr_mask

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.ipam_pool_allocation_description is not None:
            result['IpamPoolAllocationDescription'] = self.ipam_pool_allocation_description

        if self.ipam_pool_allocation_name is not None:
            result['IpamPoolAllocationName'] = self.ipam_pool_allocation_name

        if self.ipam_pool_id is not None:
            result['IpamPoolId'] = self.ipam_pool_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')

        if m.get('CidrMask') is not None:
            self.cidr_mask = m.get('CidrMask')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('IpamPoolAllocationDescription') is not None:
            self.ipam_pool_allocation_description = m.get('IpamPoolAllocationDescription')

        if m.get('IpamPoolAllocationName') is not None:
            self.ipam_pool_allocation_name = m.get('IpamPoolAllocationName')

        if m.get('IpamPoolId') is not None:
            self.ipam_pool_id = m.get('IpamPoolId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

