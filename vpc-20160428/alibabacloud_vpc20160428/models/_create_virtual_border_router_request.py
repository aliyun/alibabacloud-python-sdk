# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class CreateVirtualBorderRouterRequest(DaraModel):
    def __init__(
        self,
        bandwidth: int = None,
        circuit_code: str = None,
        client_token: str = None,
        description: str = None,
        enable_ipv_6: bool = None,
        local_gateway_ip: str = None,
        local_ipv_6gateway_ip: str = None,
        name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        peer_gateway_ip: str = None,
        peer_ipv_6gateway_ip: str = None,
        peering_ipv_6subnet_mask: str = None,
        peering_subnet_mask: str = None,
        physical_connection_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tags: List[main_models.CreateVirtualBorderRouterRequestTags] = None,
        vbr_owner_id: int = None,
        vlan_id: int = None,
    ):
        # The bandwidth of the VBR. Unit: Mbit/s.
        # 
        # *   When you create a VBR for a dedicated connection, valid values are **50**, **100**, **200**, **300**, **400**, **500**, **1000**, **2048**, **5120**, **8192**, **10240**, **20480**, **40960**, **50120**, **61440**, and **102400**.
        # *   You do not need to set this parameter when you create a VBR for a hosted connection. The bandwidth is already configured when the hosted connection is created.
        self.bandwidth = bandwidth
        # The circuit code of the Express Connect circuit. The circuit code is provided by the connectivity provider.
        # 
        # >  Only the owner of the Express Connect circuit can set this parameter.
        self.circuit_code = circuit_code
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must make sure that it is unique among different requests.
        # 
        # >  If you do not set this parameter, the system automatically sets **ClientToken** to the value of **RequestId**. The value of **RequestId** may be different for each API request.
        self.client_token = client_token
        # The description of the VBR.
        # 
        # The description must be 2 to 256 characters in length. The description must start with a letter but cannot start with `http://` or `https://`.
        self.description = description
        # Specifies whether to enable IPv6. Valid values:
        # 
        # *   **true**: enables IPv6.
        # *   **false** (default): disables IPv6.
        self.enable_ipv_6 = enable_ipv_6
        # The IP address of the VBR. Only the owner of the VBR can set or modify this parameter.
        # 
        # When you create a VBR for the owner of the Express Connect circuit, this parameter is required.
        self.local_gateway_ip = local_gateway_ip
        # The IPv6 address of the VBR. Only the owner of the VBR can set or modify this parameter.
        # 
        # When you create a VBR for the owner of the Express Connect circuit, this parameter is required.
        self.local_ipv_6gateway_ip = local_ipv_6gateway_ip
        # The name of the VBR.
        # 
        # The name must be 2 to 128 characters in length, and can contain letters, digits, underscores (_), and hyphens (-). The name must start with a letter.
        self.name = name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The IP address of the gateway device in the data center. Only the owner of the VBR can set or modify this parameter.
        # 
        # When you create a VBR for the owner of the Express Connect circuit, this parameter is required.
        self.peer_gateway_ip = peer_gateway_ip
        # The IPv6 address of the gateway device in the data center. Only the owner of the VBR can set or modify this parameter.
        # 
        # When you create a VBR for the owner of the Express Connect circuit, this parameter is required.
        self.peer_ipv_6gateway_ip = peer_ipv_6gateway_ip
        # The subnet mask of the IPv6 addresses of the VBR and the gateway device in the data center.
        # 
        # The two IPv6 addresses must fall within the same subnet.
        self.peering_ipv_6subnet_mask = peering_ipv_6subnet_mask
        # The subnet mask of the IP addresses of the VBR and the gateway device in the data center.
        # 
        # The two IP addresses must fall within the same subnet.
        self.peering_subnet_mask = peering_subnet_mask
        # The ID of the Express Connect circuit.
        # 
        # You can create a VBR for a dedicated connection or a hosted connection.
        # 
        # This parameter is required.
        self.physical_connection_id = physical_connection_id
        # The region ID of the Express Connect circuit.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID.
        # 
        # For more information about resource group, see [What is Resource Management?](https://help.aliyun.com/document_detail/94475.html)
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tags.
        self.tags = tags
        # The account ID of the VBR owner.
        # 
        # The default value is the ID of the current Alibaba Cloud account.
        self.vbr_owner_id = vbr_owner_id
        # The VLAN ID of the VBR. Valid values: **0 to 2999**.
        # 
        # >  Only the owner of the Express Connect circuit can set this parameter. The VLAN IDs of two VBRs of the same the Express Connect circuit must be different.
        # 
        # This parameter is required.
        self.vlan_id = vlan_id

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.circuit_code is not None:
            result['CircuitCode'] = self.circuit_code

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.enable_ipv_6 is not None:
            result['EnableIpv6'] = self.enable_ipv_6

        if self.local_gateway_ip is not None:
            result['LocalGatewayIp'] = self.local_gateway_ip

        if self.local_ipv_6gateway_ip is not None:
            result['LocalIpv6GatewayIp'] = self.local_ipv_6gateway_ip

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

        if self.physical_connection_id is not None:
            result['PhysicalConnectionId'] = self.physical_connection_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.vbr_owner_id is not None:
            result['VbrOwnerId'] = self.vbr_owner_id

        if self.vlan_id is not None:
            result['VlanId'] = self.vlan_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('CircuitCode') is not None:
            self.circuit_code = m.get('CircuitCode')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnableIpv6') is not None:
            self.enable_ipv_6 = m.get('EnableIpv6')

        if m.get('LocalGatewayIp') is not None:
            self.local_gateway_ip = m.get('LocalGatewayIp')

        if m.get('LocalIpv6GatewayIp') is not None:
            self.local_ipv_6gateway_ip = m.get('LocalIpv6GatewayIp')

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

        if m.get('PhysicalConnectionId') is not None:
            self.physical_connection_id = m.get('PhysicalConnectionId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.CreateVirtualBorderRouterRequestTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('VbrOwnerId') is not None:
            self.vbr_owner_id = m.get('VbrOwnerId')

        if m.get('VlanId') is not None:
            self.vlan_id = m.get('VlanId')

        return self

class CreateVirtualBorderRouterRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. You must enter at least one tag key. You can specify up to 20 tag keys. The tag key cannot be an empty string.
        # 
        # A tag key can be at most 128 characters in length. It cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
        self.key = key
        # The tag value. You can specify at most 20 tag values. The tag value can be an empty string.
        # 
        # The tag value can be up to 128 characters in length and cannot contain `http://` or `https://`. The tag value cannot start with `aliyun` or `acs:`.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

