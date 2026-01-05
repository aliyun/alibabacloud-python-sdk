# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alb20200616 import models as main_models
from darabonba.model import DaraModel

class GetLoadBalancerAttributeResponseBody(DaraModel):
    def __init__(
        self,
        access_log_config: main_models.GetLoadBalancerAttributeResponseBodyAccessLogConfig = None,
        address_allocated_mode: str = None,
        address_ip_version: str = None,
        address_type: str = None,
        bandwidth_package_id: str = None,
        create_time: str = None,
        dnsname: str = None,
        deletion_protection_config: main_models.GetLoadBalancerAttributeResponseBodyDeletionProtectionConfig = None,
        ipv_6address_type: str = None,
        load_balancer_billing_config: main_models.GetLoadBalancerAttributeResponseBodyLoadBalancerBillingConfig = None,
        load_balancer_bussiness_status: str = None,
        load_balancer_edition: str = None,
        load_balancer_id: str = None,
        load_balancer_name: str = None,
        load_balancer_operation_locks: List[main_models.GetLoadBalancerAttributeResponseBodyLoadBalancerOperationLocks] = None,
        load_balancer_status: str = None,
        modification_protection_config: main_models.GetLoadBalancerAttributeResponseBodyModificationProtectionConfig = None,
        region_id: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        security_group_ids: List[str] = None,
        tags: List[main_models.GetLoadBalancerAttributeResponseBodyTags] = None,
        vpc_id: str = None,
        zone_mappings: List[main_models.GetLoadBalancerAttributeResponseBodyZoneMappings] = None,
    ):
        # The configuration of the access log feature.
        self.access_log_config = access_log_config
        # The mode in which IP addresses are allocated. Valid values:
        # 
        # *   **Fixed**: allocates a static IP address to the ALB instance.
        # *   **Dynamic**: dynamically allocates an IP address to each zone of the ALB instance.
        self.address_allocated_mode = address_allocated_mode
        # The IP version. Valid values:
        # 
        # *   **IPv4**
        # *   **DualStack**
        self.address_ip_version = address_ip_version
        # The network type of the ALB instance. Valid values:
        # 
        # *   **Internet**: The ALB instance uses a public IP address. The domain name of the ALB instance is resolved to the public IP address. Therefore, the ALB instance can be accessed over the Internet.
        # *   **Intranet**: The ALB instance uses a private IP address. The domain name of the ALB instance is resolved to the private IP address. In this case, the ALB instance can be accessed over the virtual private cloud (VPC) where the ALB instance is deployed.
        self.address_type = address_type
        # The ID of the elastic IP address (EIP) bandwidth plan that is associated with the Internet-facing ALB instance.
        self.bandwidth_package_id = bandwidth_package_id
        # The time when the resource was created. The time follows the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time is displayed in UTC.
        self.create_time = create_time
        # The domain name of the ALB instance.
        self.dnsname = dnsname
        # The configuration of deletion protection.
        self.deletion_protection_config = deletion_protection_config
        # The type of IPv6 address that is used by the ALB instance. Valid values:
        # 
        # *   **Internet**: The ALB instance uses a public IP address. The domain name of the ALB instance is resolved to the public IP address. Therefore, the ALB instance can be accessed over the Internet.
        # *   **Intranet**: The ALB instance uses a private IP address. The domain name of the ALB instance is resolved to the private IP address. Therefore, the ALB instance can be accessed over the VPC in which the ALB instance is deployed.
        self.ipv_6address_type = ipv_6address_type
        # The billing method of the ALB instance.
        self.load_balancer_billing_config = load_balancer_billing_config
        # The service status of the ALB instance. Valid values:
        # 
        # *   **Abnormal**
        # *   **Normal**
        self.load_balancer_bussiness_status = load_balancer_bussiness_status
        # The edition of the ALB instance. The features and billing rules vary based on the edition of the ALB instance. Valid values:
        # 
        # *   **Basic**
        # *   **Standard**
        # *   **StandardWithWaf**
        self.load_balancer_edition = load_balancer_edition
        # The ALB instance ID.
        self.load_balancer_id = load_balancer_id
        # The name of the ALB instance.
        # 
        # The name must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores (_), and hyphens (-). The name must start with a letter.
        self.load_balancer_name = load_balancer_name
        # The type of the lock. Valid values:
        # 
        # *   **SecurityLocked**: The ALB instance is locked due to security reasons.
        # *   **RelatedResourceLocked**: The ALB instance is locked due to association issues.
        # *   **FinancialLocked**: The ALB instance is locked due to overdue payments.
        # *   **ResidualLocked**: The ALB instance is locked because the associated resources have overdue payments and the resources are released.
        self.load_balancer_operation_locks = load_balancer_operation_locks
        # The status of the ALB instance. Valid values:
        # 
        # *   **Inactive**: The ALB instance is disabled. ALB instances in the Inactive state do not forward traffic.
        # *   **Active**: The ALB instance is running.
        # *   **Provisioning**: The ALB instance is being created.
        # *   **Configuring**: The ALB instance is being modified.
        # *   **CreateFailed**: The system failed to create the ALB instance. In this case, you are not charged for the ALB instance. You can only delete the ALB instance.
        self.load_balancer_status = load_balancer_status
        # The configuration read-only mode settings.
        self.modification_protection_config = modification_protection_config
        # The region ID of the ALB instance.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The IDs of the security groups to which the ALB instance is added.
        self.security_group_ids = security_group_ids
        # The tag value.
        # 
        # The tag value can be up to 128 characters in length and cannot start with `acs:` or `aliyun`. The tag value cannot contain `http://` or `https://`.
        self.tags = tags
        # The ID of the VPC in which the ALB instance is deployed.
        self.vpc_id = vpc_id
        # The mappings between zones and vSwitches. At most 10 zones are returned. If the current region supports two or more zones, at least two zones are returned.
        self.zone_mappings = zone_mappings

    def validate(self):
        if self.access_log_config:
            self.access_log_config.validate()
        if self.deletion_protection_config:
            self.deletion_protection_config.validate()
        if self.load_balancer_billing_config:
            self.load_balancer_billing_config.validate()
        if self.load_balancer_operation_locks:
            for v1 in self.load_balancer_operation_locks:
                 if v1:
                    v1.validate()
        if self.modification_protection_config:
            self.modification_protection_config.validate()
        if self.tags:
            for v1 in self.tags:
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
        if self.access_log_config is not None:
            result['AccessLogConfig'] = self.access_log_config.to_map()

        if self.address_allocated_mode is not None:
            result['AddressAllocatedMode'] = self.address_allocated_mode

        if self.address_ip_version is not None:
            result['AddressIpVersion'] = self.address_ip_version

        if self.address_type is not None:
            result['AddressType'] = self.address_type

        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.dnsname is not None:
            result['DNSName'] = self.dnsname

        if self.deletion_protection_config is not None:
            result['DeletionProtectionConfig'] = self.deletion_protection_config.to_map()

        if self.ipv_6address_type is not None:
            result['Ipv6AddressType'] = self.ipv_6address_type

        if self.load_balancer_billing_config is not None:
            result['LoadBalancerBillingConfig'] = self.load_balancer_billing_config.to_map()

        if self.load_balancer_bussiness_status is not None:
            result['LoadBalancerBussinessStatus'] = self.load_balancer_bussiness_status

        if self.load_balancer_edition is not None:
            result['LoadBalancerEdition'] = self.load_balancer_edition

        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        if self.load_balancer_name is not None:
            result['LoadBalancerName'] = self.load_balancer_name

        result['LoadBalancerOperationLocks'] = []
        if self.load_balancer_operation_locks is not None:
            for k1 in self.load_balancer_operation_locks:
                result['LoadBalancerOperationLocks'].append(k1.to_map() if k1 else None)

        if self.load_balancer_status is not None:
            result['LoadBalancerStatus'] = self.load_balancer_status

        if self.modification_protection_config is not None:
            result['ModificationProtectionConfig'] = self.modification_protection_config.to_map()

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        result['ZoneMappings'] = []
        if self.zone_mappings is not None:
            for k1 in self.zone_mappings:
                result['ZoneMappings'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessLogConfig') is not None:
            temp_model = main_models.GetLoadBalancerAttributeResponseBodyAccessLogConfig()
            self.access_log_config = temp_model.from_map(m.get('AccessLogConfig'))

        if m.get('AddressAllocatedMode') is not None:
            self.address_allocated_mode = m.get('AddressAllocatedMode')

        if m.get('AddressIpVersion') is not None:
            self.address_ip_version = m.get('AddressIpVersion')

        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')

        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DNSName') is not None:
            self.dnsname = m.get('DNSName')

        if m.get('DeletionProtectionConfig') is not None:
            temp_model = main_models.GetLoadBalancerAttributeResponseBodyDeletionProtectionConfig()
            self.deletion_protection_config = temp_model.from_map(m.get('DeletionProtectionConfig'))

        if m.get('Ipv6AddressType') is not None:
            self.ipv_6address_type = m.get('Ipv6AddressType')

        if m.get('LoadBalancerBillingConfig') is not None:
            temp_model = main_models.GetLoadBalancerAttributeResponseBodyLoadBalancerBillingConfig()
            self.load_balancer_billing_config = temp_model.from_map(m.get('LoadBalancerBillingConfig'))

        if m.get('LoadBalancerBussinessStatus') is not None:
            self.load_balancer_bussiness_status = m.get('LoadBalancerBussinessStatus')

        if m.get('LoadBalancerEdition') is not None:
            self.load_balancer_edition = m.get('LoadBalancerEdition')

        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        if m.get('LoadBalancerName') is not None:
            self.load_balancer_name = m.get('LoadBalancerName')

        self.load_balancer_operation_locks = []
        if m.get('LoadBalancerOperationLocks') is not None:
            for k1 in m.get('LoadBalancerOperationLocks'):
                temp_model = main_models.GetLoadBalancerAttributeResponseBodyLoadBalancerOperationLocks()
                self.load_balancer_operation_locks.append(temp_model.from_map(k1))

        if m.get('LoadBalancerStatus') is not None:
            self.load_balancer_status = m.get('LoadBalancerStatus')

        if m.get('ModificationProtectionConfig') is not None:
            temp_model = main_models.GetLoadBalancerAttributeResponseBodyModificationProtectionConfig()
            self.modification_protection_config = temp_model.from_map(m.get('ModificationProtectionConfig'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetLoadBalancerAttributeResponseBodyTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        self.zone_mappings = []
        if m.get('ZoneMappings') is not None:
            for k1 in m.get('ZoneMappings'):
                temp_model = main_models.GetLoadBalancerAttributeResponseBodyZoneMappings()
                self.zone_mappings.append(temp_model.from_map(k1))

        return self

class GetLoadBalancerAttributeResponseBodyZoneMappings(DaraModel):
    def __init__(
        self,
        load_balancer_addresses: List[main_models.GetLoadBalancerAttributeResponseBodyZoneMappingsLoadBalancerAddresses] = None,
        status: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        # The address of the ALB instance.
        self.load_balancer_addresses = load_balancer_addresses
        # The zone status. Valid values:
        # 
        # - **Active**: The ALB instance is running.
        # 
        # - **Stopped**: The ALB instance is disabled. 
        # 
        # - **Shifted**: The ALB instance is removed.
        # 
        # - **Starting**: The ALB instance is starting.
        # 
        # - **Stopping**: The ALB instance is stopping.
        self.status = status
        # The vSwitch in the zone. You can specify only one vSwitch (subnet) in each zone of an ALB instance.
        self.v_switch_id = v_switch_id
        # The zone ID of the ALB instance.
        # 
        # You can call the [DescribeZones](https://help.aliyun.com/document_detail/189196.html) operation to query the most recent zone list.
        self.zone_id = zone_id

    def validate(self):
        if self.load_balancer_addresses:
            for v1 in self.load_balancer_addresses:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LoadBalancerAddresses'] = []
        if self.load_balancer_addresses is not None:
            for k1 in self.load_balancer_addresses:
                result['LoadBalancerAddresses'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.load_balancer_addresses = []
        if m.get('LoadBalancerAddresses') is not None:
            for k1 in m.get('LoadBalancerAddresses'):
                temp_model = main_models.GetLoadBalancerAttributeResponseBodyZoneMappingsLoadBalancerAddresses()
                self.load_balancer_addresses.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class GetLoadBalancerAttributeResponseBodyZoneMappingsLoadBalancerAddresses(DaraModel):
    def __init__(
        self,
        address: str = None,
        allocation_id: str = None,
        eip_type: str = None,
        intranet_address: str = None,
        intranet_address_hc_status: str = None,
        ipv_4local_addresses: List[str] = None,
        ipv_6address: str = None,
        ipv_6address_hc_status: str = None,
        ipv_6local_addresses: List[str] = None,
    ):
        # An IPv4 address.
        # 
        # This parameter takes effect when **AddressIPVersion** is set to **IPv4** or **DualStack**. The network type is determined by the value of **AddressType**.
        self.address = address
        # The elastic IP address (EIP).
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
        # The health status of the private IPv4 address of the ALB instance. 
        # This parameter is returned only when the Status of the zone is Active.Valid values:
        # 
        # - **Healthy**
        # 
        # - **Unhealthy**
        self.intranet_address_hc_status = intranet_address_hc_status
        # The IPv4 link-local addresses. The IP addresses that the ALB instance uses to communicate with the backend servers.
        self.ipv_4local_addresses = ipv_4local_addresses
        # An IPv6 address.
        # 
        # This parameter takes effect only when **AddressIPVersion** is set to **DualStack**. The network type is determined by the value of **Ipv6AddressType**.
        self.ipv_6address = ipv_6address
        # The health status of the private IPv6 address of the ALB instance. 
        # This parameter is returned only when the Status of the zone is Active.Valid values:
        # 
        # - **Healthy**
        # 
        # - **Unhealthy**
        self.ipv_6address_hc_status = ipv_6address_hc_status
        # The IPv6 link-local addresses. The IP addresses that the ALB instance uses to communicate with the backend servers.
        self.ipv_6local_addresses = ipv_6local_addresses

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['Address'] = self.address

        if self.allocation_id is not None:
            result['AllocationId'] = self.allocation_id

        if self.eip_type is not None:
            result['EipType'] = self.eip_type

        if self.intranet_address is not None:
            result['IntranetAddress'] = self.intranet_address

        if self.intranet_address_hc_status is not None:
            result['IntranetAddressHcStatus'] = self.intranet_address_hc_status

        if self.ipv_4local_addresses is not None:
            result['Ipv4LocalAddresses'] = self.ipv_4local_addresses

        if self.ipv_6address is not None:
            result['Ipv6Address'] = self.ipv_6address

        if self.ipv_6address_hc_status is not None:
            result['Ipv6AddressHcStatus'] = self.ipv_6address_hc_status

        if self.ipv_6local_addresses is not None:
            result['Ipv6LocalAddresses'] = self.ipv_6local_addresses

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('AllocationId') is not None:
            self.allocation_id = m.get('AllocationId')

        if m.get('EipType') is not None:
            self.eip_type = m.get('EipType')

        if m.get('IntranetAddress') is not None:
            self.intranet_address = m.get('IntranetAddress')

        if m.get('IntranetAddressHcStatus') is not None:
            self.intranet_address_hc_status = m.get('IntranetAddressHcStatus')

        if m.get('Ipv4LocalAddresses') is not None:
            self.ipv_4local_addresses = m.get('Ipv4LocalAddresses')

        if m.get('Ipv6Address') is not None:
            self.ipv_6address = m.get('Ipv6Address')

        if m.get('Ipv6AddressHcStatus') is not None:
            self.ipv_6address_hc_status = m.get('Ipv6AddressHcStatus')

        if m.get('Ipv6LocalAddresses') is not None:
            self.ipv_6local_addresses = m.get('Ipv6LocalAddresses')

        return self

class GetLoadBalancerAttributeResponseBodyTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        # 
        # The tag key can be up to 128 characters in length, and cannot contain `http://` or `https://`. It cannot start with `acs:` or `aliyun`.
        self.key = key
        # The tag value.
        # 
        # The tag value can be up to 128 characters in length, and cannot contain `http://` or `https://`. It cannot start with `aliyun` or `acs:`.
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

class GetLoadBalancerAttributeResponseBodyModificationProtectionConfig(DaraModel):
    def __init__(
        self,
        reason: str = None,
        status: str = None,
    ):
        # The reason why the configuration read-only mode is enabled.
        # 
        # The name must be 2 to 128 character characters in length, and can contain letters, digits, periods (.), underscores (_), and hyphens (-). It must start with a letter.
        # 
        # This parameter takes effect only if **Status** is set to **ConsoleProtection**.
        self.reason = reason
        # Specifies whether the configuration read-only mode is enabled. Valid values:
        # 
        # *   **NonProtection**: The configuration read-only mode is disabled. In this case, the value of the **Reason** parameter that you specify does not take effect. If you set **Reason**, the value is cleared.
        # *   **ConsoleProtection**: The configuration read-only mode is enabled. In this case, the value of the **Reason** parameter takes effect.****
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

class GetLoadBalancerAttributeResponseBodyLoadBalancerOperationLocks(DaraModel):
    def __init__(
        self,
        lock_reason: str = None,
        lock_type: str = None,
    ):
        # The reason why the ALB instance is locked. This parameter is valid only if **LoadBalancerBussinessStatus** is set to **Abnormal**.
        self.lock_reason = lock_reason
        # The lock type. Valid values:
        # 
        # *   **SecurityLocked**: The ALB instance is locked due to security reasons.
        # *   **RelatedResourceLocked**: The ALB instance is locked due to other resources that are associated with the ALB instance.
        # *   **FinancialLocked**: The ALB instance is locked due to overdue payments.
        # *   **ResidualLocked**: The ALB instance is locked because the associated resources have overdue payments and the resources are released.
        self.lock_type = lock_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason

        if self.lock_type is not None:
            result['LockType'] = self.lock_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')

        if m.get('LockType') is not None:
            self.lock_type = m.get('LockType')

        return self

class GetLoadBalancerAttributeResponseBodyLoadBalancerBillingConfig(DaraModel):
    def __init__(
        self,
        pay_type: str = None,
    ):
        # The billing method.
        # 
        # Only **PostPay** is returned, which indicates the pay-as-you-go billing method.
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

class GetLoadBalancerAttributeResponseBodyDeletionProtectionConfig(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        enabled_time: str = None,
    ):
        # Indicates whether the deletion protection feature is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.enabled = enabled
        # The time when the deletion protection feature was enabled. The time follows the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time is displayed in UTC.
        self.enabled_time = enabled_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.enabled_time is not None:
            result['EnabledTime'] = self.enabled_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('EnabledTime') is not None:
            self.enabled_time = m.get('EnabledTime')

        return self

class GetLoadBalancerAttributeResponseBodyAccessLogConfig(DaraModel):
    def __init__(
        self,
        log_project: str = None,
        log_store: str = None,
    ):
        # The Log Service project.
        self.log_project = log_project
        # The Logstore.
        self.log_store = log_store

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.log_project is not None:
            result['LogProject'] = self.log_project

        if self.log_store is not None:
            result['LogStore'] = self.log_store

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogProject') is not None:
            self.log_project = m.get('LogProject')

        if m.get('LogStore') is not None:
            self.log_store = m.get('LogStore')

        return self

