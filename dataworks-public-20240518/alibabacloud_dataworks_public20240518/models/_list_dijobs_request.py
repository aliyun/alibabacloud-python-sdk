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
        # The type of the destination data source. If you do not specify this parameter, jobs are not filtered by this criterion. Valid values: `Hologres`, `OSS-HDFS`, `OSS`, `MaxCompute`, `LogHub`, `StarRocks`, `DataHub`, `AnalyticDB_For_MySQL`, `Kafka`, and `Hive`.
        self.destination_data_source_type = destination_data_source_type
        # The synchronization type. Valid values:
        # 
        # - `FullAndRealtimeIncremental`: full and real-time incremental synchronization
        # 
        # - `RealtimeIncremental`: real-time incremental synchronization
        # 
        # - `Full`: full synchronization
        # 
        # - `OfflineIncremental`: offline incremental synchronization
        # 
        # - `FullAndOfflineIncremental`: full and offline incremental synchronization
        self.migration_type = migration_type
        # The name of the Data Integration job.
        # 
        # The name must be unique within the DataWorks workspace.
        self.name = name
        # The page number. Pages are numbered starting from 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default: 10. Maximum: 100.
        self.page_size = page_size
        # The ID of the DataWorks workspace.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The type of the source data source. If you do not specify this parameter, jobs are not filtered by this criterion. Valid values: `PolarDB`, `MySQL`, `Kafka`, `LogHub`, `Hologres`, `Oracle`, `OceanBase`, `MongoDB`, `RedShift`, `Hive`, `SQLServer`, `Doris`, and `ClickHouse`.
        self.source_data_source_type = source_data_source_type
        # The configuration type of the job. Valid values: `FILESPEC`, `CLASSIC`, and `ALL`. `FILESPEC` indicates a new job type configured based on a structured file specification. `CLASSIC` indicates a job configured in the traditional mode. If you set this parameter to `ALL`, jobs of both types are returned.
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

