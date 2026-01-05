# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alb20200616 import models as main_models
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
        # A list of ALB instances.
        self.load_balancers = load_balancers
        # The number of entries returned per page.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, no next page exists.
        # *   If a value is returned for **NextToken**, the value is used to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
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
        access_log_config: main_models.ListLoadBalancersResponseBodyLoadBalancersAccessLogConfig = None,
        address_allocated_mode: str = None,
        address_ip_version: str = None,
        address_type: str = None,
        bandwidth_package_id: str = None,
        create_time: str = None,
        dnsname: str = None,
        deletion_protection_config: main_models.ListLoadBalancersResponseBodyLoadBalancersDeletionProtectionConfig = None,
        ipv_6address_type: str = None,
        load_balancer_billing_config: main_models.ListLoadBalancersResponseBodyLoadBalancersLoadBalancerBillingConfig = None,
        load_balancer_bussiness_status: str = None,
        load_balancer_edition: str = None,
        load_balancer_id: str = None,
        load_balancer_name: str = None,
        load_balancer_operation_locks: List[main_models.ListLoadBalancersResponseBodyLoadBalancersLoadBalancerOperationLocks] = None,
        load_balancer_status: str = None,
        modification_protection_config: main_models.ListLoadBalancersResponseBodyLoadBalancersModificationProtectionConfig = None,
        resource_group_id: str = None,
        security_group_ids: List[str] = None,
        tags: List[main_models.ListLoadBalancersResponseBodyLoadBalancersTags] = None,
        vpc_id: str = None,
    ):
        # The configurations of access logs.
        self.access_log_config = access_log_config
        # The mode in which IP addresses are allocated. Valid values:
        # 
        # *   **Fixed**: The ALB instance uses a static IP address.
        # *   **Dynamic**: dynamically allocates an IP address to each zone of the ALB instance.
        self.address_allocated_mode = address_allocated_mode
        # The IP version. Valid values:
        # 
        # *   **IPv4**
        # *   **DualStack**
        self.address_ip_version = address_ip_version
        # The type of IP address that the ALB instance uses to provide services. Valid values:
        # 
        # *   **Internet**: The ALB instance is assigned a public IP address. The domain name is resolved to the public IP address. The ALB instance is accessible over the Internet.
        # *   **Intranet**: The ALB instance is assigned only a private IP address. The domain name is resolved to the private IP address. The ALB instance is accessible only within the VPC of the ALB instance.
        self.address_type = address_type
        # The ID of the Internet Shared Bandwidth instance that is associated with the Internet-facing ALB instance.
        self.bandwidth_package_id = bandwidth_package_id
        # The time when the resource was created.
        self.create_time = create_time
        # The domain name.
        self.dnsname = dnsname
        # The configuration of the deletion protection feature.
        self.deletion_protection_config = deletion_protection_config
        # The type of IPv6 address used by the ALB instance. Valid values:
        # 
        # *   **Internet** The ALB instance is assigned a public IP address. The domain name is resolved to the public IP address. The ALB instance is accessible over the Internet.
        # *   **Intranet** The ALB instance is assigned only a private IP address. The domain name is resolved to the private IP address. The ALB instance is accessible only within the VPC of the ALB instance.
        self.ipv_6address_type = ipv_6address_type
        # The billing information about the ALB instance.
        self.load_balancer_billing_config = load_balancer_billing_config
        # The status of the ALB instance. Valid values:
        # 
        # *   **Abnormal**
        # *   **Normal**
        self.load_balancer_bussiness_status = load_balancer_bussiness_status
        # The edition of the ALB instance. The features and billing rules vary based on the edition. Valid values:
        # 
        # *   **Basic**
        # *   **Standard**
        # *   **StandardWithWaf**
        self.load_balancer_edition = load_balancer_edition
        # The ID of the ALB instance.
        self.load_balancer_id = load_balancer_id
        # The name of the ALB instance.
        self.load_balancer_name = load_balancer_name
        # The configuration of the operation lock.
        self.load_balancer_operation_locks = load_balancer_operation_locks
        # The status of the ALB instance. Valid values:
        # 
        # *   **Inactive**: The ALB instance is disabled. ALB instances in the Inactive state do not forward traffic.
        # *   **Active**: The ALB instance is running.
        # *   **Provisioning**: The ALB instance is being created.
        # *   **Configuring**: The ALB instance is being modified.
        # *   **CreateFailed**: The system failed to create the ALB instance.
        self.load_balancer_status = load_balancer_status
        # The configuration read-only mode settings.
        self.modification_protection_config = modification_protection_config
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.security_group_ids = security_group_ids
        # The information about the tags.
        self.tags = tags
        # The ID of the VPC in which the ALB instance is deployed.
        self.vpc_id = vpc_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessLogConfig') is not None:
            temp_model = main_models.ListLoadBalancersResponseBodyLoadBalancersAccessLogConfig()
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
            temp_model = main_models.ListLoadBalancersResponseBodyLoadBalancersDeletionProtectionConfig()
            self.deletion_protection_config = temp_model.from_map(m.get('DeletionProtectionConfig'))

        if m.get('Ipv6AddressType') is not None:
            self.ipv_6address_type = m.get('Ipv6AddressType')

        if m.get('LoadBalancerBillingConfig') is not None:
            temp_model = main_models.ListLoadBalancersResponseBodyLoadBalancersLoadBalancerBillingConfig()
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
                temp_model = main_models.ListLoadBalancersResponseBodyLoadBalancersLoadBalancerOperationLocks()
                self.load_balancer_operation_locks.append(temp_model.from_map(k1))

        if m.get('LoadBalancerStatus') is not None:
            self.load_balancer_status = m.get('LoadBalancerStatus')

        if m.get('ModificationProtectionConfig') is not None:
            temp_model = main_models.ListLoadBalancersResponseBodyLoadBalancersModificationProtectionConfig()
            self.modification_protection_config = temp_model.from_map(m.get('ModificationProtectionConfig'))

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

        return self

