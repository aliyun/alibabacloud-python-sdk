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
        # A client token to ensure the idempotence of the request. Generate a unique value from your client for each request. ClientToken supports only ASCII characters.
        # 
        # > If you do not specify this parameter, the system uses the request ID as the client token. The request ID is different for each request.
        self.client_token = client_token
        # Specifies whether to perform a dry run. Valid values:
        # 
        # - **true**: Sends a check request without modifying the CIDR allocation. The system checks for required parameters, request format, and service limits. If the check fails, an error is returned. If the check passes, the DryRunOperation error code is returned.
        # 
        # - **false** (default): Sends a normal request. After the check passes, an HTTP 2xx status code is returned and the CIDR allocation is modified.
        self.dry_run = dry_run
        # The description of the CIDR allocation.
        # 
        # The description must be 1 to 256 characters long and must start with a letter or a Chinese character. It cannot start with `http://` or `https://`. If you do not specify this parameter, the description is empty.
        self.ipam_pool_allocation_description = ipam_pool_allocation_description
        # The ID of the CIDR allocation.
        # 
        # This parameter is required.
        self.ipam_pool_allocation_id = ipam_pool_allocation_id
        # The name of the CIDR allocation.
        # 
        # The name must be 1 to 128 characters long. It cannot start with `http://` or `https://`.
        self.ipam_pool_allocation_name = ipam_pool_allocation_name
        # The ID of the region where the CIDR allocation is located. To obtain a region ID, call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation.
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

