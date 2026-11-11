# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nlb20220430 import models as main_models
from darabonba.model import DaraModel

class GetLoadBalancerAttributeResponseBody(DaraModel):
    def __init__(
        self,
        address_ip_version: str = None,
        address_type: str = None,
        bandwidth_package_id: str = None,
        cps: int = None,
        create_time: str = None,
        cross_zone_enabled: bool = None,
        dnsname: str = None,
        deletion_protection_config: main_models.GetLoadBalancerAttributeResponseBodyDeletionProtectionConfig = None,
        ipv_6address_type: str = None,
        load_balancer_billing_config: main_models.GetLoadBalancerAttributeResponseBodyLoadBalancerBillingConfig = None,
        load_balancer_business_status: str = None,
        load_balancer_id: str = None,
        load_balancer_name: str = None,
        load_balancer_status: str = None,
        load_balancer_type: str = None,
        modification_protection_config: main_models.GetLoadBalancerAttributeResponseBodyModificationProtectionConfig = None,
        operation_locks: List[main_models.GetLoadBalancerAttributeResponseBodyOperationLocks] = None,
        region_id: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        security_group_ids: List[str] = None,
        tags: List[main_models.GetLoadBalancerAttributeResponseBodyTags] = None,
        vpc_id: str = None,
        zone_mappings: List[main_models.GetLoadBalancerAttributeResponseBodyZoneMappings] = None,
    ):
        # The protocol version. Valid values:
        # 
        # - **ipv4**: IPv4.
        # - **DualStack**: dual stack.
        self.address_ip_version = address_ip_version
        # The IPv4 network address type of the NLB instance. Valid values:
        # - **Internet**: The load balancing instance has a public IP address. The DNS domain name is resolved to the public IP address. Therefore, the instance can be accessed over the Internet.
        # - **Intranet**: The load balancing instance has only a private IP address. The DNS domain name is resolved to the private IP address. Therefore, the instance can be accessed only within the internal network of the VPC where the load balancing instance is deployed.
        self.address_type = address_type
        # The ID of the Internet Shared Bandwidth instance associated with the Internet-facing NLB instance.
        self.bandwidth_package_id = bandwidth_package_id
        # The maximum number of new connections per second that the NLB instance can process per zone (VIP). Valid values: **0** to **1000000**.
        # 
        # **0** indicates that no limit is imposed.
        self.cps = cps
        # The time when the resource was created. The time is displayed in UTC in the `yyyy-MM-ddTHH:mm:ssZ` format.
        self.create_time = create_time
        # Indicates whether cross-zone is enabled for the NLB instance. Valid values:
        # - **true**: enabled.
        # - **false**: disabled.
        self.cross_zone_enabled = cross_zone_enabled
        # The domain name of the NLB instance.
        self.dnsname = dnsname
        # The deletion protection configuration.
        self.deletion_protection_config = deletion_protection_config
        # The IPv6 address type of the NLB instance. Valid values:
        # - **Internet**: The load balancing instance has a public IP address. The DNS domain name is resolved to the public IP address. Therefore, the instance can be accessed over the Internet.
        # - **Intranet**: The load balancing instance has only a private IP address. The DNS domain name is resolved to the private IP address. Therefore, the instance can be accessed only within the internal network of the VPC where the load balancing instance is deployed.
        self.ipv_6address_type = ipv_6address_type
        # The billing configuration of the load balancing instance.
        self.load_balancer_billing_config = load_balancer_billing_config
        # The business status of the NLB instance. Valid values:
        # - **Abnormal**: The NLB instance is in an abnormal state.
        # - **Normal**: The NLB instance is in a normal state.
        self.load_balancer_business_status = load_balancer_business_status
        # The NLB instance ID.
        self.load_balancer_id = load_balancer_id
        # The name of the NLB instance.
        # 
        # The name must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores (_), and hyphens (-). The name must start with a letter or a Chinese character.
        self.load_balancer_name = load_balancer_name
        # The NLB instance status. Valid values:
        # - **Inactive**: The NLB instance is stopped. The listeners of the instance no longer forward traffic.
        # - **Active**: The NLB instance is running.
        # - **Provisioning**: The NLB instance is being created.
        # - **Configuring**: The NLB instance is being reconfigured (Upgrade/Downgrade).
        # - **CreateFailed**: The NLB instance failed to be created. In this case, no fees are incurred, and the instance can only be deleted.
        self.load_balancer_status = load_balancer_status
        # The load balancing type. Only **network** is returned, which indicates Network Load Balancer (NLB).
        self.load_balancer_type = load_balancer_type
        # The modification protection configuration.
        self.modification_protection_config = modification_protection_config
        # The lock state list of the NLB instance. This parameter is returned only when `LoadBalancerBussinessStatus` is **Abnormal**.
        self.operation_locks = operation_locks
        # The region ID of the NLB instance.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The security group IDs associated with the NLB instance.
        self.security_group_ids = security_group_ids
        # The tag list.
        self.tags = tags
        # The VPC ID of the NLB instance.
        self.vpc_id = vpc_id
        # The mappings between zones and vSwitches. A maximum of 10 zones are returned. If the current region supports two or more zones, at least two zones are returned.
        self.zone_mappings = zone_mappings

    def validate(self):
        if self.deletion_protection_config:
            self.deletion_protection_config.validate()
        if self.load_balancer_billing_config:
            self.load_balancer_billing_config.validate()
        if self.modification_protection_config:
            self.modification_protection_config.validate()
        if self.operation_locks:
            for v1 in self.operation_locks:
                 if v1:
                    v1.validate()
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
        if self.address_ip_version is not None:
            result['AddressIpVersion'] = self.address_ip_version

        if self.address_type is not None:
            result['AddressType'] = self.address_type

        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id

        if self.cps is not None:
            result['Cps'] = self.cps

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.cross_zone_enabled is not None:
            result['CrossZoneEnabled'] = self.cross_zone_enabled

        if self.dnsname is not None:
            result['DNSName'] = self.dnsname

        if self.deletion_protection_config is not None:
            result['DeletionProtectionConfig'] = self.deletion_protection_config.to_map()

        if self.ipv_6address_type is not None:
            result['Ipv6AddressType'] = self.ipv_6address_type

        if self.load_balancer_billing_config is not None:
            result['LoadBalancerBillingConfig'] = self.load_balancer_billing_config.to_map()

        if self.load_balancer_business_status is not None:
            result['LoadBalancerBusinessStatus'] = self.load_balancer_business_status

        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        if self.load_balancer_name is not None:
            result['LoadBalancerName'] = self.load_balancer_name

        if self.load_balancer_status is not None:
            result['LoadBalancerStatus'] = self.load_balancer_status

        if self.load_balancer_type is not None:
            result['LoadBalancerType'] = self.load_balancer_type

        if self.modification_protection_config is not None:
            result['ModificationProtectionConfig'] = self.modification_protection_config.to_map()

        result['OperationLocks'] = []
        if self.operation_locks is not None:
            for k1 in self.operation_locks:
                result['OperationLocks'].append(k1.to_map() if k1 else None)

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
        if m.get('AddressIpVersion') is not None:
            self.address_ip_version = m.get('AddressIpVersion')

        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')

        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')

        if m.get('Cps') is not None:
            self.cps = m.get('Cps')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CrossZoneEnabled') is not None:
            self.cross_zone_enabled = m.get('CrossZoneEnabled')

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

        if m.get('LoadBalancerBusinessStatus') is not None:
            self.load_balancer_business_status = m.get('LoadBalancerBusinessStatus')

        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        if m.get('LoadBalancerName') is not None:
            self.load_balancer_name = m.get('LoadBalancerName')

        if m.get('LoadBalancerStatus') is not None:
            self.load_balancer_status = m.get('LoadBalancerStatus')

        if m.get('LoadBalancerType') is not None:
            self.load_balancer_type = m.get('LoadBalancerType')

        if m.get('ModificationProtectionConfig') is not None:
            temp_model = main_models.GetLoadBalancerAttributeResponseBodyModificationProtectionConfig()
            self.modification_protection_config = temp_model.from_map(m.get('ModificationProtectionConfig'))

        self.operation_locks = []
        if m.get('OperationLocks') is not None:
            for k1 in m.get('OperationLocks'):
                temp_model = main_models.GetLoadBalancerAttributeResponseBodyOperationLocks()
                self.operation_locks.append(temp_model.from_map(k1))

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
        # The Network Load Balancing (NLB) instance address information.
        self.load_balancer_addresses = load_balancer_addresses
        # The zone status. Valid values:
        # 
        # - **Active**: enabled.
        # - **Stopped**: stopped. This status can be set only through the CADT disaster recovery management service invocation.
        # - **Shifted**: DNS manually removed. You can call the [CancelShiftLoadBalancerZones](https://help.aliyun.com/document_detail/2412000.html) operation to restore the DNS of the zone.
        # - **AutoShifted**: DNS automatically removed. When a zone encounters an exception, the system automatically removes the IP address of the abnormal zone to ensure that you can access services normally through the NLB domain name. The IP address is automatically restored when the zone recovers. No manual operation is required.
        # - **Starting**: starting. This status can be set only through the CADT disaster recovery management service invocation.
        # - **Stopping**: stopping. This status can be set only through the CADT disaster recovery management service invocation.
        self.status = status
        # The vSwitch in the zone. Each zone uses one vSwitch and one subnet by default.
        self.v_switch_id = v_switch_id
        # The zone ID. You can call the [DescribeZones](https://help.aliyun.com/document_detail/443890.html) operation to query the most recent zone list.
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
        allocation_id: str = None,
        eni_id: str = None,
        ipv_4local_addresses: List[str] = None,
        ipv_6address: str = None,
        ipv_6local_addresses: List[str] = None,
        private_ipv_4address: str = None,
        private_ipv_4hc_status: str = None,
        private_ipv_6hc_status: str = None,
        public_ipv_4address: str = None,
    ):
        # The Elastic IP Address (EIP) instance ID.
        self.allocation_id = allocation_id
        # The ID of the ENI.
        self.eni_id = eni_id
        # The list of IPv4 local addresses. These are the addresses used for communication between the NLB instance and backend servers.
        self.ipv_4local_addresses = ipv_4local_addresses
        # The IPv6 VIP address. The IPv6 address that the NLB instance uses to provide services.
        self.ipv_6address = ipv_6address
        # The list of IPv6 local addresses. These are the addresses used for communication between the NLB instance and backend servers.
        self.ipv_6local_addresses = ipv_6local_addresses
        # The private IPv4 VIP address. The private IPv4 address that the NLB instance uses to provide services.
        self.private_ipv_4address = private_ipv_4address
        # The health check status of the private IPv4 address of the NLB instance. Valid values:
        # 
        # - **Healthy**: healthy.
        # - **Unhealthy**: unhealthy.
        # 
        # > This parameter is returned only when the zone status (**Status**) is Active.
        self.private_ipv_4hc_status = private_ipv_4hc_status
        # The health check status of the IPv6 address of the NLB instance. Valid values:
        # 
        # - **Healthy**: healthy.
        # - **Unhealthy**: unhealthy.
        # 
        # > This parameter is returned only when the zone status (**Status**) is Active.
        self.private_ipv_6hc_status = private_ipv_6hc_status
        # The public IPv4 address of the NLB instance.
        self.public_ipv_4address = public_ipv_4address

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocation_id is not None:
            result['AllocationId'] = self.allocation_id

        if self.eni_id is not None:
            result['EniId'] = self.eni_id

        if self.ipv_4local_addresses is not None:
            result['Ipv4LocalAddresses'] = self.ipv_4local_addresses

        if self.ipv_6address is not None:
            result['Ipv6Address'] = self.ipv_6address

        if self.ipv_6local_addresses is not None:
            result['Ipv6LocalAddresses'] = self.ipv_6local_addresses

        if self.private_ipv_4address is not None:
            result['PrivateIPv4Address'] = self.private_ipv_4address

        if self.private_ipv_4hc_status is not None:
            result['PrivateIPv4HcStatus'] = self.private_ipv_4hc_status

        if self.private_ipv_6hc_status is not None:
            result['PrivateIPv6HcStatus'] = self.private_ipv_6hc_status

        if self.public_ipv_4address is not None:
            result['PublicIPv4Address'] = self.public_ipv_4address

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationId') is not None:
            self.allocation_id = m.get('AllocationId')

        if m.get('EniId') is not None:
            self.eni_id = m.get('EniId')

        if m.get('Ipv4LocalAddresses') is not None:
            self.ipv_4local_addresses = m.get('Ipv4LocalAddresses')

        if m.get('Ipv6Address') is not None:
            self.ipv_6address = m.get('Ipv6Address')

        if m.get('Ipv6LocalAddresses') is not None:
            self.ipv_6local_addresses = m.get('Ipv6LocalAddresses')

        if m.get('PrivateIPv4Address') is not None:
            self.private_ipv_4address = m.get('PrivateIPv4Address')

        if m.get('PrivateIPv4HcStatus') is not None:
            self.private_ipv_4hc_status = m.get('PrivateIPv4HcStatus')

        if m.get('PrivateIPv6HcStatus') is not None:
            self.private_ipv_6hc_status = m.get('PrivateIPv6HcStatus')

        if m.get('PublicIPv4Address') is not None:
            self.public_ipv_4address = m.get('PublicIPv4Address')

        return self

class GetLoadBalancerAttributeResponseBodyTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key of the instance.
        self.tag_key = tag_key
        # The tag value of the instance.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

class GetLoadBalancerAttributeResponseBodyOperationLocks(DaraModel):
    def __init__(
        self,
        lock_reason: str = None,
        lock_type: str = None,
    ):
        # The reason for the lock.
        self.lock_reason = lock_reason
        # The type of the lock. Valid values:
        # - **SecurityLocked**: The instance is locked due to security reasons.
        # - **RelatedResourceLocked**: The instance is locked due to associate lock.
        # - **FinancialLocked**: The instance is locked due to overdue payment.
        # - **ResidualLocked**: The instance is locked due to residual resources.
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

class GetLoadBalancerAttributeResponseBodyModificationProtectionConfig(DaraModel):
    def __init__(
        self,
        enabled_time: str = None,
        reason: str = None,
        status: str = None,
    ):
        # The time when modification protection was enabled. The time is displayed in UTC in the `yyyy-MM-ddTHH:mm:ssZ` format.
        self.enabled_time = enabled_time
        # The reason for enabling modification protection. The reason must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores (_), and hyphens (-). The reason must start with a letter or a Chinese character.
        # 
        # This parameter is valid and required only when **Status** is set to **ConsoleProtection**.
        self.reason = reason
        # The modification protection status of the Network Load Balancer (NLB) instance. Valid values:
        # 
        # - **NonProtection**: Modification protection is disabled. You cannot specify the **Reason** parameter. If the **Reason** parameter is specified, the value is cleared.
        # - **ConsoleProtection**: Console modification protection is enabled. You can specify the **Reason** parameter.
        # 
        # > If the value is **ConsoleProtection**, you cannot modify the instance configuration in the load balancing console, but you can modify the instance configuration by invoking API operations.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled_time is not None:
            result['EnabledTime'] = self.enabled_time

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnabledTime') is not None:
            self.enabled_time = m.get('EnabledTime')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetLoadBalancerAttributeResponseBodyLoadBalancerBillingConfig(DaraModel):
    def __init__(
        self,
        pay_type: str = None,
    ):
        # The billing type of the NLB instance.
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
        reason: str = None,
    ):
        # The deletion protection status. Valid values:
        # 
        # - **true**: enabled.
        # - **false**: disabled.
        self.enabled = enabled
        # The time when deletion protection was enabled. The time is displayed in UTC in the `yyyy-MM-ddTHH:mm:ssZ` format.
        self.enabled_time = enabled_time
        # The reason for changing the deletion protection status. The reason must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores (_), and hyphens (-). The reason must start with a letter or a Chinese character.
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

        if self.enabled_time is not None:
            result['EnabledTime'] = self.enabled_time

        if self.reason is not None:
            result['Reason'] = self.reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('EnabledTime') is not None:
            self.enabled_time = m.get('EnabledTime')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        return self

