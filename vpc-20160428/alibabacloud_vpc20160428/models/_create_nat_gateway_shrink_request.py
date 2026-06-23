# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class CreateNatGatewayShrinkRequest(DaraModel):
    def __init__(
        self,
        access_mode_shrink: str = None,
        auto_pay: bool = None,
        availability_mode: str = None,
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
        tag: List[main_models.CreateNatGatewayShrinkRequestTag] = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The access mode of the VPC NAT gateway for reverse endpoint access.
        self.access_mode_shrink = access_mode_shrink
        # Subscription-based public NAT gateways are no longer available for purchase. This parameter is deprecated.
        self.auto_pay = auto_pay
        self.availability_mode = availability_mode
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can create the token, but you must make sure that the token is unique among different requests.
        # 
        # > If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # The description of the NAT gateway.
        # 
        # The description must be 2 to 256 characters in length. It cannot start with `http://` or `https://`.
        self.description = description
        # Subscription-based public NAT gateways are no longer available for purchase. This parameter is deprecated.
        self.duration = duration
        # The mode in which the EIP is associated with the NAT gateway. Valid values:
        # 
        # - **MULTI_BINDED** (default): the multi-EIP-to-ENI mode.
        # 
        # - **NAT**: the EIP-to-NAT gateway mode. This mode is compatible with IPv4 gateways.
        # 
        #   > If the EIP is associated with the NAT gateway in EIP-to-NAT gateway mode, the EIP occupies a private IP address of the vSwitch to which the NAT gateway belongs. Make sure that the vSwitch has sufficient private IP addresses. Otherwise, the EIP fails to be associated. In EIP-to-NAT gateway mode, a NAT gateway can be associated with up to 50 EIPs.
        self.eip_bind_mode = eip_bind_mode
        # Specifies whether to enable ICMP reply. Valid values:
        # 
        # - **true** (default): enables ICMP reply.
        # 
        # - **false**: disables ICMP reply.
        self.icmp_reply_enabled = icmp_reply_enabled
        # The billing method of the NAT gateway. Set the value to:
        # 
        # **PostPaid** (default): pay-as-you-go.
        # 
        # For more information, see [Billing of public NAT gateways](https://help.aliyun.com/document_detail/48126.html) and [Billing of VPC NAT gateways](https://help.aliyun.com/document_detail/270913.html).
        self.instance_charge_type = instance_charge_type
        # The billing method of the NAT gateway. Set the value to **PayByLcu**, which indicates that the NAT gateway is a pay-as-you-go NAT gateway and is measured in LCUs.
        self.internet_charge_type = internet_charge_type
        # The IP address prefix. NAT IP addresses are created from the prefix. Use a reserved CIDR block that is not allocated in the vSwitch to which the NAT gateway belongs.
        self.ipv_4prefix = ipv_4prefix
        # The name of the NAT gateway.
        # 
        # Must be 2 to 128 characters in length, start with a letter or a Chinese character, and can contain digits, underscores (_), and hyphens (-).
        # 
        # If you do not specify this parameter, the system automatically specifies a name for the NAT gateway.
        self.name = name
        # The private IP address of the NAT gateway. Use an idle IP address from the CIDR block of the vSwitch to which the NAT gateway belongs. If this parameter is left empty, an IP address is randomly assigned.
        self.nat_ip = nat_ip
        # The type of NAT gateway. Set the value to **Enhanced**, which specifies an enhanced NAT gateway.
        self.nat_type = nat_type
        # The type of the NAT gateway to be created. Valid values:
        # 
        # - **internet**: a public NAT gateway
        # 
        # - **intranet**: a VPC NAT gateway
        self.network_type = network_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # Subscription-based public NAT gateways are no longer available for purchase. This parameter is no longer used.
        self.pricing_cycle = pricing_cycle
        # Specifies whether to enable PrivateLink. Valid values:
        # 
        # - true: enables PrivateLink.
        # 
        # - false (default): disables PrivateLink.
        self.private_link_enabled = private_link_enabled
        # The ID of the region in which to create the NAT gateway.
        # 
        # Call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to obtain the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Specifies whether to enable the firewall feature. Valid values:
        # 
        # - **false** (default): disables the firewall feature.
        # 
        #   >Notice: 
        # 
        #   This parameter is deprecated.
        self.security_protection_enabled = security_protection_enabled
        # Subscription-based public NAT gateways are no longer available for purchase. This parameter is deprecated.
        self.spec = spec
        # The tags.
        self.tag = tag
        # The ID of the vSwitch to which the NAT gateway belongs.
        # 
        # When you create a NAT gateway, you must specify a vSwitch to which the NAT gateway belongs. The system then assigns a private IP address to the NAT gateway from the vSwitch.
        # 
        # - To create a NAT gateway in an existing vSwitch, make sure that the zone to which the vSwitch belongs supports NAT gateways and that the vSwitch has idle IP addresses.
        # 
        # - If you have not created a vSwitch, create a vSwitch in a zone that supports NAT gateways and then specify the vSwitch.
        # 
        # > Call the [ListEnhancedNatGatewayAvailableZones](https://help.aliyun.com/document_detail/182292.html) operation to query available zones and [DescribeVSwitches](https://help.aliyun.com/document_detail/35748.html) to query the number of idle IP addresses in a vSwitch.
        self.v_switch_id = v_switch_id
        # The ID of the virtual private cloud (VPC) where you want to create the NAT gateway.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_mode_shrink is not None:
            result['AccessMode'] = self.access_mode_shrink

        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.availability_mode is not None:
            result['AvailabilityMode'] = self.availability_mode

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
            self.access_mode_shrink = m.get('AccessMode')

        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('AvailabilityMode') is not None:
            self.availability_mode = m.get('AvailabilityMode')

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
                temp_model = main_models.CreateNatGatewayShrinkRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class CreateNatGatewayShrinkRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. You can specify up to 20 tag keys. The tag key cannot be an empty string. The tag key must be 1 to 128 characters in length and cannot start with `aliyun` or `acs:`. The tag key cannot contain `http://` or `https://`.
        self.key = key
        # The tag value. You can specify up to 20 tag values. The tag value can be an empty string. The tag value must be 0 to 128 characters in length and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
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

