# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeInstancesResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        instances: main_models.DescribeInstancesResponseBodyInstances = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The returned service code. 0 indicates that the request was successful.
        self.code = code
        # The information about the instance is returned in an array of InstanceAttributesType.
        self.instances = instances
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.instances:
            self.instances.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.instances is not None:
            result['Instances'] = self.instances.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Instances') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstances()
            self.instances = temp_model.from_map(m.get('Instances'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeInstancesResponseBodyInstances(DaraModel):
    def __init__(
        self,
        instance: List[main_models.DescribeInstancesResponseBodyInstancesInstance] = None,
    ):
        self.instance = instance

    def validate(self):
        if self.instance:
            for v1 in self.instance:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Instance'] = []
        if self.instance is not None:
            for k1 in self.instance:
                result['Instance'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance = []
        if m.get('Instance') is not None:
            for k1 in m.get('Instance'):
                temp_model = main_models.DescribeInstancesResponseBodyInstancesInstance()
                self.instance.append(temp_model.from_map(k1))

        return self

class DescribeInstancesResponseBodyInstancesInstance(DaraModel):
    def __init__(
        self,
        auto_release_time: str = None,
        cpu: str = None,
        creation_time: str = None,
        data_disk: main_models.DescribeInstancesResponseBodyInstancesInstanceDataDisk = None,
        deletion_protection: bool = None,
        disk: int = None,
        ens_region_id: str = None,
        expired_time: str = None,
        host_name: str = None,
        image_id: str = None,
        inner_ip_address: main_models.DescribeInstancesResponseBodyInstancesInstanceInnerIpAddress = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_resource_type: str = None,
        instance_type_family: str = None,
        internet_max_bandwidth_in: int = None,
        internet_max_bandwidth_out: int = None,
        key_pair_name: str = None,
        memory: int = None,
        network_attributes: main_models.DescribeInstancesResponseBodyInstancesInstanceNetworkAttributes = None,
        network_interfaces: main_models.DescribeInstancesResponseBodyInstancesInstanceNetworkInterfaces = None,
        osname: str = None,
        private_ip_addresses: main_models.DescribeInstancesResponseBodyInstancesInstancePrivateIpAddresses = None,
        public_ip_address: main_models.DescribeInstancesResponseBodyInstancesInstancePublicIpAddress = None,
        public_ip_addresses: main_models.DescribeInstancesResponseBodyInstancesInstancePublicIpAddresses = None,
        security_group_ids: main_models.DescribeInstancesResponseBodyInstancesInstanceSecurityGroupIds = None,
        service_status: str = None,
        spec_name: str = None,
        spot_strategy: str = None,
        status: str = None,
        system_disk: main_models.DescribeInstancesResponseBodyInstancesInstanceSystemDisk = None,
        tags: main_models.DescribeInstancesResponseBodyInstancesInstanceTags = None,
    ):
        # The automatic release time of the instance.
        self.auto_release_time = auto_release_time
        # The number of vCPUs.
        self.cpu = cpu
        # The time when the instance was created. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.creation_time = creation_time
        # Details of the data disk.
        self.data_disk = data_disk
        self.deletion_protection = deletion_protection
        # The total size of the disk. Unit: MiB.
        self.disk = disk
        # The region ID of the instance.
        self.ens_region_id = ens_region_id
        # The expiration time. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.expired_time = expired_time
        # The hostname of the instance.
        # 
        # *   The hostname cannot start or end with a period (.) or hyphen (-). It cannot contain consecutive periods (.) or hyphens (-).
        # *   For a Windows instance, the hostname must be 2 to 15 characters in length and can contain letters, digits, and hyphens (-). The hostname cannot contain periods (.) or contain only digits.
        # *   For an instance that runs another operating system such as Linux, the hostname must be 2 to 64 characters in length. You can use periods (.) to separate the hostname into multiple segments. Each segment can contain letters, digits, and hyphens (-).
        self.host_name = host_name
        # The ID of the image.
        self.image_id = image_id
        # The private IP addresses of the instances.
        self.inner_ip_address = inner_ip_address
        # The ID of the instance.
        self.instance_id = instance_id
        # The name of the instance.
        self.instance_name = instance_name
        # The category of the instance. Valid values:
        # 
        # *   EnsInstance: ENS instances that you purchase.
        # *   EnsService: ENS instances that belong to edge services.
        # *   BuildMachine: ENS instances that are configured with image builders.
        # *   EnsPostPaidInstance: pay-as-you-go ENS instances that you purchase.
        self.instance_resource_type = instance_resource_type
        # The instance family. Valid values:
        # 
        # *   x86_vm: x86-based computing instance.
        # *   x86_pm: x86-based physical machine.
        # *   x86_bmi: x86-based bare metal instance.
        # *   x86_bm: bare metal instance with the SmartNIC.
        # *   pc_bmi: heterogeneous bare metal instance.
        # *   pc_vm: heterogeneous virtual machine.
        # *   arm_bmi: Arm-based computing instance.
        self.instance_type_family = instance_type_family
        # The maximum outbound bandwidth. Unit: Mbit/s.
        self.internet_max_bandwidth_in = internet_max_bandwidth_in
        # The minimum inbound bandwidth. Unit: Mbit/s.
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        # The name of the SSH key pair.
        self.key_pair_name = key_pair_name
        # The memory size. Unit: MB.
        self.memory = memory
        # Details of the network.
        self.network_attributes = network_attributes
        # The ENI attached to the instance.
        self.network_interfaces = network_interfaces
        # The name of the image.
        self.osname = osname
        # Details of the private IP addresses.
        self.private_ip_addresses = private_ip_addresses
        # The public IP addresses of the instances.
        self.public_ip_address = public_ip_address
        # Details of the public IP addresses.
        self.public_ip_addresses = public_ip_addresses
        # The IDs of the security groups.
        self.security_group_ids = security_group_ids
        # The ID of your Alibaba Cloud account.
        self.service_status = service_status
        # The instance type.
        self.spec_name = spec_name
        # The bidding policy of the preemptible instance.
        self.spot_strategy = spot_strategy
        # The status of the instance. Valid values:
        # 
        # *   Running
        # *   Expired
        # *   Stopped
        self.status = status
        # Details of the system disk.
        self.system_disk = system_disk
        # The tags of the instance.
        # 
        # >  This operation does not return tag information. You can call this operation in combination with the tag-related operations.
        self.tags = tags

    def validate(self):
        if self.data_disk:
            self.data_disk.validate()
        if self.inner_ip_address:
            self.inner_ip_address.validate()
        if self.network_attributes:
            self.network_attributes.validate()
        if self.network_interfaces:
            self.network_interfaces.validate()
        if self.private_ip_addresses:
            self.private_ip_addresses.validate()
        if self.public_ip_address:
            self.public_ip_address.validate()
        if self.public_ip_addresses:
            self.public_ip_addresses.validate()
        if self.security_group_ids:
            self.security_group_ids.validate()
        if self.system_disk:
            self.system_disk.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_release_time is not None:
            result['AutoReleaseTime'] = self.auto_release_time

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.data_disk is not None:
            result['DataDisk'] = self.data_disk.to_map()

        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection

        if self.disk is not None:
            result['Disk'] = self.disk

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.host_name is not None:
            result['HostName'] = self.host_name

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.inner_ip_address is not None:
            result['InnerIpAddress'] = self.inner_ip_address.to_map()

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_resource_type is not None:
            result['InstanceResourceType'] = self.instance_resource_type

        if self.instance_type_family is not None:
            result['InstanceTypeFamily'] = self.instance_type_family

        if self.internet_max_bandwidth_in is not None:
            result['InternetMaxBandwidthIn'] = self.internet_max_bandwidth_in

        if self.internet_max_bandwidth_out is not None:
            result['InternetMaxBandwidthOut'] = self.internet_max_bandwidth_out

        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.network_attributes is not None:
            result['NetworkAttributes'] = self.network_attributes.to_map()

        if self.network_interfaces is not None:
            result['NetworkInterfaces'] = self.network_interfaces.to_map()

        if self.osname is not None:
            result['OSName'] = self.osname

        if self.private_ip_addresses is not None:
            result['PrivateIpAddresses'] = self.private_ip_addresses.to_map()

        if self.public_ip_address is not None:
            result['PublicIpAddress'] = self.public_ip_address.to_map()

        if self.public_ip_addresses is not None:
            result['PublicIpAddresses'] = self.public_ip_addresses.to_map()

        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids.to_map()

        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status

        if self.spec_name is not None:
            result['SpecName'] = self.spec_name

        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy

        if self.status is not None:
            result['Status'] = self.status

        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk.to_map()

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoReleaseTime') is not None:
            self.auto_release_time = m.get('AutoReleaseTime')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DataDisk') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstancesInstanceDataDisk()
            self.data_disk = temp_model.from_map(m.get('DataDisk'))

        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')

        if m.get('Disk') is not None:
            self.disk = m.get('Disk')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('InnerIpAddress') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstancesInstanceInnerIpAddress()
            self.inner_ip_address = temp_model.from_map(m.get('InnerIpAddress'))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceResourceType') is not None:
            self.instance_resource_type = m.get('InstanceResourceType')

        if m.get('InstanceTypeFamily') is not None:
            self.instance_type_family = m.get('InstanceTypeFamily')

        if m.get('InternetMaxBandwidthIn') is not None:
            self.internet_max_bandwidth_in = m.get('InternetMaxBandwidthIn')

        if m.get('InternetMaxBandwidthOut') is not None:
            self.internet_max_bandwidth_out = m.get('InternetMaxBandwidthOut')

        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('NetworkAttributes') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstancesInstanceNetworkAttributes()
            self.network_attributes = temp_model.from_map(m.get('NetworkAttributes'))

        if m.get('NetworkInterfaces') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstancesInstanceNetworkInterfaces()
            self.network_interfaces = temp_model.from_map(m.get('NetworkInterfaces'))

        if m.get('OSName') is not None:
            self.osname = m.get('OSName')

        if m.get('PrivateIpAddresses') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstancesInstancePrivateIpAddresses()
            self.private_ip_addresses = temp_model.from_map(m.get('PrivateIpAddresses'))

        if m.get('PublicIpAddress') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstancesInstancePublicIpAddress()
            self.public_ip_address = temp_model.from_map(m.get('PublicIpAddress'))

        if m.get('PublicIpAddresses') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstancesInstancePublicIpAddresses()
            self.public_ip_addresses = temp_model.from_map(m.get('PublicIpAddresses'))

        if m.get('SecurityGroupIds') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstancesInstanceSecurityGroupIds()
            self.security_group_ids = temp_model.from_map(m.get('SecurityGroupIds'))

        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')

        if m.get('SpecName') is not None:
            self.spec_name = m.get('SpecName')

        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SystemDisk') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstancesInstanceSystemDisk()
            self.system_disk = temp_model.from_map(m.get('SystemDisk'))

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstancesInstanceTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        return self

class DescribeInstancesResponseBodyInstancesInstanceTags(DaraModel):
    def __init__(
        self,
        tags: List[main_models.DescribeInstancesResponseBodyInstancesInstanceTagsTags] = None,
    ):
        self.tags = tags

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeInstancesResponseBodyInstancesInstanceTagsTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class DescribeInstancesResponseBodyInstancesInstanceTagsTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
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

class DescribeInstancesResponseBodyInstancesInstanceSystemDisk(DaraModel):
    def __init__(
        self,
        category: str = None,
        disk_id: str = None,
        disk_name: str = None,
        size: int = None,
        device_type: str = None,
        disk_type: str = None,
        name: str = None,
        storage: int = None,
        uuid: str = None,
    ):
        # The category of the cloud disk or local disk. Valid values:
        # 
        # *   **file**: local disk.
        # *   **pangu**: ultra disk.
        # *   **local_hdd**: local HDD.
        self.category = category
        # The ID of the disk.
        self.disk_id = disk_id
        # The name of the disk.
        self.disk_name = disk_name
        # The size of the disk. Unit: MiB.
        self.size = size
        # The extended field of the disk category. Valid values:
        # 
        # *   **file**: local disk.
        # *   **pangu**: ultra disk.
        # *   **local_hdd**: local HDD.
        self.device_type = device_type
        # The type of the cloud disk or local disk. Valid values:
        # 
        # *   **system**: system disk.
        # *   **data**: data disk.
        self.disk_type = disk_type
        # The name of the disk.
        self.name = name
        # The size of the disk. Unit: MiB.
        self.storage = storage
        # The UUID of the disk.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.disk_id is not None:
            result['DiskId'] = self.disk_id

        if self.disk_name is not None:
            result['DiskName'] = self.disk_name

        if self.size is not None:
            result['Size'] = self.size

        if self.device_type is not None:
            result['device_type'] = self.device_type

        if self.disk_type is not None:
            result['disk_type'] = self.disk_type

        if self.name is not None:
            result['name'] = self.name

        if self.storage is not None:
            result['storage'] = self.storage

        if self.uuid is not None:
            result['uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')

        if m.get('DiskName') is not None:
            self.disk_name = m.get('DiskName')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('device_type') is not None:
            self.device_type = m.get('device_type')

        if m.get('disk_type') is not None:
            self.disk_type = m.get('disk_type')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('storage') is not None:
            self.storage = m.get('storage')

        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')

        return self

class DescribeInstancesResponseBodyInstancesInstanceSecurityGroupIds(DaraModel):
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

class DescribeInstancesResponseBodyInstancesInstancePublicIpAddresses(DaraModel):
    def __init__(
        self,
        public_ip_address: List[main_models.DescribeInstancesResponseBodyInstancesInstancePublicIpAddressesPublicIpAddress] = None,
    ):
        self.public_ip_address = public_ip_address

    def validate(self):
        if self.public_ip_address:
            for v1 in self.public_ip_address:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PublicIpAddress'] = []
        if self.public_ip_address is not None:
            for k1 in self.public_ip_address:
                result['PublicIpAddress'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.public_ip_address = []
        if m.get('PublicIpAddress') is not None:
            for k1 in m.get('PublicIpAddress'):
                temp_model = main_models.DescribeInstancesResponseBodyInstancesInstancePublicIpAddressesPublicIpAddress()
                self.public_ip_address.append(temp_model.from_map(k1))

        return self

class DescribeInstancesResponseBodyInstancesInstancePublicIpAddressesPublicIpAddress(DaraModel):
    def __init__(
        self,
        gate_way: str = None,
        ip: str = None,
        isp: str = None,
    ):
        # The gateway.
        self.gate_way = gate_way
        # The IP address.
        self.ip = ip
        # The Internet service provider (ISP).
        self.isp = isp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gate_way is not None:
            result['GateWay'] = self.gate_way

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.isp is not None:
            result['Isp'] = self.isp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GateWay') is not None:
            self.gate_way = m.get('GateWay')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('Isp') is not None:
            self.isp = m.get('Isp')

        return self

class DescribeInstancesResponseBodyInstancesInstancePublicIpAddress(DaraModel):
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

class DescribeInstancesResponseBodyInstancesInstancePrivateIpAddresses(DaraModel):
    def __init__(
        self,
        private_ip_address: List[main_models.DescribeInstancesResponseBodyInstancesInstancePrivateIpAddressesPrivateIpAddress] = None,
    ):
        self.private_ip_address = private_ip_address

    def validate(self):
        if self.private_ip_address:
            for v1 in self.private_ip_address:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PrivateIpAddress'] = []
        if self.private_ip_address is not None:
            for k1 in self.private_ip_address:
                result['PrivateIpAddress'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.private_ip_address = []
        if m.get('PrivateIpAddress') is not None:
            for k1 in m.get('PrivateIpAddress'):
                temp_model = main_models.DescribeInstancesResponseBodyInstancesInstancePrivateIpAddressesPrivateIpAddress()
                self.private_ip_address.append(temp_model.from_map(k1))

        return self

class DescribeInstancesResponseBodyInstancesInstancePrivateIpAddressesPrivateIpAddress(DaraModel):
    def __init__(
        self,
        gate_way: str = None,
        ip: str = None,
        isp: str = None,
    ):
        # The gateway.
        self.gate_way = gate_way
        # The IP address.
        self.ip = ip
        # The ISP.
        self.isp = isp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gate_way is not None:
            result['GateWay'] = self.gate_way

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.isp is not None:
            result['Isp'] = self.isp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GateWay') is not None:
            self.gate_way = m.get('GateWay')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('Isp') is not None:
            self.isp = m.get('Isp')

        return self

class DescribeInstancesResponseBodyInstancesInstanceNetworkInterfaces(DaraModel):
    def __init__(
        self,
        network_interfaces: List[main_models.DescribeInstancesResponseBodyInstancesInstanceNetworkInterfacesNetworkInterfaces] = None,
    ):
        self.network_interfaces = network_interfaces

    def validate(self):
        if self.network_interfaces:
            for v1 in self.network_interfaces:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NetworkInterfaces'] = []
        if self.network_interfaces is not None:
            for k1 in self.network_interfaces:
                result['NetworkInterfaces'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.network_interfaces = []
        if m.get('NetworkInterfaces') is not None:
            for k1 in m.get('NetworkInterfaces'):
                temp_model = main_models.DescribeInstancesResponseBodyInstancesInstanceNetworkInterfacesNetworkInterfaces()
                self.network_interfaces.append(temp_model.from_map(k1))

        return self

class DescribeInstancesResponseBodyInstancesInstanceNetworkInterfacesNetworkInterfaces(DaraModel):
    def __init__(
        self,
        ipv_6sets: main_models.DescribeInstancesResponseBodyInstancesInstanceNetworkInterfacesNetworkInterfacesIpv6Sets = None,
        mac_address: str = None,
        network_interface_id: str = None,
        primary_ip_address: str = None,
        private_ip_sets: main_models.DescribeInstancesResponseBodyInstancesInstanceNetworkInterfacesNetworkInterfacesPrivateIpSets = None,
        type: str = None,
    ):
        # The IPv6 addresses of the ENI. This parameter has a value only when `AdditionalAttributes.N` is set to `NETWORK_PRIMARY_ENI_IP`.
        self.ipv_6sets = ipv_6sets
        # The MAC address of the ENI.
        self.mac_address = mac_address
        # The ID of the ENI.
        self.network_interface_id = network_interface_id
        # The primary IP address of the ENI.
        self.primary_ip_address = primary_ip_address
        # The private IP addresses of the ENI.
        self.private_ip_sets = private_ip_sets
        # The type of the disk. Valid values:
        # 
        # *   system: system disk.
        # *   data: data disk.
        self.type = type

    def validate(self):
        if self.ipv_6sets:
            self.ipv_6sets.validate()
        if self.private_ip_sets:
            self.private_ip_sets.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipv_6sets is not None:
            result['Ipv6Sets'] = self.ipv_6sets.to_map()

        if self.mac_address is not None:
            result['MacAddress'] = self.mac_address

        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id

        if self.primary_ip_address is not None:
            result['PrimaryIpAddress'] = self.primary_ip_address

        if self.private_ip_sets is not None:
            result['PrivateIpSets'] = self.private_ip_sets.to_map()

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ipv6Sets') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstancesInstanceNetworkInterfacesNetworkInterfacesIpv6Sets()
            self.ipv_6sets = temp_model.from_map(m.get('Ipv6Sets'))

        if m.get('MacAddress') is not None:
            self.mac_address = m.get('MacAddress')

        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')

        if m.get('PrimaryIpAddress') is not None:
            self.primary_ip_address = m.get('PrimaryIpAddress')

        if m.get('PrivateIpSets') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstancesInstanceNetworkInterfacesNetworkInterfacesPrivateIpSets()
            self.private_ip_sets = temp_model.from_map(m.get('PrivateIpSets'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeInstancesResponseBodyInstancesInstanceNetworkInterfacesNetworkInterfacesPrivateIpSets(DaraModel):
    def __init__(
        self,
        private_ip_set: List[main_models.DescribeInstancesResponseBodyInstancesInstanceNetworkInterfacesNetworkInterfacesPrivateIpSetsPrivateIpSet] = None,
    ):
        self.private_ip_set = private_ip_set

    def validate(self):
        if self.private_ip_set:
            for v1 in self.private_ip_set:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PrivateIpSet'] = []
        if self.private_ip_set is not None:
            for k1 in self.private_ip_set:
                result['PrivateIpSet'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.private_ip_set = []
        if m.get('PrivateIpSet') is not None:
            for k1 in m.get('PrivateIpSet'):
                temp_model = main_models.DescribeInstancesResponseBodyInstancesInstanceNetworkInterfacesNetworkInterfacesPrivateIpSetsPrivateIpSet()
                self.private_ip_set.append(temp_model.from_map(k1))

        return self

class DescribeInstancesResponseBodyInstancesInstanceNetworkInterfacesNetworkInterfacesPrivateIpSetsPrivateIpSet(DaraModel):
    def __init__(
        self,
        primary: bool = None,
        private_ip_address: str = None,
    ):
        # Indicates whether the IP address is the primary private IP address. Valid values:
        # 
        # *   true
        # *   false
        self.primary = primary
        # The private IP address.
        # 
        # >  This parameter is available only if ScheduleAreaLevel is set to Region and cannot be configured if ScheduleAreaLevel is set to other values. Otherwise, an error occurs. If you specify a private IP address, the number of instances must be 1. The private IP address takes effect only when the private IP address and the vSwitch ID are not empty.
        self.private_ip_address = private_ip_address

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.primary is not None:
            result['Primary'] = self.primary

        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Primary') is not None:
            self.primary = m.get('Primary')

        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')

        return self

class DescribeInstancesResponseBodyInstancesInstanceNetworkInterfacesNetworkInterfacesIpv6Sets(DaraModel):
    def __init__(
        self,
        ipv_6set: List[main_models.DescribeInstancesResponseBodyInstancesInstanceNetworkInterfacesNetworkInterfacesIpv6SetsIpv6Set] = None,
    ):
        self.ipv_6set = ipv_6set

    def validate(self):
        if self.ipv_6set:
            for v1 in self.ipv_6set:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Ipv6Set'] = []
        if self.ipv_6set is not None:
            for k1 in self.ipv_6set:
                result['Ipv6Set'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ipv_6set = []
        if m.get('Ipv6Set') is not None:
            for k1 in m.get('Ipv6Set'):
                temp_model = main_models.DescribeInstancesResponseBodyInstancesInstanceNetworkInterfacesNetworkInterfacesIpv6SetsIpv6Set()
                self.ipv_6set.append(temp_model.from_map(k1))

        return self

class DescribeInstancesResponseBodyInstancesInstanceNetworkInterfacesNetworkInterfacesIpv6SetsIpv6Set(DaraModel):
    def __init__(
        self,
        ipv_6address: str = None,
    ):
        # IPv6 addresses N of the ENI. You can specify multiple IPv6 addresses. Valid values of N: 1 to 100.
        self.ipv_6address = ipv_6address

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipv_6address is not None:
            result['Ipv6Address'] = self.ipv_6address

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ipv6Address') is not None:
            self.ipv_6address = m.get('Ipv6Address')

        return self

class DescribeInstancesResponseBodyInstancesInstanceNetworkAttributes(DaraModel):
    def __init__(
        self,
        network_id: str = None,
        private_ip_address: main_models.DescribeInstancesResponseBodyInstancesInstanceNetworkAttributesPrivateIpAddress = None,
        v_switch_id: str = None,
    ):
        # The ID of the network.
        self.network_id = network_id
        # Details of the private IP addresses.
        self.private_ip_address = private_ip_address
        # The vSwitch ID.
        self.v_switch_id = v_switch_id

    def validate(self):
        if self.private_ip_address:
            self.private_ip_address.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.network_id is not None:
            result['NetworkId'] = self.network_id

        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address.to_map()

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')

        if m.get('PrivateIpAddress') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstancesInstanceNetworkAttributesPrivateIpAddress()
            self.private_ip_address = temp_model.from_map(m.get('PrivateIpAddress'))

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

class DescribeInstancesResponseBodyInstancesInstanceNetworkAttributesPrivateIpAddress(DaraModel):
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

class DescribeInstancesResponseBodyInstancesInstanceInnerIpAddress(DaraModel):
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

class DescribeInstancesResponseBodyInstancesInstanceDataDisk(DaraModel):
    def __init__(
        self,
        data_disk: List[main_models.DescribeInstancesResponseBodyInstancesInstanceDataDiskDataDisk] = None,
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
                temp_model = main_models.DescribeInstancesResponseBodyInstancesInstanceDataDiskDataDisk()
                self.data_disk.append(temp_model.from_map(k1))

        return self

class DescribeInstancesResponseBodyInstancesInstanceDataDiskDataDisk(DaraModel):
    def __init__(
        self,
        category: str = None,
        disk_id: str = None,
        disk_name: str = None,
        disk_size: int = None,
        encrypt_key_id: str = None,
        encrypted: bool = None,
        size: int = None,
        device_type: str = None,
        disk_type: str = None,
        name: str = None,
        storage: int = None,
        uuid: str = None,
    ):
        # The category of the cloud disk or local disk. Valid values:
        # 
        # *   **file**: local disk.
        # *   **pangu**: ultra disk.
        # *   **local_hdd**: local HDD.
        self.category = category
        # The ID of the disk.
        self.disk_id = disk_id
        # The name of the disk.
        self.disk_name = disk_name
        # The size of the disk. Unit: GiB.
        self.disk_size = disk_size
        # The KMS key ID used by the cloud drive.
        self.encrypt_key_id = encrypt_key_id
        # Specifies whether to encrypt the disk.
        self.encrypted = encrypted
        # The size of the disk. Unit: MiB.
        self.size = size
        # The extended field of the disk category. Valid values:
        # 
        # *   **file**: local disk.
        # *   **pangu**: ultra disk.
        # *   **local_hdd**: local HDD.
        self.device_type = device_type
        # The type of the cloud disk or local disk. Valid values:
        # 
        # **system**: system disk. **data**: data disk.
        self.disk_type = disk_type
        # The name of the disk.
        self.name = name
        # The size of the disk. Unit: MiB.
        self.storage = storage
        # The UUID of the disk.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.disk_id is not None:
            result['DiskId'] = self.disk_id

        if self.disk_name is not None:
            result['DiskName'] = self.disk_name

        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size

        if self.encrypt_key_id is not None:
            result['EncryptKeyId'] = self.encrypt_key_id

        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted

        if self.size is not None:
            result['Size'] = self.size

        if self.device_type is not None:
            result['device_type'] = self.device_type

        if self.disk_type is not None:
            result['disk_type'] = self.disk_type

        if self.name is not None:
            result['name'] = self.name

        if self.storage is not None:
            result['storage'] = self.storage

        if self.uuid is not None:
            result['uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')

        if m.get('DiskName') is not None:
            self.disk_name = m.get('DiskName')

        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')

        if m.get('EncryptKeyId') is not None:
            self.encrypt_key_id = m.get('EncryptKeyId')

        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('device_type') is not None:
            self.device_type = m.get('device_type')

        if m.get('disk_type') is not None:
            self.disk_type = m.get('disk_type')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('storage') is not None:
            self.storage = m.get('storage')

        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')

        return self

