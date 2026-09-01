# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateEnhancedVpnGatewayRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        disaster_recovery_vswitch_id: str = None,
        gateway_type: str = None,
        name: str = None,
        network_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        vpn_type: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** may differ for each API request.
        self.client_token = client_token
        # The second vSwitch associated with the enhanced VPN VPC-connected instance.
        # 
        # - This parameter is required.
        # - You must specify two vSwitches in different zones under the VPC associated with the enhanced VPN VPC-connected instance to implement zone-level disaster recovery for IPsec-VPN connections.
        # - For regions that support only one zone, zone-level disaster recovery is not supported. Specify two different vSwitches in the same zone to achieve high availability for IPsec-VPN connections. You can also specify the same vSwitch.
        self.disaster_recovery_vswitch_id = disaster_recovery_vswitch_id
        # The type of the enhanced VPN gateway. Valid values:
        # - **Enhanced.SiteToSite**: enhanced site-to-cloud VPN that covers only IPsec functionality.
        # 
        # This parameter is required.
        self.gateway_type = gateway_type
        # The name of the enhanced VPN gateway. The default value is the ID of the enhanced VPN gateway.
        # 
        # The name must be 2 to 100 characters in length. It cannot start with http:// or https://. It must start with an uppercase or lowercase letter and can contain uppercase and lowercase letters, digits, underscores (_), hyphens (-), and periods (.). Other special characters are not supported.
        self.name = name
        # The network type of the VPN gateway. Valid values:
        # 
        # - **public** (default): public VPN gateway.
        self.network_type = network_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the enhanced VPN gateway.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the enhanced VPN gateway belongs.
        # 
        # - You can call the [ListResourceGroups](https://help.aliyun.com/document_detail/158855.html) operation to query resource group IDs.
        # - If you do not specify a resource group ID, the enhanced VPN gateway belongs to the default resource group after it is created.
        # - After the enhanced VPN gateway is created, if you create IPsec-VPN connections under the enhanced VPN gateway (IPsec-VPN connections bound to the enhanced VPN gateway), these resources belong to the same resource group as the enhanced VPN gateway and cannot be modified independently. If you change the resource group of the enhanced VPN gateway, the resource group of the preceding resources is also changed.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The vSwitch associated with the enhanced VPN gateway instance.
        # 
        # - You must specify a vSwitch and also specify the **DisasterRecoveryVSwitchId** parameter.
        self.v_switch_id = v_switch_id
        # The ID of the VPC to which the enhanced VPN gateway belongs.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id
        # The type of the enhanced VPN gateway. Valid values:
        # - **Normal** (default): standard.
        self.vpn_type = vpn_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.disaster_recovery_vswitch_id is not None:
            result['DisasterRecoveryVSwitchId'] = self.disaster_recovery_vswitch_id

        if self.gateway_type is not None:
            result['GatewayType'] = self.gateway_type

        if self.name is not None:
            result['Name'] = self.name

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpn_type is not None:
            result['VpnType'] = self.vpn_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DisasterRecoveryVSwitchId') is not None:
            self.disaster_recovery_vswitch_id = m.get('DisasterRecoveryVSwitchId')

        if m.get('GatewayType') is not None:
            self.gateway_type = m.get('GatewayType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpnType') is not None:
            self.vpn_type = m.get('VpnType')

        return self

