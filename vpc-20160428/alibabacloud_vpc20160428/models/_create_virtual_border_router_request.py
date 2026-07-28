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
        # The bandwidth of the VBR instance. Unit: Mbit/s.
        # 
        # - When you create a VBR instance for a dedicated Express Connect circuit, valid values are **50**, **100**, **200**, **300**, **400**, **500**, **1000**, **2048**, **5120**, **8192**, **10240**, **20480**, **40960**, **50120**, **61440**, and **102400**.
        # - When you create a VBR instance for shared Express Connect circuits, you do not need to configure this parameter. The bandwidth of the VBR is the bandwidth of the shared Express Connect circuits that is specified in Settings when the shared Express Connect circuits are created.
        self.bandwidth = bandwidth
        # The circuit code provided by the carrier for the Express Connect circuit. 
        #           
        # > Only the owner of the Express Connect circuit can specify this parameter.
        self.circuit_code = circuit_code
        # The client token that is used to ensure the idempotence of the request.
        # 
        # The client generates the value of this parameter. Make sure that the value is unique among different requests.
        # 
        # > If you do not specify this parameter, the system uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** may vary for each API request.
        self.client_token = client_token
        # The description of the VBR instance.  
        # 
        # The description must be 2 to 256 characters in length and must start with a letter or a Chinese character. It cannot start with `http://` or `https://`.
        self.description = description
        # Specifies whether to enable IPv6. Valid values:
        # 
        # - **true**: Enabled.
        # 
        # - **false** (default): Disabled.
        self.enable_ipv_6 = enable_ipv_6
        # The Alibaba Cloud-side IP address of the VBR instance. Only the VBR owner can specify or modify this property.
        # 
        # This parameter is required when you create a VBR instance for the owner of the Express Connect circuit.
        self.local_gateway_ip = local_gateway_ip
        # The Alibaba Cloud-side IPv6 address of the VBR instance. Only the VBR owner can specify or modify this property.
        # 
        # This parameter is required when you create a VBR instance for the owner of the Express Connect circuit.
        self.local_ipv_6gateway_ip = local_ipv_6gateway_ip
        # The name of the VBR instance.
        # 
        # The name must be 2 to 128 characters in length and must start with a letter or a Chinese character. It can contain digits, underscores (_), and hyphens (-). It cannot start with `http://` or `https://`.
        self.name = name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The customer-side IP address of the VBR instance. Only the VBR owner can specify or modify this property.
        # 
        # This parameter is required when you create a VBR instance for the owner of the Express Connect circuit.
        self.peer_gateway_ip = peer_gateway_ip
        # The customer-side IPv6 address of the VBR instance. Only the VBR owner can specify or modify this property.
        # 
        # This parameter is required when you create a VBR instance for the owner of the Express Connect circuit.
        self.peer_ipv_6gateway_ip = peer_ipv_6gateway_ip
        # The subnet mask for the Alibaba Cloud-side and customer-side IPv6 addresses of the VBR instance. 
        # 
        # The two IPv6 addresses must be in the same subnet.
        self.peering_ipv_6subnet_mask = peering_ipv_6subnet_mask
        # The subnet mask for the Alibaba Cloud-side and customer-side IP addresses of the VBR instance. 
        # 
        # The two IP addresses must be in the same subnet.
        self.peering_subnet_mask = peering_subnet_mask
        # The instance ID of the Express Connect circuit. 
        # 
        # You can create a VBR instance for a dedicated Express Connect circuit or for shared Express Connect circuits.
        # 
        # This parameter is required.
        self.physical_connection_id = physical_connection_id
        # The region ID of the Express Connect circuit.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID.
        # 
        # For more information about resource groups, see [What is a resource group?](https://help.aliyun.com/document_detail/2381067.html).
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tags of the resource.
        self.tags = tags
        # The account ID of the VBR instance owner.
        # 
        # The default value is the Alibaba Cloud account ID used for logon.
        self.vbr_owner_id = vbr_owner_id
        # The VLAN ID of the VBR instance. Valid values: **0 to 2999**. 
        # 
        # > Only the owner of the Express Connect circuit can specify this parameter. The VLAN IDs of two VBR instances on the same Express Connect circuit must be different.
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
        # The tag key of the resource. You must specify at least 1 tag key and can specify at most 20 tag keys. The tag key cannot be an empty string.
        # 
        # A tag key can be up to 128 characters in length. It cannot start with `aliyun` or `acs:` and cannot contain `http://` or `https://`.
        self.key = key
        # The tag value of the resource. You can specify at most 20 tag values. The tag value can be an empty string.
        # 
        # The tag value can be up to 128 characters in length. It cannot start with `aliyun` or `acs:` and cannot contain `http://` or `https://`.
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

