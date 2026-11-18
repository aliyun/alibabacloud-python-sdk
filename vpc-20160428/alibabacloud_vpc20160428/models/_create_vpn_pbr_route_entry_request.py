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
        # You can use the client to generate the value, but you must ensure that it is unique among different requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** of each API request is unique.
        self.client_token = client_token
        # The description of the policy-based route.
        # 
        # The description must be 1 to 100 characters in length.
        self.description = description
        # Specifies whether to only precheck the request. Valid values:
        # - **true**: Prechecks the request without creating the route. The system checks whether the required parameters are specified, the request format, and the service limits. If the request fails the precheck, the corresponding error is returned. If the request passes the precheck, the `DryRunOperation` error code is returned.
        # - **false** (default): Sends the request. If the request passes the precheck, the HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The next hop of the policy-based route.
        # 
        # This parameter is required.
        self.next_hop = next_hop
        # The tunnel protocol. Set the value to **Ipsec** (IPsec tunnel protocol).
        self.overlay_mode = overlay_mode
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The policy priority of the policy-based route. Valid values: **1** to **100**. Default value: **10**.
        # 
        # A smaller value indicates a higher policy priority.
        self.priority = priority
        # Specifies whether to publish the policy-based route to the VPC. Valid values:
        # 
        # - **true**: Publishes the policy-based route to the VPC. The system publishes the route only to the system route table of the VPC, but not to custom route tables.
        # 
        #   If you want the custom route tables of the VPC to include this route, you must manually add it. For more information, see [CreateRouteEntry](https://help.aliyun.com/document_detail/448722.html).
        # 
        # - **false**: Does not publish the policy-based route to the route tables of the VPC.
        # 
        #   You must manually add a policy-based route whose next hop points to the VPN gateway in both the system route table and custom route tables of the VPC. Otherwise, the VPC cannot access resources in the CIDR block through the IPsec-VPN connection.
        # 
        # This parameter is required.
        self.publish_vpc = publish_vpc
        # The region ID of the VPN gateway. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query region IDs.
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
        # The ID of the VPN gateway.
        # 
        # This parameter is required.
        self.vpn_gateway_id = vpn_gateway_id
        # The weight of the policy-based route.
        # 
        # When you use the same VPN gateway instance to establish active/standby IPsec-VPN connections, you can specify the active/standby links by configuring the weight of the policy-based route. A policy-based route with a weight of 100 is the active link by default, and a policy-based route with a weight of 0 is the standby link by default.
        # 
        # You can configure health checks for the IPsec-VPN connections to automatically detect the connectivity of the links. If the active link fails, the system automatically switches traffic to the standby link to ensure high availability of the cloud access link. For more information, see [CreateVpnConnection](https://help.aliyun.com/document_detail/120391.html).
        # 
        # Valid values:
        # - **100**: The IPsec-VPN connection associated with the policy-based route is the active link.
        # - **0**: The IPsec-VPN connection associated with the policy-based route is the standby link.
        # 
        # > - When you specify the active/standby links, the source and destination CIDR blocks of the active/standby policy-based routes must be the same.
        # > - For VPN gateway instances that support dual-tunnel IPsec-VPN connections, you do not need to configure this parameter. A dual-tunnel IPsec-VPN connection contains two tunnels that automatically form active/standby links. You do not need to specify the active/standby links by configuring this parameter. If you configure this parameter, the parameter settings do not take effect.
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

