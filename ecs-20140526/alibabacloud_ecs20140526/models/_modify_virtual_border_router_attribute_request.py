# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyVirtualBorderRouterAttributeRequest(DaraModel):
    def __init__(
        self,
        circuit_code: str = None,
        client_token: str = None,
        description: str = None,
        local_gateway_ip: str = None,
        name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        peer_gateway_ip: str = None,
        peering_subnet_mask: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        user_cidr: str = None,
        vbr_id: str = None,
        vlan_id: int = None,
    ):
        # The circuit code of the Express Connect circuit. The circuit code is provided by your connectivity provider.
        self.circuit_code = circuit_code
        # A client-generated token that ensures the request is idempotent. The token must be unique for each request, contain only ASCII characters, and not exceed 64 characters in length.
        self.client_token = client_token
        # The description of the VBR.
        # 
        # The description must be 2 to 256 characters long. It must start with a letter and cannot start with `http://` or `https://`.
        self.description = description
        # The local gateway IP address for the BGP session.
        self.local_gateway_ip = local_gateway_ip
        # The name of the VBR.
        # 
        # The name must be 2 to 128 characters long. It must start with a letter and can contain letters, digits, underscores (_), and hyphens (-).
        self.name = name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The peer gateway IP address for the BGP session.
        self.peer_gateway_ip = peer_gateway_ip
        # The subnet mask for the `LocalGatewayIp` and `PeerGatewayIp`.
        self.peering_subnet_mask = peering_subnet_mask
        # The ID of the region where the virtual border router (VBR) is deployed.
        # 
        # To get a list of the latest regions, call the `DescribeRegions` operation.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The CIDR block of the on-premises network that is connected to the VBR.
        self.user_cidr = user_cidr
        # The ID of the VBR to modify.
        # 
        # This parameter is required.
        self.vbr_id = vbr_id
        # The VLAN ID of the VBR. The VLAN ID must be unique on the physical connection.
        # 
        # Valid values: 0 to 4095.
        # 
        # A value of 0 indicates that the VBR does not use a VLAN.
        self.vlan_id = vlan_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.circuit_code is not None:
            result['CircuitCode'] = self.circuit_code

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.local_gateway_ip is not None:
            result['LocalGatewayIp'] = self.local_gateway_ip

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.peer_gateway_ip is not None:
            result['PeerGatewayIp'] = self.peer_gateway_ip

        if self.peering_subnet_mask is not None:
            result['PeeringSubnetMask'] = self.peering_subnet_mask

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.user_cidr is not None:
            result['UserCidr'] = self.user_cidr

        if self.vbr_id is not None:
            result['VbrId'] = self.vbr_id

        if self.vlan_id is not None:
            result['VlanId'] = self.vlan_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CircuitCode') is not None:
            self.circuit_code = m.get('CircuitCode')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('LocalGatewayIp') is not None:
            self.local_gateway_ip = m.get('LocalGatewayIp')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PeerGatewayIp') is not None:
            self.peer_gateway_ip = m.get('PeerGatewayIp')

        if m.get('PeeringSubnetMask') is not None:
            self.peering_subnet_mask = m.get('PeeringSubnetMask')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('UserCidr') is not None:
            self.user_cidr = m.get('UserCidr')

        if m.get('VbrId') is not None:
            self.vbr_id = m.get('VbrId')

        if m.get('VlanId') is not None:
            self.vlan_id = m.get('VlanId')

        return self

