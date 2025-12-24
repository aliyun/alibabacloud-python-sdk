# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_slb20140515 import models as main_models
from darabonba.model import DaraModel

class CreateLoadBalancerRequest(DaraModel):
    def __init__(
        self,
        address: str = None,
        address_ipversion: str = None,
        address_type: str = None,
        auto_pay: bool = None,
        bandwidth: int = None,
        client_token: str = None,
        delete_protection: str = None,
        duration: int = None,
        instance_charge_type: str = None,
        internet_charge_type: str = None,
        load_balancer_name: str = None,
        load_balancer_spec: str = None,
        master_zone_id: str = None,
        modification_protection_reason: str = None,
        modification_protection_status: str = None,
        owner_account: str = None,
        owner_id: int = None,
        pay_type: str = None,
        pricing_cycle: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        slave_zone_id: str = None,
        tag: List[main_models.CreateLoadBalancerRequestTag] = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The private IP address of the CLB instance. The private IP address must belong to the destination CIDR block of the vSwitch.
        self.address = address
        # The IP version of the CLB instance. Valid values: **ipv4** and **ipv6**.
        self.address_ipversion = address_ipversion
        # The network type of the CLB instance. Valid values:
        # 
        # *   **internet**: After an Internet-facing CLB instance is created, the system allocates a public IP address to the instance. The CLB instance can forward requests over the Internet.
        # *   **intranet**: After an internal-facing CLB instance is created, the system allocates a private IP address to the CLB instance. The CLB instance can forward requests only within the VPC.
        self.address_type = address_type
        # Specifies whether to automatically pay the subscription fee of the Internet-facing CLB instance. Valid values:
        # 
        # *   **true**: yes. The CLB instance is created after you call the API operation.
        # *   **false** (default): After you call the operation, the order is created but the payment is not completed. You can view pending orders in the console. The CLB instance will not be created until you complete the payment.
        # 
        # >  This parameter takes effect only for subscription CLB instances created on the Alibaba Cloud China site.
        self.auto_pay = auto_pay
        # The maximum bandwidth of the listener. Unit: Mbit/s.
        # 
        # Valid values: **1** to **5120**. For a pay-by-bandwidth Internet-facing CLB instance, you can specify a maximum bandwidth for each listener. The sum of the maximum bandwidth of all listeners cannot exceed the maximum bandwidth of the CLB instance.
        self.bandwidth = bandwidth
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # >  If you do not specify this parameter, the system uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # Specifies whether to enable deletion protection for the CLB instance. Valid values:
        # 
        # *   **on**
        # *   **off**
        self.delete_protection = delete_protection
        # The subscription duration of the Internet-facing CLB instance. Valid values:
        # 
        # *   If **PricingCycle** is set to **month**, the valid values are **1 to 9**.
        # *   If **PricingCycle** is set to **year**, the valid values are **1 to 5**.
        # 
        # >  This parameter is supported only by subscription instances created on the Alibaba Cloud China site.
        self.duration = duration
        # The metering method of the CLB instance. Valid values:
        # 
        # *   **PayBySpec** (default)
        # *   **PayByCLCU**
        # 
        # >  This parameter is supported only by instances created on the Alibaba Cloud China site and only when **PayType** is set to **PayOnDemand**.
        self.instance_charge_type = instance_charge_type
        # The metering method of the Internet-facing CLB instance. Valid values:
        # 
        # *   **paybytraffic** (default): pay-by-data-transfer
        # 
        #     >  If you set InternetChargeType to **paybytraffic**, you do not need to configure the **Bandwidth** parameter. The value of **Bandwidth** does not take effect even if you specify one.
        # 
        # *   **paybybandwidth**: pay-by-bandwidth
        # 
        # >  If you set **PayType** to **PayOnDemand** and **InstanceChargeType** to **PayByCLCU**, the only valid value for InternetChargeType is **paybytraffic**.
        self.internet_charge_type = internet_charge_type
        # The CLB instance name.
        # 
        # The name must be 1 to 80 characters in length, and can contain digits, periods (.), underscores (_), and hyphens (-). It must start with a letter.
        # 
        # If you do not specify this parameter, the system automatically assigns a name to the CLB instance.
        self.load_balancer_name = load_balancer_name
        # The specification of the CLB instance. Valid values:
        # 
        # *   **slb.s1.small**
        # 
        # *   **slb.s2.small**
        # 
        # *   **slb.s2.medium**
        # 
        # *   **slb.s3.small**
        # 
        # *   **slb.s3.medium**
        # 
        # *   **slb.s3.large**
        # 
        #     
        #  >   If you do not specify this parameter, a shared-resource CLB instance is created. Shared-resource CLB instances are no longer available for purchase. Therefore, you must specify this parameter.
        # 
        # If **InstanceChargeType** is set to **PayByCLCU**, this parameter is invalid and you do not need to specify this parameter.
        self.load_balancer_spec = load_balancer_spec
        # The ID of the primary zone to which the CLB instance belongs.
        # 
        # You can call the [DescribeZone](https://help.aliyun.com/document_detail/2401683.html) operation to query the primary and secondary zones in the region where you want to create the CLB instance.
        self.master_zone_id = master_zone_id
        # The reason for enabling the configuration read-only mode. The reason must be 1 to 80 characters in length. It must start with a letter and can contain letters, digits, periods (.), underscores (_), and hyphens (-).
        # 
        # >  This parameter takes effect only when **ModificationProtectionStatus** is set to **ConsoleProtection**.
        self.modification_protection_reason = modification_protection_reason
        # Specifies whether to enable the configuration read-only mode. Valid values:
        # 
        # *   **NonProtection**: disables the configuration read-only mode. After you disable the configuration read-only mode, the value of **ModificationProtectionReason** is cleared.
        # *   **ConsoleProtection**: enables the configuration read-only mode.
        # 
        # >  If you set this parameter to **ConsoleProtection**, you cannot modify instance configurations in the CLB console. However, you can modify instance configurations by calling API operations.
        self.modification_protection_status = modification_protection_status
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The billing method of the CLB instance. Valid values:
        # 
        # **PayOnDemand**: pay-as-you-go.
        # 
        # >  The Alibaba Cloud International site supports only pay-as-you-go CLB instances.
        self.pay_type = pay_type
        # The billing cycle of the subscription Internet-facing CLB instance. Valid values:
        # 
        # *   **month**
        # *   **year**
        # 
        # >  This parameter is supported only by subscription instances created on the Alibaba Cloud China site.
        self.pricing_cycle = pricing_cycle
        # The region ID of the CLB instance.
        # 
        # You can call the [DescribeRegions](~~DescribeRegions~~) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the secondary zone to which the CLB instance belongs.
        # 
        # You can call the [DescribeZone](https://help.aliyun.com/document_detail/2401683.html) operation to query the primary and secondary zones in the region where you want to create the CLB instance.
        self.slave_zone_id = slave_zone_id
        # The tags.
        self.tag = tag
        # The ID of the vSwitch to which the CLB instance belongs.
        # 
        # If you want to deploy the CLB instance in a VPC, this parameter is required. If this parameter is specified, **AddessType** is set to **intranet** by default.
        self.v_switch_id = v_switch_id
        # The ID of the virtual private cloud (VPC) to which the CLB instance belongs.
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
        if self.address is not None:
            result['Address'] = self.address

        if self.address_ipversion is not None:
            result['AddressIPVersion'] = self.address_ipversion

        if self.address_type is not None:
            result['AddressType'] = self.address_type

        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.delete_protection is not None:
            result['DeleteProtection'] = self.delete_protection

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type

        if self.load_balancer_name is not None:
            result['LoadBalancerName'] = self.load_balancer_name

        if self.load_balancer_spec is not None:
            result['LoadBalancerSpec'] = self.load_balancer_spec

        if self.master_zone_id is not None:
            result['MasterZoneId'] = self.master_zone_id

        if self.modification_protection_reason is not None:
            result['ModificationProtectionReason'] = self.modification_protection_reason

        if self.modification_protection_status is not None:
            result['ModificationProtectionStatus'] = self.modification_protection_status

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.slave_zone_id is not None:
            result['SlaveZoneId'] = self.slave_zone_id

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
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('AddressIPVersion') is not None:
            self.address_ipversion = m.get('AddressIPVersion')

        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')

        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DeleteProtection') is not None:
            self.delete_protection = m.get('DeleteProtection')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')

        if m.get('LoadBalancerName') is not None:
            self.load_balancer_name = m.get('LoadBalancerName')

        if m.get('LoadBalancerSpec') is not None:
            self.load_balancer_spec = m.get('LoadBalancerSpec')

        if m.get('MasterZoneId') is not None:
            self.master_zone_id = m.get('MasterZoneId')

        if m.get('ModificationProtectionReason') is not None:
            self.modification_protection_reason = m.get('ModificationProtectionReason')

        if m.get('ModificationProtectionStatus') is not None:
            self.modification_protection_status = m.get('ModificationProtectionStatus')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SlaveZoneId') is not None:
            self.slave_zone_id = m.get('SlaveZoneId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateLoadBalancerRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class CreateLoadBalancerRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the bastion host. Valid values of N: **1 to 20**. The tag key cannot be an empty string.
        # 
        # The tag key can be at most 64 characters in length, and cannot contain `http://` or `https://`. It must not start with `aliyun` or `acs:`.
        self.key = key
        # The tag value. Valid values of N: **1 to 20**. The tag value can be an empty string.
        # 
        # The tag value can be up to 128 characters in length and cannot start with `acs:` or `aliyun`. The tag value cannot contain `http://` or `https://`.
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

