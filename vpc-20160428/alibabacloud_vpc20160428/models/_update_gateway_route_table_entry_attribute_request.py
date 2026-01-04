# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateGatewayRouteTableEntryAttributeRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        destination_cidr_block: str = None,
        dry_run: bool = None,
        gateway_route_table_id: str = None,
        ipv_4gateway_route_table_id: str = None,
        name: str = None,
        next_hop_id: str = None,
        next_hop_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # The description of the gateway route table.
        # 
        # The description must be 2 to 256 characters in length. The description must start with a letter but cannot start with `http://` or `https://`.
        self.description = description
        # The destination CIDR block of the route entry in the gateway route table.
        # 
        # This parameter is required.
        self.destination_cidr_block = destination_cidr_block
        # Specifies whether to precheck only this request. Valid values:
        # 
        # *   **true**: prechecks the request without modifying the gateway route table. The system checks the required parameters, request format, and service limits. If the request fails to pass the precheck, an error code is returned. If the request passes the precheck, the `DryRunOperation` error code is returned.
        # *   **false**: sends the request. This is the default value. If the request passes the precheck, a 2xx HTTP status code is returned and the gateway route table is modified.
        self.dry_run = dry_run
        # The ID of the gateway route table that you want to modify.
        self.gateway_route_table_id = gateway_route_table_id
        # The ID of the gateway route table that you want to modify.
        self.ipv_4gateway_route_table_id = ipv_4gateway_route_table_id
        # The name of the gateway route table.
        # 
        # The name must be 2 to 128 characters in length and can contain letter, digits, periods (.), underscores (_), and hyphens (-). The name must start with a letter.
        self.name = name
        # The new next hop ID of the route entry.
        # 
        # *   If you set **NextHopType** to **Instance**, specify an ECS instance ID for **NextHopId**.
        # *   If you set **NextHopType** to **NetworkInterface**, specify an ENI ID for **NextHopId**.
        # *   If you set **NextHopType** to **Local**, leave **NextHopId** empty. This indicates a local next hop.
        # 
        # >  If the value of NextHopType is **Instance** or **NetworkInterface**, and you want to modify the next hop, you must set **NextHopType** to **Local** first. Then, set **NextHopType** to **Instance** or **NetworkInterface** and specify **NextHopId** based on your requirements. If the next hop type of a route entry is Instance or NetworkInterface, you cannot directly specify a different ENI ID or ECS instance ID for the NextHopId parameter.
        self.next_hop_id = next_hop_id
        # The new next hop type of the route. Valid values:
        # 
        # *   **Instance**: Elastic Compute Service (ECS) instance
        # *   **NetworkInterface**: elastic network interface (ENI)
        # *   **Local**: local next hop
        # 
        # This parameter is required.
        self.next_hop_type = next_hop_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region to which the gateway route table that you want to modify belongs.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
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

        if self.description is not None:
            result['Description'] = self.description

        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.gateway_route_table_id is not None:
            result['GatewayRouteTableId'] = self.gateway_route_table_id

        if self.ipv_4gateway_route_table_id is not None:
            result['IPv4GatewayRouteTableId'] = self.ipv_4gateway_route_table_id

        if self.name is not None:
            result['Name'] = self.name

        if self.next_hop_id is not None:
            result['NextHopId'] = self.next_hop_id

        if self.next_hop_type is not None:
            result['NextHopType'] = self.next_hop_type

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

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('GatewayRouteTableId') is not None:
            self.gateway_route_table_id = m.get('GatewayRouteTableId')

        if m.get('IPv4GatewayRouteTableId') is not None:
            self.ipv_4gateway_route_table_id = m.get('IPv4GatewayRouteTableId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NextHopId') is not None:
            self.next_hop_id = m.get('NextHopId')

        if m.get('NextHopType') is not None:
            self.next_hop_type = m.get('NextHopType')

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

