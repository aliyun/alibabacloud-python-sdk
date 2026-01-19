# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class CreateInstanceRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        charge_type: str = None,
        duration: int = None,
        https_policy: str = None,
        instance_cidr: str = None,
        instance_name: str = None,
        instance_spec: str = None,
        instance_type: str = None,
        pricing_cycle: str = None,
        tag: List[main_models.CreateInstanceRequestTag] = None,
        token: str = None,
        user_vpc_id: str = None,
        zone_id: str = None,
        zone_vswitch_security_group: List[main_models.CreateInstanceRequestZoneVSwitchSecurityGroup] = None,
    ):
        # Whether to automatically pay when renewing. Value:
        # 
        # - True: Automatic payment. Please ensure that your account has sufficient balance.
        # - False: Console manual payment. The specific operation is to log in to the console, select Expenses in the upper right corner, enter the Expense Center, and find the target order in Order Management to make payment.
        # 
        # Default value: False.
        self.auto_pay = auto_pay
        # The billing method of the instance. Valid values: PostPaid (pay-as-you-go) and PrePaid (subscription).
        # 
        # This parameter is required.
        self.charge_type = charge_type
        # The subscription duration of the instance.
        # 
        # *   If PricingCycle is set to **Month**, set this parameter to an integer ranges from **1** to **9**.
        # *   If PricingCycle is set to **Year**, set this parameter to an integer ranges from **1** to **3**.
        # 
        # >  This parameter is valid and required only if the ChargeType parameter is set to **PrePaid**.
        self.duration = duration
        # The HTTPS policy.
        self.https_policy = https_policy
        # The CIDR block of the VPC integration instance.
        # 
        # *   192.168.0.0/16
        # *   172.16.0.0/12
        # 
        # **
        # 
        # **Warning** The VPC integration instance is connected to the specified CIDR block. Plan your CIDR block carefully to prevent overlaps with the private IP addresses of cloud services.
        # 
        # >  This parameter is in invitational preview and not available for public use.
        self.instance_cidr = instance_cidr
        # Instance Name
        # 
        # This parameter is required.
        self.instance_name = instance_name
        # Instance specifications
        # 
        # This parameter is required.
        self.instance_spec = instance_spec
        # The type of the dedicated instance. Valid values:
        # 
        # *   vpc_connect: a VPC integration instance
        # *   normal: a conventional dedicated instance
        # 
        # >  This parameter is in invitational preview and not available for public use.
        self.instance_type = instance_type
        # The unit of the subscription duration of the subscription instance. Valid values:
        # 
        # *   **year**
        # *   **month**
        # 
        # >  This parameter is required if the ChargeType parameter is set to Prepaid.
        self.pricing_cycle = pricing_cycle
        # The tags that you want to add to the instance.
        self.tag = tag
        # Passwords are used to prevent duplicate requests from being submitted, please do not reuse them.
        # 
        # This parameter is required.
        self.token = token
        # The ID of the user\\"s VPC to be connected by the VPC integration instance.
        # 
        # >  This parameter is in invitational preview and not available for public use.
        self.user_vpc_id = user_vpc_id
        # The zone in which you want to create the instance. This parameter is required for a conventional dedicated instance and optional for a virtual private cloud (VPC) integration instance.
        self.zone_id = zone_id
        # The network information when the instance is a VPC integration instance, such as the zone, vSwitch, and security group.
        # 
        # >  This parameter is in invitational preview and not available for public use.
        self.zone_vswitch_security_group = zone_vswitch_security_group

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()
        if self.zone_vswitch_security_group:
            for v1 in self.zone_vswitch_security_group:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.https_policy is not None:
            result['HttpsPolicy'] = self.https_policy

        if self.instance_cidr is not None:
            result['InstanceCidr'] = self.instance_cidr

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.token is not None:
            result['Token'] = self.token

        if self.user_vpc_id is not None:
            result['UserVpcId'] = self.user_vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        result['ZoneVSwitchSecurityGroup'] = []
        if self.zone_vswitch_security_group is not None:
            for k1 in self.zone_vswitch_security_group:
                result['ZoneVSwitchSecurityGroup'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('HttpsPolicy') is not None:
            self.https_policy = m.get('HttpsPolicy')

        if m.get('InstanceCidr') is not None:
            self.instance_cidr = m.get('InstanceCidr')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceSpec') is not None:
            self.instance_spec = m.get('InstanceSpec')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateInstanceRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('Token') is not None:
            self.token = m.get('Token')

        if m.get('UserVpcId') is not None:
            self.user_vpc_id = m.get('UserVpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        self.zone_vswitch_security_group = []
        if m.get('ZoneVSwitchSecurityGroup') is not None:
            for k1 in m.get('ZoneVSwitchSecurityGroup'):
                temp_model = main_models.CreateInstanceRequestZoneVSwitchSecurityGroup()
                self.zone_vswitch_security_group.append(temp_model.from_map(k1))

        return self

class CreateInstanceRequestZoneVSwitchSecurityGroup(DaraModel):
    def __init__(
        self,
        cidr_block: str = None,
        security_group_id: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        # The IPv4 CIDR block for the vSwitch.
        self.cidr_block = cidr_block
        # The ID of the security group. Services in the same security group can access each other.
        self.security_group_id = security_group_id
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class CreateInstanceRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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

