# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetNatIpAttributeRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        nat_ip_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Client Token, used to ensure the idempotence of requests. Generate a unique value for this parameter from your client, ensuring that it is unique across different requests. ClientToken only supports ASCII characters. If not specified, the system automatically uses the **RequestId** of the API request as the **ClientToken** identifier. The **RequestId** may differ for each API request.
        self.client_token = client_token
        # Indicates whether to perform a dry run of the request. Values:
        # - **true**: Sends a check request without querying NAT IP address information. The checks include whether the AccessKey is valid, the RAM user\\"s authorization status, and if all required parameters are filled out. If any check fails, the corresponding error is returned. If all checks pass, the `DryRunOperation` error code is returned.
        # - **false** (default): Sends a normal request. After passing the checks, it returns an HTTP 2xx status code and queries the NAT IP address information.
        self.dry_run = dry_run
        # The ID of the NAT IP address instance to be queried.
        # 
        # This parameter is required.
        self.nat_ip_id = nat_ip_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the NAT gateway instance to which the NAT IP address to be queried belongs. You can obtain the region ID by calling the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) interface.
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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.nat_ip_id is not None:
            result['NatIpId'] = self.nat_ip_id

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
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('NatIpId') is not None:
            self.nat_ip_id = m.get('NatIpId')

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

