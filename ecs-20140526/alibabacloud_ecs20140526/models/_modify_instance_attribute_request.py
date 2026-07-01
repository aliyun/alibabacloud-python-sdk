# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class ModifyInstanceAttributeRequest(DaraModel):
    def __init__(
        self,
        cpu_options: main_models.ModifyInstanceAttributeRequestCpuOptions = None,
        credit_specification: str = None,
        deletion_protection: bool = None,
        description: str = None,
        enable_jumbo_frame: bool = None,
        enable_network_encryption: bool = None,
        host_name: str = None,
        instance_id: str = None,
        instance_name: str = None,
        network_interface_queue_number: int = None,
        owner_account: str = None,
        owner_id: int = None,
        password: str = None,
        private_dns_name_options: main_models.ModifyInstanceAttributeRequestPrivateDnsNameOptions = None,
        recyclable: bool = None,
        remote_connection_options: main_models.ModifyInstanceAttributeRequestRemoteConnectionOptions = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_group_ids: List[str] = None,
        user_data: str = None,
    ):
        self.cpu_options = cpu_options
        # The running mode of the burstable instance. Valid values:
        # 
        # - Standard: standard mode.
        # - Unlimited: unlimited mode.
        # 
        # For more information about the running modes of burstable instances, see [What are burstable instances?](https://help.aliyun.com/document_detail/59977.html).
        self.credit_specification = credit_specification
        # The release protection attribute of the instance. Specifies whether the instance can be released from the console or by calling [DeleteInstance](https://help.aliyun.com/document_detail/25507.html).
        # 
        # > This attribute applies only to pay-as-you-go instances and only prevents manual release operations. It does not apply to system-initiated release operations.
        self.deletion_protection = deletion_protection
        # The description of the instance. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # Specifies whether to enable the Jumbo Frame feature for the instance MTU. Valid values:
        # 
        # - true: enables the feature.
        # - false: does not enable the feature.
        # 
        # Take note of the following items:
        # - The instance must be in the Running or Stopped state.
        # - The instance must be a VPC-connected instance.
        # - After the Jumbo Frame feature is enabled, the MTU value of the instance changes to 8500. After the feature is disabled, the MTU value reverts to 1500.
        # Only some instance types support the Jumbo Frame feature. For more information, see [ECS instance MTU](https://help.aliyun.com/document_detail/200512.html).
        self.enable_jumbo_frame = enable_jumbo_frame
        # Specifies whether to enable VPC network traffic encryption. Valid values:
        # 
        # - true: enables the encryption.
        # - false: disables the encryption.
        # > This parameter is in invitational preview and is not publicly available.
        self.enable_network_encryption = enable_network_encryption
        # The hostname of the operating system. Take note of the following items:
        # 
        # - The instance cannot be in the Pending or Starting state. Otherwise, the hostname and `/etc/hosts` configuration may not take effect. You can call [DescribeInstances](https://help.aliyun.com/document_detail/25506.html) to query the current status of the instance.
        # 
        # - The new hostname takes effect after you restart the instance. You can restart the instance in the ECS console (for more information, see [Restart an instance](https://help.aliyun.com/document_detail/25440.html)) or by calling [RebootInstance](https://help.aliyun.com/document_detail/25502.html). Restarting the instance from within the operating system does not take effect.
        # 
        # 
        # The hostname has the following limits for different operating systems:
        # 
        # - Windows Server: The hostname must be 2 to 15 characters in length and can contain uppercase letters, lowercase letters, digits, and hyphens (-). It cannot start or end with a hyphen (-), cannot contain consecutive hyphens (-), and cannot contain only digits.
        # 
        # - Other instances (such as Linux): The hostname must be 2 to 64 characters in length. You can use periods (.) to separate the hostname into multiple segments. Each segment can contain uppercase letters, lowercase letters, digits, and hyphens (-), but cannot contain consecutive periods (.) or hyphens (-). The hostname cannot start or end with a period (.) or hyphen (-).
        self.host_name = host_name
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the instance. The name must be 2 to 128 characters in length. It must start with an uppercase letter, lowercase letter, or Chinese character and cannot start with `http://` or `https://`. The name can contain digits, colons (:), underscores (_), and hyphens (-).
        self.instance_name = instance_name
        # The number of queues for the primary network interface controller (NIC). Take note of the following items:
        # - The instance must be in the Stopped state.
        # - The value cannot exceed the maximum number of queues per NIC allowed by the instance type. The total number of queues for all NICs on the instance cannot exceed the total queue quota allowed by the instance type. You can call [DescribeInstanceTypes](https://help.aliyun.com/document_detail/25620.html) to query the maximum number of queues per NIC and the total queue quota for an instance type.
        # - If you set this parameter to -1, the number of queues for the primary NIC is reset to the default value for the instance type. You can call [DescribeInstanceTypes](https://help.aliyun.com/document_detail/25620.html) to query the default number of Elastic Network Interface (ENI) queues for an instance type.
        self.network_interface_queue_number = network_interface_queue_number
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The password of the instance. The password must be 8 to 30 characters in length and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The following special characters are supported: **()`~!@#$%^&*-_+=|{}[]:;\\"<>,.?/**
        # . For Windows instances, the password cannot start with a forward slash (/). Take note of the following items:
        # 
        # - The instance cannot be in the Starting state.
        # - The new password takes effect after you restart the instance. You can restart the instance in the ECS console (for more information, see [Restart an instance](https://help.aliyun.com/document_detail/25440.html)) or by calling [RebootInstance](https://help.aliyun.com/document_detail/25502.html). Restarting the instance from within the operating system does not take effect.
        # 
        # > If you specify the Password parameter, use HTTPS to send the request to avoid password leaks.
        self.password = password
        # The private domain name configuration of the instance.
        # 
        # 
        # For more information about private private domain resolution, see [ECS private private domain resolution](https://help.aliyun.com/document_detail/2844797.html).
        self.private_dns_name_options = private_dns_name_options
        # > This parameter is in invitational preview and is not publicly available.
        self.recyclable = recyclable
        # > This parameter is in invitational preview and is not publicly available.
        self.remote_connection_options = remote_connection_options
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The IDs of the security groups to which the instance is reassigned. Take note of the following items:
        # 
        # - Security group IDs in the array cannot be duplicated. The maximum length of the array depends on the maximum number of security groups to which the instance can belong. For more information, see [Limits](~~25412#SecurityGroupQuota1~~).
        # - The instance leaves its current security groups. To retain the current security groups, add their IDs to the array.
        # - You can switch between security group types, but the list cannot contain both basic security groups and advanced security groups at the same time.
        # - The security groups must belong to the same VPC as the instance.
        # 
        # > Changes to security groups take effect on the instance shortly after the modification, but a slight delay may occur.
        self.security_group_ids = security_group_ids
        # The instance user data. We recommend that you Base64-encode the data before you pass it in. Take note of the following items:
        # 
        # - The instance must meet the usage limits for instance user data. For more information, see [Create instance user data](https://help.aliyun.com/document_detail/49121.html).
        # - After you restart the instance, the new user data is displayed on the instance but is not run.
        # 
        # > Before Base64 encoding, the raw data cannot exceed 32 KB. Do not pass in sensitive information such as passwords and private keys in plaintext. If you must pass in sensitive information, encrypt the information, Base64-encode it, and then decrypt it in the same way within the instance.
        self.user_data = user_data

    def validate(self):
        if self.cpu_options:
            self.cpu_options.validate()
        if self.private_dns_name_options:
            self.private_dns_name_options.validate()
        if self.remote_connection_options:
            self.remote_connection_options.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu_options is not None:
            result['CpuOptions'] = self.cpu_options.to_map()

        if self.credit_specification is not None:
            result['CreditSpecification'] = self.credit_specification

        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection

        if self.description is not None:
            result['Description'] = self.description

        if self.enable_jumbo_frame is not None:
            result['EnableJumboFrame'] = self.enable_jumbo_frame

        if self.enable_network_encryption is not None:
            result['EnableNetworkEncryption'] = self.enable_network_encryption

        if self.host_name is not None:
            result['HostName'] = self.host_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.network_interface_queue_number is not None:
            result['NetworkInterfaceQueueNumber'] = self.network_interface_queue_number

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.password is not None:
            result['Password'] = self.password

        if self.private_dns_name_options is not None:
            result['PrivateDnsNameOptions'] = self.private_dns_name_options.to_map()

        if self.recyclable is not None:
            result['Recyclable'] = self.recyclable

        if self.remote_connection_options is not None:
            result['RemoteConnectionOptions'] = self.remote_connection_options.to_map()

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuOptions') is not None:
            temp_model = main_models.ModifyInstanceAttributeRequestCpuOptions()
            self.cpu_options = temp_model.from_map(m.get('CpuOptions'))

        if m.get('CreditSpecification') is not None:
            self.credit_specification = m.get('CreditSpecification')

        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnableJumboFrame') is not None:
            self.enable_jumbo_frame = m.get('EnableJumboFrame')

        if m.get('EnableNetworkEncryption') is not None:
            self.enable_network_encryption = m.get('EnableNetworkEncryption')

        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('NetworkInterfaceQueueNumber') is not None:
            self.network_interface_queue_number = m.get('NetworkInterfaceQueueNumber')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('PrivateDnsNameOptions') is not None:
            temp_model = main_models.ModifyInstanceAttributeRequestPrivateDnsNameOptions()
            self.private_dns_name_options = temp_model.from_map(m.get('PrivateDnsNameOptions'))

        if m.get('Recyclable') is not None:
            self.recyclable = m.get('Recyclable')

        if m.get('RemoteConnectionOptions') is not None:
            temp_model = main_models.ModifyInstanceAttributeRequestRemoteConnectionOptions()
            self.remote_connection_options = temp_model.from_map(m.get('RemoteConnectionOptions'))

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class ModifyInstanceAttributeRequestRemoteConnectionOptions(DaraModel):
    def __init__(
        self,
        password: str = None,
        type: str = None,
    ):
        # > This parameter is in invitational preview and is not publicly available.
        self.password = password
        # > This parameter is in invitational preview and is not publicly available.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.password is not None:
            result['Password'] = self.password

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ModifyInstanceAttributeRequestPrivateDnsNameOptions(DaraModel):
    def __init__(
        self,
        enable_instance_id_dns_aaaarecord: bool = None,
        enable_instance_id_dns_arecord: bool = None,
        enable_ip_dns_arecord: bool = None,
        enable_ip_dns_ptr_record: bool = None,
        hostname_type: str = None,
    ):
        # Specifies whether to enable DNS resolution from the instance ID-based domain name to the IPv6 address. Valid values:
        #  
        # - true: enables the resolution.
        # - false: disables the resolution.
        # 
        # Default value: false.
        self.enable_instance_id_dns_aaaarecord = enable_instance_id_dns_aaaarecord
        # Specifies whether to enable DNS resolution from the instance ID-based domain name to the IPv4 address. Valid values:
        #  
        # - true: enables the resolution.
        # - false: disables the resolution.
        # 
        # Default value: false.
        self.enable_instance_id_dns_arecord = enable_instance_id_dns_arecord
        # Specifies whether to enable DNS resolution from the IP-based domain name to the IPv4 address. Valid values:
        # - true: enables the resolution.
        # - false: disables the resolution.
        # 
        # Default value: false.
        self.enable_ip_dns_arecord = enable_ip_dns_arecord
        # Specifies whether to enable reverse DNS resolution from the IPv4 address to the IP-based domain name. Valid values:
        # - true: enables the resolution.
        # - false: disables the resolution.
        # 
        # Default value: false.
        self.enable_ip_dns_ptr_record = enable_ip_dns_ptr_record
        # The hostname type. Valid values:
        # 
        # - Custom: custom.
        # - IpBased: IP-based hostname.
        # - InstanceIdBased: instance ID-based hostname.
        # 
        # Default value: Custom.
        self.hostname_type = hostname_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_instance_id_dns_aaaarecord is not None:
            result['EnableInstanceIdDnsAAAARecord'] = self.enable_instance_id_dns_aaaarecord

        if self.enable_instance_id_dns_arecord is not None:
            result['EnableInstanceIdDnsARecord'] = self.enable_instance_id_dns_arecord

        if self.enable_ip_dns_arecord is not None:
            result['EnableIpDnsARecord'] = self.enable_ip_dns_arecord

        if self.enable_ip_dns_ptr_record is not None:
            result['EnableIpDnsPtrRecord'] = self.enable_ip_dns_ptr_record

        if self.hostname_type is not None:
            result['HostnameType'] = self.hostname_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableInstanceIdDnsAAAARecord') is not None:
            self.enable_instance_id_dns_aaaarecord = m.get('EnableInstanceIdDnsAAAARecord')

        if m.get('EnableInstanceIdDnsARecord') is not None:
            self.enable_instance_id_dns_arecord = m.get('EnableInstanceIdDnsARecord')

        if m.get('EnableIpDnsARecord') is not None:
            self.enable_ip_dns_arecord = m.get('EnableIpDnsARecord')

        if m.get('EnableIpDnsPtrRecord') is not None:
            self.enable_ip_dns_ptr_record = m.get('EnableIpDnsPtrRecord')

        if m.get('HostnameType') is not None:
            self.hostname_type = m.get('HostnameType')

        return self

class ModifyInstanceAttributeRequestCpuOptions(DaraModel):
    def __init__(
        self,
        core: int = None,
        threads_per_core: int = None,
        topology_type: str = None,
        nested_virtualization: str = None,
    ):
        # The number of CPU cores. This parameter does not support custom values and can only use the default value.
        # 
        # <props="china">Default value: see [Customize CPU options](https://help.aliyun.com/document_detail/145895.html).
        self.core = core
        # The number of threads per CPU core. The number of vCPUs of the ECS instance = CpuOptions.Core value × CpuOptions.ThreadsPerCore value.
        # 
        # - CpuOptions.ThreadsPerCore=1 indicates that hyper-threading is disabled.
        # 
        # - Only some instance types support custom thread counts.
        # 
        # <props="china">Valid values and default value: see [Customize CPU options](https://help.aliyun.com/document_detail/145895.html).
        self.threads_per_core = threads_per_core
        # The CPU topology type of the instance. Valid values:
        # 
        # - ContinuousCoreToHTMapping: the hyper-threads of the same core in the CPU topology are continuous.
        # - DiscreteCoreToHTMapping: the hyper-threads of the same core are discrete.
        # 
        # Default value: none.
        # 
        # Take note of the following items:
        # - The instance must be in the Stopped state.
        # 
        # > Only some instance families support this parameter. For information about the supported instance families, see [View and modify the CPU topology structure](https://help.aliyun.com/document_detail/2636059.html).
        self.topology_type = topology_type
        # > This parameter is in invitational preview and is not publicly available.
        self.nested_virtualization = nested_virtualization

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.core is not None:
            result['Core'] = self.core

        if self.threads_per_core is not None:
            result['ThreadsPerCore'] = self.threads_per_core

        if self.topology_type is not None:
            result['TopologyType'] = self.topology_type

        if self.nested_virtualization is not None:
            result['NestedVirtualization'] = self.nested_virtualization

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Core') is not None:
            self.core = m.get('Core')

        if m.get('ThreadsPerCore') is not None:
            self.threads_per_core = m.get('ThreadsPerCore')

        if m.get('TopologyType') is not None:
            self.topology_type = m.get('TopologyType')

        if m.get('NestedVirtualization') is not None:
            self.nested_virtualization = m.get('NestedVirtualization')

        return self

