# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20190315 import models as main_models
from darabonba.model import DaraModel

class DescribeSyncJobListResponseBody(DaraModel):
    def __init__(
        self,
        dbcluster_id: int = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        sync_jobs: List[main_models.DescribeSyncJobListResponseBodySyncJobs] = None,
        total_count: int = None,
    ):
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The queried synchronization jobs.
        self.sync_jobs = sync_jobs
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.sync_jobs:
            for v1 in self.sync_jobs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SyncJobs'] = []
        if self.sync_jobs is not None:
            for k1 in self.sync_jobs:
                result['SyncJobs'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.sync_jobs = []
        if m.get('SyncJobs') is not None:
            for k1 in m.get('SyncJobs'):
                temp_model = main_models.DescribeSyncJobListResponseBodySyncJobs()
                self.sync_jobs.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeSyncJobListResponseBodySyncJobs(DaraModel):
    def __init__(
        self,
        job_id: str = None,
        region_id: str = None,
        source_dbcluster_description: str = None,
        source_dbcluster_id: str = None,
        source_dbtype: str = None,
        source_storage_size: int = None,
        source_table_number: int = None,
        sync_platform: str = None,
    ):
        # The ID of the Spark job.
        self.job_id = job_id
        # The region ID.
        self.region_id = region_id
        # The description of the source instance or cluster.
        self.source_dbcluster_description = source_dbcluster_description
        # The ID of the source cluster. You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/170879.html) operation to query backup set IDs.
        # 
        # >  If you want to restore the data of an ApsaraDB for ClickHouse cluster, this parameter is required.
        self.source_dbcluster_id = source_dbcluster_id
        # The database type of the source instance or cluster.
        self.source_dbtype = source_dbtype
        # The storage size of the source instance or cluster.
        self.source_storage_size = source_storage_size
        # The number of tables in the source instance or cluster.
        self.source_table_number = source_table_number
        # The synchronization platform.
        self.sync_platform = sync_platform

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.source_dbcluster_description is not None:
            result['SourceDBClusterDescription'] = self.source_dbcluster_description

        if self.source_dbcluster_id is not None:
            result['SourceDBClusterId'] = self.source_dbcluster_id

        if self.source_dbtype is not None:
            result['SourceDBType'] = self.source_dbtype

        if self.source_storage_size is not None:
            result['SourceStorageSize'] = self.source_storage_size

        if self.source_table_number is not None:
            result['SourceTableNumber'] = self.source_table_number

        if self.sync_platform is not None:
            result['SyncPlatform'] = self.sync_platform

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SourceDBClusterDescription') is not None:
            self.source_dbcluster_description = m.get('SourceDBClusterDescription')

        if m.get('SourceDBClusterId') is not None:
            self.source_dbcluster_id = m.get('SourceDBClusterId')

        if m.get('SourceDBType') is not None:
            self.source_dbtype = m.get('SourceDBType')

        if m.get('SourceStorageSize') is not None:
            self.source_storage_size = m.get('SourceStorageSize')

        if m.get('SourceTableNumber') is not None:
            self.source_table_number = m.get('SourceTableNumber')

        if m.get('SyncPlatform') is not None:
            self.sync_platform = m.get('SyncPlatform')

        return self

