# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateVcoRouteEntryRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        dry_run: bool = None,
        next_hop: str = None,
        overlay_mode: str = None,
        owner_account: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        route_dest: str = None,
        vpn_connection_id: str = None,
        weight: int = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** may be different for each API request.
        self.client_token = client_token
        # The description of the destination route entry.
        self.description = description
        # Specifies whether to perform a dry run. Valid values:
        # - **true**: performs a dry run. The system checks the required parameters, request syntax, and business restrictions. If the check fails, the corresponding error is returned. If the check succeeds, the error code `DryRunOperation` is returned.
        # - **false** (default): performs a dry run and sends the request. If the check succeeds, an HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The next hop of the destination route entry.
        # 
        # This parameter is required.
        self.next_hop = next_hop
        # The tunneling protocol. Set the value to **Ipsec** (default), which specifies the IPsec tunneling protocol.
        self.overlay_mode = overlay_mode
        self.owner_account = owner_account
        # The region ID of the IPsec-VPN connection.
        # 
        # You can call [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) to query the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The destination CIDR block of the destination route entry.
        # 
        # This parameter is required.
        self.route_dest = route_dest
        # The ID of the IPsec-VPN connection.
        # 
        # This parameter is required.
        self.vpn_connection_id = vpn_connection_id
        # The weight of the destination route entry. Valid values:
        # 
        # - **0**: low priority.
        # - **100**: high priority.
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

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.route_dest is not None:
            result['RouteDest'] = self.route_dest

        if self.vpn_connection_id is not None:
            result['VpnConnectionId'] = self.vpn_connection_id

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

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RouteDest') is not None:
            self.route_dest = m.get('RouteDest')

        if m.get('VpnConnectionId') is not None:
            self.vpn_connection_id = m.get('VpnConnectionId')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

