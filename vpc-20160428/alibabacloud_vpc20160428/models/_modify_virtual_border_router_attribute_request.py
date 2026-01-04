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
        # The information about the Express Connect circuit associated with the VBR, including the following parameters:
        # 
        # *   **CircuitCode**: the circuit code provided by the connectivity provider for the Express Connect circuit.
        # *   **LocalGatewayIp**: the IP address of the gateway device on the Alibaba Cloud side.
        # *   **PeerGatewayIp**: the IP address of the gateway device on the customer side.
        # *   **PeeringSubnetMask**: the subnet mask for the IP addresses of gateway devices on the Alibaba Cloud side and the customer side.
        # *   **PhysicalConnectionId**: the ID of the Express Connect circuit.
        self.associated_physical_connections = associated_physical_connections
        # The bandwidth value. Unit: Mbit/s.
        self.bandwidth = bandwidth
        # The circuit code of the Express Connect circuit. The circuit code is provided by the connectivity provider.
        # 
        # >  Only the owner of the Express Connect circuit can set this property.
        self.circuit_code = circuit_code
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # The description of the VBR.
        # 
        # It must be 2 to 256 characters in length. It must start with a letter but cannot start with `http://` or `https://`.
        self.description = description
        # The maximum number of dropped packets that is allowed by the receiver when the initiator transmits packets. This value can be used to check whether a connection works as expected.
        # 
        # Valid values: **3 to 10**.
        self.detect_multiplier = detect_multiplier
        # Specifies whether to enable IPv6. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        self.enable_ipv_6 = enable_ipv_6
        # The IP address of the VBR.
        # 
        # Only the owner of the VBR can set or modify this parameter.
        self.local_gateway_ip = local_gateway_ip
        # The IPv6 address of the VBR.
        self.local_ipv_6gateway_ip = local_ipv_6gateway_ip
        # The time interval to receive BFD packets. Valid values: **200 to 1000**. Unit: milliseconds.
        self.min_rx_interval = min_rx_interval
        # The time interval to send BFD packets. Valid values: **200 to 1000**. Unit: milliseconds.
        self.min_tx_interval = min_tx_interval
        self.mtu = mtu
        # The name of the VBR.
        # 
        # The name must be 2 to 128 characters in length, and can contain letters, digits, underscores (_), and hyphens (-). The name must start with a letter. It cannot start with `http://` or `https://`.
        self.name = name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The IP address of the gateway device in the data center.
        # 
        # Only the owner of the VBR can set or modify this parameter.
        self.peer_gateway_ip = peer_gateway_ip
        # The IPv6 address of the gateway device in the data center.
        # 
        # *   Only the owner of the VBR can set or modify this property.
        # *   This property is required when you create a VBR for the owner of the Express Connect circuit. You can ignore this property when you create a VBR for another Alibaba Cloud account.
        self.peer_ipv_6gateway_ip = peer_ipv_6gateway_ip
        # The subnet mask of the IPv6 addresses of the VBR and the gateway device in the data center.
        # 
        # The two IPv6 addresses must fall within the same subnet.
        self.peering_ipv_6subnet_mask = peering_ipv_6subnet_mask
        # The subnet mask for the IP addresses of the gateway devices on the Alibaba Cloud side and on the customer side. Only the owner of the VBR can set or modify this parameter.
        # 
        # The two IP addresses must fall within the same subnet.
        self.peering_subnet_mask = peering_subnet_mask
        # The region ID of the VBR.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Indicates whether to allow service access between data centers. Valid values:
        # 
        # - **true**
        # - **false**
        self.sitelink_enable = sitelink_enable
        # The VBR ID.
        # 
        # This parameter is required.
        self.vbr_id = vbr_id
        # The VLAN ID of the VBR. Valid values: **0 to 2999**.
        # 
        # >  This parameter is available only to Express Connect owners. The VLAN IDs of VBRs on the same Express Connect circuit must be unique.
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

