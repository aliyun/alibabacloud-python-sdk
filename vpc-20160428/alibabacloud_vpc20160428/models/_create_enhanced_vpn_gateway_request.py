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
        # A client token used to ensure request idempotence.
        # 
        # You can generate this token from your client. Make sure that the token is unique for each request. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the request as the **ClientToken**. Each request may have a different **RequestId**.
        self.client_token = client_token
        # The ID of the second vSwitch to associate with the enhanced VPN gateway for high availability.
        # 
        # -
        # 
        # - For zone-level disaster recovery, the two vSwitches must be in different availability zones within the same VPC.
        # 
        # - In regions with only one availability zone, zone-level disaster recovery is not supported. To ensure high availability, specify two different vSwitches from that zone. You can also specify the same vSwitch for both the **VSwitchId** and **DisasterRecoveryVSwitchId** parameters.
        self.disaster_recovery_vswitch_id = disaster_recovery_vswitch_id
        # The type of the enhanced VPN gateway. Valid value:
        # 
        # - **Enhanced.SiteToSite**: an enhanced site-to-site VPN gateway that supports only the IPsec feature.
        # 
        # This parameter is required.
        self.gateway_type = gateway_type
        # The name of the enhanced VPN gateway. If you do not specify this parameter, the gateway ID is used as the name.
        # 
        # The name must be 2 to 100 characters long, start with a letter, and not start with http\\:// or https\\://. It can contain only letters, digits, underscores (_), hyphens (-), and periods (.).
        self.name = name
        # The network type of the VPN gateway. Valid value:
        # 
        # - **public** (default): a public VPN gateway.
        self.network_type = network_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where you want to create the enhanced VPN gateway.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to get the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which you want to assign the enhanced VPN gateway.
        # 
        # - You can call the [ListResourceGroups](https://help.aliyun.com/document_detail/158855.html) operation to query resource group IDs.
        # 
        # - If you do not specify this parameter, the enhanced VPN gateway is added to the Default Resource Group.
        # 
        # - Associated IPsec connections are automatically added to the same resource group as the enhanced VPN gateway. You cannot directly change the resource group of an IPsec connection. If you change the resource group of the gateway, the resource group of its associated IPsec connections is also updated.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the vSwitch to associate with the enhanced VPN gateway.
        # 
        # -
        self.v_switch_id = v_switch_id
        # The ID of the VPC where you want to create the enhanced VPN gateway.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id
        # The type of the enhanced VPN gateway. Valid value:
        # 
        # - **Normal** (default): standard type.
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

