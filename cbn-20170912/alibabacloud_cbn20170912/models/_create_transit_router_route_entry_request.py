# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTransitRouterRouteEntryRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        transit_router_route_entry_description: str = None,
        transit_router_route_entry_destination_cidr_block: str = None,
        transit_router_route_entry_name: str = None,
        transit_router_route_entry_next_hop_id: str = None,
        transit_router_route_entry_next_hop_type: str = None,
        transit_router_route_table_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** is different for each request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **false** (default): performs a dry run and performs the actual request.
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        self.dry_run = dry_run
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The description of the route.
        # 
        # The description must be 1 to 256 characters in length, and cannot start with http:// or https://. You can also leave this parameter empty.
        self.transit_router_route_entry_description = transit_router_route_entry_description
        # The destination CIDR block of the route entry. IPv4 and IPv6 addresses are supported.
        # 
        # This parameter is required.
        self.transit_router_route_entry_destination_cidr_block = transit_router_route_entry_destination_cidr_block
        # The name of the route.
        # 
        # The name must be 1 to 128 characters in length, and cannot start with http:// or https://. You can also leave this parameter empty.
        self.transit_router_route_entry_name = transit_router_route_entry_name
        # The ID of the network instance connection that you want to specify as the next hop.
        self.transit_router_route_entry_next_hop_id = transit_router_route_entry_next_hop_id
        # The type of the next hop. Valid values:
        # 
        # *   **BlackHole**: routes network traffic to a black hole. All packets that match this route are dropped. If you select this option, you do not need to specify the next hop information.
        # *   **Attachment**: routes network traffic to a network instance connection. If you select this option, you must specify the ID of the network instance connection. All packets that match this route are routed to the specified network instance connection.
        # 
        # This parameter is required.
        self.transit_router_route_entry_next_hop_type = transit_router_route_entry_next_hop_type
        # The ID of the route table of the Enterprise Edition transit router.
        # 
        # This parameter is required.
        self.transit_router_route_table_id = transit_router_route_table_id

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

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.transit_router_route_entry_description is not None:
            result['TransitRouterRouteEntryDescription'] = self.transit_router_route_entry_description

        if self.transit_router_route_entry_destination_cidr_block is not None:
            result['TransitRouterRouteEntryDestinationCidrBlock'] = self.transit_router_route_entry_destination_cidr_block

        if self.transit_router_route_entry_name is not None:
            result['TransitRouterRouteEntryName'] = self.transit_router_route_entry_name

        if self.transit_router_route_entry_next_hop_id is not None:
            result['TransitRouterRouteEntryNextHopId'] = self.transit_router_route_entry_next_hop_id

        if self.transit_router_route_entry_next_hop_type is not None:
            result['TransitRouterRouteEntryNextHopType'] = self.transit_router_route_entry_next_hop_type

        if self.transit_router_route_table_id is not None:
            result['TransitRouterRouteTableId'] = self.transit_router_route_table_id

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

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TransitRouterRouteEntryDescription') is not None:
            self.transit_router_route_entry_description = m.get('TransitRouterRouteEntryDescription')

        if m.get('TransitRouterRouteEntryDestinationCidrBlock') is not None:
            self.transit_router_route_entry_destination_cidr_block = m.get('TransitRouterRouteEntryDestinationCidrBlock')

        if m.get('TransitRouterRouteEntryName') is not None:
            self.transit_router_route_entry_name = m.get('TransitRouterRouteEntryName')

        if m.get('TransitRouterRouteEntryNextHopId') is not None:
            self.transit_router_route_entry_next_hop_id = m.get('TransitRouterRouteEntryNextHopId')

        if m.get('TransitRouterRouteEntryNextHopType') is not None:
            self.transit_router_route_entry_next_hop_type = m.get('TransitRouterRouteEntryNextHopType')

        if m.get('TransitRouterRouteTableId') is not None:
            self.transit_router_route_table_id = m.get('TransitRouterRouteTableId')

        return self

