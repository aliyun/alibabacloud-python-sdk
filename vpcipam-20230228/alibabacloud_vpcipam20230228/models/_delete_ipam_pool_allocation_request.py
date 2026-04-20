# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteIpamPoolAllocationRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        ipam_pool_allocation_id: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # **Usage notes** If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the DryRunOperation error code is returned.
        # *   **false** (default): sends the API request. If the request passes the check, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The ID of the custom reserved CIDR block to be deleted.
        # 
        # This parameter is required.
        self.ipam_pool_allocation_id = ipam_pool_allocation_id
        # The region ID of the custom reserved CIDR block.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
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

        if self.ipam_pool_allocation_id is not None:
            result['IpamPoolAllocationId'] = self.ipam_pool_allocation_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('IpamPoolAllocationId') is not None:
            self.ipam_pool_allocation_id = m.get('IpamPoolAllocationId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

