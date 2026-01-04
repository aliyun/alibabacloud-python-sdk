# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeDisksResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        disks: main_models.DescribeDisksResponseBodyDisks = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The returned service code. 0 indicates that the request was successful.
        self.code = code
        # The information about the disks.
        self.disks = disks
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page. Maximum value: **50**. Default value: **10**.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of returned pages.
        self.total_count = total_count

    def validate(self):
        if self.disks:
            self.disks.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.disks is not None:
            result['Disks'] = self.disks.to_map()

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

        if m.get('Disks') is not None:
            temp_model = main_models.DescribeDisksResponseBodyDisks()
            self.disks = temp_model.from_map(m.get('Disks'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDisksResponseBodyDisks(DaraModel):
    def __init__(
        self,
        disks: List[main_models.DescribeDisksResponseBodyDisksDisks] = None,
    ):
        self.disks = disks

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.disks = []
        if m.get('Disks') is not None:
            for k1 in m.get('Disks'):
                temp_model = main_models.DescribeDisksResponseBodyDisksDisks()
                self.disks.append(temp_model.from_map(k1))

        return self

class DescribeDisksResponseBodyDisksDisks(DaraModel):
    def __init__(
        self,
        category: str = None,
        creation_time: str = None,
        delete_with_instance: bool = None,
        description: str = None,
        disk_charge_type: str = None,
        disk_id: str = None,
        disk_name: str = None,
        encrypted: bool = None,
        encrypted_key_id: str = None,
        ens_region_id: str = None,
        instance_id: str = None,
        instance_name: str = None,
        portable: bool = None,
        serial_id: str = None,
        size: int = None,
        snapshot_id: str = None,
        status: str = None,
        tags: main_models.DescribeDisksResponseBodyDisksDisksTags = None,
        type: str = None,
    ):
        # The category of the disk.
        # 
        # *   cloud_efficiency: ultra disk.
        # *   cloud_ssd: all-flash disk.
        # *   local_hdd: local HDD.
        # *   local_ssd: local SSD.
        self.category = category
        # The time when the disk was created. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.creation_time = creation_time
        # Indicates whether the disk is released when the instance to which the disk is attached is released. Valid values:
        # 
        # *   true: The disk is released when the associated instance is released.
        # *   false: The disk is retained when the associated instance is released.
        self.delete_with_instance = delete_with_instance
        # The namespace description.
        self.description = description
        # The billing method of the cloud disk or local disk. Valid values:
        # 
        # *   **prepaid**: subscription.
        # *   **postpaid**: pay-as-you-go.
        self.disk_charge_type = disk_charge_type
        # The ID of the disk.
        self.disk_id = disk_id
        # The name of the disk.
        self.disk_name = disk_name
        # Indicates whether the cloud disk is encrypted. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.encrypted = encrypted
        # The ID of the Key Management Service (KMS) key that is used for the cloud disk.
        self.encrypted_key_id = encrypted_key_id
        # The ID of the edge node.
        self.ens_region_id = ens_region_id
        # The ID of the instance.
        self.instance_id = instance_id
        # The name of the instance.
        self.instance_name = instance_name
        # Indicates whether the cloud disk or local disk is removable. Valid values:
        # 
        # *   true: The disk is removable. A removable disk can independently exist and can be attached to or detached from an instance within the same zone.
        # *   false: The disk is not removable. A disk that is not removable cannot independently exist or be attached to or detached from an instance within the same zone.
        # 
        # If disks are of the following categories or types, the **Portable** value is **false** and the disks have the same lifecycle as their attached instances:
        # 
        # *   Local HDDs
        # *   Local SSDs
        # *   Data disks that use the subscription billing method
        self.portable = portable
        # The serial number.
        self.serial_id = serial_id
        # The size of the disk. Unit: MiB.
        self.size = size
        # The ID of the snapshot.
        self.snapshot_id = snapshot_id
        # The status of the disk. Valid values:
        # 
        # *   In-use: The disk is in use.
        # *   Available: The disk can be attached.
        # *   Attaching: The disk is being attached.
        # *   Detaching: The disk is being detached.
        # *   Creating: The disk is being created.
        # *   ReIniting: The disk is being reset.
        self.status = status
        self.tags = tags
        # The type of the cloud disk or local disk. Valid values:
        # 
        # *   1: system disk.
        # *   2: data disk.
        self.type = type

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.delete_with_instance is not None:
            result['DeleteWithInstance'] = self.delete_with_instance

        if self.description is not None:
            result['Description'] = self.description

        if self.disk_charge_type is not None:
            result['DiskChargeType'] = self.disk_charge_type

        if self.disk_id is not None:
            result['DiskId'] = self.disk_id

        if self.disk_name is not None:
            result['DiskName'] = self.disk_name

        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted

        if self.encrypted_key_id is not None:
            result['EncryptedKeyId'] = self.encrypted_key_id

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.portable is not None:
            result['Portable'] = self.portable

        if self.serial_id is not None:
            result['SerialId'] = self.serial_id

        if self.size is not None:
            result['Size'] = self.size

        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DeleteWithInstance') is not None:
            self.delete_with_instance = m.get('DeleteWithInstance')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DiskChargeType') is not None:
            self.disk_charge_type = m.get('DiskChargeType')

        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')

        if m.get('DiskName') is not None:
            self.disk_name = m.get('DiskName')

        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')

        if m.get('EncryptedKeyId') is not None:
            self.encrypted_key_id = m.get('EncryptedKeyId')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('Portable') is not None:
            self.portable = m.get('Portable')

        if m.get('SerialId') is not None:
            self.serial_id = m.get('SerialId')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeDisksResponseBodyDisksDisksTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeDisksResponseBodyDisksDisksTags(DaraModel):
    def __init__(
        self,
        tags: List[main_models.DescribeDisksResponseBodyDisksDisksTagsTags] = None,
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
                temp_model = main_models.DescribeDisksResponseBodyDisksDisksTagsTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class DescribeDisksResponseBodyDisksDisksTagsTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
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

