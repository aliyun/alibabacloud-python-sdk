# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alb20200616 import models as main_models
from darabonba.model import DaraModel

class CreateLoadBalancerRequest(DaraModel):
    def __init__(
        self,
        address_allocated_mode: str = None,
        address_ip_version: str = None,
        address_type: str = None,
        client_token: str = None,
        deletion_protection_enabled: bool = None,
        dry_run: bool = None,
        load_balancer_billing_config: main_models.CreateLoadBalancerRequestLoadBalancerBillingConfig = None,
        load_balancer_edition: str = None,
        load_balancer_name: str = None,
        modification_protection_config: main_models.CreateLoadBalancerRequestModificationProtectionConfig = None,
        resource_group_id: str = None,
        tag: List[main_models.CreateLoadBalancerRequestTag] = None,
        vpc_id: str = None,
        zone_mappings: List[main_models.CreateLoadBalancerRequestZoneMappings] = None,
    ):
        # The mode in which IP addresses are allocated to the ALB instance. Valid values:
        # 
        # *   **Fixed** (default): a fixed IP address is assigned to the ALB instance in each zone.
        # *   **Dynamic**: IP addresses are dynamically allocated to the ALB instance in each zone.
        # 
        # >  Starting from 00:00:00 on February 25, 2025 (UTC+8), when you call this operation to create an ALB instance, the instance is automatically the [upgraded version](https://help.aliyun.com/document_detail/2864070.html) regardless of the mode you specify. Upgraded ALB instances no longer differentiate between IP modes. Instead, they globally auto-scale IP addresses for providing load balancing services. The ALB instances you created before this date and time are not affected.
        self.address_allocated_mode = address_allocated_mode
        # The protocol version. Valid values:
        # 
        # *   **IPv4:** IPv4.
        # *   **DualStack:** dual stack.
        self.address_ip_version = address_ip_version
        # The type of the address of the ALB instance. Valid values:
        # 
        # *   **Internet:** The ALB instance uses a public IP address. The domain name of the ALB instance is resolved to the public IP address. In this case, the ALB instance can be accessed over the Internet.
        # *   **Intranet:** The ALB instance uses a private IP address. The domain name of the ALB instance is resolved to the private IP address. In this case, the ALB instance can be accessed over the VPC in which the ALB instance is deployed.
        # 
        # This parameter is required.
        self.address_type = address_type
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can only contain ASCII characters.
        # 
        # >  If you do not specify this parameter, the system uses the value of **RequestId** as the value of **ClientToken**. The value of the **RequestId** parameter may be different for each API request.
        self.client_token = client_token
        # Specifies whether to enable deletion protection. Default value: false. Valid values:
        # 
        # *   **true:** enables deletion protection.
        # *   **false:** disables deletion protection.
        self.deletion_protection_enabled = deletion_protection_enabled
        # Specifies whether to perform a dry run. Default value: false. Valid values:
        # 
        # *   **true:** performs a dry run. The system checks the required parameters, request format, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false:** performs a dry run and sends the request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The billing method of the ALB instance.
        # 
        # This parameter is required.
        self.load_balancer_billing_config = load_balancer_billing_config
        # The edition of the ALB instance. The features and billing rules vary based on the edition of the ALB instance. Valid values:
        # 
        # *   **Basic:** basic.
        # *   **Standard:** standard.
        # *   **StandardWithWaf:** WAF-enabled.
        # 
        # This parameter is required.
        self.load_balancer_edition = load_balancer_edition
        # The name of the ALB instance.
        # 
        # The name must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores (_), and hyphens (-). The name must start with a letter.
        self.load_balancer_name = load_balancer_name
        # The configuration read-only mode settings.
        self.modification_protection_config = modification_protection_config
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The tags.
        self.tag = tag
        # The ID of the virtual private cloud (VPC) in which you want to create the ALB instance.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id
        # The mappings between zones an vSwitches. You can specify at most 10 zones. If the selected region supports two or more zones, select at least two zones to ensure the high availability of your service.
        # 
        # This parameter is required.
        self.zone_mappings = zone_mappings

    def validate(self):
        if self.load_balancer_billing_config:
            self.load_balancer_billing_config.validate()
        if self.modification_protection_config:
            self.modification_protection_config.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()
        if self.zone_mappings:
            for v1 in self.zone_mappings:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_allocated_mode is not None:
            result['AddressAllocatedMode'] = self.address_allocated_mode

        if self.address_ip_version is not None:
            result['AddressIpVersion'] = self.address_ip_version

        if self.address_type is not None:
            result['AddressType'] = self.address_type

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.deletion_protection_enabled is not None:
            result['DeletionProtectionEnabled'] = self.deletion_protection_enabled

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.load_balancer_billing_config is not None:
            result['LoadBalancerBillingConfig'] = self.load_balancer_billing_config.to_map()

        if self.load_balancer_edition is not None:
            result['LoadBalancerEdition'] = self.load_balancer_edition

        if self.load_balancer_name is not None:
            result['LoadBalancerName'] = self.load_balancer_name

        if self.modification_protection_config is not None:
            result['ModificationProtectionConfig'] = self.modification_protection_config.to_map()

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        result['ZoneMappings'] = []
        if self.zone_mappings is not None:
            for k1 in self.zone_mappings:
                result['ZoneMappings'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressAllocatedMode') is not None:
            self.address_allocated_mode = m.get('AddressAllocatedMode')

        if m.get('AddressIpVersion') is not None:
            self.address_ip_version = m.get('AddressIpVersion')

        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DeletionProtectionEnabled') is not None:
            self.deletion_protection_enabled = m.get('DeletionProtectionEnabled')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('LoadBalancerBillingConfig') is not None:
            temp_model = main_models.CreateLoadBalancerRequestLoadBalancerBillingConfig()
            self.load_balancer_billing_config = temp_model.from_map(m.get('LoadBalancerBillingConfig'))

        if m.get('LoadBalancerEdition') is not None:
            self.load_balancer_edition = m.get('LoadBalancerEdition')

        if m.get('LoadBalancerName') is not None:
            self.load_balancer_name = m.get('LoadBalancerName')

        if m.get('ModificationProtectionConfig') is not None:
            temp_model = main_models.CreateLoadBalancerRequestModificationProtectionConfig()
            self.modification_protection_config = temp_model.from_map(m.get('ModificationProtectionConfig'))

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateLoadBalancerRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        self.zone_mappings = []
        if m.get('ZoneMappings') is not None:
            for k1 in m.get('ZoneMappings'):
                temp_model = main_models.CreateLoadBalancerRequestZoneMappings()
                self.zone_mappings.append(temp_model.from_map(k1))

        return self

class CreateLoadBalancerRequestZoneMappings(DaraModel):
    def __init__(
        self,
        allocation_id: str = None,
        eip_type: str = None,
        intranet_address: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        # The ID of the EIP to be associated with the Internet-facing ALB instance.
        self.allocation_id = allocation_id
        # The type of EIP. Valid values:
        # 
        # *   **Common**: an EIP.
        # *   **Anycast**: an Anycast EIP.
        # 
        # >  For more information about the regions in which ALB supports Anycast EIPs, see [Limits](https://help.aliyun.com/document_detail/460727.html).
        self.eip_type = eip_type
        # The private IPv4 address.
        self.intranet_address = intranet_address
        # The vSwitch in the zone. You can specify only one vSwitch (subnet) in each zone. You can specify at most 10 zones. If the region supports two or more zones, specify at least two zones.
        # 
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # The zone ID of the cluster. You can specify at most 10 zones. If the region supports two or more zones, specify at least two zones. You can call the [DescribeZones](https://help.aliyun.com/document_detail/36064.html) operation to query the most recent zone list.
        # 
        # This parameter is required.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocation_id is not None:
            result['AllocationId'] = self.allocation_id

        if self.eip_type is not None:
            result['EipType'] = self.eip_type

        if self.intranet_address is not None:
            result['IntranetAddress'] = self.intranet_address

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationId') is not None:
            self.allocation_id = m.get('AllocationId')

        if m.get('EipType') is not None:
            self.eip_type = m.get('EipType')

        if m.get('IntranetAddress') is not None:
            self.intranet_address = m.get('IntranetAddress')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class CreateLoadBalancerRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key can be up to 128 characters in length, and cannot start with acs: or aliyun. It cannot contain http:// or https://.
        self.key = key
        # The tag value can be up to 128 characters in length, and cannot start with acs: or aliyun. It cannot contain http:// or https://.
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

class CreateLoadBalancerRequestModificationProtectionConfig(DaraModel):
    def __init__(
        self,
        reason: str = None,
        status: str = None,
    ):
        # The reason for enabling the configuration read-only mode.
        # 
        # The reason must be 2 to 128 characters in length, can contain letters, digits, periods (.), underscores (_), and hyphens (-), and must start with a letter.
        # 
        # >  This parameter takes effect only when **Status** is set to **ConsoleProtection**.
        self.reason = reason
        # Specifies whether to enable the configuration read-only mode. Valid values:
        # 
        # *   **NonProtection**: Disables the configuration read-only mode. In this case, the value of the **Reason** parameter that you specify does not take effect. If you specify **Reason**, the value of the parameter is cleared.
        # *   **ConsoleProtection**: Enables the configuration read-only mode. In this case, the value of the **Reason** parameter that you specify takes effect.****
        # 
        # >  If the parameter is set to **ConsoleProtection**, the configuration read-only mode is enabled. You cannot modify the configurations of the ALB instance in the ALB console. However, you can call API operations to modify the configurations of the ALB instance.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.reason is not None:
            result['Reason'] = self.reason

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class CreateLoadBalancerRequestLoadBalancerBillingConfig(DaraModel):
    def __init__(
        self,
        bandwidth_package_id: str = None,
        pay_type: str = None,
    ):
        # The ID of the Internet Shared Bandwidth instance that is associated with the Internet-facing ALB instance.
        self.bandwidth_package_id = bandwidth_package_id
        # The billing method of the instance.
        # 
        # Set the value to **PostPay**, which specifies the pay-as-you-go billing method.
        # 
        # This parameter is required.
        self.pay_type = pay_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        return self

