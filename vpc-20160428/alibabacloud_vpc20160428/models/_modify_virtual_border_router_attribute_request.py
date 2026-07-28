# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyVirtualBorderRouterAttributeRequest(DaraModel):
    def __init__(
        self,
        associated_physical_connections: str = None,
        bandwidth: int = None,
        circuit_code: str = None,
        client_token: str = None,
        description: str = None,
        detect_multiplier: int = None,
        enable_ipv_6: bool = None,
        local_gateway_ip: str = None,
        local_ipv_6gateway_ip: str = None,
        min_rx_interval: int = None,
        min_tx_interval: int = None,
        mtu: int = None,
        name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        peer_gateway_ip: str = None,
        peer_ipv_6gateway_ip: str = None,
        peering_ipv_6subnet_mask: str = None,
        peering_subnet_mask: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sitelink_enable: bool = None,
        vbr_id: str = None,
        vlan_id: int = None,
    ):
        # The list of Express Connect circuits associated with the VBR, which contains the following parameters:
        # 
        # - **VlanId**: The VLAN ID of the VBR instance.
        # - **CircuitCode**: The circuit encoding provided by the carrier for the Express Connect circuit.
        # - **LocalGatewayIp**: The Alibaba Cloud-side IP address of the VBR instance.
        # - **PeerGatewayIp**: The client-side IP address of the VBR instance.
        # - **PeeringSubnetMask**: The subnet mask for the Alibaba Cloud-side and client-side IP addresses of the VBR instance.
        # - **LocalIpv6GatewayIp**: The Alibaba Cloud-side IPv6 address of the VBR instance.
        # - **PeerIpv6GatewayIp**: The client-side IPv6 address of the VBR instance.
        # - **PeeringIpv6SubnetMask**: The subnet mask for the Alibaba Cloud-side and client-side IPv6 addresses of the VBR instance.
        # - **ipv6Enable**: Enables IPv6.
        # - **PhysicalConnectionId**: The Express Connect circuit instance ID.
        self.associated_physical_connections = associated_physical_connections
        # The bandwidth value. Unit: Mbit/s.
        self.bandwidth = bandwidth
        # The circuit code provided by the carrier for the Express Connect circuit. 
        #           
        # > Only the owner of the Express Connect circuit can specify this parameter.
        self.circuit_code = circuit_code
        # The client token that is used to ensure the idempotence of the request.
        # 
        # Generate a parameter value from your client to ensure uniqueness across different requests. ClientToken supports only ASCII characters.
        # 
        # > If you do not specify this parameter, the system uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** may be different for each API request.
        self.client_token = client_token
        # The description of the VBR.
        # 
        # The description must be 2 to 256 characters in length and must start with a letter or Chinese character. It cannot start with `http://` or `https://`.
        self.description = description
        # The detection multiplier, which specifies the maximum number of consecutive packet losses allowed by the receiver from the sender. This parameter is used to detect whether the link is normal.
        # 
        # Valid values: **3 to 10**.
        self.detect_multiplier = detect_multiplier
        # Specifies whether to enable IPv6. Valid values:
        # 
        # - **true**: Enabled.
        # 
        # - **false** (default): Disabled.
        self.enable_ipv_6 = enable_ipv_6
        # The Alibaba Cloud-side IP address of the VBR instance.
        # 
        # This property can be specified or modified only by the VBR owner.
        self.local_gateway_ip = local_gateway_ip
        # The Alibaba Cloud-side IPv6 address of the VBR instance.
        self.local_ipv_6gateway_ip = local_ipv_6gateway_ip
        # The receive interval of BFD packets. Valid values: **200 to 1000**. Unit: ms.
        self.min_rx_interval = min_rx_interval
        # The alert interval for sending Bidirectional Forwarding Detection (BFD) packets. Valid values: **200 to 1000**. Unit: ms.
        self.min_tx_interval = min_tx_interval
        # The MTU value supported by the VBR. Valid values: 1500 and 8500.
        # This value can be set only when the VBR is attached to an Express Connect Router (ECR). This value also affects all other VBRs and VPCs within the same ECR.
        self.mtu = mtu
        # The name of the VBR.
        # 
        # The name must be 2 to 128 characters in length and must start with a letter or Chinese character. It can contain digits, underscores (_), and hyphens (-). It cannot start with `http://` or `https://`.
        self.name = name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The client-side IP address of the VBR instance.
        # 
        # This property can be specified or modified only by the VBR owner.
        self.peer_gateway_ip = peer_gateway_ip
        # The client-side IPv6 address of the VBR instance.
        # 
        # - This property can be specified or modified only by the VBR owner.
        # 
        # - This parameter is required when the Express Connect circuit owner creates a VBR instance. It is not required when creating a VBR instance for another account.
        self.peer_ipv_6gateway_ip = peer_ipv_6gateway_ip
        # The subnet mask for the Alibaba Cloud-side and client-side IPv6 addresses of the VBR instance.
        # 
        # The two IPv6 addresses must be in the same subnet.
        self.peering_ipv_6subnet_mask = peering_ipv_6subnet_mask
        # The subnet mask for the Alibaba Cloud-side and client-side IP addresses of the VBR instance. This property can be specified or modified only by the VBR owner.
        # 
        # The two IP addresses must be in the same subnet.
        self.peering_subnet_mask = peering_subnet_mask
        # The region ID of the VBR.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Specifies whether to allow inter-IDC service access. Valid values:
        # 
        # - true: Allowed.
        # 
        # - false (default): Not allowed.
        self.sitelink_enable = sitelink_enable
        # The VBR instance ID.
        # 
        # This parameter is required.
        self.vbr_id = vbr_id
        # The VLAN ID of the VBR. Valid values: **0 to 2999**. 
        # 
        # > Only the owner of the Express Connect circuit can specify this parameter. The VLAN IDs of two VBRs on the same Express Connect circuit must be different.
        self.vlan_id = vlan_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.associated_physical_connections is not None:
            result['AssociatedPhysicalConnections'] = self.associated_physical_connections

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.circuit_code is not None:
            result['CircuitCode'] = self.circuit_code

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.detect_multiplier is not None:
            result['DetectMultiplier'] = self.detect_multiplier

        if self.enable_ipv_6 is not None:
            result['EnableIpv6'] = self.enable_ipv_6

        if self.local_gateway_ip is not None:
            result['LocalGatewayIp'] = self.local_gateway_ip

        if self.local_ipv_6gateway_ip is not None:
            result['LocalIpv6GatewayIp'] = self.local_ipv_6gateway_ip

        if self.min_rx_interval is not None:
            result['MinRxInterval'] = self.min_rx_interval

        if self.min_tx_interval is not None:
            result['MinTxInterval'] = self.min_tx_interval

        if self.mtu is not None:
            result['Mtu'] = self.mtu

        if self.name is not None:
            result['Name'] = self.name

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

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.sitelink_enable is not None:
            result['SitelinkEnable'] = self.sitelink_enable

        if self.vbr_id is not None:
            result['VbrId'] = self.vbr_id

        if self.vlan_id is not None:
            result['VlanId'] = self.vlan_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociatedPhysicalConnections') is not None:
            self.associated_physical_connections = m.get('AssociatedPhysicalConnections')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('CircuitCode') is not None:
            self.circuit_code = m.get('CircuitCode')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DetectMultiplier') is not None:
            self.detect_multiplier = m.get('DetectMultiplier')

        if m.get('EnableIpv6') is not None:
            self.enable_ipv_6 = m.get('EnableIpv6')

        if m.get('LocalGatewayIp') is not None:
            self.local_gateway_ip = m.get('LocalGatewayIp')

        if m.get('LocalIpv6GatewayIp') is not None:
            self.local_ipv_6gateway_ip = m.get('LocalIpv6GatewayIp')

        if m.get('MinRxInterval') is not None:
            self.min_rx_interval = m.get('MinRxInterval')

        if m.get('MinTxInterval') is not None:
            self.min_tx_interval = m.get('MinTxInterval')

        if m.get('Mtu') is not None:
            self.mtu = m.get('Mtu')

        if m.get('Name') is not None:
            self.name = m.get('Name')

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

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SitelinkEnable') is not None:
            self.sitelink_enable = m.get('SitelinkEnable')

        if m.get('VbrId') is not None:
            self.vbr_id = m.get('VbrId')

        if m.get('VlanId') is not None:
            self.vlan_id = m.get('VlanId')

        return self

