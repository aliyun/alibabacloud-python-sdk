# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBClusterRequest(DaraModel):
    def __init__(
        self,
        dbcluster_class: str = None,
        dbcluster_id: str = None,
        dbnode_group_count: str = None,
        dbnode_storage: str = None,
        db_node_storage_type: str = None,
        disable_write_windows: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The specifications of the cluster.
        # 
        # *   Valid values when the cluster is of Single-replica Edition:
        # 
        #     *   **S8**
        #     *   **S16**
        #     *   **S32**
        #     *   **S64**
        #     *   **S104**
        # 
        # *   Valid values when the cluster is of Double-replica Edition:
        # 
        #     *   **C8**
        #     *   **C16**
        #     *   **C32**
        #     *   **C64**
        #     *   **C104**
        # 
        # This parameter is required.
        self.dbcluster_class = dbcluster_class
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The number of nodes in the cluster.
        # 
        # *   If the cluster is of Single-replica Edition, the value must be an integer that ranges from 1 to 48.
        # *   If the cluster is of Double-replica Edition, the value must be an integer that ranges from 1 to 24.
        # 
        # This parameter is required.
        self.dbnode_group_count = dbnode_group_count
        # The storage capacity of a single node of the cluster. Unit: GB.
        # 
        # Valid values: 100 to 32000.
        # 
        # >  This value is a multiple of 100.
        # 
        # This parameter is required.
        self.dbnode_storage = dbnode_storage
        # The storage type of the cluster. Valid values:
        # 
        # *   **CloudESSD**: The cluster uses an Enterprise SSD (ESSD) of performance level 1 (PL1).
        # *   **CloudESSD_PL2**: The cluster uses an ESSD of PL2.
        # *   **CloudESSD_PL3**: The cluster uses an ESSD of PL3.
        # *   **CloudEfficiency**: The cluster uses an ultra disk.
        # *   **CloudSSD**: The cluster uses a standard SSD.
        self.db_node_storage_type = db_node_storage_type
        # The time window during which write operations are stopped. Separate the start time and end time with commas (,). Specify the time in the ISO 8601 standard.
        self.disable_write_windows = disable_write_windows
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID You can call the [DescribeRegions](https://help.aliyun.com/document_detail/170875.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_class is not None:
            result['DBClusterClass'] = self.dbcluster_class

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.dbnode_group_count is not None:
            result['DBNodeGroupCount'] = self.dbnode_group_count

        if self.dbnode_storage is not None:
            result['DBNodeStorage'] = self.dbnode_storage

        if self.db_node_storage_type is not None:
            result['DbNodeStorageType'] = self.db_node_storage_type

        if self.disable_write_windows is not None:
            result['DisableWriteWindows'] = self.disable_write_windows

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterClass') is not None:
            self.dbcluster_class = m.get('DBClusterClass')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DBNodeGroupCount') is not None:
            self.dbnode_group_count = m.get('DBNodeGroupCount')

        if m.get('DBNodeStorage') is not None:
            self.dbnode_storage = m.get('DBNodeStorage')

        if m.get('DbNodeStorageType') is not None:
            self.db_node_storage_type = m.get('DbNodeStorageType')

        if m.get('DisableWriteWindows') is not None:
            self.disable_write_windows = m.get('DisableWriteWindows')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

