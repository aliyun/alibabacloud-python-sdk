# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RegisterTransitRouterMulticastGroupSourcesRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        group_ip_address: str = None,
        network_interface_ids: List[str] = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        transit_router_multicast_domain_id: str = None,
        vpc_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID is different for each request.
        self.client_token = client_token
        # Specifies whether to perform a dry run, without sending the actual request. Default values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error code is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The IP address of the multicast group to which the multicast source belongs. Valid values: **224.0.1.0** to **239.255.255.254**.
        # 
        # > 224.0.0.0 to 224.0.0.255 are reserved by the system and cannot be used by multicast groups.
        # 
        # If the multicast group does not exist in the multicast domain, the system automatically creates the multicast group in the multicast domain.
        # 
        # This parameter is required.
        self.group_ip_address = group_ip_address
        # The IDs of the ENIs.
        self.network_interface_ids = network_interface_ids
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the multicast domain to which the multicast source belongs.
        # 
        # This parameter is required.
        self.transit_router_multicast_domain_id = transit_router_multicast_domain_id
        # The ID of the VPC to which the ENI belongs.
        # 
        # *   If the ENI belongs to the current Alibaba Cloud account, ignore this parameter.
        # *   If the ENI belongs to a different Alibaba Cloud account, you must set this parameter.
        self.vpc_id = vpc_id

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

        if self.group_ip_address is not None:
            result['GroupIpAddress'] = self.group_ip_address

        if self.network_interface_ids is not None:
            result['NetworkInterfaceIds'] = self.network_interface_ids

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.transit_router_multicast_domain_id is not None:
            result['TransitRouterMulticastDomainId'] = self.transit_router_multicast_domain_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('GroupIpAddress') is not None:
            self.group_ip_address = m.get('GroupIpAddress')

        if m.get('NetworkInterfaceIds') is not None:
            self.network_interface_ids = m.get('NetworkInterfaceIds')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TransitRouterMulticastDomainId') is not None:
            self.transit_router_multicast_domain_id = m.get('TransitRouterMulticastDomainId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

