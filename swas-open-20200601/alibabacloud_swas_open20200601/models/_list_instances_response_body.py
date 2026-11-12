# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_swas_open20200601 import models as main_models
from darabonba.model import DaraModel

class ListInstancesResponseBody(DaraModel):
    def __init__(
        self,
        instances: List[main_models.ListInstancesResponseBodyInstances] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The array of simple application server information.
        self.instances = instances
        # The page number of the simple application server list.
        self.page_number = page_number
        # The settings for the number of entries per page for paging in a paged query.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of instances returned.
        self.total_count = total_count

    def validate(self):
        if self.instances:
            for v1 in self.instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Instances'] = []
        if self.instances is not None:
            for k1 in self.instances:
                result['Instances'].append(k1.to_map() if k1 else None)

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
        self.instances = []
        if m.get('Instances') is not None:
            for k1 in m.get('Instances'):
                temp_model = main_models.ListInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListInstancesResponseBodyInstances(DaraModel):
    def __init__(
        self,
        business_status: str = None,
        charge_type: str = None,
        combination: bool = None,
        combination_instance_id: str = None,
        commodity_code: str = None,
        creation_time: str = None,
        ddos_status: str = None,
        disable_reason: str = None,
        disks: List[main_models.ListInstancesResponseBodyInstancesDisks] = None,
        expired_time: str = None,
        image: main_models.ListInstancesResponseBodyInstancesImage = None,
        image_id: str = None,
        inner_ip_address: str = None,
        instance_id: str = None,
        instance_name: str = None,
        network_attributes: List[main_models.ListInstancesResponseBodyInstancesNetworkAttributes] = None,
        plan_id: str = None,
        plan_type: str = None,
        public_ip_address: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_spec: main_models.ListInstancesResponseBodyInstancesResourceSpec = None,
        status: str = None,
        tags: List[main_models.ListInstancesResponseBodyInstancesTags] = None,
        uuid: str = None,
    ):
        # The server status. Valid values:
        # 
        # - Normal: Normal.
        # - Expired: Expired.
        # - Overdue: Overdue payment.
        self.business_status = business_status
        # The billing method.
        self.charge_type = charge_type
        # Specifies whether the plan is a combination plan.
        self.combination = combination
        # The combination plan instance ID.
        self.combination_instance_id = combination_instance_id
        # The commodity code of the instance.
        self.commodity_code = commodity_code
        # The creation time. The time is displayed in UTC in the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the yyyy-MM-ddTHH:mm:ssZ format.
        self.creation_time = creation_time
        # The DDoS status. Valid values:
        # 
        # - Normal: Normal.
        # - BlackHole: Blackhole filtering is activated.
        # - Defense: Traffic is being scrubbed.
        self.ddos_status = ddos_status
        # The reason why the resource is disabled. Valid values:
        # 
        # - FINANCIAL: The resource is locked due to an overdue payment.
        # - SECURITY: The resource is locked due to security reasons.
        # - EXPIRED: The instance has expired.
        self.disable_reason = disable_reason
        # The array of cloud disk information for the simple application server.
        self.disks = disks
        # The expiration time. The time is displayed in UTC in the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the yyyy-MM-ddTHH:mm:ssZ format.
        self.expired_time = expired_time
        # The image information.
        self.image = image
        # The image ID.
        self.image_id = image_id
        # The internal IP address.
        self.inner_ip_address = inner_ip_address
        # The instance ID.
        self.instance_id = instance_id
        # The server name.
        self.instance_name = instance_name
        # The network attributes.
        self.network_attributes = network_attributes
        # The plan ID.
        self.plan_id = plan_id
        # The plan type. Valid values:
        # 
        # - NORMAL: general-purpose.
        # - CAPACITY: storage-optimized.
        # - PREVIOUS: previous generation.
        # - MULTI_IP: multi-public-IP.
        # - INTERNATIONAL: international.
        # 
        # > For more information, see [Instance families](https://help.aliyun.com/document_detail/2861773.html).
        self.plan_type = plan_type
        # The public IP address.
        self.public_ip_address = public_ip_address
        # The region ID.
        self.region_id = region_id
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id
        # The resource specifications.
        self.resource_spec = resource_spec
        # The instance status. Valid values:
        # 
        # - Pending: The instance is being prepared.
        # - Starting: The instance is starting.
        # - Running: The instance is running.
        # - Stopping: The instance is stopping.
        # - Stopped: The instance is stopped.
        # - Resetting: The instance is being reset.
        # - Upgrading: The instance is being upgraded.
        # - Disabled: The instance is unavailable.
        self.status = status
        # The tags of the instance.
        self.tags = tags
        # The UUID of the instance.
        self.uuid = uuid

    def validate(self):
        if self.disks:
            for v1 in self.disks:
                 if v1:
                    v1.validate()
        if self.image:
            self.image.validate()
        if self.network_attributes:
            for v1 in self.network_attributes:
                 if v1:
                    v1.validate()
        if self.resource_spec:
            self.resource_spec.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.combination is not None:
            result['Combination'] = self.combination

        if self.combination_instance_id is not None:
            result['CombinationInstanceId'] = self.combination_instance_id

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.ddos_status is not None:
            result['DdosStatus'] = self.ddos_status

        if self.disable_reason is not None:
            result['DisableReason'] = self.disable_reason

        result['Disks'] = []
        if self.disks is not None:
            for k1 in self.disks:
                result['Disks'].append(k1.to_map() if k1 else None)

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.image is not None:
            result['Image'] = self.image.to_map()

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.inner_ip_address is not None:
            result['InnerIpAddress'] = self.inner_ip_address

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        result['NetworkAttributes'] = []
        if self.network_attributes is not None:
            for k1 in self.network_attributes:
                result['NetworkAttributes'].append(k1.to_map() if k1 else None)

        if self.plan_id is not None:
            result['PlanId'] = self.plan_id

        if self.plan_type is not None:
            result['PlanType'] = self.plan_type

        if self.public_ip_address is not None:
            result['PublicIpAddress'] = self.public_ip_address

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_spec is not None:
            result['ResourceSpec'] = self.resource_spec.to_map()

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('Combination') is not None:
            self.combination = m.get('Combination')

        if m.get('CombinationInstanceId') is not None:
            self.combination_instance_id = m.get('CombinationInstanceId')

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DdosStatus') is not None:
            self.ddos_status = m.get('DdosStatus')

        if m.get('DisableReason') is not None:
            self.disable_reason = m.get('DisableReason')

        self.disks = []
        if m.get('Disks') is not None:
            for k1 in m.get('Disks'):
                temp_model = main_models.ListInstancesResponseBodyInstancesDisks()
                self.disks.append(temp_model.from_map(k1))

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('Image') is not None:
            temp_model = main_models.ListInstancesResponseBodyInstancesImage()
            self.image = temp_model.from_map(m.get('Image'))

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('InnerIpAddress') is not None:
            self.inner_ip_address = m.get('InnerIpAddress')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        self.network_attributes = []
        if m.get('NetworkAttributes') is not None:
            for k1 in m.get('NetworkAttributes'):
                temp_model = main_models.ListInstancesResponseBodyInstancesNetworkAttributes()
                self.network_attributes.append(temp_model.from_map(k1))

        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')

        if m.get('PlanType') is not None:
            self.plan_type = m.get('PlanType')

        if m.get('PublicIpAddress') is not None:
            self.public_ip_address = m.get('PublicIpAddress')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceSpec') is not None:
            temp_model = main_models.ListInstancesResponseBodyInstancesResourceSpec()
            self.resource_spec = temp_model.from_map(m.get('ResourceSpec'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListInstancesResponseBodyInstancesTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

class ListInstancesResponseBodyInstancesTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the instance.
        self.key = key
        # The tag value of the instance.
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

class ListInstancesResponseBodyInstancesResourceSpec(DaraModel):
    def __init__(
        self,
        bandwidth: int = None,
        cpu: int = None,
        disk_category: str = None,
        disk_size: int = None,
        flow: float = None,
        memory: float = None,
    ):
        # The bandwidth. Unit: Mbit/s.
        self.bandwidth = bandwidth
        # The number of vCPUs.
        self.cpu = cpu
        # The cloud disk category. Valid values:
        # 
        # - ESSD: ESSD at performance level (PL) 0.
        # - SSD: Standard SSD.
        # - CLOUD_EFFICIENCY: Ultra disk.
        self.disk_category = disk_category
        # The cloud disk size. Unit: GiB.
        self.disk_size = disk_size
        # The data transfer quota.
        # 
        # - A value of 0 indicates a bandwidth-based instance.
        # - A non-zero value indicates a data transfer plan-based instance.
        self.flow = flow
        # The memory size. Unit: GiB.
        self.memory = memory

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.disk_category is not None:
            result['DiskCategory'] = self.disk_category

        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size

        if self.flow is not None:
            result['Flow'] = self.flow

        if self.memory is not None:
            result['Memory'] = self.memory

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('DiskCategory') is not None:
            self.disk_category = m.get('DiskCategory')

        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')

        if m.get('Flow') is not None:
            self.flow = m.get('Flow')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        return self

class ListInstancesResponseBodyInstancesNetworkAttributes(DaraModel):
    def __init__(
        self,
        peak_bandwidth: int = None,
        private_ip_address: str = None,
        public_ip_address: str = None,
        public_ip_ddos_status: str = None,
    ):
        # The peak public bandwidth. Unit: Mbit/s.
        self.peak_bandwidth = peak_bandwidth
        # The private IP address.
        self.private_ip_address = private_ip_address
        # The public IP address.
        self.public_ip_address = public_ip_address
        # The DDoS status of the public IP address.
        self.public_ip_ddos_status = public_ip_ddos_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.peak_bandwidth is not None:
            result['PeakBandwidth'] = self.peak_bandwidth

        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address

        if self.public_ip_address is not None:
            result['PublicIpAddress'] = self.public_ip_address

        if self.public_ip_ddos_status is not None:
            result['PublicIpDdosStatus'] = self.public_ip_ddos_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PeakBandwidth') is not None:
            self.peak_bandwidth = m.get('PeakBandwidth')

        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')

        if m.get('PublicIpAddress') is not None:
            self.public_ip_address = m.get('PublicIpAddress')

        if m.get('PublicIpDdosStatus') is not None:
            self.public_ip_ddos_status = m.get('PublicIpDdosStatus')

        return self

class ListInstancesResponseBodyInstancesImage(DaraModel):
    def __init__(
        self,
        image_contact: str = None,
        image_icon_url: str = None,
        image_name: str = None,
        image_type: str = None,
        image_version: str = None,
        os_type: str = None,
    ):
        # The image provider.
        self.image_contact = image_contact
        # The URL of the image icon.
        self.image_icon_url = image_icon_url
        # The image name.
        self.image_name = image_name
        # The image type. Valid values:
        # 
        # - system: system image.
        # - app: application image.
        # - custom: custom image.
        self.image_type = image_type
        # The image version.
        self.image_version = image_version
        # The operating system type.
        self.os_type = os_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_contact is not None:
            result['ImageContact'] = self.image_contact

        if self.image_icon_url is not None:
            result['ImageIconUrl'] = self.image_icon_url

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        if self.image_type is not None:
            result['ImageType'] = self.image_type

        if self.image_version is not None:
            result['ImageVersion'] = self.image_version

        if self.os_type is not None:
            result['OsType'] = self.os_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageContact') is not None:
            self.image_contact = m.get('ImageContact')

        if m.get('ImageIconUrl') is not None:
            self.image_icon_url = m.get('ImageIconUrl')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')

        if m.get('ImageVersion') is not None:
            self.image_version = m.get('ImageVersion')

        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        return self

class ListInstancesResponseBodyInstancesDisks(DaraModel):
    def __init__(
        self,
        category: str = None,
        creation_time: str = None,
        device: str = None,
        disk_charge_type: str = None,
        disk_id: str = None,
        disk_name: str = None,
        disk_tags: List[main_models.ListInstancesResponseBodyInstancesDisksDiskTags] = None,
        disk_type: str = None,
        region_id: str = None,
        remark: str = None,
        resource_group_id: str = None,
        size: int = None,
        status: str = None,
    ):
        # The cloud disk category. Valid values:
        # 
        # - ESSD: ESSD at performance level (PL) 0.
        # - SSD: Standard SSD.
        # - CLOUD_EFFICIENCY: Ultra disk.
        self.category = category
        # The creation time of the instance. The time is displayed in UTC in the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the yyyy-MM-ddTHH:mm:ssZ format.
        self.creation_time = creation_time
        # The device name of the cloud disk on the server.
        self.device = device
        # The billing method of the cloud disk.
        self.disk_charge_type = disk_charge_type
        # The cloud disk ID.
        self.disk_id = disk_id
        # The cloud disk name.
        self.disk_name = disk_name
        # The tag information of the cloud disk.
        self.disk_tags = disk_tags
        # The cloud disk type. Valid values:
        # 
        # - system: system cloud disk.
        # - data: data cloud disk.
        self.disk_type = disk_type
        # The region ID.
        self.region_id = region_id
        # The remarks of the cloud disk.
        self.remark = remark
        # The ID of the resource group to which the cloud disk belongs.
        self.resource_group_id = resource_group_id
        # The cloud disk size. Unit: GiB.
        self.size = size
        # The cloud disk status. Valid values:
        # 
        # - ReIniting: The cloud disk is being initialized.
        # - Creating: The cloud disk is being created.
        # - In_use: The cloud disk is in use.
        # - Available: The cloud disk is unattached.
        # - Attaching: The cloud disk is being mounted.
        # - Detaching: The cloud disk is being unmounted.
        self.status = status

    def validate(self):
        if self.disk_tags:
            for v1 in self.disk_tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.device is not None:
            result['Device'] = self.device

        if self.disk_charge_type is not None:
            result['DiskChargeType'] = self.disk_charge_type

        if self.disk_id is not None:
            result['DiskId'] = self.disk_id

        if self.disk_name is not None:
            result['DiskName'] = self.disk_name

        result['DiskTags'] = []
        if self.disk_tags is not None:
            for k1 in self.disk_tags:
                result['DiskTags'].append(k1.to_map() if k1 else None)

        if self.disk_type is not None:
            result['DiskType'] = self.disk_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.size is not None:
            result['Size'] = self.size

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Device') is not None:
            self.device = m.get('Device')

        if m.get('DiskChargeType') is not None:
            self.disk_charge_type = m.get('DiskChargeType')

        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')

        if m.get('DiskName') is not None:
            self.disk_name = m.get('DiskName')

        self.disk_tags = []
        if m.get('DiskTags') is not None:
            for k1 in m.get('DiskTags'):
                temp_model = main_models.ListInstancesResponseBodyInstancesDisksDiskTags()
                self.disk_tags.append(temp_model.from_map(k1))

        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class ListInstancesResponseBodyInstancesDisksDiskTags(DaraModel):
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

