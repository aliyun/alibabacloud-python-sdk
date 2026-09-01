# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AssociatePhysicalConnectionToVirtualBorderRouterRequest(DaraModel):
    def __init__(
        self,
        circuit_code: str = None,
        client_token: str = None,
        enable_ipv_6: str = None,
        local_gateway_ip: str = None,
        local_ipv_6gateway_ip: str = None,
        owner_account: str = None,
        owner_id: int = None,
        peer_gateway_ip: str = None,
        peer_ipv_6gateway_ip: str = None,
        peering_ipv_6subnet_mask: str = None,
        peering_subnet_mask: str = None,
        physical_connection_id: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        vbr_id: str = None,
        vlan_id: str = None,
    ):
        # The circuit code provided by the carrier for the Express Connect circuit. 
        # 
        # > Only the owner of the Express Connect circuit can specify this parameter.
        self.circuit_code = circuit_code
        # The client token that is used to ensure the idempotence of the request.
        # 
        # The client generates the value of this parameter. The value must be unique among different requests and cannot exceed 64 ASCII characters in length.
        # 
        # > If you do not specify this parameter, the system uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** may differ for each API request.
        self.client_token = client_token
        # Specifies whether to enable IPv6. Valid values:
        # 
        # - **true**: Enabled.
        # 
        # - **false** (default): Disabled.
        self.enable_ipv_6 = enable_ipv_6
        # The Alibaba Cloud-side IP address of the VBR instance. You must specify **LocalGatewayIp**, **PeerGatewayIp**, and **PeeringSubnetMask** together when you call this operation. The request fails if any of these parameters is missing.
        self.local_gateway_ip = local_gateway_ip
        # The Alibaba Cloud-side IPv6 address of the VBR instance.
        self.local_ipv_6gateway_ip = local_ipv_6gateway_ip
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The client-side IP address of the VBR instance.
        # 
        # Only the VBR owner can specify or modify this property. You must specify **LocalGatewayIp**, **PeerGatewayIp**, and **PeeringSubnetMask** together when you call this operation. The request fails if any of these parameters is missing.
        self.peer_gateway_ip = peer_gateway_ip
        # The client-side IPv6 address of the VBR instance.
        # 
        # - Only the VBR owner can specify or modify this property.
        # 
        # - This parameter is required when you create a VBR instance for the Express Connect circuit owner.
        self.peer_ipv_6gateway_ip = peer_ipv_6gateway_ip
        # The subnet mask for the Alibaba Cloud-side and client-side IPv6 addresses of the VBR instance.
        # 
        # The two IPv6 addresses must be in the same subnet.
        self.peering_ipv_6subnet_mask = peering_ipv_6subnet_mask
        # The subnet mask for the Alibaba Cloud-side and client-side IP addresses of the VBR instance.
        # 
        # The two IP addresses must be in the same subnet. You must specify **LocalGatewayIp**, **PeerGatewayIp**, and **PeeringSubnetMask** together when you call this operation. The request fails if any of these parameters is missing.
        self.peering_subnet_mask = peering_subnet_mask
        # The Express Connect circuit instance ID.
        # 
        # This parameter is required.
        self.physical_connection_id = physical_connection_id
        # The region ID of the Express Connect circuit.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/448570.html) operation to query region IDs.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The VBR instance ID.
        # 
        # This parameter is required.
        self.vbr_id = vbr_id
        # The VLAN ID of the VBR. Valid values: **0 to 2999**. 
        # 
        # > Only the owner of the Express Connect circuit can specify this parameter. Two VBRs on the same Express Connect circuit cannot have the same VLAN ID.
        # 
        # This parameter is required.
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

        if self.enable_ipv_6 is not None:
            result['EnableIpv6'] = self.enable_ipv_6

        if self.local_gateway_ip is not None:
            result['LocalGatewayIp'] = self.local_gateway_ip

        if self.local_ipv_6gateway_ip is not None:
            result['LocalIpv6GatewayIp'] = self.local_ipv_6gateway_ip

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.peer_gateway_ip is not None:
            result['PeerGatewayIp'] = self.peer_gateway_ip

        if self.peer_ipv_6gateway_ip is not None:
            result['PeerIpv6GatewayIp'] = self.peer_ipv_6gateway_ip

        if self.peering_ipv_6subnet_mask is not None:
            result['PeeringIpv6SubnetMask'] = self.peering_ipv_6subnet_mask

        if self.peering_subnet_mask is not None:
            result['PeeringSubnetMask'] = self.peering_subnet_mask

        if self.physical_connection_id is not None:
            result['PhysicalConnectionId'] = self.physical_connection_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

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

        if m.get('EnableIpv6') is not None:
            self.enable_ipv_6 = m.get('EnableIpv6')

        if m.get('LocalGatewayIp') is not None:
            self.local_gateway_ip = m.get('LocalGatewayIp')

        if m.get('LocalIpv6GatewayIp') is not None:
            self.local_ipv_6gateway_ip = m.get('LocalIpv6GatewayIp')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PeerGatewayIp') is not None:
            self.peer_gateway_ip = m.get('PeerGatewayIp')

        if m.get('PeerIpv6GatewayIp') is not None:
            self.peer_ipv_6gateway_ip = m.get('PeerIpv6GatewayIp')

        if m.get('PeeringIpv6SubnetMask') is not None:
            self.peering_ipv_6subnet_mask = m.get('PeeringIpv6SubnetMask')

        if m.get('PeeringSubnetMask') is not None:
            self.peering_subnet_mask = m.get('PeeringSubnetMask')

        if m.get('PhysicalConnectionId') is not None:
            self.physical_connection_id = m.get('PhysicalConnectionId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('VbrId') is not None:
            self.vbr_id = m.get('VbrId')

        if m.get('VlanId') is not None:
            self.vlan_id = m.get('VlanId')

        return self

