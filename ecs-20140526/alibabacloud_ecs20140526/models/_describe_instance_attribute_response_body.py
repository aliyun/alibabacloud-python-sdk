# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceAttributeResponseBody(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cpu: int = None,
        creation_time: str = None,
        credit_specification: str = None,
        dedicated_host_attribute: main_models.DescribeInstanceAttributeResponseBodyDedicatedHostAttribute = None,
        description: str = None,
        eip_address: main_models.DescribeInstanceAttributeResponseBodyEipAddress = None,
        enable_jumbo_frame: bool = None,
        enable_network_encryption: bool = None,
        expired_time: str = None,
        host_name: str = None,
        image_id: str = None,
        inner_ip_address: main_models.DescribeInstanceAttributeResponseBodyInnerIpAddress = None,
        instance_charge_type: str = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_network_type: str = None,
        instance_type: str = None,
        internet_charge_type: str = None,
        internet_max_bandwidth_in: int = None,
        internet_max_bandwidth_out: int = None,
        io_optimized: str = None,
        memory: int = None,
        network_options: main_models.DescribeInstanceAttributeResponseBodyNetworkOptions = None,
        operation_locks: main_models.DescribeInstanceAttributeResponseBodyOperationLocks = None,
        public_ip_address: main_models.DescribeInstanceAttributeResponseBodyPublicIpAddress = None,
        region_id: str = None,
        request_id: str = None,
        security_group_ids: main_models.DescribeInstanceAttributeResponseBodySecurityGroupIds = None,
        serial_number: str = None,
        status: str = None,
        stopped_mode: str = None,
        vlan_id: str = None,
        vpc_attributes: main_models.DescribeInstanceAttributeResponseBodyVpcAttributes = None,
        zone_id: str = None,
    ):
        # The ID of the cluster to which the instance belongs.
        # 
        # > This parameter will be removed in the future. To ensure future compatibility, we recommend that you use other parameters.
        self.cluster_id = cluster_id
        # The number of vCPUs.
        self.cpu = cpu
        # The time when the instance was created. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. For more information, see [ISO 8601](https://help.aliyun.com/document_detail/25696.html).
        self.creation_time = creation_time
        # The performance mode of the burstable instance. Valid values:
        # 
        # *   Standard: the standard mode. For more information, see the [Performance modes](~~59977#section-svb-w9d-dju~~) section of the "Overview of burstable instances" topic.
        # *   Unlimited: the unlimited mode. For more information, see the [Performance modes](~~59977#section-svb-w9d-dju~~) section of the "Overview of burstable instances" topic.
        self.credit_specification = credit_specification
        # Details about the dedicated host. It is an array that consists of the DedicatedHostClusterId, DedicatedHostId, and DedicatedHostName parameters.
        self.dedicated_host_attribute = dedicated_host_attribute
        # The description of the instance.
        self.description = description
        # The elastic IP address (EIP) associated with the instance.
        self.eip_address = eip_address
        # Indicates whether the Jumbo Frame feature is enabled for the instance. Valid values:
        # 
        # *   true
        # *   false
        # 
        # For more information, see [MTUs](https://help.aliyun.com/document_detail/200512.html).
        self.enable_jumbo_frame = enable_jumbo_frame
        self.enable_network_encryption = enable_network_encryption
        # The time when the instance expires. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. For more information, see [ISO 8601](https://help.aliyun.com/document_detail/25696.html).
        self.expired_time = expired_time
        # The hostname of the instance.
        self.host_name = host_name
        # The ID of the image that the instance is running.
        self.image_id = image_id
        # The internal IP address of the instance located in the classic network.
        self.inner_ip_address = inner_ip_address
        # The billing method of the instance. Valid values:
        # 
        # *   PrePaid: subscription.
        # *   PostPaid: pay-as-you-go
        self.instance_charge_type = instance_charge_type
        # The instance ID
        self.instance_id = instance_id
        # The instance name.
        self.instance_name = instance_name
        # The network type of the instance. Valid values:
        # 
        # *   classic: classic network
        # *   vpc: VPC
        self.instance_network_type = instance_network_type
        # The instance type.
        self.instance_type = instance_type
        # The billing method for network usage. Valid values:
        # 
        # *   PayByBandwidth
        # *   PayByTraffic
        # 
        # >  When the **pay-by-traffic** billing method is used for network usage, the maximum inbound and outbound bandwidths are used as the upper limits of bandwidths instead of guaranteed performance specifications. In scenarios in which demands exceed resource supplies, the maximum bandwidths may not be reached. If you want guaranteed bandwidths for your instance, use the **pay-by-bandwidth** billing method for network usage.
        self.internet_charge_type = internet_charge_type
        # The maximum inbound public bandwidth. Unit: Mbit/s.
        self.internet_max_bandwidth_in = internet_max_bandwidth_in
        # The maximum outbound public bandwidth. Unit: Mbit/s.
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        # Indicates whether the ECS instance is I/O optimized. Valid values:
        # 
        # *   optimized: The ECS instance is I/O optimized.
        # *   none: The ECS instance is not I/O optimized.
        self.io_optimized = io_optimized
        # The memory size of the instance. Unit: MiB.
        self.memory = memory
        # Details about network options.
        # 
        # > This parameter is in invitational preview and is not publicly available.
        self.network_options = network_options
        # The reason why the instance was locked. Valid values:
        # 
        # *   financial: The dedicated host was locked due to overdue payments.
        # *   security: The instance was locked due to security reasons.
        # *   recycling: The spot instance was locked and pending release.
        # *   dedicatedhostfinancial: The instance was locked due to overdue payments for the dedicated host.
        # *   refunded: The instance was locked because a refund was made for the instance.
        self.operation_locks = operation_locks
        # The public IP address of the instance.
        self.public_ip_address = public_ip_address
        # The ID of the region in which the instance resides.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # The IDs of the security groups to which the instance belongs.
        self.security_group_ids = security_group_ids
        # The serial number of the instance.
        self.serial_number = serial_number
        # The status of the instance. Valid values:
        # 
        # *   Pending: The instance is being created.
        # *   Running: The instance is running.
        # *   Starting: The instance is being started.
        # *   Stopping: The instance is being stopped.
        # *   Stopped: The instance is stopped.
        self.status = status
        # Indicates whether the system implements billing after the instance is stopped. Valid values:
        # 
        # *   KeepCharging: The instance is stopped in standard mode. The billing of the instance continues after the instance is stopped, and resources are retained for the instance.
        # *   StopCharging: The instance is stopped in economical mode. The billing of some resources of the instance stops after the instance is stopped. When the instance is stopped, its resources such as vCPUs, memory, and public IP address are released. The instance may be unable to start again if some required resources are out of stock in the current region.
        # *   Not-applicable: The instance does not support economical mode.
        self.stopped_mode = stopped_mode
        # The virtual LAN (VLAN) ID of the instance.
        # 
        # > This parameter will be removed in the future. To ensure future compatibility, we recommend that you use other parameters.
        self.vlan_id = vlan_id
        # The VPC attributes of the instance.
        self.vpc_attributes = vpc_attributes
        # The ID of the zone in which the instance resides.
        self.zone_id = zone_id

    def validate(self):
        if self.dedicated_host_attribute:
            self.dedicated_host_attribute.validate()
        if self.eip_address:
            self.eip_address.validate()
        if self.inner_ip_address:
            self.inner_ip_address.validate()
        if self.network_options:
            self.network_options.validate()
        if self.operation_locks:
            self.operation_locks.validate()
        if self.public_ip_address:
            self.public_ip_address.validate()
        if self.security_group_ids:
            self.security_group_ids.validate()
        if self.vpc_attributes:
            self.vpc_attributes.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.credit_specification is not None:
            result['CreditSpecification'] = self.credit_specification

        if self.dedicated_host_attribute is not None:
            result['DedicatedHostAttribute'] = self.dedicated_host_attribute.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.eip_address is not None:
            result['EipAddress'] = self.eip_address.to_map()

        if self.enable_jumbo_frame is not None:
            result['EnableJumboFrame'] = self.enable_jumbo_frame

        if self.enable_network_encryption is not None:
            result['EnableNetworkEncryption'] = self.enable_network_encryption

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.host_name is not None:
            result['HostName'] = self.host_name

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.inner_ip_address is not None:
            result['InnerIpAddress'] = self.inner_ip_address.to_map()

        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type

        if self.internet_max_bandwidth_in is not None:
            result['InternetMaxBandwidthIn'] = self.internet_max_bandwidth_in

        if self.internet_max_bandwidth_out is not None:
            result['InternetMaxBandwidthOut'] = self.internet_max_bandwidth_out

        if self.io_optimized is not None:
            result['IoOptimized'] = self.io_optimized

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.network_options is not None:
            result['NetworkOptions'] = self.network_options.to_map()

        if self.operation_locks is not None:
            result['OperationLocks'] = self.operation_locks.to_map()

        if self.public_ip_address is not None:
            result['PublicIpAddress'] = self.public_ip_address.to_map()

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids.to_map()

        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number

        if self.status is not None:
            result['Status'] = self.status

        if self.stopped_mode is not None:
            result['StoppedMode'] = self.stopped_mode

        if self.vlan_id is not None:
            result['VlanId'] = self.vlan_id

        if self.vpc_attributes is not None:
            result['VpcAttributes'] = self.vpc_attributes.to_map()

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('CreditSpecification') is not None:
            self.credit_specification = m.get('CreditSpecification')

        if m.get('DedicatedHostAttribute') is not None:
            temp_model = main_models.DescribeInstanceAttributeResponseBodyDedicatedHostAttribute()
            self.dedicated_host_attribute = temp_model.from_map(m.get('DedicatedHostAttribute'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EipAddress') is not None:
            temp_model = main_models.DescribeInstanceAttributeResponseBodyEipAddress()
            self.eip_address = temp_model.from_map(m.get('EipAddress'))

        if m.get('EnableJumboFrame') is not None:
            self.enable_jumbo_frame = m.get('EnableJumboFrame')

        if m.get('EnableNetworkEncryption') is not None:
            self.enable_network_encryption = m.get('EnableNetworkEncryption')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('InnerIpAddress') is not None:
            temp_model = main_models.DescribeInstanceAttributeResponseBodyInnerIpAddress()
            self.inner_ip_address = temp_model.from_map(m.get('InnerIpAddress'))

        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')

        if m.get('InternetMaxBandwidthIn') is not None:
            self.internet_max_bandwidth_in = m.get('InternetMaxBandwidthIn')

        if m.get('InternetMaxBandwidthOut') is not None:
            self.internet_max_bandwidth_out = m.get('InternetMaxBandwidthOut')

        if m.get('IoOptimized') is not None:
            self.io_optimized = m.get('IoOptimized')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('NetworkOptions') is not None:
            temp_model = main_models.DescribeInstanceAttributeResponseBodyNetworkOptions()
            self.network_options = temp_model.from_map(m.get('NetworkOptions'))

        if m.get('OperationLocks') is not None:
            temp_model = main_models.DescribeInstanceAttributeResponseBodyOperationLocks()
            self.operation_locks = temp_model.from_map(m.get('OperationLocks'))

        if m.get('PublicIpAddress') is not None:
            temp_model = main_models.DescribeInstanceAttributeResponseBodyPublicIpAddress()
            self.public_ip_address = temp_model.from_map(m.get('PublicIpAddress'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SecurityGroupIds') is not None:
            temp_model = main_models.DescribeInstanceAttributeResponseBodySecurityGroupIds()
            self.security_group_ids = temp_model.from_map(m.get('SecurityGroupIds'))

        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StoppedMode') is not None:
            self.stopped_mode = m.get('StoppedMode')

        if m.get('VlanId') is not None:
            self.vlan_id = m.get('VlanId')

        if m.get('VpcAttributes') is not None:
            temp_model = main_models.DescribeInstanceAttributeResponseBodyVpcAttributes()
            self.vpc_attributes = temp_model.from_map(m.get('VpcAttributes'))

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeInstanceAttributeResponseBodyVpcAttributes(DaraModel):
    def __init__(
        self,
        nat_ip_address: str = None,
        private_ip_address: main_models.DescribeInstanceAttributeResponseBodyVpcAttributesPrivateIpAddress = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The NAT IP address of the instance. It is used by ECS instances in different VPCs for communication.
        self.nat_ip_address = nat_ip_address
        # The private IP address of the instance.
        self.private_ip_address = private_ip_address
        # The ID of the vSwitch to which the instance is connected.
        self.v_switch_id = v_switch_id
        # The ID of the VPC.
        self.vpc_id = vpc_id

    def validate(self):
        if self.private_ip_address:
            self.private_ip_address.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.nat_ip_address is not None:
            result['NatIpAddress'] = self.nat_ip_address

        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address.to_map()

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NatIpAddress') is not None:
            self.nat_ip_address = m.get('NatIpAddress')

        if m.get('PrivateIpAddress') is not None:
            temp_model = main_models.DescribeInstanceAttributeResponseBodyVpcAttributesPrivateIpAddress()
            self.private_ip_address = temp_model.from_map(m.get('PrivateIpAddress'))

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class DescribeInstanceAttributeResponseBodyVpcAttributesPrivateIpAddress(DaraModel):
    def __init__(
        self,
        ip_address: List[str] = None,
    ):
        self.ip_address = ip_address

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')

        return self

class DescribeInstanceAttributeResponseBodySecurityGroupIds(DaraModel):
    def __init__(
        self,
        security_group_id: List[str] = None,
    ):
        self.security_group_id = security_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        return self

class DescribeInstanceAttributeResponseBodyPublicIpAddress(DaraModel):
    def __init__(
        self,
        ip_address: List[str] = None,
    ):
        self.ip_address = ip_address

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')

        return self

class DescribeInstanceAttributeResponseBodyOperationLocks(DaraModel):
    def __init__(
        self,
        lock_reason: List[main_models.DescribeInstanceAttributeResponseBodyOperationLocksLockReason] = None,
    ):
        self.lock_reason = lock_reason

    def validate(self):
        if self.lock_reason:
            for v1 in self.lock_reason:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LockReason'] = []
        if self.lock_reason is not None:
            for k1 in self.lock_reason:
                result['LockReason'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.lock_reason = []
        if m.get('LockReason') is not None:
            for k1 in m.get('LockReason'):
                temp_model = main_models.DescribeInstanceAttributeResponseBodyOperationLocksLockReason()
                self.lock_reason.append(temp_model.from_map(k1))

        return self

class DescribeInstanceAttributeResponseBodyOperationLocksLockReason(DaraModel):
    def __init__(
        self,
        lock_reason: str = None,
    ):
        # The reason why the instance was locked. Valid values:
        # 
        # *   financial: The instance was locked due to overdue payments.
        # *   security: The instance was locked due to security reasons.
        # *   recycling: The spot instance was locked and pending release.
        # *   dedicatedhostfinancial: The instance was locked due to overdue payments for the dedicated host.
        # *   refunded: The instance was locked because a refund is made for the instance.
        self.lock_reason = lock_reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')

        return self

class DescribeInstanceAttributeResponseBodyNetworkOptions(DaraModel):
    def __init__(
        self,
        bandwidth_weighting: str = None,
        enable_jumbo_frame: bool = None,
        enable_network_encryption: bool = None,
    ):
        # The bandwidth weight.
        # 
        # The supported values vary with instance types. You can query the bandwidth weights supported by the current instance type by using the DescribeInstanceTypes.
        # 
        # Valid values:
        # 
        # *   Vpc-L1.
        # *   Vpc-L2.
        # *   Ebs-L1.
        # *   Ebs-L2.
        # *   Default.
        self.bandwidth_weighting = bandwidth_weighting
        self.enable_jumbo_frame = enable_jumbo_frame
        self.enable_network_encryption = enable_network_encryption

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth_weighting is not None:
            result['BandwidthWeighting'] = self.bandwidth_weighting

        if self.enable_jumbo_frame is not None:
            result['EnableJumboFrame'] = self.enable_jumbo_frame

        if self.enable_network_encryption is not None:
            result['EnableNetworkEncryption'] = self.enable_network_encryption

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthWeighting') is not None:
            self.bandwidth_weighting = m.get('BandwidthWeighting')

        if m.get('EnableJumboFrame') is not None:
            self.enable_jumbo_frame = m.get('EnableJumboFrame')

        if m.get('EnableNetworkEncryption') is not None:
            self.enable_network_encryption = m.get('EnableNetworkEncryption')

        return self

class DescribeInstanceAttributeResponseBodyInnerIpAddress(DaraModel):
    def __init__(
        self,
        ip_address: List[str] = None,
    ):
        self.ip_address = ip_address

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')

        return self

class DescribeInstanceAttributeResponseBodyEipAddress(DaraModel):
    def __init__(
        self,
        allocation_id: str = None,
        bandwidth: int = None,
        internet_charge_type: str = None,
        ip_address: str = None,
    ):
        # The ID of the EIP.
        self.allocation_id = allocation_id
        # The maximum public bandwidth of the EIP. Unit: Mbit/s.
        self.bandwidth = bandwidth
        # The billing method for network usage. Valid values:
        # 
        # *   PayByBandwidth
        # *   PayByTraffic
        # 
        # >  When the **pay-by-traffic** billing method is used for network usage, the maximum inbound and outbound bandwidths are used as the upper limits of bandwidths instead of guaranteed performance specifications. In scenarios in which demands exceed resource supplies, the maximum bandwidths may not be reached. If you want guaranteed bandwidths for your instance, use the **pay-by-bandwidth** billing method for network usage.
        self.internet_charge_type = internet_charge_type
        # The ID of the elastic IP address (EIP).
        self.ip_address = ip_address

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocation_id is not None:
            result['AllocationId'] = self.allocation_id

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type

        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationId') is not None:
            self.allocation_id = m.get('AllocationId')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')

        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')

        return self

class DescribeInstanceAttributeResponseBodyDedicatedHostAttribute(DaraModel):
    def __init__(
        self,
        dedicated_host_id: str = None,
        dedicated_host_name: str = None,
    ):
        # The ID of the dedicated host.
        self.dedicated_host_id = dedicated_host_id
        # The name of the dedicated host.
        self.dedicated_host_name = dedicated_host_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id

        if self.dedicated_host_name is not None:
            result['DedicatedHostName'] = self.dedicated_host_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')

        if m.get('DedicatedHostName') is not None:
            self.dedicated_host_name = m.get('DedicatedHostName')

        return self

