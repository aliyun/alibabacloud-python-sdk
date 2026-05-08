# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20190315 import models as main_models
from darabonba.model import DaraModel

class DescribeSyncAvailableDBClusterListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        sync_available_dbclusters: List[main_models.DescribeSyncAvailableDBClusterListResponseBodySyncAvailableDBClusters] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The queried instances or clusters.
        self.sync_available_dbclusters = sync_available_dbclusters

    def validate(self):
        if self.sync_available_dbclusters:
            for v1 in self.sync_available_dbclusters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SyncAvailableDBClusters'] = []
        if self.sync_available_dbclusters is not None:
            for k1 in self.sync_available_dbclusters:
                result['SyncAvailableDBClusters'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.sync_available_dbclusters = []
        if m.get('SyncAvailableDBClusters') is not None:
            for k1 in m.get('SyncAvailableDBClusters'):
                temp_model = main_models.DescribeSyncAvailableDBClusterListResponseBodySyncAvailableDBClusters()
                self.sync_available_dbclusters.append(temp_model.from_map(k1))

        return self

class DescribeSyncAvailableDBClusterListResponseBodySyncAvailableDBClusters(DaraModel):
    def __init__(
        self,
        dbcluster_description: str = None,
        dbcluster_id: str = None,
        dbtype: str = None,
        storage_size: float = None,
        table_number: int = None,
    ):
        # The description of the instance or cluster.
        self.dbcluster_description = dbcluster_description
        # The instance or cluster ID.
        self.dbcluster_id = dbcluster_id
        # The database type of the instance or cluster.
        self.dbtype = dbtype
        # The storage size.
        self.storage_size = storage_size
        # The number of tables.
        self.table_number = table_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_description is not None:
            result['DBClusterDescription'] = self.dbcluster_description

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.dbtype is not None:
            result['DBType'] = self.dbtype

        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size

        if self.table_number is not None:
            result['TableNumber'] = self.table_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterDescription') is not None:
            self.dbcluster_description = m.get('DBClusterDescription')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')

        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')

        if m.get('TableNumber') is not None:
            self.table_number = m.get('TableNumber')

        return self

