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
        file_spec: str = None,
        job_name: str = None,
        job_settings_shrink: str = None,
        job_type: str = None,
        migration_type: str = None,
        name: str = None,
        owner: str = None,
        project_id: int = None,
        resource_settings_shrink: str = None,
        source_data_source_settings_shrink: str = None,
        source_data_source_type: str = None,
        table_mappings_shrink: str = None,
        transformation_rules_shrink: str = None,
    ):
        # The description of the task.
        self.description = description
        # The list of destination data source settings.
        self.destination_data_source_settings_shrink = destination_data_source_settings_shrink
        # The type of the destination data source. Valid values: Hologres, OSS-HDFS, OSS, MaxCompute, LogHub, StarRocks, DataHub, AnalyticDB_For_MySQL, Kafka, Hive.
        self.destination_data_source_type = destination_data_source_type
        # The code content in script mode.
        self.file_spec = file_spec
        # **[Deprecated]** Use the Name parameter instead.
        self.job_name = job_name
        # The task-level settings, including DDL handling policies, source-to-destination column data type mapping policies, and task runtime parameters.
        self.job_settings_shrink = job_settings_shrink
        # The task type. Valid values:
        # 
        #  - DatabaseRealtimeMigration: real-time migration of entire databases. Performs streaming synchronization of multiple tables from multiple source databases. Supports full-only, incremental-only, or full and incremental synchronization.
        # 
        #  - DatabaseOfflineMigration: offline migration of entire databases. Performs batch synchronization of multiple tables from multiple source databases. Supports full-only, incremental-only, or full and incremental synchronization.
        # 
        #  - SingleTableRealtimeMigration: real-time migration of a single table. Performs streaming synchronization of a single source table.
        self.job_type = job_type
        # The synchronization type. Valid values:
        # - FullAndRealtimeIncremental: full and real-time incremental synchronization for entire databases in real time.
        # - RealtimeIncremental: real-time incremental synchronization for single tables in real time.
        # - Full: full synchronization for entire databases offline.
        # - OfflineIncremental: offline incremental synchronization for entire databases offline.
        # - FullAndOfflineIncremental: full and offline incremental synchronization for entire databases offline.
        self.migration_type = migration_type
        # The name of the task.
        self.name = name
        # The owner of the task.
        self.owner = owner
        # The ID of the DataWorks workspace. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the workspace management page to obtain the ID.
        # 
        # This parameter specifies the DataWorks workspace for this API call.
        self.project_id = project_id
        # The resource settings.
        self.resource_settings_shrink = resource_settings_shrink
        # The list of source data source settings.
        self.source_data_source_settings_shrink = source_data_source_settings_shrink
        # The type of the source data source. Valid values: PolarDB, MySQL, Kafka, LogHub, Hologres, Oracle, OceanBase, MongoDB, RedShift, Hive, SQLServer, Doris, ClickHouse.
        self.source_data_source_type = source_data_source_type
        # The list of synchronization object transformation mappings. Each element describes a group of source object selection rules and the transformation rules applied to that group.
        # 
        # > [ { "SourceObjectSelectionRules":[ { "ObjectType":"Database", "Action":"Include", "ExpressionType":"Exact", "Expression":"biz_db" }, { "ObjectType":"Schema", "Action":"Include", "ExpressionType":"Exact", "Expression":"s1" }, { "ObjectType":"Table", "Action":"Include", "ExpressionType":"Exact", "Expression":"table1" } ], "TransformationRuleNames":[ { "RuleName":"my_database_rename_rule", "RuleActionType":"Rename", "RuleTargetType":"Schema" } ] } ]
        self.table_mappings_shrink = table_mappings_shrink
        # The list of synchronization object transformation rule definitions.
        # >[ { "RuleName":"my_database_rename_rule", "RuleActionType":"Rename", "RuleTargetType":"Schema", "RuleExpression":"{"expression":"${srcDatasoureName}_${srcDatabaseName}"}" } ]
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

        if self.file_spec is not None:
            result['FileSpec'] = self.file_spec

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

        if self.owner is not None:
            result['Owner'] = self.owner

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

        if m.get('FileSpec') is not None:
            self.file_spec = m.get('FileSpec')

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

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

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

