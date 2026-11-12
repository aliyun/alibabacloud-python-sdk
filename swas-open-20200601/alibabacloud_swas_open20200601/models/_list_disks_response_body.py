# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_swas_open20200601 import models as main_models
from darabonba.model import DaraModel

class ListDisksResponseBody(DaraModel):
    def __init__(
        self,
        disks: List[main_models.ListDisksResponseBodyDisks] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The queried disks.
        self.disks = disks
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.disks:
            for v1 in self.disks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Disks'] = []
        if self.disks is not None:
            for k1 in self.disks:
                result['Disks'].append(k1.to_map() if k1 else None)

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
        self.disks = []
        if m.get('Disks') is not None:
            for k1 in m.get('Disks'):
                temp_model = main_models.ListDisksResponseBodyDisks()
                self.disks.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListDisksResponseBodyDisks(DaraModel):
    def __init__(
        self,
        category: str = None,
        creation_time: str = None,
        device: str = None,
        disk_charge_type: str = None,
        disk_id: str = None,
        disk_name: str = None,
        disk_type: str = None,
        instance_id: str = None,
        instance_name: str = None,
        region_id: str = None,
        remark: str = None,
        resource_group_id: str = None,
        size: int = None,
        status: str = None,
        tags: List[main_models.ListDisksResponseBodyDisksTags] = None,
    ):
        # The category of the disk. Valid values:
        # 
        # - ESSD: enhanced SSD (ESSD) of PL0
        # 
        # - SSD: standard SSD
        # 
        # - CLOUD_EFFICIENCY: ultra disk
        self.category = category
        # The time when the disk was created. The time follows the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The device name of the disk after the disk is attached to the simple application server.
        self.device = device
        # The billing method of the disk.
        self.disk_charge_type = disk_charge_type
        # The disk ID.
        self.disk_id = disk_id
        # The name of the disk.
        self.disk_name = disk_name
        # The disk type. Valid values:
        # 
        # - system: system disk
        # 
        # - data: data disk
        self.disk_type = disk_type
        # The ID of the simple application server to which the disk is attached.
        self.instance_id = instance_id
        # The name of the simple application server.
        self.instance_name = instance_name
        # The region ID.
        self.region_id = region_id
        # The remarks of the disk.
        self.remark = remark
        # The ID of the resource group to which the disk belongs.
        self.resource_group_id = resource_group_id
        # The size of the disk. Unit: GB.
        self.size = size
        # The status of the disk. Valid values:
        # 
        # - ReIniting: The disk is being initialized.
        # 
        # - Creating: The disk is being created.
        # 
        # - In_use: The disk is in use.
        # 
        # - Available: The disk can be attached.
        # 
        # - Attaching: The disk is being attached.
        # 
        # - Detaching: The disk is being detached.
        self.status = status
        # The tags that are added to the disks.
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

        if self.disk_type is not None:
            result['DiskType'] = self.disk_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

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

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

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

        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

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

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListDisksResponseBodyDisksTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class ListDisksResponseBodyDisksTags(DaraModel):
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

