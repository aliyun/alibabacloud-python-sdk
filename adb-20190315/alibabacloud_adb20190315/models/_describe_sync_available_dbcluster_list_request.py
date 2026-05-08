# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20190315 import models as main_models
from darabonba.model import DaraModel

class DescribeSyncAvailableDBClusterListRequest(DaraModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        query_type: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        source_dbcluster: List[main_models.DescribeSyncAvailableDBClusterListRequestSourceDBCluster] = None,
        sync_platform: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The query type.
        # 
        # Valid values:
        # 
        # *   Target
        # *   Source
        # 
        # This parameter is required.
        self.query_type = query_type
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The source instances or clusters.
        self.source_dbcluster = source_dbcluster
        # The synchronization platform.
        self.sync_platform = sync_platform

    def validate(self):
        if self.source_dbcluster:
            for v1 in self.source_dbcluster:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.query_type is not None:
            result['QueryType'] = self.query_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        result['SourceDBCluster'] = []
        if self.source_dbcluster is not None:
            for k1 in self.source_dbcluster:
                result['SourceDBCluster'].append(k1.to_map() if k1 else None)

        if self.sync_platform is not None:
            result['SyncPlatform'] = self.sync_platform

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        self.source_dbcluster = []
        if m.get('SourceDBCluster') is not None:
            for k1 in m.get('SourceDBCluster'):
                temp_model = main_models.DescribeSyncAvailableDBClusterListRequestSourceDBCluster()
                self.source_dbcluster.append(temp_model.from_map(k1))

        if m.get('SyncPlatform') is not None:
            self.sync_platform = m.get('SyncPlatform')

        return self

class DescribeSyncAvailableDBClusterListRequestSourceDBCluster(DaraModel):
    def __init__(
        self,
        cluster_ids: str = None,
        region_id: str = None,
        type: str = None,
    ):
        # The ID of the source instance or cluster. Separate multiple IDs with commas (,).
        self.cluster_ids = cluster_ids
        # The region ID.
        self.region_id = region_id
        # The database type of the source instance or cluster.
        # 
        # Valid values:
        # 
        # *   rds: ApsaraDB RDS.
        # *   sls: Simple Log Service.
        # *   polardb: PolarDB.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_ids is not None:
            result['ClusterIds'] = self.cluster_ids

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterIds') is not None:
            self.cluster_ids = m.get('ClusterIds')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

