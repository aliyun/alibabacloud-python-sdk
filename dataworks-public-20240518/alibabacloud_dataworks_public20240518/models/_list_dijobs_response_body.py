# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListDIJobsResponseBody(DaraModel):
    def __init__(
        self,
        paging_info: main_models.ListDIJobsResponseBodyPagingInfo = None,
        request_id: str = None,
    ):
        # The pagination information.
        self.paging_info = paging_info
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.paging_info:
            self.paging_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.paging_info is not None:
            result['PagingInfo'] = self.paging_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PagingInfo') is not None:
            temp_model = main_models.ListDIJobsResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m.get('PagingInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListDIJobsResponseBodyPagingInfo(DaraModel):
    def __init__(
        self,
        dijobs: List[main_models.ListDIJobsResponseBodyPagingInfoDIJobs] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The synchronization tasks returned.
        self.dijobs = dijobs
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.dijobs:
            for v1 in self.dijobs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DIJobs'] = []
        if self.dijobs is not None:
            for k1 in self.dijobs:
                result['DIJobs'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dijobs = []
        if m.get('DIJobs') is not None:
            for k1 in m.get('DIJobs'):
                temp_model = main_models.ListDIJobsResponseBodyPagingInfoDIJobs()
                self.dijobs.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListDIJobsResponseBodyPagingInfoDIJobs(DaraModel):
    def __init__(
        self,
        dijob_id: int = None,
        destination_data_source_type: str = None,
        id: int = None,
        job_name: str = None,
        job_status: str = None,
        migration_type: str = None,
        project_id: int = None,
        source_data_source_type: str = None,
    ):
        # This parameter is deprecated. Use the Id parameter instead.
        self.dijob_id = dijob_id
        # The destination type. Valid values: Hologres, OSS-HDFS, OSS, MaxCompute, Loghub, STARROCKS, DataHub, ANALYTICDB_FOR_MYSQL, Kafka, and Hive.
        self.destination_data_source_type = destination_data_source_type
        # The ID of the synchronization task.
        self.id = id
        # The name of the synchronization task.
        self.job_name = job_name
        # The status of the synchronization task. Valid values:
        # 
        # *   Finished
        # *   Initialized
        # *   Stopped
        # *   Failed
        # *   Running
        # *   Stopping
        self.job_status = job_status
        # The synchronization type. Valid values:
        # 
        # *   FullAndRealtimeIncremental: one-time full synchronization and real-time incremental synchronization
        # *   RealtimeIncremental: real-time incremental synchronization
        # *   Full: full synchronization
        # *   OfflineIncremental: batch incremental synchronization
        # *   FullAndOfflineIncremental: one-time full synchronization and batch incremental synchronization
        self.migration_type = migration_type
        # The ID of the DataWorks workspace to which the synchronization task belongs.
        self.project_id = project_id
        # The source type. Valid values: PolarDB, MySQL, Kafka, Loghub, Hologres, Oracle, OceanBase, MongoDB, RedShift, Hive, SqlServer, Doris, and ClickHouse. If you do not configure this parameter, the API operation returns synchronization tasks that use all types of sources.
        self.source_data_source_type = source_data_source_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dijob_id is not None:
            result['DIJobId'] = self.dijob_id

        if self.destination_data_source_type is not None:
            result['DestinationDataSourceType'] = self.destination_data_source_type

        if self.id is not None:
            result['Id'] = self.id

        if self.job_name is not None:
            result['JobName'] = self.job_name

        if self.job_status is not None:
            result['JobStatus'] = self.job_status

        if self.migration_type is not None:
            result['MigrationType'] = self.migration_type

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.source_data_source_type is not None:
            result['SourceDataSourceType'] = self.source_data_source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DIJobId') is not None:
            self.dijob_id = m.get('DIJobId')

        if m.get('DestinationDataSourceType') is not None:
            self.destination_data_source_type = m.get('DestinationDataSourceType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        if m.get('JobStatus') is not None:
            self.job_status = m.get('JobStatus')

        if m.get('MigrationType') is not None:
            self.migration_type = m.get('MigrationType')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('SourceDataSourceType') is not None:
            self.source_data_source_type = m.get('SourceDataSourceType')

        return self

