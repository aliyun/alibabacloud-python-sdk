# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateVpnRouteEntryRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        dry_run: bool = None,
        next_hop: str = None,
        overlay_mode: str = None,
        owner_account: str = None,
        owner_id: int = None,
        publish_vpc: bool = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        route_dest: str = None,
        vpn_gateway_id: str = None,
        weight: int = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** may be different for each API request.
        self.client_token = client_token
        # The description of the destination route.
        # 
        # The description must be **1** to **100** characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # Specifies whether to perform a dry run, without performing the actual request. Valid values:
        # - **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error code is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # - **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, an HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The next hop of the destination route.
        # 
        # This parameter is required.
        self.next_hop = next_hop
        # The tunneling protocol. Set the value to **Ipsec** (IPsec tunneling protocol).
        self.overlay_mode = overlay_mode
        self.owner_account = owner_account
        self.owner_id = owner_id
        # Specifies whether to publish the destination route to the VPC. Valid values:
        # 
        # - **true**: Publishes the destination route to the VPC. The system publishes the route only to the VPC system route table, not to VPC custom route tables.
        # 
        #   If you want the custom route table to contain this route, manually add the route. For more information, see [CreateRouteEntry](https://help.aliyun.com/document_detail/448722.html).
        # - **false**: Does not publish the destination route to the VPC.
        # 
        #   You must manually add a destination route with the next hop pointing to the VPN gateway instance in both the VPC system route table and custom route tables. Otherwise, the VPC cannot access resources in the destination CIDR block through the IPsec-VPN connection.
        # 
        # This parameter is required.
        self.publish_vpc = publish_vpc
        # The region ID of the VPN gateway instance.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The destination CIDR block of the destination route.
        # 
        # This parameter is required.
        self.route_dest = route_dest
        # The instance ID of the VPN gateway.
        # 
        # This parameter is required.
        self.vpn_gateway_id = vpn_gateway_id
        # The weight of the destination routing entry.
        # 
        # When you use the same VPN gateway instance to establish active/standby IPsec-VPN connections, you can specify the active and standby links by configuring the weight of the destination routing entry. A destination routing entry with a weight of 100 is the active link by default, and a destination routing entry with a weight of 0 is the standby link by default.
        # 
        # You can configure health checks for the IPsec-VPN connection to automatically detect the connectivity of the link. If the active link is unavailable, the system automatically switches traffic to the standby link, ensuring high availability of the cloud connection. For more information, see [CreateVpnConnection](https://help.aliyun.com/document_detail/120391.html).
        # 
        # - **100**: The IPsec-VPN connection associated with the destination route serves as the active link.
        # - **0**: The IPsec-VPN connection associated with the destination route serves as the standby link.
        # 
        # > - When you specify active and standby links, the active and standby destination routes must have the same destination CIDR block, different next hops, and different weights.
        # > - For VPN gateway instances that support dual-tunnel pattern IPsec-VPN connections, you do not need to configure this parameter. A dual-tunnel pattern IPsec-VPN connection contains two tunnels that automatically form active/standby links. You do not need to specify active/standby links by configuring this parameter. If you configure this parameter, the parameter settings do not take effect.
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

        if m.get('VpnGatewayId') is not None:
            self.vpn_gateway_id = m.get('VpnGatewayId')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

