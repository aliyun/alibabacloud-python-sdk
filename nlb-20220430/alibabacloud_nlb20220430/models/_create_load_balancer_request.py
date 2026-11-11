# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nlb20220430 import models as main_models
from darabonba.model import DaraModel

class CreateLoadBalancerRequest(DaraModel):
    def __init__(
        self,
        address_ip_version: str = None,
        address_type: str = None,
        bandwidth_package_id: str = None,
        client_token: str = None,
        deletion_protection_config: main_models.CreateLoadBalancerRequestDeletionProtectionConfig = None,
        dry_run: bool = None,
        load_balancer_billing_config: main_models.CreateLoadBalancerRequestLoadBalancerBillingConfig = None,
        load_balancer_name: str = None,
        load_balancer_type: str = None,
        modification_protection_config: main_models.CreateLoadBalancerRequestModificationProtectionConfig = None,
        region_id: str = None,
        resource_group_id: str = None,
        tag: List[main_models.CreateLoadBalancerRequestTag] = None,
        vpc_id: str = None,
        zone_mappings: List[main_models.CreateLoadBalancerRequestZoneMappings] = None,
    ):
        # The IP version. Valid values:
        # 
        # - **ipv4** (default): IPv4.
        # - **DualStack**: dual-stack.
        self.address_ip_version = address_ip_version
        # The IPv4 address type of the Network Load Balancing (NLB) instance. Valid values:
        # 
        # - **Internet**: The load balancing instance has a public IP address. The DNS domain name is resolved to the public IP address, so it can be accessed over the Internet.
        # - **Intranet**: The load balancing instance has only a private IP address. The DNS domain name is resolved to the private IP address, so it can be accessed only over the internal network of the VPC where the load balancing instance is deployed.
        # 
        # > To enable IPv6 access over the Internet for a dual-stack Network Load Balancing (NLB) instance, invoke the [EnableLoadBalancerIpv6Internet](https://help.aliyun.com/document_detail/445878.html) operation.
        # 
        # This parameter is required.
        self.address_type = address_type
        # The ID of the Internet Shared Bandwidth instance that is associated with the Internet-facing instance.
        self.bandwidth_package_id = bandwidth_package_id
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that it is unique among different requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** of each API request is unique.
        self.client_token = client_token
        # The deletion protection configuration.
        self.deletion_protection_config = deletion_protection_config
        # Specifies whether to only precheck the request. Valid values:
        # - **true**: prechecks the request without creating the instance. The system checks whether required parameters are specified, the request format is valid, and service limits are met. If the request fails the precheck, the corresponding error is returned. If the request passes the precheck, the `DryRunOperation` error code is returned.
        # - **false** (default): sends the request. If the request passes the precheck, an HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The billing configuration of the Network Load Balancing (NLB) instance.
        self.load_balancer_billing_config = load_balancer_billing_config
        # The name of the Network Load Balancing (NLB) instance.
        # 
        # The name must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores (_), and hyphens (-). It must start with a letter.
        self.load_balancer_name = load_balancer_name
        # The type of load balancing. Valid value: **network**, which indicates Network Load Balancing (NLB).
        self.load_balancer_type = load_balancer_type
        # The modification protection configuration.
        self.modification_protection_config = modification_protection_config
        # The region ID of the Network Load Balancing (NLB) instance. 
        # 
        # You can invoke the [DescribeRegions](https://help.aliyun.com/document_detail/443657.html) operation to query region IDs.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The list of tags.
        self.tag = tag
        # The ID of the virtual private cloud (VPC) where the Network Load Balancing (NLB) instance is deployed.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id
        # The zone and vSwitch mappings. You can add up to 10 zones. If the current region supports two or more zones, you must add at least two zones.
        # 
        # This parameter is required.
        self.zone_mappings = zone_mappings

    def validate(self):
        if self.deletion_protection_config:
            self.deletion_protection_config.validate()
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
        if self.address_ip_version is not None:
            result['AddressIpVersion'] = self.address_ip_version

        if self.address_type is not None:
            result['AddressType'] = self.address_type

        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.deletion_protection_config is not None:
            result['DeletionProtectionConfig'] = self.deletion_protection_config.to_map()

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.load_balancer_billing_config is not None:
            result['LoadBalancerBillingConfig'] = self.load_balancer_billing_config.to_map()

        if self.load_balancer_name is not None:
            result['LoadBalancerName'] = self.load_balancer_name

        if self.load_balancer_type is not None:
            result['LoadBalancerType'] = self.load_balancer_type

        if self.modification_protection_config is not None:
            result['ModificationProtectionConfig'] = self.modification_protection_config.to_map()

        if self.region_id is not None:
            result['RegionId'] = self.region_id

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
        if m.get('AddressIpVersion') is not None:
            self.address_ip_version = m.get('AddressIpVersion')

        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')

        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DeletionProtectionConfig') is not None:
            temp_model = main_models.CreateLoadBalancerRequestDeletionProtectionConfig()
            self.deletion_protection_config = temp_model.from_map(m.get('DeletionProtectionConfig'))

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('LoadBalancerBillingConfig') is not None:
            temp_model = main_models.CreateLoadBalancerRequestLoadBalancerBillingConfig()
            self.load_balancer_billing_config = temp_model.from_map(m.get('LoadBalancerBillingConfig'))

        if m.get('LoadBalancerName') is not None:
            self.load_balancer_name = m.get('LoadBalancerName')

        if m.get('LoadBalancerType') is not None:
            self.load_balancer_type = m.get('LoadBalancerType')

        if m.get('ModificationProtectionConfig') is not None:
            temp_model = main_models.CreateLoadBalancerRequestModificationProtectionConfig()
            self.modification_protection_config = temp_model.from_map(m.get('ModificationProtectionConfig'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

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
        ipv_4local_addresses: List[str] = None,
        ipv_6address: str = None,
        ipv_6local_addresses: List[str] = None,
        private_ipv_4address: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        # The EIP instance ID associated with the Internet-facing instance. Each zone corresponds to one EIP instance ID. You can add up to 10 zones. If the current region supports two or more zones, you must add at least two zones.
        self.allocation_id = allocation_id
        # The list of IPv4 local addresses. These are the addresses used by the NLB to interact with backend services.
        # The number of addresses must be an even number, with a minimum of 2 and a maximum of 8.
        self.ipv_4local_addresses = ipv_4local_addresses
        # The IPv6 VIP. This is the IPv6 address used by the NLB to provide services.
        self.ipv_6address = ipv_6address
        # The list of IPv6 local addresses. These are the addresses used by the NLB to interact with backend services.
        # The number of addresses must be an even number, with a minimum of 2 and a maximum of 8.
        self.ipv_6local_addresses = ipv_6local_addresses
        # The private IPv4 virtual IP address (VIP). This is the private IPv4 address used by the NLB to provide services.
        self.private_ipv_4address = private_ipv_4address
        # The vSwitch that corresponds to the zone. You can use only one vSwitch and one subnet in each zone. You can add up to 10 zones.
        # If the current region supports two or more zones, you must add at least two zones.
        # 
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # The ID of the zone where the Network Load Balancing (NLB) instance is deployed. You can add up to 10 zones. If the current region supports two or more zones, you must add at least two zones.
        # 
        # You can invoke the [DescribeZones](https://help.aliyun.com/document_detail/443890.html) operation to query zone IDs.
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

        if self.ipv_4local_addresses is not None:
            result['Ipv4LocalAddresses'] = self.ipv_4local_addresses

        if self.ipv_6address is not None:
            result['Ipv6Address'] = self.ipv_6address

        if self.ipv_6local_addresses is not None:
            result['Ipv6LocalAddresses'] = self.ipv_6local_addresses

        if self.private_ipv_4address is not None:
            result['PrivateIPv4Address'] = self.private_ipv_4address

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationId') is not None:
            self.allocation_id = m.get('AllocationId')

        if m.get('Ipv4LocalAddresses') is not None:
            self.ipv_4local_addresses = m.get('Ipv4LocalAddresses')

        if m.get('Ipv6Address') is not None:
            self.ipv_6address = m.get('Ipv6Address')

        if m.get('Ipv6LocalAddresses') is not None:
            self.ipv_6local_addresses = m.get('Ipv6LocalAddresses')

        if m.get('PrivateIPv4Address') is not None:
            self.private_ipv_4address = m.get('PrivateIPv4Address')

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
        # The tag key. The key can be up to 64 characters in length, and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`. The key can contain letters, digits, underscores (_), periods (.), colons (:), forward slashes (/), equal signs (=), plus signs (+), hyphens (-), and at signs (@).
        # 
        # You can add up to 20 tags in a single call.
        self.key = key
        # The tag value. The value can be up to 128 characters in length, and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`. The value can contain letters, digits, underscores (_), periods (.), colons (:), forward slashes (/), equal signs (=), plus signs (+), hyphens (-), and at signs (@).
        # 
        # You can add up to 20 tags in a single call.
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
        # The reason for enabling modification protection. The reason must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores (_), and hyphens (-). It must start with a letter.
        # 
        # > This parameter is valid and takes effect only when **Status** is set to **ConsoleProtection**.
        self.reason = reason
        # The modification protection status of the Network Load Balancing (NLB). Valid values:
        # 
        # - **NonProtection**: modification protection is disabled. You cannot specify the **Reason** parameter. If you specify the **Reason** parameter, the configuration is cleared.
        # - **ConsoleProtection**: console modification protection is enabled. You can specify the **Reason** parameter.
        # 
        # > If you set the value to **ConsoleProtection**, modification protection is enabled. You cannot modify the instance configurations in the load balancing console, but you can invoke API operations to modify the instance configurations.
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
        pay_type: str = None,
    ):
        # The billing method of the Network Load Balancing (NLB) instance.
        # 
        # Valid value: **PostPay**, which indicates the pay-as-you-go billing method.
        self.pay_type = pay_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        return self

class CreateLoadBalancerRequestDeletionProtectionConfig(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        reason: str = None,
    ):
        # The deletion protection status. Valid values:
        # 
        # - **true**: enabled.
        # - **false** (default): disabled.
        self.enabled = enabled
        # The reason for changing the deletion protection status. The reason must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores (_), and hyphens (-). It must start with a letter.
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.reason is not None:
            result['Reason'] = self.reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        return self

