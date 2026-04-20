# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateIpamPoolAllocationRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        ipam_pool_allocation_description: str = None,
        ipam_pool_allocation_id: str = None,
        ipam_pool_allocation_name: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # Specifies whether to precheck this request. Valid values:
        # 
        # *   **true**: performs a dry run without modifying the CIDR blocks of IPAM pools. The system checks the required parameters, request syntax, and limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the DryRunOperation error code is returned.
        # *   **false** (default): performs a dry run and the actual request. If the request passes the check, an HTTP 2xx status code is returned and the CIDR allocation information of the IPAM address pool is modified.
        self.dry_run = dry_run
        # The description of the CIDR allocation of the IPAM pool.
        # 
        # The description must be 1 to 256 characters in length and start with a letter, but cannot start with a `http://` or `https://`. This parameter is empty by default.
        self.ipam_pool_allocation_description = ipam_pool_allocation_description
        # The ID of the instance to which CIDR blocks are allocated from the IPAM pool.
        # 
        # This parameter is required.
        self.ipam_pool_allocation_id = ipam_pool_allocation_id
        # The name of the CIDR allocation of the IPAM pool.
        # 
        # It must be 1 to 128 characters in length and cannot start with `http://` or `https://`.
        self.ipam_pool_allocation_name = ipam_pool_allocation_name
        # The ID of the region where you want to perform the operation. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the region list.
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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.ipam_pool_allocation_description is not None:
            result['IpamPoolAllocationDescription'] = self.ipam_pool_allocation_description

        if self.ipam_pool_allocation_id is not None:
            result['IpamPoolAllocationId'] = self.ipam_pool_allocation_id

        if self.ipam_pool_allocation_name is not None:
            result['IpamPoolAllocationName'] = self.ipam_pool_allocation_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('IpamPoolAllocationDescription') is not None:
            self.ipam_pool_allocation_description = m.get('IpamPoolAllocationDescription')

        if m.get('IpamPoolAllocationId') is not None:
            self.ipam_pool_allocation_id = m.get('IpamPoolAllocationId')

        if m.get('IpamPoolAllocationName') is not None:
            self.ipam_pool_allocation_name = m.get('IpamPoolAllocationName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

