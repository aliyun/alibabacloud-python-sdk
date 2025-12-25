# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeRCInstanceAttributeResponseBody(DaraModel):
    def __init__(
        self,
        auto_renew: bool = None,
        cluster_id: str = None,
        cpu: int = None,
        create_mode: int = None,
        creation_time: str = None,
        credit_specification: str = None,
        data_disks: main_models.DescribeRCInstanceAttributeResponseBodyDataDisks = None,
        db_type: str = None,
        dedicated_host_attribute: main_models.DescribeRCInstanceAttributeResponseBodyDedicatedHostAttribute = None,
        deletion_protection: bool = None,
        deployment_set_id: str = None,
        description: str = None,
        disk_type: str = None,
        ecs_instance_type: str = None,
        eip_address: main_models.DescribeRCInstanceAttributeResponseBodyEipAddress = None,
        enable_jumbo_frame: bool = None,
        expired_time: str = None,
        gpu: int = None,
        gpu_types: str = None,
        host_name: str = None,
        host_type: str = None,
        image_id: str = None,
        inner_ip_address: main_models.DescribeRCInstanceAttributeResponseBodyInnerIpAddress = None,
        instance_charge_type: str = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_network_type: str = None,
        instance_type: str = None,
        internet_charge_type: str = None,
        internet_max_bandwidth_in: int = None,
        internet_max_bandwidth_out: int = None,
        io_optimized: str = None,
        key_pair_name: str = None,
        memory: int = None,
        node_type: str = None,
        operation_locks: main_models.DescribeRCInstanceAttributeResponseBodyOperationLocks = None,
        public_ip_address: main_models.DescribeRCInstanceAttributeResponseBodyPublicIpAddress = None,
        region_id: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        security_group_ids: main_models.DescribeRCInstanceAttributeResponseBodySecurityGroupIds = None,
        serial_number: str = None,
        spot_strategy: str = None,
        status: str = None,
        stopped_mode: str = None,
        system_disk: main_models.DescribeRCInstanceAttributeResponseBodySystemDisk = None,
        tags: main_models.DescribeRCInstanceAttributeResponseBodyTags = None,
        user_data: str = None,
        vlan_id: str = None,
        vpc_attributes: main_models.DescribeRCInstanceAttributeResponseBodyVpcAttributes = None,
        zone_id: str = None,
    ):
        self.auto_renew = auto_renew
        # The ID of the cluster to which the instance belongs.
        # 
        # >  This parameter will be deprecated. We recommend that you use other parameters to ensure compatibility.
        self.cluster_id = cluster_id
        # The number of CPU cores.
        self.cpu = cpu
        self.create_mode = create_mode
        # The time when the instance was created. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The performance mode of the burstable instance.
        self.credit_specification = credit_specification
        # The details of the data disk.
        self.data_disks = data_disks
        self.db_type = db_type
        # The attributes of the dedicated hosts.
        self.dedicated_host_attribute = dedicated_host_attribute
        self.deletion_protection = deletion_protection
        # The ID of the deployment set.
        self.deployment_set_id = deployment_set_id
        # The instance description.
        self.description = description
        # The reserved parameter.
        self.disk_type = disk_type
        # The Elastic Compute Service (ECS) instance family.
        self.ecs_instance_type = ecs_instance_type
        # The elastic IP address (EIP) associated with the instance.
        self.eip_address = eip_address
        # Indicates whether the Jumbo Frame feature is enabled for the instance. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.enable_jumbo_frame = enable_jumbo_frame
        # The expiration time. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time is displayed in UTC.
        self.expired_time = expired_time
        self.gpu = gpu
        self.gpu_types = gpu_types
        # The instance hostname.
        self.host_name = host_name
        # The storage type of the host. Valid values:
        # 
        # *   **dhg_cloud_ssd**: ESSD
        # *   **dhg_local_ssd**: local SSD
        self.host_type = host_type
        # The image ID of the instance.
        self.image_id = image_id
        # The private IP addresses of the instance in the classic network.
        self.inner_ip_address = inner_ip_address
        self.instance_charge_type = instance_charge_type
        # The instance ID.
        self.instance_id = instance_id
        # The instance name.
        self.instance_name = instance_name
        # The network type. Valid values:
        # 
        # *   **classic**
        # *   **vpc**
        self.instance_network_type = instance_network_type
        # The instance type of the instance.
        self.instance_type = instance_type
        # The billing method for network usage. Valid values:
        # 
        # *   **PayByBandwidth**: pay-by-bandwidth
        # *   **PayByTraffic**: pay-by-data-transfer
        # 
        # >  If the **pay-by-traffic** billing method is used for network usage, the maximum inbound and outbound bandwidths are used as the upper limits of bandwidths instead of guaranteed performance specifications. In scenarios in which demands exceed resource supplies, the maximum bandwidths may not be reached. If you want guaranteed bandwidths for your instance, use the **pay-by-bandwidth** billing method for network usage.
        self.internet_charge_type = internet_charge_type
        # The maximum inbound bandwidth from the Internet. Unit: Mbit/s.
        self.internet_max_bandwidth_in = internet_max_bandwidth_in
        # The maximum outbound bandwidth to the Internet. Unit: Mbit/s.
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        # Indicates whether the instance is I/O optimized.
        # 
        # *   **optimized**: The instance is I/O optimized.
        # *   **none**: The instance is not I/O optimized.
        self.io_optimized = io_optimized
        # The name of the key pair.
        self.key_pair_name = key_pair_name
        # The memory capacity of the instance. Unit: MiB.
        self.memory = memory
        self.node_type = node_type
        # The reasons why the instance is locked.
        self.operation_locks = operation_locks
        # The public IP address of the instance.
        self.public_ip_address = public_ip_address
        # The region ID.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        self.resource_group_id = resource_group_id
        # The security groups.
        self.security_group_ids = security_group_ids
        # The serial number of the instance.
        self.serial_number = serial_number
        self.spot_strategy = spot_strategy
        # The instance status. Valid values:
        # 
        # *   **Pending**
        # *   **Running**
        # *   **Starting**
        # *   **Stopping**
        # *   **Stopped**
        self.status = status
        # Indicates whether the billing of the instance continues after the instance is stopped. Valid values:
        # 
        # *   **KeepCharging**: The billing of the instance continues after the instance is stopped, and resources are retained for the instance.
        # *   **StopCharging**: The billing of the instance stops after the instance is stopped. After the instance is stopped, resources such as CPU cores, memory resources, and public IP address are released. The instance may be unable to restart if some required resources are out of stock in the current region.
        # *   **Not-applicable**: The No Fees for Stopped Instances feature is not supported for the instance.
        self.stopped_mode = stopped_mode
        self.system_disk = system_disk
        self.tags = tags
        self.user_data = user_data
        # The virtual LAN (VLAN) ID of the instance.
        # 
        # >  This parameter will be deprecated. We recommend that you use other parameters to ensure compatibility.
        self.vlan_id = vlan_id
        # The virtual private cloud (VPC) attributes of the instance.
        self.vpc_attributes = vpc_attributes
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        if self.data_disks:
            self.data_disks.validate()
        if self.dedicated_host_attribute:
            self.dedicated_host_attribute.validate()
        if self.eip_address:
            self.eip_address.validate()
        if self.inner_ip_address:
            self.inner_ip_address.validate()
        if self.operation_locks:
            self.operation_locks.validate()
        if self.public_ip_address:
            self.public_ip_address.validate()
        if self.security_group_ids:
            self.security_group_ids.validate()
        if self.system_disk:
            self.system_disk.validate()
        if self.tags:
            self.tags.validate()
        if self.vpc_attributes:
            self.vpc_attributes.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.create_mode is not None:
            result['CreateMode'] = self.create_mode

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.credit_specification is not None:
            result['CreditSpecification'] = self.credit_specification

        if self.data_disks is not None:
            result['DataDisks'] = self.data_disks.to_map()

        if self.db_type is not None:
            result['DbType'] = self.db_type

        if self.dedicated_host_attribute is not None:
            result['DedicatedHostAttribute'] = self.dedicated_host_attribute.to_map()

        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection

        if self.deployment_set_id is not None:
            result['DeploymentSetId'] = self.deployment_set_id

        if self.description is not None:
            result['Description'] = self.description

        if self.disk_type is not None:
            result['DiskType'] = self.disk_type

        if self.ecs_instance_type is not None:
            result['EcsInstanceType'] = self.ecs_instance_type

        if self.eip_address is not None:
            result['EipAddress'] = self.eip_address.to_map()

        if self.enable_jumbo_frame is not None:
            result['EnableJumboFrame'] = self.enable_jumbo_frame

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.gpu is not None:
            result['Gpu'] = self.gpu

        if self.gpu_types is not None:
            result['GpuTypes'] = self.gpu_types

        if self.host_name is not None:
            result['HostName'] = self.host_name

        if self.host_type is not None:
            result['HostType'] = self.host_type

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

        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.operation_locks is not None:
            result['OperationLocks'] = self.operation_locks.to_map()

        if self.public_ip_address is not None:
            result['PublicIpAddress'] = self.public_ip_address.to_map()

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids.to_map()

        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number

        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy

        if self.status is not None:
            result['Status'] = self.status

        if self.stopped_mode is not None:
            result['StoppedMode'] = self.stopped_mode

        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk.to_map()

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.user_data is not None:
            result['UserData'] = self.user_data

        if self.vlan_id is not None:
            result['VlanId'] = self.vlan_id

        if self.vpc_attributes is not None:
            result['VpcAttributes'] = self.vpc_attributes.to_map()

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('CreateMode') is not None:
            self.create_mode = m.get('CreateMode')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('CreditSpecification') is not None:
            self.credit_specification = m.get('CreditSpecification')

        if m.get('DataDisks') is not None:
            temp_model = main_models.DescribeRCInstanceAttributeResponseBodyDataDisks()
            self.data_disks = temp_model.from_map(m.get('DataDisks'))

        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        if m.get('DedicatedHostAttribute') is not None:
            temp_model = main_models.DescribeRCInstanceAttributeResponseBodyDedicatedHostAttribute()
            self.dedicated_host_attribute = temp_model.from_map(m.get('DedicatedHostAttribute'))

        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')

        if m.get('DeploymentSetId') is not None:
            self.deployment_set_id = m.get('DeploymentSetId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')

        if m.get('EcsInstanceType') is not None:
            self.ecs_instance_type = m.get('EcsInstanceType')

        if m.get('EipAddress') is not None:
            temp_model = main_models.DescribeRCInstanceAttributeResponseBodyEipAddress()
            self.eip_address = temp_model.from_map(m.get('EipAddress'))

        if m.get('EnableJumboFrame') is not None:
            self.enable_jumbo_frame = m.get('EnableJumboFrame')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')

        if m.get('GpuTypes') is not None:
            self.gpu_types = m.get('GpuTypes')

        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')

        if m.get('HostType') is not None:
            self.host_type = m.get('HostType')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('InnerIpAddress') is not None:
            temp_model = main_models.DescribeRCInstanceAttributeResponseBodyInnerIpAddress()
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

        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('OperationLocks') is not None:
            temp_model = main_models.DescribeRCInstanceAttributeResponseBodyOperationLocks()
            self.operation_locks = temp_model.from_map(m.get('OperationLocks'))

        if m.get('PublicIpAddress') is not None:
            temp_model = main_models.DescribeRCInstanceAttributeResponseBodyPublicIpAddress()
            self.public_ip_address = temp_model.from_map(m.get('PublicIpAddress'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SecurityGroupIds') is not None:
            temp_model = main_models.DescribeRCInstanceAttributeResponseBodySecurityGroupIds()
            self.security_group_ids = temp_model.from_map(m.get('SecurityGroupIds'))

        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')

        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StoppedMode') is not None:
            self.stopped_mode = m.get('StoppedMode')

        if m.get('SystemDisk') is not None:
            temp_model = main_models.DescribeRCInstanceAttributeResponseBodySystemDisk()
            self.system_disk = temp_model.from_map(m.get('SystemDisk'))

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeRCInstanceAttributeResponseBodyTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        if m.get('VlanId') is not None:
            self.vlan_id = m.get('VlanId')

        if m.get('VpcAttributes') is not None:
            temp_model = main_models.DescribeRCInstanceAttributeResponseBodyVpcAttributes()
            self.vpc_attributes = temp_model.from_map(m.get('VpcAttributes'))

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeRCInstanceAttributeResponseBodyVpcAttributes(DaraModel):
    def __init__(
        self,
        nat_ip_address: str = None,
        private_ip_address: main_models.DescribeRCInstanceAttributeResponseBodyVpcAttributesPrivateIpAddress = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The network address translation (NAT) IP address of the instance. The NAT IP address is used by instances in different VPCs for communication.
        self.nat_ip_address = nat_ip_address
        # The private IP addresses of the instance.
        self.private_ip_address = private_ip_address
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The VPC ID.
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
            temp_model = main_models.DescribeRCInstanceAttributeResponseBodyVpcAttributesPrivateIpAddress()
            self.private_ip_address = temp_model.from_map(m.get('PrivateIpAddress'))

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class DescribeRCInstanceAttributeResponseBodyVpcAttributesPrivateIpAddress(DaraModel):
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

class DescribeRCInstanceAttributeResponseBodyTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeRCInstanceAttributeResponseBodyTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeRCInstanceAttributeResponseBodyTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeRCInstanceAttributeResponseBodyTagsTag(DaraModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

class DescribeRCInstanceAttributeResponseBodySystemDisk(DaraModel):
    def __init__(
        self,
        delete_with_instance: bool = None,
        encrypted: str = None,
        system_disk_category: str = None,
        system_disk_performance_level: str = None,
        system_disk_size: int = None,
    ):
        self.delete_with_instance = delete_with_instance
        self.encrypted = encrypted
        self.system_disk_category = system_disk_category
        self.system_disk_performance_level = system_disk_performance_level
        self.system_disk_size = system_disk_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delete_with_instance is not None:
            result['DeleteWithInstance'] = self.delete_with_instance

        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted

        if self.system_disk_category is not None:
            result['SystemDiskCategory'] = self.system_disk_category

        if self.system_disk_performance_level is not None:
            result['SystemDiskPerformanceLevel'] = self.system_disk_performance_level

        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeleteWithInstance') is not None:
            self.delete_with_instance = m.get('DeleteWithInstance')

        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')

        if m.get('SystemDiskCategory') is not None:
            self.system_disk_category = m.get('SystemDiskCategory')

        if m.get('SystemDiskPerformanceLevel') is not None:
            self.system_disk_performance_level = m.get('SystemDiskPerformanceLevel')

        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')

        return self

class DescribeRCInstanceAttributeResponseBodySecurityGroupIds(DaraModel):
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

class DescribeRCInstanceAttributeResponseBodyPublicIpAddress(DaraModel):
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

class DescribeRCInstanceAttributeResponseBodyOperationLocks(DaraModel):
    def __init__(
        self,
        lock_reason: List[main_models.DescribeRCInstanceAttributeResponseBodyOperationLocksLockReason] = None,
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
                temp_model = main_models.DescribeRCInstanceAttributeResponseBodyOperationLocksLockReason()
                self.lock_reason.append(temp_model.from_map(k1))

        return self

class DescribeRCInstanceAttributeResponseBodyOperationLocksLockReason(DaraModel):
    def __init__(
        self,
        lock_reason: str = None,
    ):
        # The reason why the instance is locked. Valid values:
        # 
        # *   **financial**: The instance is locked due to overdue payments.
        # *   **security**: The instance is locked for security purposes.
        # *   **recycling**: The instance is locked because the instance is a preemptible instance and pending to be released.
        # *   **dedicatedhostfinancial**: The instance is locked due to overdue payments for the dedicated host.
        # *   **refunded**: The instance is locked because a refund was made for the instance.
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

class DescribeRCInstanceAttributeResponseBodyInnerIpAddress(DaraModel):
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

class DescribeRCInstanceAttributeResponseBodyEipAddress(DaraModel):
    def __init__(
        self,
        allocation_id: str = None,
        bandwidth: int = None,
        internet_charge_type: str = None,
        ip_address: str = None,
    ):
        # The EIP ID.
        self.allocation_id = allocation_id
        # The maximum Internet bandwidth of the EIP. Unit: Mbit/s.
        self.bandwidth = bandwidth
        # The billing method of the Internet-facing instance. Valid values:
        # 
        # *   **paybytraffic:** pay-by-data-transfer
        # *   **paybybandwidth**: pay-by-bandwidth
        # 
        # >  If the **pay-by-traffic** billing method is used for network usage, the maximum inbound and outbound bandwidths are used as the upper limits of bandwidths instead of guaranteed performance specifications. In scenarios in which demands exceed resource supplies, the maximum bandwidths may not be reached. If you want guaranteed bandwidths for your instance, use the **pay-by-bandwidth** billing method for network usage.
        self.internet_charge_type = internet_charge_type
        # The EIP.
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

class DescribeRCInstanceAttributeResponseBodyDedicatedHostAttribute(DaraModel):
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

class DescribeRCInstanceAttributeResponseBodyDataDisks(DaraModel):
    def __init__(
        self,
        data_disk: List[main_models.DescribeRCInstanceAttributeResponseBodyDataDisksDataDisk] = None,
    ):
        self.data_disk = data_disk

    def validate(self):
        if self.data_disk:
            for v1 in self.data_disk:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataDisk'] = []
        if self.data_disk is not None:
            for k1 in self.data_disk:
                result['DataDisk'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_disk = []
        if m.get('DataDisk') is not None:
            for k1 in m.get('DataDisk'):
                temp_model = main_models.DescribeRCInstanceAttributeResponseBodyDataDisksDataDisk()
                self.data_disk.append(temp_model.from_map(k1))

        return self

class DescribeRCInstanceAttributeResponseBodyDataDisksDataDisk(DaraModel):
    def __init__(
        self,
        category: str = None,
        delete_with_instance: bool = None,
        device: str = None,
        encrypted: str = None,
        performance_level: str = None,
        size: int = None,
        snapshot_id: str = None,
    ):
        # The category of the data disk.
        self.category = category
        # Indicates whether the data disk is released when the instance is released. Valid values:
        # 
        # *   **true**: The data disk is released when the instance is released.
        # *   **false**: The data disk is reserved when the instance is released.
        self.delete_with_instance = delete_with_instance
        self.device = device
        # Indicates whether the data disk is encrypted. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.encrypted = encrypted
        # The performance level of data disk. This parameter is available when the data disk is an Enterprise SSD (ESSD).
        self.performance_level = performance_level
        # The size of the data disk. Unit: GiB.
        self.size = size
        self.snapshot_id = snapshot_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.delete_with_instance is not None:
            result['DeleteWithInstance'] = self.delete_with_instance

        if self.device is not None:
            result['Device'] = self.device

        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted

        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level

        if self.size is not None:
            result['Size'] = self.size

        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('DeleteWithInstance') is not None:
            self.delete_with_instance = m.get('DeleteWithInstance')

        if m.get('Device') is not None:
            self.device = m.get('Device')

        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')

        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')

        return self

