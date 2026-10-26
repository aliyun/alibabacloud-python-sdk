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
        # The new disk category. This parameter is valid only during migration between different dedicated block storage clusters. Currently, only cloud_essd (ESSD) is supported.
        # 
        # Default value: empty, which indicates that the disk category is not changed.
        self.disk_category = disk_category
        # The disk ID.
        # 
        # This parameter is required.
        self.disk_id = disk_id
        # Specifies whether to only precheck the request. Valid values:
        # - true: sends a precheck request. The check items include whether required parameters are specified, the request format, business limits, and ECS inventory. If the check fails, the corresponding error is returned. If the check succeeds, the DryRunOperation error code is returned.
        # - false: sends a normal request. If the check succeeds, a 2xx HTTP status code is returned and the disk is directly migrated.
        # 
        # Default value: false.
        self.dry_run = dry_run
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The new ESSD performance level. This parameter is valid only during migration between different dedicated block storage clusters. Valid values:
        # - PL0: A single disk can deliver up to 10,000 random read/write IOPS.
        # - PL1: A single disk can deliver up to 50,000 random read/write IOPS.
        # 
        # Default value: empty, which indicates that the performance level is not changed.
        self.performance_level = performance_level
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the dedicated block storage cluster. Before migrating a disk into a dedicated block storage cluster, you must purchase and create the cluster, and ensure that the disk and the destination cluster are in the same zone.
        # - When migrating a disk to a dedicated block storage cluster, you must specify `StorageClusterId`.
        # - When migrating a disk to a public cloud block storage cluster, `StorageClusterId` must be empty.
        # 
        # Default value: empty, which indicates that the disk is migrated to a public cloud block storage cluster.
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

