# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteTransitRouterCidrRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        transit_router_cidr_id: str = None,
        transit_router_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # Generate a parameter value from your client to ensure uniqueness across different requests. ClientToken supports only ASCII characters.
        # 
        # > If you do not specify this parameter, the system uses the RequestId of the API request as the ClientToken. The RequestId may vary for each API request.
        self.client_token = client_token
        # Specifies whether to perform a dry run. Valid values:
        # 
        # - **true**: performs a dry run without deleting the transit router CIDR block. The system checks the required parameters, request format, and service limits. If the check fails, the corresponding error is returned. If the check succeeds, the error code `DryRunOperation` is returned.
        # - **false** (default): performs a dry run and then deletes the transit router CIDR block after the request passes the check.
        self.dry_run = dry_run
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the transit router instance.
        # 
        # You can call the [DescribeChildInstanceRegions](https://help.aliyun.com/document_detail/132080.html) operation to query region IDs.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the transit router CIDR block.
        # 
        # You can call the [ListTransitRouterCidr](https://help.aliyun.com/document_detail/462772.html) operation to query the ID of a transit router CIDR block.
        # 
        # This parameter is required.
        self.transit_router_cidr_id = transit_router_cidr_id
        # The transit router instance ID.
        # 
        # This parameter is required.
        self.transit_router_id = transit_router_id

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

        if self.transit_router_cidr_id is not None:
            result['TransitRouterCidrId'] = self.transit_router_cidr_id

        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

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

        if m.get('TransitRouterCidrId') is not None:
            self.transit_router_cidr_id = m.get('TransitRouterCidrId')

        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')

        return self

