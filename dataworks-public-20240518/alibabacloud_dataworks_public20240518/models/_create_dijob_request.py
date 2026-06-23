# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class CreateDIJobRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        destination_data_source_settings: List[main_models.CreateDIJobRequestDestinationDataSourceSettings] = None,
        destination_data_source_type: str = None,
        file_spec: str = None,
        job_name: str = None,
        job_settings: main_models.CreateDIJobRequestJobSettings = None,
        job_type: str = None,
        migration_type: str = None,
        name: str = None,
        owner: str = None,
        project_id: int = None,
        resource_settings: main_models.CreateDIJobRequestResourceSettings = None,
        source_data_source_settings: List[main_models.CreateDIJobRequestSourceDataSourceSettings] = None,
        source_data_source_type: str = None,
        table_mappings: List[main_models.CreateDIJobRequestTableMappings] = None,
        transformation_rules: List[main_models.CreateDIJobRequestTransformationRules] = None,
    ):
        # The description of the job.
        self.description = description
        # Settings for the destination data sources.
        self.destination_data_source_settings = destination_data_source_settings
        # The type of the destination data source. Valid values: `Hologres`, `OSS-HDFS`, `OSS`, `MaxCompute`, `LogHub`, `StarRocks`, `DataHub`, `AnalyticDB for MySQL`, `Kafka`, and `Hive`.
        self.destination_data_source_type = destination_data_source_type
        # The code for a job created in script mode.
        self.file_spec = file_spec
        # This parameter is deprecated. Use the `Name` parameter instead.
        self.job_name = job_name
        # The settings for the synchronization job, including DDL processing policies, data type mappings between source and destination columns, and runtime parameters.
        self.job_settings = job_settings
        # The job type. Valid values:
        # 
        # - `DatabaseRealtimeMigration`: Synchronizes multiple tables from multiple source databases in real time (stream synchronization). This type supports full, incremental, or both full and incremental synchronization.
        # 
        # - `DatabaseOfflineMigration`: Synchronizes multiple tables from multiple source databases in batches. This type supports full, incremental, or both full and incremental synchronization.
        # 
        # - `SingleTableRealtimeMigration`: Synchronizes a single source table in real time (stream synchronization).
        self.job_type = job_type
        # The synchronization type. Valid values:
        # 
        # - `FullAndRealtimeIncremental`: Full and real-time incremental synchronization for an entire database.
        # 
        # - `RealtimeIncremental`: Real-time incremental synchronization for a single table.
        # 
        # - `Full`: Full batch synchronization for an entire database.
        # 
        # - `OfflineIncremental`: Incremental synchronization in batch mode.
        # 
        # - `FullAndOfflineIncremental`: Full and incremental batch synchronization for an entire database.
        self.migration_type = migration_type
        # The name of the job.
        self.name = name
        # The job owner.
        self.owner = owner
        # The ID of the DataWorks workspace for this API call. To obtain the workspace ID, log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace Management page.
        self.project_id = project_id
        # The resource settings.
        self.resource_settings = resource_settings
        # Settings for the source data sources.
        self.source_data_source_settings = source_data_source_settings
        # The type of the source data source. Valid values: `PolarDB`, `MySQL`, `Kafka`, `LogHub`, `Hologres`, `Oracle`, `OceanBase`, `MongoDB`, `Redshift`, `Hive`, `SQL Server`, `Doris`, and `ClickHouse`.
        self.source_data_source_type = source_data_source_type
        # Transformation mappings for the objects to be synchronized. Each mapping defines selection rules for a group of source objects and the transformation rules to apply to them.
        # 
        # > [ { "SourceObjectSelectionRules":[ { "ObjectType":"Database", "Action":"Include", "ExpressionType":"Exact", "Expression":"biz_db" }, { "ObjectType":"Schema", "Action":"Include", "ExpressionType":"Exact", "Expression":"s1" }, { "ObjectType":"Table", "Action":"Include", "ExpressionType":"Exact", "Expression":"table1" } ], "TransformationRuleNames":[ { "RuleName":"my_database_rename_rule", "RuleActionType":"Rename", "RuleTargetType":"Schema" } ] } ]
        self.table_mappings = table_mappings
        # A list of transformation rules for the objects to be synchronized.
        # 
        # > [ { "RuleName":"my_database_rename_rule", "RuleActionType":"Rename", "RuleTargetType":"Schema", "RuleExpression":"{\\\\"expression\\\\":\\\\"${srcDatasoureName}_${srcDatabaseName}\\\\"}" } ]
        self.transformation_rules = transformation_rules

    def validate(self):
        if self.destination_data_source_settings:
            for v1 in self.destination_data_source_settings:
                 if v1:
                    v1.validate()
        if self.job_settings:
            self.job_settings.validate()
        if self.resource_settings:
            self.resource_settings.validate()
        if self.source_data_source_settings:
            for v1 in self.source_data_source_settings:
                 if v1:
                    v1.validate()
        if self.table_mappings:
            for v1 in self.table_mappings:
                 if v1:
                    v1.validate()
        if self.transformation_rules:
            for v1 in self.transformation_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        result['DestinationDataSourceSettings'] = []
        if self.destination_data_source_settings is not None:
            for k1 in self.destination_data_source_settings:
                result['DestinationDataSourceSettings'].append(k1.to_map() if k1 else None)

        if self.destination_data_source_type is not None:
            result['DestinationDataSourceType'] = self.destination_data_source_type

        if self.file_spec is not None:
            result['FileSpec'] = self.file_spec

        if self.job_name is not None:
            result['JobName'] = self.job_name

        if self.job_settings is not None:
            result['JobSettings'] = self.job_settings.to_map()

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

        if self.resource_settings is not None:
            result['ResourceSettings'] = self.resource_settings.to_map()

        result['SourceDataSourceSettings'] = []
        if self.source_data_source_settings is not None:
            for k1 in self.source_data_source_settings:
                result['SourceDataSourceSettings'].append(k1.to_map() if k1 else None)

        if self.source_data_source_type is not None:
            result['SourceDataSourceType'] = self.source_data_source_type

        result['TableMappings'] = []
        if self.table_mappings is not None:
            for k1 in self.table_mappings:
                result['TableMappings'].append(k1.to_map() if k1 else None)

        result['TransformationRules'] = []
        if self.transformation_rules is not None:
            for k1 in self.transformation_rules:
                result['TransformationRules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.destination_data_source_settings = []
        if m.get('DestinationDataSourceSettings') is not None:
            for k1 in m.get('DestinationDataSourceSettings'):
                temp_model = main_models.CreateDIJobRequestDestinationDataSourceSettings()
                self.destination_data_source_settings.append(temp_model.from_map(k1))

        if m.get('DestinationDataSourceType') is not None:
            self.destination_data_source_type = m.get('DestinationDataSourceType')

        if m.get('FileSpec') is not None:
            self.file_spec = m.get('FileSpec')

        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        if m.get('JobSettings') is not None:
            temp_model = main_models.CreateDIJobRequestJobSettings()
            self.job_settings = temp_model.from_map(m.get('JobSettings'))

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
            temp_model = main_models.CreateDIJobRequestResourceSettings()
            self.resource_settings = temp_model.from_map(m.get('ResourceSettings'))

        self.source_data_source_settings = []
        if m.get('SourceDataSourceSettings') is not None:
            for k1 in m.get('SourceDataSourceSettings'):
                temp_model = main_models.CreateDIJobRequestSourceDataSourceSettings()
                self.source_data_source_settings.append(temp_model.from_map(k1))

        if m.get('SourceDataSourceType') is not None:
            self.source_data_source_type = m.get('SourceDataSourceType')

        self.table_mappings = []
        if m.get('TableMappings') is not None:
            for k1 in m.get('TableMappings'):
                temp_model = main_models.CreateDIJobRequestTableMappings()
                self.table_mappings.append(temp_model.from_map(k1))

        self.transformation_rules = []
        if m.get('TransformationRules') is not None:
            for k1 in m.get('TransformationRules'):
                temp_model = main_models.CreateDIJobRequestTransformationRules()
                self.transformation_rules.append(temp_model.from_map(k1))

        return self

class CreateDIJobRequestTransformationRules(DaraModel):
    def __init__(
        self,
        rule_action_type: str = None,
        rule_expression: str = None,
        rule_name: str = None,
        rule_target_type: str = None,
    ):
        # The action type. Valid values:
        # 
        # - `DefinePrimaryKey`: Defines a primary key.
        # 
        # - `Rename`: Renames an object.
        # 
        # - `AddColumn`: Adds a column.
        # 
        # - `HandleDml`: Handles DML operations.
        # 
        # - `DefineIncrementalCondition`: Defines an incremental condition.
        # 
        # - `DefineCycleScheduleSettings`: Defines periodic scheduling settings.
        # 
        # - `DefinePartitionKey`: Defines a partition key.
        self.rule_action_type = rule_action_type
        # The rule expression, specified as a JSON string.
        # 
        # 1. Renaming rule (`Rename`)
        # 
        # - Example: `{"expression":"${srcDatasourceName}_${srcDatabaseName}_0922" }`
        # 
        # - `expression`: The renaming expression. You can use the following variables: `${srcDatasourceName}` (name of the source data source), `${srcDatabaseName}` (name of the source database), and `${srcTableName}` (name of the source table).
        # 
        # 2. Rule for adding a column (`AddColumn`)
        # 
        # - Example: `{"columns":[{"columnName":"my_add_column","columnValueType":"Constant","columnValue":"123"}]}`
        # 
        # - If you do not specify this rule, no columns are added.
        # 
        # - `columnName`: The name of the column to add.
        # 
        # - `columnValueType`: The value type of the added column. Valid values: `Constant` and `Variable`.
        # 
        # - `columnValue`: The value of the added column. If `columnValueType` is `Constant`, the value is a custom string constant. If `columnValueType` is `Variable`, the value is a built-in variable. Valid built-in variables include: `EXECUTE_TIME` (execution time, Long), `DB_NAME_SRC` (source database name, String), `DATASOURCE_NAME_SRC` (source data source name, String), `TABLE_NAME_SRC` (source table name, String), `DB_NAME_DEST` (destination database name, String), `DATASOURCE_NAME_DEST` (destination data source name, String), `TABLE_NAME_DEST` (destination table name, String), and `DB_NAME_SRC_TRANSED` (transformed database name, String).
        # 
        # 3. Rule for defining the primary key columns of a destination table (`DefinePrimaryKey`)
        # 
        # - Example: `{"columns":["ukcolumn1","ukcolumn2"]}`
        # 
        # - If you do not specify this rule, the primary key columns of the source table are used by default.
        # 
        # - If the destination is an existing table, Data Integration does not modify its schema. If a specified primary key column does not exist in the destination table, the job fails to start and an error is reported.
        # 
        # - If the destination table is automatically created, Data Integration automatically creates its schema with the defined primary key columns. If a specified primary key column does not exist in the source table, the job fails to start and an error is reported.
        # 
        # 4. DML handling rule (`HandleDml`)
        # 
        # - Example: `{"dmlPolicies":[{"dmlType":"Delete","dmlAction":"Filter","filterCondition":"id > 1"}]}`
        # 
        # - If you do not specify this rule, the default `dmlAction` is `Normal` for `Insert`, `Update`, and `Delete` operations.
        # 
        # - `dmlType`: The DML operation type. Valid values: `Insert`, `Update`, and `Delete`.
        # 
        # - `dmlAction`: The DML handling policy. Valid values: `Normal` (normal processing), `Ignore`, `Filter` (conditional processing, used when `dmlType` is `Update` or `Delete`), and `LogicalDelete` (logical deletion).
        # 
        # - `filterCondition`: The DML filter condition, used when `dmlAction` is `Filter`.
        # 
        # 5. Incremental condition (`DefineIncrementalCondition`)
        # 
        # - Example: `{"where":"id > 0"}`
        # 
        # - Specifies the filter condition for incremental synchronization.
        # 
        # 6. Parameters for periodic scheduling (`DefineCycleScheduleSettings`)
        # 
        # - Example: `{"cronExpress":" * * * * * *", "cycleType":"1"}`
        # 
        # - Specifies the parameters for periodically scheduling a job.
        # 
        # 7. Rule to define a partition key (`DefinePartitionKey`)
        # 
        # - Example: `{"columns":["id"]}`
        # 
        # - Specifies a partition key.
        self.rule_expression = rule_expression
        # The name of the rule. The rule name must be unique for a specific action type and target object type. Maximum length: 50 characters.
        self.rule_name = rule_name
        # The type of the object to which the action applies. Valid values:
        # 
        # - `Table`
        # 
        # - `Schema`
        # 
        # - `Database`
        self.rule_target_type = rule_target_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rule_action_type is not None:
            result['RuleActionType'] = self.rule_action_type

        if self.rule_expression is not None:
            result['RuleExpression'] = self.rule_expression

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.rule_target_type is not None:
            result['RuleTargetType'] = self.rule_target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleActionType') is not None:
            self.rule_action_type = m.get('RuleActionType')

        if m.get('RuleExpression') is not None:
            self.rule_expression = m.get('RuleExpression')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('RuleTargetType') is not None:
            self.rule_target_type = m.get('RuleTargetType')

        return self

class CreateDIJobRequestTableMappings(DaraModel):
    def __init__(
        self,
        source_object_selection_rules: List[main_models.CreateDIJobRequestTableMappingsSourceObjectSelectionRules] = None,
        transformation_rules: List[main_models.CreateDIJobRequestTableMappingsTransformationRules] = None,
    ):
        # Each rule can select a set of source objects to synchronize. Multiple rules combine to select one table.
        self.source_object_selection_rules = source_object_selection_rules
        # The names of the transformation rules to apply to the selected objects.
        self.transformation_rules = transformation_rules

    def validate(self):
        if self.source_object_selection_rules:
            for v1 in self.source_object_selection_rules:
                 if v1:
                    v1.validate()
        if self.transformation_rules:
            for v1 in self.transformation_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SourceObjectSelectionRules'] = []
        if self.source_object_selection_rules is not None:
            for k1 in self.source_object_selection_rules:
                result['SourceObjectSelectionRules'].append(k1.to_map() if k1 else None)

        result['TransformationRules'] = []
        if self.transformation_rules is not None:
            for k1 in self.transformation_rules:
                result['TransformationRules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.source_object_selection_rules = []
        if m.get('SourceObjectSelectionRules') is not None:
            for k1 in m.get('SourceObjectSelectionRules'):
                temp_model = main_models.CreateDIJobRequestTableMappingsSourceObjectSelectionRules()
                self.source_object_selection_rules.append(temp_model.from_map(k1))

        self.transformation_rules = []
        if m.get('TransformationRules') is not None:
            for k1 in m.get('TransformationRules'):
                temp_model = main_models.CreateDIJobRequestTableMappingsTransformationRules()
                self.transformation_rules.append(temp_model.from_map(k1))

        return self

class CreateDIJobRequestTableMappingsTransformationRules(DaraModel):
    def __init__(
        self,
        rule_action_type: str = None,
        rule_name: str = None,
        rule_target_type: str = None,
    ):
        # The action type. Valid values:
        # 
        # - `DefinePrimaryKey`: Defines a primary key.
        # 
        # - `Rename`: Renames an object.
        # 
        # - `AddColumn`: Adds a column.
        # 
        # - `HandleDml`: Handles DML operations.
        # 
        # - `DefineIncrementalCondition`: Defines an incremental condition.
        # 
        # - `DefineCycleScheduleSettings`: Defines periodic scheduling settings.
        # 
        # - `DefinePartitionKey`: Defines a partition key.
        self.rule_action_type = rule_action_type
        # The name of the transformation rule. The rule name must be unique for a specific action type and target object type. Maximum length: 50 characters.
        self.rule_name = rule_name
        # The type of the object to which the action applies. Valid values:
        # 
        # - `Table`
        # 
        # - `Schema`
        # 
        # - `Database`
        self.rule_target_type = rule_target_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rule_action_type is not None:
            result['RuleActionType'] = self.rule_action_type

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.rule_target_type is not None:
            result['RuleTargetType'] = self.rule_target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleActionType') is not None:
            self.rule_action_type = m.get('RuleActionType')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('RuleTargetType') is not None:
            self.rule_target_type = m.get('RuleTargetType')

        return self

class CreateDIJobRequestTableMappingsSourceObjectSelectionRules(DaraModel):
    def __init__(
        self,
        action: str = None,
        expression: str = None,
        expression_type: str = None,
        object_type: str = None,
    ):
        # The selection action. Valid values: `Include` and `Exclude`.
        self.action = action
        # The expression.
        self.expression = expression
        # The expression type. Valid values: `Exact` and `Regex`.
        self.expression_type = expression_type
        # The object type. Valid values:
        # 
        # - `Table`
        # 
        # - `Schema`
        # 
        # - `Database`
        self.object_type = object_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.expression is not None:
            result['Expression'] = self.expression

        if self.expression_type is not None:
            result['ExpressionType'] = self.expression_type

        if self.object_type is not None:
            result['ObjectType'] = self.object_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('Expression') is not None:
            self.expression = m.get('Expression')

        if m.get('ExpressionType') is not None:
            self.expression_type = m.get('ExpressionType')

        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')

        return self

class CreateDIJobRequestSourceDataSourceSettings(DaraModel):
    def __init__(
        self,
        data_source_name: str = None,
        data_source_properties: main_models.CreateDIJobRequestSourceDataSourceSettingsDataSourceProperties = None,
    ):
        # The name of the data source.
        self.data_source_name = data_source_name
        # The properties of the data source.
        self.data_source_properties = data_source_properties

    def validate(self):
        if self.data_source_properties:
            self.data_source_properties.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_source_name is not None:
            result['DataSourceName'] = self.data_source_name

        if self.data_source_properties is not None:
            result['DataSourceProperties'] = self.data_source_properties.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceName') is not None:
            self.data_source_name = m.get('DataSourceName')

        if m.get('DataSourceProperties') is not None:
            temp_model = main_models.CreateDIJobRequestSourceDataSourceSettingsDataSourceProperties()
            self.data_source_properties = temp_model.from_map(m.get('DataSourceProperties'))

        return self

class CreateDIJobRequestSourceDataSourceSettingsDataSourceProperties(DaraModel):
    def __init__(
        self,
        connection_properties: str = None,
        encoding: str = None,
        timezone: str = None,
    ):
        # Custom connection settings for the data source, such as instance ID, access credentials, and instance region. You must specify this parameter or `DataSourceName`.
        # 
        # This parameter applies only when the data source is configured in instance mode (`ConnectionPropertiesMode`). The property format varies by data source. For more information, see [ConnectionProperties for data sources](https://help.aliyun.com/document_detail/2852465.html).
        self.connection_properties = connection_properties
        # The database encoding format.
        self.encoding = encoding
        # The time zone.
        self.timezone = timezone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_properties is not None:
            result['ConnectionProperties'] = self.connection_properties

        if self.encoding is not None:
            result['Encoding'] = self.encoding

        if self.timezone is not None:
            result['Timezone'] = self.timezone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionProperties') is not None:
            self.connection_properties = m.get('ConnectionProperties')

        if m.get('Encoding') is not None:
            self.encoding = m.get('Encoding')

        if m.get('Timezone') is not None:
            self.timezone = m.get('Timezone')

        return self

class CreateDIJobRequestResourceSettings(DaraModel):
    def __init__(
        self,
        offline_resource_settings: main_models.CreateDIJobRequestResourceSettingsOfflineResourceSettings = None,
        realtime_resource_settings: main_models.CreateDIJobRequestResourceSettingsRealtimeResourceSettings = None,
        schedule_resource_settings: main_models.CreateDIJobRequestResourceSettingsScheduleResourceSettings = None,
    ):
        # Resource settings for batch synchronization.
        self.offline_resource_settings = offline_resource_settings
        # The resources for real-time synchronization.
        self.realtime_resource_settings = realtime_resource_settings
        # The scheduling resources.
        self.schedule_resource_settings = schedule_resource_settings

    def validate(self):
        if self.offline_resource_settings:
            self.offline_resource_settings.validate()
        if self.realtime_resource_settings:
            self.realtime_resource_settings.validate()
        if self.schedule_resource_settings:
            self.schedule_resource_settings.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.offline_resource_settings is not None:
            result['OfflineResourceSettings'] = self.offline_resource_settings.to_map()

        if self.realtime_resource_settings is not None:
            result['RealtimeResourceSettings'] = self.realtime_resource_settings.to_map()

        if self.schedule_resource_settings is not None:
            result['ScheduleResourceSettings'] = self.schedule_resource_settings.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OfflineResourceSettings') is not None:
            temp_model = main_models.CreateDIJobRequestResourceSettingsOfflineResourceSettings()
            self.offline_resource_settings = temp_model.from_map(m.get('OfflineResourceSettings'))

        if m.get('RealtimeResourceSettings') is not None:
            temp_model = main_models.CreateDIJobRequestResourceSettingsRealtimeResourceSettings()
            self.realtime_resource_settings = temp_model.from_map(m.get('RealtimeResourceSettings'))

        if m.get('ScheduleResourceSettings') is not None:
            temp_model = main_models.CreateDIJobRequestResourceSettingsScheduleResourceSettings()
            self.schedule_resource_settings = temp_model.from_map(m.get('ScheduleResourceSettings'))

        return self

class CreateDIJobRequestResourceSettingsScheduleResourceSettings(DaraModel):
    def __init__(
        self,
        requested_cu: float = None,
        resource_group_identifier: str = None,
    ):
        # The number of CUs for the scheduling resource group that is used for batch synchronization jobs.
        self.requested_cu = requested_cu
        # The identifier of the scheduling resource group used for batch synchronization jobs.
        self.resource_group_identifier = resource_group_identifier

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.requested_cu is not None:
            result['RequestedCu'] = self.requested_cu

        if self.resource_group_identifier is not None:
            result['ResourceGroupIdentifier'] = self.resource_group_identifier

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestedCu') is not None:
            self.requested_cu = m.get('RequestedCu')

        if m.get('ResourceGroupIdentifier') is not None:
            self.resource_group_identifier = m.get('ResourceGroupIdentifier')

        return self

class CreateDIJobRequestResourceSettingsRealtimeResourceSettings(DaraModel):
    def __init__(
        self,
        requested_cu: float = None,
        resource_group_identifier: str = None,
    ):
        # The number of CUs for the resource group for data integration that is used for real-time synchronization.
        self.requested_cu = requested_cu
        # The identifier of the resource group for data integration used for real-time synchronization.
        self.resource_group_identifier = resource_group_identifier

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.requested_cu is not None:
            result['RequestedCu'] = self.requested_cu

        if self.resource_group_identifier is not None:
            result['ResourceGroupIdentifier'] = self.resource_group_identifier

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestedCu') is not None:
            self.requested_cu = m.get('RequestedCu')

        if m.get('ResourceGroupIdentifier') is not None:
            self.resource_group_identifier = m.get('ResourceGroupIdentifier')

        return self

class CreateDIJobRequestResourceSettingsOfflineResourceSettings(DaraModel):
    def __init__(
        self,
        requested_cu: float = None,
        resource_group_identifier: str = None,
    ):
        # The number of CUs for the resource group for data integration that is used for batch synchronization.
        self.requested_cu = requested_cu
        # The identifier of the resource group for data integration used for batch synchronization.
        self.resource_group_identifier = resource_group_identifier

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.requested_cu is not None:
            result['RequestedCu'] = self.requested_cu

        if self.resource_group_identifier is not None:
            result['ResourceGroupIdentifier'] = self.resource_group_identifier

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestedCu') is not None:
            self.requested_cu = m.get('RequestedCu')

        if m.get('ResourceGroupIdentifier') is not None:
            self.resource_group_identifier = m.get('ResourceGroupIdentifier')

        return self

class CreateDIJobRequestJobSettings(DaraModel):
    def __init__(
        self,
        channel_settings: str = None,
        column_data_type_settings: List[main_models.CreateDIJobRequestJobSettingsColumnDataTypeSettings] = None,
        cycle_schedule_settings: main_models.CreateDIJobRequestJobSettingsCycleScheduleSettings = None,
        ddl_handling_settings: List[main_models.CreateDIJobRequestJobSettingsDdlHandlingSettings] = None,
        runtime_settings: List[main_models.CreateDIJobRequestJobSettingsRuntimeSettings] = None,
    ):
        # Settings for data synchronization channels. You can configure special settings for specific channels. The following channels are supported: synchronization from Hologres to Hologres (Holo2Holo) and from Hologres to Kafka (Holo2Kafka).
        # 
        # 1. Holo2Kafka
        # 
        # - Example: `{"destinationChannelSettings":{"kafkaClientProperties":[{"key":"linger.ms","value":"100"}],"keyColumns":["col3"],"writeMode":"canal"}}`
        #   `kafkaClientProperties`: Parameters for the Kafka producer.
        # 
        # - `keyColumns`: The columns whose values are used as keys for data written to Kafka.
        # 
        # - `writeMode`: The data format for writing to Kafka. Valid values: `json` and `canal`.
        # 
        # 2. Holo2Holo
        # 
        # - Example: `{"destinationChannelSettings":{"conflictMode":"replace","dynamicColumnAction":"replay","writeMode":"replay"}}`
        # 
        # - `conflictMode`: The conflict handling policy for writing data to Hologres. Valid values: `replace` (overwrite) and `ignore`.
        # 
        # - `writeMode`: The method for writing data to Hologres. Valid values: `replay` and `insert`.
        # 
        # - `dynamicColumnAction`: The method for handling dynamic columns when writing data to Hologres. Valid values: `replay`, `insert`, and `ignore`.
        self.channel_settings = channel_settings
        # Column data type mappings.
        # 
        # > "ColumnDataTypeSettings":[ { "SourceDataType":"Bigint", "DestinationDataType":"Text" } ]
        self.column_data_type_settings = column_data_type_settings
        # The periodic scheduling settings.
        self.cycle_schedule_settings = cycle_schedule_settings
        # DDL handling settings.
        # 
        # > "DDLHandlingSettings":[ { "Type":"Insert", "Action":"Normal" } ]
        self.ddl_handling_settings = ddl_handling_settings
        # The runtime settings.
        self.runtime_settings = runtime_settings

    def validate(self):
        if self.column_data_type_settings:
            for v1 in self.column_data_type_settings:
                 if v1:
                    v1.validate()
        if self.cycle_schedule_settings:
            self.cycle_schedule_settings.validate()
        if self.ddl_handling_settings:
            for v1 in self.ddl_handling_settings:
                 if v1:
                    v1.validate()
        if self.runtime_settings:
            for v1 in self.runtime_settings:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_settings is not None:
            result['ChannelSettings'] = self.channel_settings

        result['ColumnDataTypeSettings'] = []
        if self.column_data_type_settings is not None:
            for k1 in self.column_data_type_settings:
                result['ColumnDataTypeSettings'].append(k1.to_map() if k1 else None)

        if self.cycle_schedule_settings is not None:
            result['CycleScheduleSettings'] = self.cycle_schedule_settings.to_map()

        result['DdlHandlingSettings'] = []
        if self.ddl_handling_settings is not None:
            for k1 in self.ddl_handling_settings:
                result['DdlHandlingSettings'].append(k1.to_map() if k1 else None)

        result['RuntimeSettings'] = []
        if self.runtime_settings is not None:
            for k1 in self.runtime_settings:
                result['RuntimeSettings'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelSettings') is not None:
            self.channel_settings = m.get('ChannelSettings')

        self.column_data_type_settings = []
        if m.get('ColumnDataTypeSettings') is not None:
            for k1 in m.get('ColumnDataTypeSettings'):
                temp_model = main_models.CreateDIJobRequestJobSettingsColumnDataTypeSettings()
                self.column_data_type_settings.append(temp_model.from_map(k1))

        if m.get('CycleScheduleSettings') is not None:
            temp_model = main_models.CreateDIJobRequestJobSettingsCycleScheduleSettings()
            self.cycle_schedule_settings = temp_model.from_map(m.get('CycleScheduleSettings'))

        self.ddl_handling_settings = []
        if m.get('DdlHandlingSettings') is not None:
            for k1 in m.get('DdlHandlingSettings'):
                temp_model = main_models.CreateDIJobRequestJobSettingsDdlHandlingSettings()
                self.ddl_handling_settings.append(temp_model.from_map(k1))

        self.runtime_settings = []
        if m.get('RuntimeSettings') is not None:
            for k1 in m.get('RuntimeSettings'):
                temp_model = main_models.CreateDIJobRequestJobSettingsRuntimeSettings()
                self.runtime_settings.append(temp_model.from_map(k1))

        return self

class CreateDIJobRequestJobSettingsRuntimeSettings(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name of the setting. Valid values:
        # 
        # - `src.offline.datasource.max.connection`: The maximum number of connections to the source of a batch synchronization job.
        # 
        # - `dst.offline.truncate`: Specifies whether to truncate the destination table before a batch job starts.
        # 
        # - `runtime.offline.speed.limit.enable`: Specifies whether to enable throttling for a batch synchronization job.
        # 
        # - `runtime.offline.concurrent`: The concurrency level of a batch synchronization job.
        # 
        # - `runtime.enable.auto.create.schema`: Specifies whether to automatically create a destination schema.
        # 
        # - `runtime.realtime.concurrent`: The concurrency level of a real-time synchronization job.
        # 
        # - `runtime.realtime.failover.minute.dataxcdc`: The wait time in minutes for a failover restart.
        # 
        # - `runtime.realtime.failover.times.dataxcdc`: The number of failover restart attempts.
        self.name = name
        # The value of the setting.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateDIJobRequestJobSettingsDdlHandlingSettings(DaraModel):
    def __init__(
        self,
        action: str = None,
        type: str = None,
    ):
        # The handling action. Valid values:
        # 
        # - `Ignore`: Ignores the DDL message.
        # 
        # - `Critical`: Reports an error.
        # 
        # - `Normal`: Processes the DDL message normally.
        self.action = action
        # The DDL type. Valid values:
        # 
        # - `RenameColumn`: Renames a column.
        # 
        # - `ModifyColumn`: Modifies a column.
        # 
        # - `CreateTable`: Creates a table.
        # 
        # - `TruncateTable`: Truncates a table.
        # 
        # - `DropTable`: Drops a table.
        # 
        # - `DropColumn`: Drops a column.
        # 
        # - `AddColumn`: Adds a column.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class CreateDIJobRequestJobSettingsCycleScheduleSettings(DaraModel):
    def __init__(
        self,
        cycle_migration_type: str = None,
        schedule_parameters: str = None,
    ):
        # The synchronization type for periodic scheduling. Valid values:
        # 
        # - `Full`: Full synchronization.
        # 
        # - `OfflineIncremental`: Incremental synchronization in batch mode.
        self.cycle_migration_type = cycle_migration_type
        # The scheduling parameters.
        self.schedule_parameters = schedule_parameters

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cycle_migration_type is not None:
            result['CycleMigrationType'] = self.cycle_migration_type

        if self.schedule_parameters is not None:
            result['ScheduleParameters'] = self.schedule_parameters

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CycleMigrationType') is not None:
            self.cycle_migration_type = m.get('CycleMigrationType')

        if m.get('ScheduleParameters') is not None:
            self.schedule_parameters = m.get('ScheduleParameters')

        return self

class CreateDIJobRequestJobSettingsColumnDataTypeSettings(DaraModel):
    def __init__(
        self,
        destination_data_type: str = None,
        source_data_type: str = None,
    ):
        # The destination data type. For example: `bigint`, `boolean`, `string`, `text`, `datetime`, `timestamp`, `decimal`, or `binary`. Available data types vary by data source.
        self.destination_data_type = destination_data_type
        # The source data type. For example: `bigint`, `boolean`, `string`, `text`, `datetime`, `timestamp`, `decimal`, or `binary`. Available data types vary by data source.
        self.source_data_type = source_data_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination_data_type is not None:
            result['DestinationDataType'] = self.destination_data_type

        if self.source_data_type is not None:
            result['SourceDataType'] = self.source_data_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationDataType') is not None:
            self.destination_data_type = m.get('DestinationDataType')

        if m.get('SourceDataType') is not None:
            self.source_data_type = m.get('SourceDataType')

        return self

class CreateDIJobRequestDestinationDataSourceSettings(DaraModel):
    def __init__(
        self,
        data_source_name: str = None,
        data_source_properties: main_models.CreateDIJobRequestDestinationDataSourceSettingsDataSourceProperties = None,
    ):
        # The name of the data source.
        self.data_source_name = data_source_name
        # The properties of the data source.
        self.data_source_properties = data_source_properties

    def validate(self):
        if self.data_source_properties:
            self.data_source_properties.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_source_name is not None:
            result['DataSourceName'] = self.data_source_name

        if self.data_source_properties is not None:
            result['DataSourceProperties'] = self.data_source_properties.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceName') is not None:
            self.data_source_name = m.get('DataSourceName')

        if m.get('DataSourceProperties') is not None:
            temp_model = main_models.CreateDIJobRequestDestinationDataSourceSettingsDataSourceProperties()
            self.data_source_properties = temp_model.from_map(m.get('DataSourceProperties'))

        return self

class CreateDIJobRequestDestinationDataSourceSettingsDataSourceProperties(DaraModel):
    def __init__(
        self,
        connection_properties: str = None,
    ):
        # Custom connection settings for the data source, such as instance ID, access credentials, and instance region. You must specify this parameter or `DataSourceName`.
        # 
        # This parameter applies only when the data source is configured in instance mode (`ConnectionPropertiesMode`). The property format varies by data source. For more information, see [ConnectionProperties for data sources](https://help.aliyun.com/document_detail/2852465.html).
        self.connection_properties = connection_properties

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_properties is not None:
            result['ConnectionProperties'] = self.connection_properties

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionProperties') is not None:
            self.connection_properties = m.get('ConnectionProperties')

        return self

