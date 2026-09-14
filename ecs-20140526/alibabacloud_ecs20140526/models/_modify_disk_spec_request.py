# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class ModifyDiskSpecRequest(DaraModel):
    def __init__(
        self,
        destination_zone_id: str = None,
        disk_category: str = None,
        disk_id: str = None,
        dry_run: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        performance_control_options: main_models.ModifyDiskSpecRequestPerformanceControlOptions = None,
        performance_level: str = None,
        provisioned_iops: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # > This parameter is currently in invitational preview and is not available for use.
        self.destination_zone_id = destination_zone_id
        # The new disk type. Valid values:
        # 
        # - cloud_essd: enterprise SSD (ESSD).
        # - cloud_auto: ESSD AutoPL disk.
        # - cloud_ssd: standard SSD.
        # <props="china">
        # - cloud_essd_entry: ESSD Entry disk.
        # 
        # - cloud_efficiency: ultra disk.
        # 
        # Default value: empty, which means no specification change is performed.
        # 
        # > - The valid values above are listed in descending order of disk performance. If the specified disk is a subscription disk, you cannot decrease the quota of the disk type.
        # 
        # <props="china">
        # - ESSD Entry disks can only be changed to enterprise SSDs (ESSDs) or ESSD AutoPL disks. For more information, see [Change the disk type](https://help.aliyun.com/document_detail/161980.html).
        self.disk_category = disk_category
        # The ID of the disk.
        # 
        # This parameter is required.
        self.disk_id = disk_id
        # Specifies whether to perform only a dry run for this request. Valid values:
        # 
        # * true: performs a dry run. The system checks whether the required parameters are specified, the request format is valid, business limits are met, and ECS resources are sufficient. If the check fails, the corresponding error is returned. If the check passes, the error code `DryRunOperation` is returned.
        # 
        # * false: performs the actual request. After the check passes, a 2XX HTTP status code is returned and the disk type or ESSD performance level is changed immediately.
        # 
        # Default value: false.
        self.dry_run = dry_run
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The collection of disk performance control parameters.
        self.performance_control_options = performance_control_options
        # The new performance level (PL) of the enterprise SSD (ESSD). Valid values:
        # 
        # - PL0: maximum random read/write IOPS of 10,000 per standard SSD.
        # - PL1: maximum random read/write IOPS of 50,000 per standard SSD.
        # - PL2: maximum random read/write IOPS of 100,000 per standard SSD.
        # - PL3: maximum random read/write IOPS of 1,000,000 per standard SSD.
        # 
        # Default value: PL1.
        self.performance_level = performance_level
        # Specifies whether to modify the provisioned read/write IOPS of the ESSD AutoPL disk.
        # 
        # Valid values: 0 to min{50,000, 1,000 × capacity − baseline performance}.
        # 
        # Baseline performance = min{1,800 + 50 × capacity, 50,000}.
        # 
        # > This parameter is supported only when DiskCategory is set to cloud_auto. For more information, see [ESSD AutoPL disk](https://help.aliyun.com/document_detail/368372.html) and [Modify the provisioned performance of an ESSD AutoPL disk](https://help.aliyun.com/document_detail/413275.html).
        self.provisioned_iops = provisioned_iops
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        if self.performance_control_options:
            self.performance_control_options.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination_zone_id is not None:
            result['DestinationZoneId'] = self.destination_zone_id

        if self.disk_category is not None:
            result['DiskCategory'] = self.disk_category

        if self.disk_id is not None:
            result['DiskId'] = self.disk_id

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.performance_control_options is not None:
            result['PerformanceControlOptions'] = self.performance_control_options.to_map()

        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level

        if self.provisioned_iops is not None:
            result['ProvisionedIops'] = self.provisioned_iops

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationZoneId') is not None:
            self.destination_zone_id = m.get('DestinationZoneId')

        if m.get('DiskCategory') is not None:
            self.disk_category = m.get('DiskCategory')

        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PerformanceControlOptions') is not None:
            temp_model = main_models.ModifyDiskSpecRequestPerformanceControlOptions()
            self.performance_control_options = temp_model.from_map(m.get('PerformanceControlOptions'))

        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')

        if m.get('ProvisionedIops') is not None:
            self.provisioned_iops = m.get('ProvisionedIops')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

class ModifyDiskSpecRequestPerformanceControlOptions(DaraModel):
    def __init__(
        self,
        iops: int = None,
        recover: str = None,
        throughput: int = None,
    ):
        # The target IOPS of the disk. Only the IOPS of dedicated block storage cluster disks can be modified.
        # 
        # Valid values: 900 to the maximum IOPS of a single disk, in increments of 100.
        # 
        # For more information, see [Disk performance](https://help.aliyun.com/document_detail/25382.html).
        self.iops = iops
        # Resets the disk performance. This parameter is supported only for dedicated block storage cluster disks.
        # 
        # If this parameter is specified, the PerformanceControlOptions.IOPS and PerformanceControlOptions.Throughput parameters do not take effect.
        # 
        # Currently, only All is supported, which resets the disk IOPS and throughput to their initial values.
        self.recover = recover
        # The target throughput of the disk, in MB/s. Only the throughput of dedicated block storage cluster disks can be modified.
        # 
        # Valid values: 60 to the maximum throughput of a single disk.
        # 
        # For more information, see [Disk performance](https://help.aliyun.com/document_detail/25382.html).
        self.throughput = throughput

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.iops is not None:
            result['IOPS'] = self.iops

        if self.recover is not None:
            result['Recover'] = self.recover

        if self.throughput is not None:
            result['Throughput'] = self.throughput

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IOPS') is not None:
            self.iops = m.get('IOPS')

        if m.get('Recover') is not None:
            self.recover = m.get('Recover')

        if m.get('Throughput') is not None:
            self.throughput = m.get('Throughput')

        return self

