# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DataDisk(DaraModel):
    def __init__(
        self,
        auto_format: bool = None,
        auto_snapshot_policy_id: str = None,
        bursting_enabled: bool = None,
        category: str = None,
        device: str = None,
        disk_name: str = None,
        encrypted: str = None,
        file_system: str = None,
        kms_key_id: str = None,
        mount_target: str = None,
        performance_level: str = None,
        provisioned_iops: int = None,
        size: int = None,
        snapshot_id: str = None,
    ):
        # Specifies whether to mount the data cloud disk.
        self.auto_format = auto_format
        # The ID of the automatic snapshot policy. The cloud disk is automatically backed up based on the snapshot policy.
        # 
        # Default value: empty, which indicates that automatic backup is disabled.
        self.auto_snapshot_policy_id = auto_snapshot_policy_id
        # Specifies whether to enable performance burst for the data cloud disk. Valid values:
        # - true: Yes.
        # - false: No.
        # 
        # This parameter is supported only when DiskCategory is set to cloud_auto. For more information, see [ESSD AutoPL cloud disks](https://help.aliyun.com/document_detail/368372.html).
        self.bursting_enabled = bursting_enabled
        # The type of the data cloud disk. Valid values:
        # 
        # - cloud: Basic cloud disk.
        # - cloud_efficiency: Ultra disk.
        # - cloud_ssd: Standard SSD.
        # - cloud_essd: ESSD.
        # - cloud_auto: ESSD AutoPL cloud disk.
        # - cloud_essd_entry: ESSD Entry cloud disk.
        # - elastic_ephemeral_disk_premium: Premium elastic ephemeral disk.
        # - elastic_ephemeral_disk_standard: Standard elastic ephemeral disk.
        # 
        # Default value: cloud_efficiency.
        self.category = category
        # The mount point of the data cloud disk. If you do not specify this parameter, the system will allocate a mount point by default during the automatic creation of an ECS instance. The mount point starts from /dev/xvdb and ends at /dev/xvdz.
        self.device = device
        # The name of the data cloud disk. The name must be 2 to 128 characters in length and can contain letters and Chinese characters. It must start with a letter or a Chinese character and cannot start with http:// or https://. It can contain digits, colons (:), underscores (_), and hyphens (-).
        self.disk_name = disk_name
        # Specifies whether to encrypt the data cloud disk. Valid values:
        # 
        # - true: Encrypts the data cloud disk.
        # - false: Does not encrypt the data cloud disk.
        # 
        # Default value: false.
        self.encrypted = encrypted
        # The type of the file system to be mounted. This parameter takes effect only when auto_format is set to true. Valid values: ext4 and xfs.
        self.file_system = file_system
        # The ID of the Key Management Service (KMS) key used to encrypt the data cloud disk.
        self.kms_key_id = kms_key_id
        # The mount path. It must be a valid file path.
        self.mount_target = mount_target
        # The performance level of the node data cloud disk. This parameter takes effect only for ESSDs, not standard SSDs. The performance level is related to the disk size. For more information, see [ESSD cloud disks](https://help.aliyun.com/document_detail/122389.html).
        self.performance_level = performance_level
        # The provisioned read and write IOPS of the data cloud disk. Valid values: 0 to min{50,000, 1000 × Capacity - Baseline performance}.
        # Baseline performance = min{1,800 + 50 × Capacity, 50,000}.
        # 
        # This parameter is supported only when DiskCategory is set to cloud_auto. For more information, see [ESSD AutoPL cloud disks](https://help.aliyun.com/document_detail/368372.html).
        self.provisioned_iops = provisioned_iops
        # The size of the data cloud disk. Unit: GiB.
        # 
        # Valid values: 40 to 32768.
        # 
        # Default value: 120.
        self.size = size
        # The ID of the snapshot used to create the data cloud disk. If you specify this parameter, the DataDisks.Size parameter is ignored, and the actual size of the created disk is the same as the size of the specified snapshot. If the snapshot was created on or before July 15, 2013, the call is rejected and the InvalidSnapshot.TooOld error code is returned.
        self.snapshot_id = snapshot_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_format is not None:
            result['auto_format'] = self.auto_format

        if self.auto_snapshot_policy_id is not None:
            result['auto_snapshot_policy_id'] = self.auto_snapshot_policy_id

        if self.bursting_enabled is not None:
            result['bursting_enabled'] = self.bursting_enabled

        if self.category is not None:
            result['category'] = self.category

        if self.device is not None:
            result['device'] = self.device

        if self.disk_name is not None:
            result['disk_name'] = self.disk_name

        if self.encrypted is not None:
            result['encrypted'] = self.encrypted

        if self.file_system is not None:
            result['file_system'] = self.file_system

        if self.kms_key_id is not None:
            result['kms_key_id'] = self.kms_key_id

        if self.mount_target is not None:
            result['mount_target'] = self.mount_target

        if self.performance_level is not None:
            result['performance_level'] = self.performance_level

        if self.provisioned_iops is not None:
            result['provisioned_iops'] = self.provisioned_iops

        if self.size is not None:
            result['size'] = self.size

        if self.snapshot_id is not None:
            result['snapshot_id'] = self.snapshot_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auto_format') is not None:
            self.auto_format = m.get('auto_format')

        if m.get('auto_snapshot_policy_id') is not None:
            self.auto_snapshot_policy_id = m.get('auto_snapshot_policy_id')

        if m.get('bursting_enabled') is not None:
            self.bursting_enabled = m.get('bursting_enabled')

        if m.get('category') is not None:
            self.category = m.get('category')

        if m.get('device') is not None:
            self.device = m.get('device')

        if m.get('disk_name') is not None:
            self.disk_name = m.get('disk_name')

        if m.get('encrypted') is not None:
            self.encrypted = m.get('encrypted')

        if m.get('file_system') is not None:
            self.file_system = m.get('file_system')

        if m.get('kms_key_id') is not None:
            self.kms_key_id = m.get('kms_key_id')

        if m.get('mount_target') is not None:
            self.mount_target = m.get('mount_target')

        if m.get('performance_level') is not None:
            self.performance_level = m.get('performance_level')

        if m.get('provisioned_iops') is not None:
            self.provisioned_iops = m.get('provisioned_iops')

        if m.get('size') is not None:
            self.size = m.get('size')

        if m.get('snapshot_id') is not None:
            self.snapshot_id = m.get('snapshot_id')

        return self

