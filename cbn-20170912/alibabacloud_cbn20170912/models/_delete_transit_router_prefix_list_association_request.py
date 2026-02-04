# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteTransitRouterPrefixListAssociationRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        next_hop: str = None,
        next_hop_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        prefix_list_id: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        transit_router_id: str = None,
        transit_router_table_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among all requests. The token can contain only ASCII characters.
        # 
        # >  If you do not set this parameter, **ClientToken** is set to the value of **RequestId**. The value of **RequestId** for each API request may be different.
        self.client_token = client_token
        # Specifies whether to perform a dry run. Valid values:
        # 
        # *   **true**: performs a dry run. The system checks the required parameters, request syntax, and limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and sends the task.
        self.dry_run = dry_run
        # The ID of the next hop.
        # 
        # > If **NextHopType** is set to **BlackHole**, you must set this parameter to **BlackHole**.
        # 
        # This parameter is required.
        self.next_hop = next_hop
        # The type of the next hop. Valid values:
        # 
        # *   **BlackHole**: All the CIDR blocks in the prefix list are blackhole routes. Packets destined for the CIDR blocks are dropped.
        # *   **VPC**: The next hop of the CIDR blocks in the prefix list is a VPC connection.
        # *   **VBR**: The next hop of the CIDR blocks in the prefix list is a VBR connection.
        # *   **TR**: The next hop of the CIDR blocks in the prefix list is an inter-region connection.
        self.next_hop_type = next_hop_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the prefix list.
        # 
        # This parameter is required.
        self.prefix_list_id = prefix_list_id
        # The ID of the region where the transit router is deployed.
        # 
        # You can call the [DescribeChildInstanceRegions](https://help.aliyun.com/document_detail/132080.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the transit router.
        # 
        # This parameter is required.
        self.transit_router_id = transit_router_id
        # The ID of the route table of the transit router.
        # 
        # This parameter is required.
        self.transit_router_table_id = transit_router_table_id

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

        if self.next_hop is not None:
            result['NextHop'] = self.next_hop

        if self.next_hop_type is not None:
            result['NextHopType'] = self.next_hop_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.prefix_list_id is not None:
            result['PrefixListId'] = self.prefix_list_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id

        if self.transit_router_table_id is not None:
            result['TransitRouterTableId'] = self.transit_router_table_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('NextHop') is not None:
            self.next_hop = m.get('NextHop')

        if m.get('NextHopType') is not None:
            self.next_hop_type = m.get('NextHopType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PrefixListId') is not None:
            self.prefix_list_id = m.get('PrefixListId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')

        if m.get('TransitRouterTableId') is not None:
            self.transit_router_table_id = m.get('TransitRouterTableId')

        return self

