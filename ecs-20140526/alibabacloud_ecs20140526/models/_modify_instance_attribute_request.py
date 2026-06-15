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
        # The performance mode of the burstable performance instance. Valid values:
        # 
        # - Standard: standard mode.
        # 
        # - Unlimited: unlimited mode.
        # 
        # For more information about the performance modes of burstable performance instances, see [Overview of burstable performance instances](https://help.aliyun.com/document_detail/59977.html).
        self.credit_specification = credit_specification
        # Specifies whether to enable deletion protection for the instance. This setting prevents the instance from being released from the console or by calling the [DeleteInstance](https://help.aliyun.com/document_detail/25507.html) operation.
        # 
        # > This feature applies only to pay-as-you-go instances and protects instances only from manual release operations. It does not affect system-initiated release operations.
        self.deletion_protection = deletion_protection
        # The instance description. The description must be 2 to 256 characters long and cannot start with `http://` or `https://`.
        self.description = description
        # Specifies whether to enable jumbo frames. When jumbo frames are enabled, the MTU of the instance is 8500. When jumbo frames are disabled, the MTU of the instance is 1500. Valid values:
        # 
        # - true
        # 
        # - false
        # 
        # Note the following when you use this parameter:
        # 
        # - The instance must be in the `Running` or `Stopped` state.
        # 
        # - The instance must be in a VPC.
        # 
        # - Only some instance types support jumbo frames. For more information, see [ECS instance MTU](https://help.aliyun.com/document_detail/200512.html).
        self.enable_jumbo_frame = enable_jumbo_frame
        # Specifies whether to enable VPC network traffic encryption. Valid values:
        # 
        # - true
        # 
        # - false
        # 
        # > This parameter is in invitation-only preview and is not publicly available.
        self.enable_network_encryption = enable_network_encryption
        # The hostname of the operating system. Note the following when you use this parameter:
        # 
        # - The instance cannot be in the `Pending` or `Starting` state. Otherwise, the specified hostname and the `/etc/hosts` configuration may not take effect. You can call the [DescribeInstances](https://help.aliyun.com/document_detail/25506.html) operation to query the current state of the instance.
        # 
        # - The new hostname takes effect after you restart the instance from the ECS console (see [Restart an instance](https://help.aliyun.com/document_detail/25440.html)) or by calling the [RebootInstance](https://help.aliyun.com/document_detail/25502.html) operation. Restarting the instance from within its operating system does not apply the change.
        # 
        # The hostname must meet the following requirements for different operating systems:
        # 
        # - For Windows Server instances: The hostname must be 2 to 15 characters long and contain letters, digits, and hyphens (-). It cannot start or end with a hyphen, contain consecutive hyphens, or consist of only digits.
        # 
        # - For other types of instances (such as Linux): The hostname must be 2 to 64 characters long. You can use periods (.) to separate the hostname into segments. Each segment can contain letters, digits, and hyphens (-). The hostname cannot start or end with a period or hyphen, and cannot contain consecutive periods or hyphens.
        self.host_name = host_name
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The instance name. The name must be 2 to 128 characters long. It must start with a letter or a Chinese character and cannot start with `http://` or `https://`. The name can contain digits, colons (:), underscores (_), and hyphens (-).
        self.instance_name = instance_name
        # The number of queues for the primary network interface. Note the following when you use this parameter:
        # 
        # - The instance must be in the `Stopped` state.
        # 
        # - The value cannot exceed the maximum number of queues that the instance type supports for a single network interface. The total number of queues across all network interfaces of the instance cannot exceed the total queue quota that the instance type supports. You can call the [DescribeInstanceTypes](https://help.aliyun.com/document_detail/25620.html) operation to query the maximum number of queues per network interface and the total queue quota for an instance type.
        # 
        # - If you set this parameter to -1, the number of queues for the primary network interface is reset to the default value for the instance type. You can call the [DescribeInstanceTypes](https://help.aliyun.com/document_detail/25620.html) operation to query the default number of queues for an elastic network interface of an instance type.
        self.network_interface_queue_number = network_interface_queue_number
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The password of the instance. The password must be 8 to 30 characters long and contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The supported special characters are **()\\~!@#$%^&\\*-_+=|{}[]:;\\"<>,.?/**. For a Windows instance, the password cannot start with a forward slash (/). Note the following when you use this parameter:
        # 
        # - The instance cannot be in the `Starting` state.
        # 
        # - The new password takes effect after you restart the instance from the ECS console (see [Restart an instance](https://help.aliyun.com/document_detail/25440.html)) or by calling the [RebootInstance](https://help.aliyun.com/document_detail/25502.html) operation. Restarting the instance from within its operating system does not apply the change.
        # 
        # > To prevent password exposure, send requests that include the `Password` parameter over HTTPS.
        self.password = password
        # The private DNS name settings for the instance.
        # 
        # For more information about private DNS name resolution, see [ECS private DNS resolution
        # ](https://help.aliyun.com/document_detail/2844797.html).
        self.private_dns_name_options = private_dns_name_options
        # > This parameter is in invitation-only preview and is not publicly available.
        self.recyclable = recyclable
        # > This parameter is in invitation-only preview and is not publicly available.
        self.remote_connection_options = remote_connection_options
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The IDs of security groups to assign to the instance. Note the following when you use this parameter:
        # 
        # - The security group IDs in the array must be unique. The number of security groups that an instance can join is limited. For more information, see [Limits](~~25412#SecurityGroupQuota1~~).
        # 
        # - Specifying this parameter removes the instance from its current security groups. To retain existing security group associations, you must include their IDs in this array.
        # 
        # - You can switch the security group type. However, the specified security groups cannot include both basic and enterprise security groups.
        # 
        # - The security groups must belong to the same VPC as the instance.
        # 
        # - This parameter is not supported for instances in the classic network.
        # 
        # > The change takes effect on the instance after a short delay.
        self.security_group_ids = security_group_ids
        # The user data of the instance. User data should be Base64-encoded before it is passed. Note the following when you use this parameter:
        # 
        # - The user data must comply with the limits described in [Generate user data](https://help.aliyun.com/document_detail/49121.html).
        # 
        # - After you restart the instance, the new user data is available on the instance but is not executed.
        # 
        # > The raw data cannot exceed 32 KB before being encoded. Do not pass confidential information, such as passwords and private keys, in plaintext. If you must pass confidential information, encrypt and then Base64-encode it. On the instance, decrypt the information by using the corresponding decryption method.
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
        # > This parameter is in invitation-only preview and is not publicly available.
        self.password = password
        # > This parameter is in invitation-only preview and is not publicly available.
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
        # Specifies whether to enable resolution of the instance ID-based domain name to an IPv6 address. Valid values:
        # 
        # - true
        # 
        # - false
        # 
        # Default value: false.
        self.enable_instance_id_dns_aaaarecord = enable_instance_id_dns_aaaarecord
        # Specifies whether to enable resolution of the instance ID-based domain name to an IPv4 address. Valid values:
        # 
        # - true
        # 
        # - false
        # 
        # Default value: false.
        self.enable_instance_id_dns_arecord = enable_instance_id_dns_arecord
        # Specifies whether to enable resolution of the IP address-based domain name to an IPv4 address. Valid values:
        # 
        # - true
        # 
        # - false
        # 
        # Default value: false.
        self.enable_ip_dns_arecord = enable_ip_dns_arecord
        # Specifies whether to enable reverse DNS resolution of an IPv4 address to an IP address-based domain name. Valid values:
        # 
        # - true
        # 
        # - false
        # 
        # Default value: false.
        self.enable_ip_dns_ptr_record = enable_ip_dns_ptr_record
        # The hostname type. Valid values:
        # 
        # - Custom: a custom hostname.
        # 
        # - IpBased: an IP address-based hostname.
        # 
        # - InstanceIdBased: an instance ID-based hostname.
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
        # The number of CPU cores. This parameter is not customizable and uses a default value.
        # 
        # <props="china">
        # 
        # For information about the default value, see [Custom CPU options](https://help.aliyun.com/document_detail/145895.html).
        self.core = core
        # The number of threads per core. The total number of vCPUs for an ECS instance is the value of `CpuOptions.Core` multiplied by the value of `CpuOptions.ThreadsPerCore`.
        # 
        # - Setting `CpuOptions.ThreadsPerCore` to 1 disables hyper-threading.
        # 
        # - Only some instance types support specifying the number of threads per core.
        # 
        # <props="china">
        # 
        # For information about the valid values and default value, see [Custom CPU options](https://help.aliyun.com/document_detail/145895.html).
        self.threads_per_core = threads_per_core
        # The CPU topology type of the instance. Valid values:
        # 
        # - ContinuousCoreToHTMapping: The hyper-threads of the same core are contiguous.
        # 
        # - DiscreteCoreToHTMapping: The hyper-threads of the same core are discrete.
        # 
        # Default value: None.
        # 
        # Note the following when you use this parameter:
        # 
        # - The instance must be in the `Stopped` state.
        # 
        # > This parameter is supported by only some instance families. See [View and modify the CPU topology](https://help.aliyun.com/document_detail/2636059.html) for a list of supported families.
        self.topology_type = topology_type
        # > This parameter is in invitation-only preview and is not publicly available.
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

