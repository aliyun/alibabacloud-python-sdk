# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDIJobsRequest(DaraModel):
    def __init__(
        self,
        destination_data_source_type: str = None,
        migration_type: str = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: int = None,
        source_data_source_type: str = None,
        spec_type: str = None,
    ):
        # The destination type. Valid values: Hologres, OSS-HDFS, OSS, MaxCompute, Loghub, STARROCKS, Datahub, ANALYTICDB_FOR_MYSQL, Kafka, and Hive. If you do not configure this parameter, the API operation queries synchronization tasks that use all type of destinations.
        self.destination_data_source_type = destination_data_source_type
        # The synchronization type. Valid values:
        # 
        # *   FullAndRealtimeIncremental: one-time full synchronization and real-time incremental synchronization
        # *   RealtimeIncremental: real-time incremental synchronization
        # *   Full: full synchronization
        # *   OfflineIncremental: batch incremental synchronization
        # *   FullAndOfflineIncremental: one-time full synchronization and batch incremental synchronization
        self.migration_type = migration_type
        # The name of the export task.
        # 
        # The name of each export task must be unique. You must make sure that the names of the export tasks in the current workspace are unique.
        self.name = name
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The DataWorks workspace ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The source type. Valid values: PolarDB, MySQL, Kafka, Loghub, Hologres, Oracle, OceanBase, MongoDB, RedShift, Hive, SqlServer, Doris, and ClickHouse. If you do not configure this parameter, the API operation queries synchronization tasks that use all types of sources.
        self.source_data_source_type = source_data_source_type
        self.spec_type = spec_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination_data_source_type is not None:
            result['DestinationDataSourceType'] = self.destination_data_source_type

        if self.migration_type is not None:
            result['MigrationType'] = self.migration_type

        if self.name is not None:
            result['Name'] = self.name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.source_data_source_type is not None:
            result['SourceDataSourceType'] = self.source_data_source_type

        if self.spec_type is not None:
            result['SpecType'] = self.spec_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationDataSourceType') is not None:
            self.destination_data_source_type = m.get('DestinationDataSourceType')

        if m.get('MigrationType') is not None:
            self.migration_type = m.get('MigrationType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('SourceDataSourceType') is not None:
            self.source_data_source_type = m.get('SourceDataSourceType')

        if m.get('SpecType') is not None:
            self.spec_type = m.get('SpecType')

        return self