class ListLoadBalancersResponseBodyLoadBalancersTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the ALB instance.
        self.key = key
        # The tag value of the ALB instance.
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

class ListLoadBalancersResponseBodyLoadBalancersModificationProtectionConfig(DaraModel):
    def __init__(
        self,
        reason: str = None,
        status: str = None,
    ):
        # The reason why the configuration read-only mode is enabled.
        # 
        # The reason must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores (_), and hyphens (-).
        # 
        # This parameter takes effect only if **Status** is set to **ConsoleProtection**.
        self.reason = reason
        # Indicates whether the configuration read-only mode is enabled. Valid values:
        # 
        # *   **NonProtection**: The configuration read-only mode is disabled. In this case, **Reason** is not returned. If **Reason** is set, the value is cleared.
        # *   **ConsoleProtection**: The configuration read-only mode is enabled. In this case, **Reason** is returned.****
        # 
        # >  If the value is **ConsoleProtection**, the configuration read-only mode is enabled. You cannot modify the configurations of the ALB instance in the ALB console. However, you can call API operations to modify the configurations of the ALB instance.
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

class ListLoadBalancersResponseBodyLoadBalancersLoadBalancerOperationLocks(DaraModel):
    def __init__(
        self,
        lock_reason: str = None,
        lock_type: str = None,
    ):
        # The reason why the ALB instance is locked. This parameter is valid only if **LoadBalancerBussinessStatus** is set to **Abnormal**.
        self.lock_reason = lock_reason
        # The lock type. Valid values:
        # 
        # *   **SecurityLocked**: The ALB instance is locked due to security risks.
        # *   **RelatedResourceLocked**: The ALB instance is locked due to other resources associated with the ALB instance.
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

class ListLoadBalancersResponseBodyLoadBalancersLoadBalancerBillingConfig(DaraModel):
    def __init__(
        self,
        pay_type: str = None,
    ):
        # The billing method. Valid value:
        # 
        # **PostPay**: You are charged for the ALB instance on a pay-as-you-go basis.
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
    ):
        # Indicates whether deletion protection is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.enabled = enabled
        # The time when deletion protection is enabled.
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

class ListLoadBalancersResponseBodyLoadBalancersAccessLogConfig(DaraModel):
    def __init__(
        self,
        log_project: str = None,
        log_store: str = None,
    ):
        # The Simple Log Service project.
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

