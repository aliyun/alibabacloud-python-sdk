# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nlb20220430 import models as main_models
from darabonba.model import DaraModel

class ListLoadBalancersResponseBody(DaraModel):
    def __init__(
        self,
        load_balancers: List[main_models.ListLoadBalancersResponseBodyLoadBalancers] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The NLB instances.
        self.load_balancers = load_balancers
        # The number of entries returned per page.
        self.max_results = max_results
        # The token that determines the start point of the next query. Valid values:
        # 
        # *   If this is your first query and no subsequent queries are to be sent, ignore this parameter.
        # *   If a subsequent query is to be sent, set the parameter to the value of NextToken that is returned from the last call.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.load_balancers:
            for v1 in self.load_balancers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LoadBalancers'] = []
        if self.load_balancers is not None:
            for k1 in self.load_balancers:
                result['LoadBalancers'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.load_balancers = []
        if m.get('LoadBalancers') is not None:
            for k1 in m.get('LoadBalancers'):
                temp_model = main_models.ListLoadBalancersResponseBodyLoadBalancers()
                self.load_balancers.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListLoadBalancersResponseBodyLoadBalancers(DaraModel):
    def __init__(
        self,
        address_ip_version: str = None,
        address_type: str = None,
        bandwidth_package_id: str = None,
        create_time: str = None,
        cross_zone_enabled: bool = None,
        dnsname: str = None,
        deletion_protection_config: main_models.ListLoadBalancersResponseBodyLoadBalancersDeletionProtectionConfig = None,
        ipv_6address_type: str = None,
        load_balancer_billing_config: main_models.ListLoadBalancersResponseBodyLoadBalancersLoadBalancerBillingConfig = None,
        load_balancer_business_status: str = None,
        load_balancer_id: str = None,
        load_balancer_name: str = None,
        load_balancer_status: str = None,
        load_balancer_type: str = None,
        modification_protection_config: main_models.ListLoadBalancersResponseBodyLoadBalancersModificationProtectionConfig = None,
        operation_locks: List[main_models.ListLoadBalancersResponseBodyLoadBalancersOperationLocks] = None,
        region_id: str = None,
        resource_group_id: str = None,
        security_group_ids: List[str] = None,
        tags: List[main_models.ListLoadBalancersResponseBodyLoadBalancersTags] = None,
        vpc_id: str = None,
        zone_mappings: List[main_models.ListLoadBalancersResponseBodyLoadBalancersZoneMappings] = None,
    ):
        # The IP version. Valid values:
        # 
        # *   **ipv4**: IPv4
        # *   **DualStack**: dual stack
        self.address_ip_version = address_ip_version
        # The type of IPv4 address used by the NLB instance. Valid values:
        # 
        # *   **Internet**: The NLB instance uses a public IP address. The domain name of the NLB instance is resolved to the public IP address. Therefore, the NLB instance can be accessed over the Internet.
        # *   **Intranet**: The NLB instance uses a private IP address. The domain name of the NLB instance is resolved to the private IP address. Therefore, the NLB instance can be accessed over the VPC where the NLB instance is deployed.
        self.address_type = address_type
        # The ID of the EIP bandwidth plan that is associated with the NLB instance if the NLB instance uses a public IP address.
        self.bandwidth_package_id = bandwidth_package_id
        # The time when the resource was created. The time is displayed in UTC in the `yyyy-MM-ddTHH:mm:ssZ` format.
        self.create_time = create_time
        # Indicates whether cross-zone load balancing is enabled for the NLB instance. Valid values:
        # 
        # *   **true**: enabled
        # *   **false**: disabled
        self.cross_zone_enabled = cross_zone_enabled
        # The domain name of the NLB instance.
        self.dnsname = dnsname
        # The configuration of the deletion protection feature.
        self.deletion_protection_config = deletion_protection_config
        # The type of IPv6 address used by the NLB instance. Valid values:
        # 
        # *   **Internet**: The NLB instance uses a public IP address. The domain name of the NLB instance is resolved to the public IP address. Therefore, the NLB instance can be accessed over the Internet.
        # *   **Intranet**: The NLB instance uses a private IP address. The domain name of the NLB instance is resolved to the private IP address. Therefore, the NLB instance can be accessed over the VPC where the NLB instance is deployed.
        self.ipv_6address_type = ipv_6address_type
        # The billing settings of the NLB instance.
        self.load_balancer_billing_config = load_balancer_billing_config
        # The business status of the NLB instance. Valid values:
        # 
        # *   **Abnormal**: The NLB instance is not working as expected.
        # *   **Normal**: The NLB instance is working as expected.
        self.load_balancer_business_status = load_balancer_business_status
        # The ID of the NLB instance.
        self.load_balancer_id = load_balancer_id
        # The name of the NLB instance.
        self.load_balancer_name = load_balancer_name
        # The status of the NLB instance. Valid values:
        # 
        # *   **Inactive**: The NLB instance is disabled. Listeners of NLB instances in the Inactive state do not forward traffic.
        # *   **Active**: The NLB instance is running.
        # *   **Provisioning**: The NLB instance is being created.
        # *   **Configuring**: The NLB instance is being modified.
        # *   **Deleting**: The NLB instance is being deleted.
        # *   **Deleted**: The NLB instance is deleted.
        self.load_balancer_status = load_balancer_status
        # The type of the SLB instance. Only **Network** is returned, which indicates NLB.
        self.load_balancer_type = load_balancer_type
        # The configuration of the configuration read-only mode.
        self.modification_protection_config = modification_protection_config
        # The configuration of the operation lock. This parameter takes effect if the value of `LoadBalancerBussinessStatus` is **Abnormal**.
        self.operation_locks = operation_locks
        # The ID of the region where the NLB instance is deployed.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The security group to which the NLB instance is added.
        self.security_group_ids = security_group_ids
        # A list of tags.
        self.tags = tags
        # The ID of the VPC where the NLB instance is deployed.
        self.vpc_id = vpc_id
        # The mappings between zones and vSwitches.
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

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CrossZoneEnabled') is not None:
            self.cross_zone_enabled = m.get('CrossZoneEnabled')

        if m.get('DNSName') is not None:
            self.dnsname = m.get('DNSName')

        if m.get('DeletionProtectionConfig') is not None:
            temp_model = main_models.ListLoadBalancersResponseBodyLoadBalancersDeletionProtectionConfig()
            self.deletion_protection_config = temp_model.from_map(m.get('DeletionProtectionConfig'))

        if m.get('Ipv6AddressType') is not None:
            self.ipv_6address_type = m.get('Ipv6AddressType')

        if m.get('LoadBalancerBillingConfig') is not None:
            temp_model = main_models.ListLoadBalancersResponseBodyLoadBalancersLoadBalancerBillingConfig()
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
            temp_model = main_models.ListLoadBalancersResponseBodyLoadBalancersModificationProtectionConfig()
            self.modification_protection_config = temp_model.from_map(m.get('ModificationProtectionConfig'))

        self.operation_locks = []
        if m.get('OperationLocks') is not None:
            for k1 in m.get('OperationLocks'):
                temp_model = main_models.ListLoadBalancersResponseBodyLoadBalancersOperationLocks()
                self.operation_locks.append(temp_model.from_map(k1))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListLoadBalancersResponseBodyLoadBalancersTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        self.zone_mappings = []
        if m.get('ZoneMappings') is not None:
            for k1 in m.get('ZoneMappings'):
                temp_model = main_models.ListLoadBalancersResponseBodyLoadBalancersZoneMappings()
                self.zone_mappings.append(temp_model.from_map(k1))

        return self

class ListLoadBalancersResponseBodyLoadBalancersZoneMappings(DaraModel):
    def __init__(
        self,
        load_balancer_addresses: List[main_models.ListLoadBalancersResponseBodyLoadBalancersZoneMappingsLoadBalancerAddresses] = None,
        status: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        # The IP addresses that are used by the NLB instance.
        self.load_balancer_addresses = load_balancer_addresses
        # The zone status. Valid values:
        # 
        # - **Active**: The zone is available.
        # 
        # - **Stopped**: The zone is disabled. You can set the zone to this status only by using Cloud Architect Design Tools (CADT).
        # 
        # - **Shifted**: The DNS record is removed.
        # 
        # - **Starting**: The zone is being enabled. You can set the zone to this status only by using CADT.
        # 
        # - **Stopping** You can set the zone to this status only by using CADT.
        self.status = status
        # The ID of the vSwitch in the zone. By default, each zone contains one vSwitch and one subnet.
        self.v_switch_id = v_switch_id
        # The name of the zone. You can call the [DescribeZones](https://help.aliyun.com/document_detail/443890.html) operation to query the zones.
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
                temp_model = main_models.ListLoadBalancersResponseBodyLoadBalancersZoneMappingsLoadBalancerAddresses()
                self.load_balancer_addresses.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class ListLoadBalancersResponseBodyLoadBalancersZoneMappingsLoadBalancerAddresses(DaraModel):
    def __init__(
        self,
        allocation_id: str = None,
        eni_id: str = None,
        ipv_6address: str = None,
        private_ipv_4address: str = None,
        private_ipv_4hc_status: str = None,
        private_ipv_6hc_status: str = None,
        public_ipv_4address: str = None,
    ):
        # The ID of the elastic IP address (EIP).
        self.allocation_id = allocation_id
        # The ID of the elastic network interface (ENI) attached to the NLB instance.
        self.eni_id = eni_id
        # The IPv6 address used by the NLB instance.
        self.ipv_6address = ipv_6address
        # The private IPv4 address of the NLB instance.
        self.private_ipv_4address = private_ipv_4address
        # The health status of the private IPv4 address of the NLB instance. Valid values:
        # 
        # - **Healthy**
        # - **Unhealthy**
        # 
        # > This parameter is returned only when the Status of the zone is Active.
        self.private_ipv_4hc_status = private_ipv_4hc_status
        # The health status of the IPv6 address of the NLB instance. Valid values:
        # 
        # - **Healthy**
        # - **Unhealthy**
        # 
        # > This parameter is returned only when the Status of the zone is Active.
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

        if self.ipv_6address is not None:
            result['Ipv6Address'] = self.ipv_6address

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

        if m.get('Ipv6Address') is not None:
            self.ipv_6address = m.get('Ipv6Address')

        if m.get('PrivateIPv4Address') is not None:
            self.private_ipv_4address = m.get('PrivateIPv4Address')

        if m.get('PrivateIPv4HcStatus') is not None:
            self.private_ipv_4hc_status = m.get('PrivateIPv4HcStatus')

        if m.get('PrivateIPv6HcStatus') is not None:
            self.private_ipv_6hc_status = m.get('PrivateIPv6HcStatus')

        if m.get('PublicIPv4Address') is not None:
            self.public_ipv_4address = m.get('PublicIPv4Address')

        return self

class ListLoadBalancersResponseBodyLoadBalancersTags(DaraModel):
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

class ListLoadBalancersResponseBodyLoadBalancersOperationLocks(DaraModel):
    def __init__(
        self,
        lock_reason: str = None,
        lock_type: str = None,
    ):
        # The reason why the NLB instance is locked.
        self.lock_reason = lock_reason
        # The type of lock. Valid values:
        # 
        # *   **SecurityLocked**: The NLB instance is locked due to security reasons.
        # *   **RelatedResourceLocked**: The NLB instance is locked due to association issues.
        # *   **FinancialLocked**: The NLB instance is locked due to overdue payments.
        # *   **ResidualLocked**: The NLB instance is locked because the payments of the associated resources are overdue and the resources are released.
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

class ListLoadBalancersResponseBodyLoadBalancersModificationProtectionConfig(DaraModel):
    def __init__(
        self,
        enabled_time: str = None,
        reason: str = None,
        status: str = None,
    ):
        # The time when the configuration read-only mode was enabled. The time is displayed in UTC in `yyyy-MM-ddTHH:mm:ssZ` format.
        self.enabled_time = enabled_time
        # The reason why the configuration read-only mode is enabled. The reason must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores (_), and hyphens (-). The reason must start with a letter.
        # 
        # This parameter takes effect only if **Status** is set to **ConsoleProtection**.
        self.reason = reason
        # Indicates whether the configuration read-only mode is enabled. Valid values:
        # 
        # *   **NonProtection**: disabled. In this case, **Reason** is not returned. If **Reason** is set, the value is cleared.
        # *   **ConsoleProtection**: enabled. In this case, **Reason** is returned.
        # 
        # >  If you set this parameter to **ConsoleProtection**, you cannot use the NLB console to modify instance configurations. However, you can call API operations to modify instance configurations.
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

class ListLoadBalancersResponseBodyLoadBalancersLoadBalancerBillingConfig(DaraModel):
    def __init__(
        self,
        pay_type: str = None,
    ):
        # The billing method of the NLB instance. Only **PostPay** is supported, which indicates the pay-as-you-go billing method.
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

class ListLoadBalancersResponseBodyLoadBalancersDeletionProtectionConfig(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        enabled_time: str = None,
        reason: str = None,
    ):
        # Indicates whether deletion protection is enabled. Valid values:
        # 
        # *   **true**: enabled
        # *   **false**: disabled
        self.enabled = enabled
        # The time when deletion protection was enabled. The time is displayed in UTC in `yyyy-MM-ddTHH:mm:ssZ` format.
        self.enabled_time = enabled_time
        # The reason why the deletion protection feature is enabled or disabled. The reason must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores (_), and hyphens (-). The reason must start with a letter.
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

