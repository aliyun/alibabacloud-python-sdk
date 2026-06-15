# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDiskDeploymentRequest(DaraModel):
    def __init__(
        self,
        disk_category: str = None,
        disk_id: str = None,
        dry_run: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        performance_level: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        storage_cluster_id: str = None,
    ):
        # The new category of the disk. This parameter is valid only when you migrate a disk between different dedicated block storage clusters. The only valid value is `cloud_essd` (ESSD disk).
        # 
        # Default value: An empty string. If you leave this parameter empty, the category of the disk remains unchanged.
        self.disk_category = disk_category
        # The ID of the disk.
        # 
        # This parameter is required.
        self.disk_id = disk_id
        # Specifies whether to perform a dry run. Valid values:
        # 
        # - `true`: Performs a dry run. The system checks the request for required parameters, format, service limits, and inventory. The system returns an error if the check fails, or the `DryRunOperation` error code if the check succeeds.
        # 
        # - `false`: Sends the request. If the request passes the check, the system returns a 2xx HTTP status code and migrates the disk.
        # 
        # Default value: `false`.
        self.dry_run = dry_run
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The new performance level of the ESSD disk. This parameter is valid only when you migrate a disk between different dedicated block storage clusters. Valid values:
        # 
        # - `PL0`: A maximum of 10,000 random read/write IOPS per disk.
        # 
        # - `PL1`: A maximum of 50,000 random read/write IOPS per disk.
        # 
        # Default value: An empty string. If you leave this parameter empty, the performance level of the disk remains unchanged.
        self.performance_level = performance_level
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the dedicated block storage cluster.
        # 
        # - To migrate the disk to a dedicated block storage cluster, specify `StorageClusterId`.
        # 
        # - To migrate the disk to a public cloud block storage cluster, leave `StorageClusterId` empty.
        # 
        # Default value: An empty string. If you leave this parameter empty, the disk is migrated to a public cloud block storage cluster.
        self.storage_cluster_id = storage_cluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.storage_cluster_id is not None:
            result['StorageClusterId'] = self.storage_cluster_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('StorageClusterId') is not None:
            self.storage_cluster_id = m.get('StorageClusterId')

        return self

