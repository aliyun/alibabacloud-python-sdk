# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDIJobShrinkRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        destination_data_source_settings_shrink: str = None,
        destination_data_source_type: str = None,
        job_name: str = None,
        job_settings_shrink: str = None,
        job_type: str = None,
        migration_type: str = None,
        name: str = None,
        project_id: int = None,
        resource_settings_shrink: str = None,
        source_data_source_settings_shrink: str = None,
        source_data_source_type: str = None,
        table_mappings_shrink: str = None,
        transformation_rules_shrink: str = None,
    ):
        self.description = description
        # This parameter is required.
        self.destination_data_source_settings_shrink = destination_data_source_settings_shrink
        # The destination type. Valid values: Hologres, OSS-HDFS, OSS, MaxCompute, LogHub, StarRocks, DataHub, AnalyticDB for MySQL, Kafka, and Hive.
        # 
        # This parameter is required.
        self.destination_data_source_type = destination_data_source_type
        # This parameter is deprecated and is replaced by the Name parameter.
        self.job_name = job_name
        self.job_settings_shrink = job_settings_shrink
        # The type of the synchronization task. Valid values:
        # 
        # *   DatabaseRealtimeMigration: A real-time synchronization task used to synchronize only full data, only incremental data, or full and incremental data in multiple tables of multiple databases in the source.
        # *   DatabaseOfflineMigration: A batch synchronization task used to synchronize only full data, only incremental data, or full and incremental data in multiple tables of multiple databases in the source.
        # *   SingleTableRealtimeMigration: A real-time synchronization task used to synchronize data only in a single table in the source.
        self.job_type = job_type
        # The synchronization type. Valid values:
        # 
        # *   FullAndRealtimeIncremental
        # *   RealtimeIncremental
        # *   Full
        # *   OfflineIncremental
        # *   FullAndOfflineIncremental
        # 
        # This parameter is required.
        self.migration_type = migration_type
        # The name of the synchronization task.
        self.name = name
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to obtain the ID.
        # 
        # You must configure this parameter to specify the DataWorks workspace to which the API operation is applied.
        self.project_id = project_id
        # This parameter is required.
        self.resource_settings_shrink = resource_settings_shrink
        # This parameter is required.
        self.source_data_source_settings_shrink = source_data_source_settings_shrink
        # The source type. Valid values: PolarDB, MySQL, Kafka, LogHub, Hologres, Oracle, OceanBase, MongoDB, Redshift, Hive, SQL Server, Doris, and ClickHouse.
        # 
        # This parameter is required.
        self.source_data_source_type = source_data_source_type
        # This parameter is required.
        self.table_mappings_shrink = table_mappings_shrink
        self.transformation_rules_shrink = transformation_rules_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.destination_data_source_settings_shrink is not None:
            result['DestinationDataSourceSettings'] = self.destination_data_source_settings_shrink

        if self.destination_data_source_type is not None:
            result['DestinationDataSourceType'] = self.destination_data_source_type

        if self.job_name is not None:
            result['JobName'] = self.job_name

        if self.job_settings_shrink is not None:
            result['JobSettings'] = self.job_settings_shrink

        if self.job_type is not None:
            result['JobType'] = self.job_type

        if self.migration_type is not None:
            result['MigrationType'] = self.migration_type

        if self.name is not None:
            result['Name'] = self.name

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.resource_settings_shrink is not None:
            result['ResourceSettings'] = self.resource_settings_shrink

        if self.source_data_source_settings_shrink is not None:
            result['SourceDataSourceSettings'] = self.source_data_source_settings_shrink

        if self.source_data_source_type is not None:
            result['SourceDataSourceType'] = self.source_data_source_type

        if self.table_mappings_shrink is not None:
            result['TableMappings'] = self.table_mappings_shrink

        if self.transformation_rules_shrink is not None:
            result['TransformationRules'] = self.transformation_rules_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DestinationDataSourceSettings') is not None:
            self.destination_data_source_settings_shrink = m.get('DestinationDataSourceSettings')

        if m.get('DestinationDataSourceType') is not None:
            self.destination_data_source_type = m.get('DestinationDataSourceType')

        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        if m.get('JobSettings') is not None:
            self.job_settings_shrink = m.get('JobSettings')

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        if m.get('MigrationType') is not None:
            self.migration_type = m.get('MigrationType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ResourceSettings') is not None:
            self.resource_settings_shrink = m.get('ResourceSettings')

        if m.get('SourceDataSourceSettings') is not None:
            self.source_data_source_settings_shrink = m.get('SourceDataSourceSettings')

        if m.get('SourceDataSourceType') is not None:
            self.source_data_source_type = m.get('SourceDataSourceType')

        if m.get('TableMappings') is not None:
            self.table_mappings_shrink = m.get('TableMappings')

        if m.get('TransformationRules') is not None:
            self.transformation_rules_shrink = m.get('TransformationRules')

        return self

