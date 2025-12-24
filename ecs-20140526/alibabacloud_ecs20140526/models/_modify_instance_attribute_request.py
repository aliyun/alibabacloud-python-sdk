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
        # The performance mode of the burstable instance. Valid values:
        # 
        # *   Standard
        # *   Unlimited
        # 
        # For more information about the performance modes of burstable instances, see [Overview](https://help.aliyun.com/document_detail/59977.html).
        self.credit_specification = credit_specification
        # The release protection attribute of the instance. This parameter specifies whether you can use the ECS console or call the [DeleteInstance](https://help.aliyun.com/document_detail/25507.html) operation to release the instance.
        # 
        # >  This parameter is applicable only to pay-as-you-go instances. The release protection attribute can protect instances against manual releases, but not against automatic releases.
        self.deletion_protection = deletion_protection
        # The description of the instance. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # Specifies whether to enable the Jumbo Frames feature for the instance. Valid values:
        # 
        # *   true: The Jumbo Frame feature is enabled for the instance.
        # *   false: The Jumbo Frame feature is disabled for the instance.
        # 
        # Take note of the following items:
        # 
        # *   The instance must be in the Running (`Running`) or Stopped (`Stopped`) state.
        # *   The instance must reside in a VPC.
        # *   After the Jumbo Frames feature is enabled, the MTU value of the instance is set to 8500. After the Jumbo Frames feature is disabled, the MTU value of the instance is set to 1500. You can enable the Jumbo Frames feature only for specific instance types. For more information, see [Jumbo Frames](https://help.aliyun.com/document_detail/200512.html).
        self.enable_jumbo_frame = enable_jumbo_frame
        self.enable_network_encryption = enable_network_encryption
        # The hostname of the instance. Take note of the following items:
        # 
        # *   The instance cannot be in the Creating (`Pending`) or Starting (`Starting`) state. Otherwise, the new hostname and the configurations in the `/etc/hosts` file may not take effect. You can call the [DescribeInstances](https://help.aliyun.com/document_detail/25506.html) operation to query the status of the instance.
        # *   The parameter takes effect after the instance is restarted. You can restart an instance in the ECS console. For more information, see [Restart an instance](https://help.aliyun.com/document_detail/25440.html). You can also call the [RebootInstance](https://help.aliyun.com/document_detail/25502.html) operation to restart the instance. The parameter cannot take effect if you restart an instance within the operating system.
        # 
        # The following limits apply to the hostnames of instances that run different operating systems:
        # 
        # *   For Windows Server, the hostname must be 2 to 15 characters in length and can contain letters, digits, and hyphens (-). The hostname cannot start or end with a hyphen (-), contain consecutive hyphens (-), or contain only digits.
        # *   For other operating systems such as Linux, the hostname must be 2 to 64 characters in length. You can use periods (.) to separate a hostname into multiple segments. Each segment can contain letters, digits, and hyphens (-). The hostname cannot contain consecutive periods (.) or hyphens (-). The hostname cannot start or end with a period (.) or a hyphen (-).
        self.host_name = host_name
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the instance. The name must be 2 to 128 characters in length. The name must start with a letter and cannot start with `http://` or `https://`. The name can contain letters, digits, colons (:), underscores (_), and hyphens (-).
        self.instance_name = instance_name
        # The number of queues supported by the primary elastic network interface (ENI) of the instance. Take note of the following items:
        # 
        # *   The instance must be in the Stopped (`Stopped`) state.
        # *   The number of queues supported by an ENI cannot exceed the maximum number of queues that the instance type allows for each ENI. The total number of queues on all ENIs on the instance cannot exceed the queue quota that the instance type supports. To query the maximum number of queues that an instance type allows for each ENI and the queue quota for the instance type, call the [DescribeInstanceTypes](https://help.aliyun.com/document_detail/25620.html) operation.
        # *   If you set this parameter to -1, the value is reset to the default value for the instance type. To query the default number of queues of an ENI of each instance type, call the [DescribeInstanceTypes](https://help.aliyun.com/document_detail/25620.html) operation.
        self.network_interface_queue_number = network_interface_queue_number
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The password of the instance. The password must be 8 to 30 characters in length and contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Special characters include **( ) \\` ~ ! @ # $ % ^ & \\* - _ + = | { } [ ] : ; \\" < > , . ? /** The password of a Windows instance cannot start with a forward slash (/). Take note of the following items:
        # 
        # *   The instance cannot be in the Starting (`Starting`) state.
        # *   The parameter takes effect after the instance is restarted. You can restart an instance in the ECS console. For more information, see [Restart an instance](https://help.aliyun.com/document_detail/25440.html). You can also call the [RebootInstance](https://help.aliyun.com/document_detail/25502.html) operation to restart the instance. The parameter cannot take effect if you restart an instance within the operating system.
        # 
        # >  For security reasons, we recommend that you use HTTPS to send requests if `Password` is specified.
        self.password = password
        # The private domain name options of the ECS instance.
        # 
        # For information about private domain name resolution, see [ECS private DNS resolution](https://help.aliyun.com/document_detail/2844797.html).
        self.private_dns_name_options = private_dns_name_options
        # >  This parameter is in invitational preview and is not publicly available.
        self.recyclable = recyclable
        # >  This parameter is in invitational preview and is not publicly available.
        self.remote_connection_options = remote_connection_options
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The IDs of the new security groups to which to assign the instance. Take note of the following items:
        # 
        # *   The security group IDs in the array cannot be duplicate. The length of the array is related to the quota of security groups to which the instance can be assigned. For more information, see the [Security group limits](~~25412#SecurityGroupQuota1~~) section in the "Limits and quotas" topic.
        # *   The instance is moved from the current security groups to the replacement security groups. If you want the instance to remain in the current security groups, add the IDs of the current security groups to the array.
        # *   You can move the instance to security groups of a different type. However, the array cannot contain the IDs of both basic and advanced security groups.
        # *   The security groups and the instance must belong to the same VPC.
        # *   Security groups of instances in the classic network cannot be changed.
        # 
        # >  New security groups become valid for the instance after a short delay.
        self.security_group_ids = security_group_ids
        # The user data of the instance. We recommend that you encode the data in Base64. Take note of the following items:
        # 
        # *   The instance must meet the limits for user data. For more information, see [Initialize an instance by using instance user data](https://help.aliyun.com/document_detail/49121.html).
        # *   After you restart the instance, the new user data is displayed but not run as scripts.
        # 
        # >  The maximum size of the raw data before encoding is 32 KB. We recommend that you do not pass in confidential information such as passwords and private keys in plaintext. If you must pass in confidential information, we recommend that you encrypt and Base64-encode the information before you pass it in. Then, you can decode and decrypt the information in the same way within the instance.
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
        # >  This parameter is in invitational preview and is not publicly available.
        self.password = password
        # >  This parameter is in invitational preview and is not publicly available.
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
        # Specifies whether DNS Resolution from the Instance ID-based Hostname to the Instance Primary Private IPv6 Address (AAAA Record) is enabled. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.enable_instance_id_dns_aaaarecord = enable_instance_id_dns_aaaarecord
        # Specifies whether DNS Resolution from the Instance ID-based Hostname to the Instance Primary Private IPv4 Address (A Record) is enabled. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.enable_instance_id_dns_arecord = enable_instance_id_dns_arecord
        # Specifies whether DNS Resolution from the IP Address-based Hostname to the Instance Primary Private IPv4 Address (A Record) is enabled. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.enable_ip_dns_arecord = enable_ip_dns_arecord
        # Specifies whether Reverse DNS Resolution from the Instance Primary Private IPv4 Address to the IP Address-based Hostname (PTR Record) is enabled. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.enable_ip_dns_ptr_record = enable_ip_dns_ptr_record
        # The type of the hostname. Valid values:
        # 
        # *   Custom: custom hostname.
        # *   IpBased: IP address-based hostname.
        # *   InstanceIdBased: instance ID-based hostname.
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
    ):
        # The number of CPU cores. This parameter cannot be specified but only uses its default value.
        self.core = core
        # The number of threads per CPU core. The following formula is used to calculate the number of vCPUs of the instance: `CpuOptions.Core` value × `CpuOptions.ThreadsPerCore` value.
        # 
        # *   If `CpuOptionsThreadPerCore` is set to 1, Hyper-Threading (HT) is disabled.
        # *   This parameter is applicable only to specific instance types.
        self.threads_per_core = threads_per_core
        # The CPU topology type of the instance. Valid values:
        # 
        # *   ContinuousCoreToHTMapping: The Hyper-Threading (HT) technology allows continuous threads to run on the same core in the CPU topology of the instance.
        # *   DiscreteCoreToHTMapping: The HT technology allows discrete threads to run on the same core.
        # 
        # This parameter is left empty by default.
        # 
        # Take note of the following items:
        # 
        # *   The instance must be in the Stopped (`Stopped`) state.
        # 
        # >  This parameter is supported only for specific instance families. For information about the supported instance families, see [View and modify CPU topologies](https://help.aliyun.com/document_detail/2636059.html).
        self.topology_type = topology_type

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Core') is not None:
            self.core = m.get('Core')

        if m.get('ThreadsPerCore') is not None:
            self.threads_per_core = m.get('ThreadsPerCore')

        if m.get('TopologyType') is not None:
            self.topology_type = m.get('TopologyType')

        return self

