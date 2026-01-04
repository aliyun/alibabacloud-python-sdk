# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class CreateNatGatewayRequest(DaraModel):
    def __init__(
        self,
        access_mode: main_models.CreateNatGatewayRequestAccessMode = None,
        auto_pay: bool = None,
        client_token: str = None,
        description: str = None,
        duration: str = None,
        eip_bind_mode: str = None,
        icmp_reply_enabled: bool = None,
        instance_charge_type: str = None,
        internet_charge_type: str = None,
        ipv_4prefix: str = None,
        name: str = None,
        nat_ip: str = None,
        nat_type: str = None,
        network_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        pricing_cycle: str = None,
        private_link_enabled: bool = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_protection_enabled: bool = None,
        spec: str = None,
        tag: List[main_models.CreateNatGatewayRequestTag] = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The access mode for reverse access to the VPC NAT gateway.
        self.access_mode = access_mode
        # Subscription Internet NAT gateways are no longer available for purchase. Ignore this parameter.
        self.auto_pay = auto_pay
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # The description of the NAT gateway.
        # 
        # You can leave this parameter empty or enter a description. If you enter a description, the description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # Subscription Internet NAT gateways are no longer available for purchase. Ignore this parameter.
        self.duration = duration
        # The mode in which the EIP is associated with the NAT gateway. Valid values:
        # 
        # - **MULTI_BINDED**(default): the multi-EIP-to-ENI mode.
        # 
        # - **NAT**: NAT mode, which is compatible with IPv4 addresses.
        # 
        # > If an EIP is associated with a NAT gateway in NAT mode, the EIP occupies a private IP address of the vSwitch where the NAT gateway is deployed. Make sure that the vSwitch has sufficient private IP addresses. Otherwise, EIPs cannot be associated with the NAT gateway. In NAT mode, a maximum number of 50 EIPs can be associated with each NAT gateway.
        self.eip_bind_mode = eip_bind_mode
        # Specifies whether to enable ICMP retrieval. Valid values:
        # 
        # *   **true** (default)
        # *   **false**
        self.icmp_reply_enabled = icmp_reply_enabled
        # The billing method of the NAT gateway.
        # 
        # Set the value to **PostPaid** (pay-as-you-go), which is the default value.
        # 
        # For more information, see [Internet NAT gateway billing](https://help.aliyun.com/document_detail/48126.html) and [VPC NAT gateway billing](https://help.aliyun.com/document_detail/270913.html).
        self.instance_charge_type = instance_charge_type
        # The metering method of the NAT gateway. Set the value to **PayByLcu**, which specifies the pay-by-CU metering method.
        self.internet_charge_type = internet_charge_type
        self.ipv_4prefix = ipv_4prefix
        # The name of the NAT gateway.
        # 
        # The name must be 2 to 128 characters in length and can contain letters, digits, underscores (_), and hyphens (-). The name must start with a letter.
        # 
        # If this parameter is not set, the system assigns a default name to the NAT gateway.
        self.name = name
        self.nat_ip = nat_ip
        # The type of NAT gateway. Set the value to **Enhanced**, which specifies enhanced NAT gateway.
        self.nat_type = nat_type
        # The network type of the NAT gateway. Valid values:
        # 
        # *   **internet**: Internet
        # *   **intranet**: VPC
        self.network_type = network_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # Subscription Internet NAT gateways are no longer available for purchase. Ignore this parameter.
        self.pricing_cycle = pricing_cycle
        # PrivateLink is not supported by default. If you set the value to true, PrivateLink is supported.
        self.private_link_enabled = private_link_enabled
        # The region ID of the NAT gateway.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to obtain the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Specifies whether to enable the firewall feature. Valid values:
        # 
        # *   **false** (default)>Notice: This parameter is deprecated.
        self.security_protection_enabled = security_protection_enabled
        # Subscription Internet NAT gateways are no longer available for purchase. Ignore this parameter.
        self.spec = spec
        # The tags.
        self.tag = tag
        # The ID of the vSwitch to which the NAT gateway is attached.
        # 
        # When you create a NAT gateway, you must specify a vSwitch for the NAT gateway. Then, the system assigns an idle private IP address from the vSwitch to the NAT gateway.
        # 
        # *   To attach the NAT gateway to an existing vSwitch, make sure that the zone to which the vSwitch belongs supports NAT gateways. In addition, the vSwitch must have idle IP addresses.
        # *   If no vSwitch exists in the VPC, create a vSwitch in a zone that supports NAT gateways. Then, specify the vSwitch for the NAT gateway.
        # 
        # >  You can call the [ListEnhanhcedNatGatewayAvailableZones](https://help.aliyun.com/document_detail/182292.html) operation to query zones that support NAT gateways. You can call the [DescribeVSwitches](https://help.aliyun.com/document_detail/35748.html) operation to query idle IP addresses in a vSwitch.
        self.v_switch_id = v_switch_id
        # The ID of the VPC where you want to create the NAT gateway.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id

    def validate(self):
        if self.access_mode:
            self.access_mode.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_mode is not None:
            result['AccessMode'] = self.access_mode.to_map()

        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.eip_bind_mode is not None:
            result['EipBindMode'] = self.eip_bind_mode

        if self.icmp_reply_enabled is not None:
            result['IcmpReplyEnabled'] = self.icmp_reply_enabled

        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type

        if self.ipv_4prefix is not None:
            result['Ipv4Prefix'] = self.ipv_4prefix

        if self.name is not None:
            result['Name'] = self.name

        if self.nat_ip is not None:
            result['NatIp'] = self.nat_ip

        if self.nat_type is not None:
            result['NatType'] = self.nat_type

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle

        if self.private_link_enabled is not None:
            result['PrivateLinkEnabled'] = self.private_link_enabled

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.security_protection_enabled is not None:
            result['SecurityProtectionEnabled'] = self.security_protection_enabled

        if self.spec is not None:
            result['Spec'] = self.spec

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessMode') is not None:
            temp_model = main_models.CreateNatGatewayRequestAccessMode()
            self.access_mode = temp_model.from_map(m.get('AccessMode'))

        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('EipBindMode') is not None:
            self.eip_bind_mode = m.get('EipBindMode')

        if m.get('IcmpReplyEnabled') is not None:
            self.icmp_reply_enabled = m.get('IcmpReplyEnabled')

        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')

        if m.get('Ipv4Prefix') is not None:
            self.ipv_4prefix = m.get('Ipv4Prefix')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NatIp') is not None:
            self.nat_ip = m.get('NatIp')

        if m.get('NatType') is not None:
            self.nat_type = m.get('NatType')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')

        if m.get('PrivateLinkEnabled') is not None:
            self.private_link_enabled = m.get('PrivateLinkEnabled')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecurityProtectionEnabled') is not None:
            self.security_protection_enabled = m.get('SecurityProtectionEnabled')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateNatGatewayRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class CreateNatGatewayRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. The format of Tag.N.Key when you call the operation. Valid values of N: 1 to 20. The tag key cannot be an empty string. The tag key can be up to 128 characters in length and cannot contain http:// or https://. The tag key cannot start with acs: or aliyun.
        self.key = key
        # The tag value. The format of Tag.N.Value when you call the operation. Valid values of N: 1 to 20. The tag key cannot be an empty string. The tag key can be up to 128 characters in length and cannot contain http:// or https://. The tag key cannot start with acs: or aliyun.
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

class CreateNatGatewayRequestAccessMode(DaraModel):
    def __init__(
        self,
        mode_value: str = None,
        tunnel_type: str = None,
    ):
        # Access mode. Valid values:
        # 
        # - **route**: route mode
        # 
        # - **tunnel**: tunnel mode
        # 
        # > If this parameter is specified, you must set **PrivateLinkEnabled** to **true**.
        self.mode_value = mode_value
        # Tunnel mode type:
        # 
        # - **geneve**: Geneve type
        # 
        # > This value takes effect if the access mode is the tunnel mode.
        self.tunnel_type = tunnel_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mode_value is not None:
            result['ModeValue'] = self.mode_value

        if self.tunnel_type is not None:
            result['TunnelType'] = self.tunnel_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModeValue') is not None:
            self.mode_value = m.get('ModeValue')

        if m.get('TunnelType') is not None:
            self.tunnel_type = m.get('TunnelType')

        return self

