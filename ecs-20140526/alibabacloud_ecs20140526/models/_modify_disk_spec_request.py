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
        # >  This parameter is in invitational preview and is not publicly available.
        self.destination_zone_id = destination_zone_id
        # The new disk category of the cloud disk. Valid values:
        # 
        # *   cloud_essd: ESSD
        # *   cloud_auto: ESSD AutoPL disk
        # *   cloud_ssd: standard SSD
        # *   cloud_efficiency: utra disk
        # 
        # This parameter is empty by default, which indicates that the disk category is not changed.
        # 
        # > 
        # 
        # *   The preceding values are listed in descending order of disk performance. Subscription disks cannot be downgraded.
        self.disk_category = disk_category
        # The disk ID.
        # 
        # This parameter is required.
        self.disk_id = disk_id
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   true: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, service limits, and insufficient ECS resources. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   false: performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        # 
        # Default value: false.
        self.dry_run = dry_run
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The disk performance specifications.
        self.performance_control_options = performance_control_options
        # The new performance level of the ESSD. Valid values:
        # 
        # *   PL0: An ESSD can deliver up to 10,000 random read/write IOPS.
        # *   PL1: An ESSD can deliver up to 50,000 random read/write IOPS.
        # *   PL2: An ESSD can deliver up to 100,000 random read/write IOPS.
        # *   PL3: An ESSD delivers up to 1,000,000 random read/write IOPS.
        # 
        # Default value: PL1.
        self.performance_level = performance_level
        # The provisioned read/write IOPS of the ESSD AutoPL disk.
        # 
        # Valid values: 0 to min{50,000, 1,000 × Capacity - Baseline IOPS}.
        # 
        # Baseline IOPS = min{1,800 + 50 × Capacity, 50,000}.
        # 
        # >  This parameter is available only if you set `DiskCategory` to `cloud_auto`. For more information, see [ESSD AutoPL disks](https://help.aliyun.com/document_detail/368372.html) and [Modify the performance configurations of an ESSD AutoPL disk](https://help.aliyun.com/document_detail/413275.html).
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
        # The new IOPS rate of the cloud disk. You can modify the IOPS rate of only cloud disks in dedicated block storage clusters.
        # 
        # Valid values: 900 to maximum IOPS per disk (with an increment of 100).
        # 
        # For more information, see [Block storage performance](https://help.aliyun.com/document_detail/25382.html).
        self.iops = iops
        # Specifies whether to reset the IOPS rate and throughput of the cloud disk. This parameter takes effect only when the cloud disk belongs to a dedicated block storage cluster.
        # 
        # After you specify this parameter, PerformanceControlOptions.IOPS and PerformanceControlOptions.Throughput do not take effect.
        # 
        # Set the value to All, which indicates that the IOPS rate and throughput of the cloud disk are reset to the initial values.
        self.recover = recover
        # The new throughput of the cloud disk. You can change the throughput of only cloud disks in dedicated block storage clusters. Unit: MB/s.
        # 
        # Valid values: 60 to maximum throughput per disk.
        # 
        # For more information, see [Block storage performance](https://help.aliyun.com/document_detail/25382.html).
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

