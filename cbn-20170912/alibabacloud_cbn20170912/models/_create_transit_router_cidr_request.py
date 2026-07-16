# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTransitRouterCidrRequest(DaraModel):
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
        transit_router_id: str = None,
    ):
        # The CIDR block of the transit router.
        # 
        # This parameter is required.
        self.cidr = cidr
        # The client token that is used to ensure the idempotence of the request.
        # 
        # Generate a token on your client to make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID is different for each request.
        self.client_token = client_token
        # The description of the transit router CIDR block.
        # 
        # The description can be empty or 1 to 256 characters in length, and cannot start with http\\:// or https\\://.
        self.description = description
        # Specifies whether to perform a dry run. Valid values:
        # 
        # - **true**: performs a dry run. The system checks the required parameters, request format, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # 
        # - **false** (default): performs a dry run and sends the request. If the request passes the dry run, the transit router CIDR block is created.
        self.dry_run = dry_run
        # The name of the transit router CIDR block.
        # 
        # The name can be empty or 1 to 128 characters in length, and cannot start with http\\:// or https\\://.
        self.name = name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # Specifies whether to allow the system to automatically add a route that points to the transit router CIDR block to the route table of the transit router.
        # 
        # - **true** (default): Yes.
        # 
        #   After you create a VPN connection that uses a private VPN gateway and enable route learning for the connection, the system automatically adds a blackhole route to the route table of the associated transit router. The destination of this route is the transit router CIDR block. The transit router CIDR block is the CIDR block from which a gateway IP address is allocated to the IPsec connection. This blackhole route is advertised only to the route tables of virtual border routers (VBRs) that are connected to the transit router.
        # 
        #   A blackhole route whose destination CIDR block is the transit router CIDR block, which refers to the CIDR block from which gateway IP addresses are allocated to the IPsec-VPN connection. The blackhole route is advertised only to the route tables of virtual border routers (VBRs) connected to the transit router.
        # 
        # - **false**: No.
        self.publish_cidr_route = publish_cidr_route
        # The ID of the region where the transit router is deployed.
        # 
        # Call the [DescribeChildInstanceRegions](https://help.aliyun.com/document_detail/132080.html) operation to query region IDs.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the transit router.
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

        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')

        return self

