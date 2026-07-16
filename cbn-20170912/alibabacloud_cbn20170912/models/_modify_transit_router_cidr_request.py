# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyTransitRouterCidrRequest(DaraModel):
    def __init__(
        self,
        cidr: str = None,
        client_token: str = None,
        description: str = None,
        dry_run: bool = None,
        name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        publish_cidr_route: bool = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        transit_router_cidr_id: str = None,
        transit_router_id: str = None,
    ):
        # The new CIDR block.
        self.cidr = cidr
        # The client token that is used to ensure the idempotence of the request.
        # 
        # Generate a client token to make sure that the token is unique for each request. The token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID is different for each request.
        self.client_token = client_token
        # The new description of the CIDR block.
        # 
        # The description can be empty or 1 to 256 characters in length. It cannot start with http\\:// or https\\://.
        self.description = description
        # Specifies whether to perform a dry run. The valid values are:
        # 
        # - **true**: Sends a check request but does not modify the CIDR block. The system checks the required parameters, request format, and service limits. If the request fails the check, the corresponding error is returned. If the request passes the check, the `DryRunOperation` error code is returned.
        # 
        # - **false** (default): Sends a normal request. The CIDR block is modified after the request passes the check.
        self.dry_run = dry_run
        # The new name of the CIDR block.
        # 
        # The name can be empty or 1 to 128 characters in length. It cannot start with http\\:// or https\\://.
        self.name = name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # Specifies whether to automatically add a route that points to the CIDR block to the route table of the transit router.
        # 
        # - **true**: Yes.
        # 
        #   This blackhole route is advertised only to the route tables of virtual border routers (VBRs) that are attached to the transit router.
        # 
        # - **false**: No.
        self.publish_cidr_route = publish_cidr_route
        # The ID of the region where the Transit Router instance is deployed.
        # 
        # Call the [DescribeChildInstanceRegions](https://help.aliyun.com/document_detail/132080.html) operation to query region IDs.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the CIDR block.
        # 
        # Call the [ListTransitRouterCidr](https://help.aliyun.com/document_detail/462772.html) operation to query the ID of the CIDR block.
        # 
        # This parameter is required.
        self.transit_router_cidr_id = transit_router_cidr_id
        # The ID of the Transit Router instance.
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
        if self.cidr is not None:
            result['Cidr'] = self.cidr

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.publish_cidr_route is not None:
            result['PublishCidrRoute'] = self.publish_cidr_route

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
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PublishCidrRoute') is not None:
            self.publish_cidr_route = m.get('PublishCidrRoute')

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

