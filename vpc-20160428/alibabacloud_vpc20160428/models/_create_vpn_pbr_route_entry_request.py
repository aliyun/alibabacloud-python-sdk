# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateVpnPbrRouteEntryRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        dry_run: bool = None,
        next_hop: str = None,
        overlay_mode: str = None,
        owner_account: str = None,
        owner_id: int = None,
        priority: int = None,
        publish_vpc: bool = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        route_dest: str = None,
        route_source: str = None,
        vpn_gateway_id: str = None,
        weight: int = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate a token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID is different for each request.
        self.client_token = client_token
        # The description of the policy-based route.
        # 
        # The description must be 1 to 100 characters in length, and cannot start with http:// or https://.
        self.description = description
        self.dry_run = dry_run
        # The next hop of the policy-based route.
        # 
        # This parameter is required.
        self.next_hop = next_hop
        # The tunneling protocol. Set the value to **Ipsec**.
        self.overlay_mode = overlay_mode
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The priority of the policy-based route. Valid values: **1** to **100**. Default value: **10**.
        # 
        # A smaller value indicates a higher priority.
        self.priority = priority
        # Specifies whether to advertise the policy-based route to a virtual private cloud (VPC) route table. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # This parameter is required.
        self.publish_vpc = publish_vpc
        # The region ID of the VPN gateway. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The destination CIDR block of the policy-based route.
        # 
        # This parameter is required.
        self.route_dest = route_dest
        # The source CIDR block of the policy-based route.
        # 
        # This parameter is required.
        self.route_source = route_source
        # The VPN gateway ID.
        # 
        # This parameter is required.
        self.vpn_gateway_id = vpn_gateway_id
        # The weight of the policy-based route.
        # 
        # If you use the same VPN gateway to establish active/standby IPsec-VPN connections, you can configure route weights to specify which connection is active. A value of 100 specifies the active connection, whereas a value of 0 specifies the standby connection.
        # 
        # You can configure health checks to automatically check the connectivity of IPsec-VPN connections. If the active connection is down, the standby connection automatically takes over. For more information, see [CreateVpnConnection](https://help.aliyun.com/document_detail/120391.html).
        # 
        # *   **100**: The IPsec-VPN connection associated with the policy-based route serves as an active connection.
        # *   **0**: The IPsec-VPN connection associated with the policy-based route serves as a standby connection.
        # 
        # >  If you specify active/standby IPsec-VPN connections, the active policy-based route and the standby policy-based route must have the same source and destination CIDR blocks.
        # 
        # This parameter is required.
        self.weight = weight

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

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.next_hop is not None:
            result['NextHop'] = self.next_hop

        if self.overlay_mode is not None:
            result['OverlayMode'] = self.overlay_mode

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.publish_vpc is not None:
            result['PublishVpc'] = self.publish_vpc

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.route_dest is not None:
            result['RouteDest'] = self.route_dest

        if self.route_source is not None:
            result['RouteSource'] = self.route_source

        if self.vpn_gateway_id is not None:
            result['VpnGatewayId'] = self.vpn_gateway_id

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('NextHop') is not None:
            self.next_hop = m.get('NextHop')

        if m.get('OverlayMode') is not None:
            self.overlay_mode = m.get('OverlayMode')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('PublishVpc') is not None:
            self.publish_vpc = m.get('PublishVpc')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RouteDest') is not None:
            self.route_dest = m.get('RouteDest')

        if m.get('RouteSource') is not None:
            self.route_source = m.get('RouteSource')

        if m.get('VpnGatewayId') is not None:
            self.vpn_gateway_id = m.get('VpnGatewayId')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

