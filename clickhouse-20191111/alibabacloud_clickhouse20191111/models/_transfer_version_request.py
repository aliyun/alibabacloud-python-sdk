# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TransferVersionRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        disable_write_windows: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        source_account: str = None,
        source_cluster_name: str = None,
        source_password: str = None,
        source_shards: str = None,
        target_account: str = None,
        target_db_cluster_id: str = None,
        target_password: str = None,
    ):
        # The ID of the source ApsaraDB for ClickHouse cluster.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The time window during which write operations are stopped.
        self.disable_write_windows = disable_write_windows
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Valid values:
        # 
        # *   **30** (default)
        # *   **50**
        # *   **100**
        self.page_size = page_size
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/170875.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The database account that is used to log on to the database in the source ApsaraDB for ClickHouse cluster.
        # 
        # This parameter is required.
        self.source_account = source_account
        # The name of the self-managed ClickHouse cluster. You can execute the `SELECT * FROM system.clusters` statement to query the cluster name.
        self.source_cluster_name = source_cluster_name
        # The password that corresponds to the database account for logging on to the database in the source ApsaraDB for ClickHouse cluster.
        # 
        # This parameter is required.
        self.source_password = source_password
        # The endpoint and TCP port of the self-managed ClickHouse cluster.
        self.source_shards = source_shards
        # The database account that is used to log on to the database in the destination ApsaraDB for ClickHouse cluster.
        # 
        # This parameter is required.
        self.target_account = target_account
        # The ID of the destination ApsaraDB for ClickHouse cluster.
        # 
        # This parameter is required.
        self.target_db_cluster_id = target_db_cluster_id
        # The password that corresponds to the database account for logging on to the database in the destination ApsaraDB for ClickHouse cluster.
        # 
        # This parameter is required.
        self.target_password = target_password

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.disable_write_windows is not None:
            result['DisableWriteWindows'] = self.disable_write_windows

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.source_account is not None:
            result['SourceAccount'] = self.source_account

        if self.source_cluster_name is not None:
            result['SourceClusterName'] = self.source_cluster_name

        if self.source_password is not None:
            result['SourcePassword'] = self.source_password

        if self.source_shards is not None:
            result['SourceShards'] = self.source_shards

        if self.target_account is not None:
            result['TargetAccount'] = self.target_account

        if self.target_db_cluster_id is not None:
            result['TargetDbClusterId'] = self.target_db_cluster_id

        if self.target_password is not None:
            result['TargetPassword'] = self.target_password

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DisableWriteWindows') is not None:
            self.disable_write_windows = m.get('DisableWriteWindows')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SourceAccount') is not None:
            self.source_account = m.get('SourceAccount')

        if m.get('SourceClusterName') is not None:
            self.source_cluster_name = m.get('SourceClusterName')

        if m.get('SourcePassword') is not None:
            self.source_password = m.get('SourcePassword')

        if m.get('SourceShards') is not None:
            self.source_shards = m.get('SourceShards')

        if m.get('TargetAccount') is not None:
            self.target_account = m.get('TargetAccount')

        if m.get('TargetDbClusterId') is not None:
            self.target_db_cluster_id = m.get('TargetDbClusterId')

        if m.get('TargetPassword') is not None:
            self.target_password = m.get('TargetPassword')

        return self

