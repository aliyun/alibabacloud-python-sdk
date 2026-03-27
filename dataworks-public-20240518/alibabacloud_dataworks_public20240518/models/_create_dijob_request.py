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
        # The task description.
        self.description = description
        # The list of destination data source settings.
        self.destination_data_source_settings = destination_data_source_settings
        # The destination type. Valid values: Hologres, OSS-HDFS, OSS, MaxCompute, LogHub, StarRocks, DataHub, AnalyticDB for MySQL, Kafka, and Hive.
        self.destination_data_source_type = destination_data_source_type
        self.file_spec = file_spec
        # This parameter is deprecated and is replaced by the Name parameter.
        self.job_name = job_name
        # The task-level settings, including DDL handling policies, column data type mapping between source and destination, and runtime parameters.
        self.job_settings = job_settings
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
        self.migration_type = migration_type
        # The name of the synchronization task.
        self.name = name
        # The task owner.
        self.owner = owner
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to obtain the ID.
        # 
        # You must configure this parameter to specify the DataWorks workspace to which the API operation is applied.
        self.project_id = project_id
        # The resource settings.
        self.resource_settings = resource_settings
        # The list of source data source settings.
        self.source_data_source_settings = source_data_source_settings
        # The source type. Valid values: PolarDB, MySQL, Kafka, LogHub, Hologres, Oracle, OceanBase, MongoDB, Redshift, Hive, SQL Server, Doris, and ClickHouse.
        self.source_data_source_type = source_data_source_type
        # The list of synchronization object transformation mappings. Each element describes a set of source object selection rules and the transformation rules applied to those objects.
        # 
        # >  [ { "SourceObjectSelectionRules":[ { "ObjectType":"Database", "Action":"Include", "ExpressionType":"Exact", "Expression":"biz_db" }, { "ObjectType":"Schema", "Action":"Include", "ExpressionType":"Exact", "Expression":"s1" }, { "ObjectType":"Table", "Action":"Include", "ExpressionType":"Exact", "Expression":"table1" } ], "TransformationRuleNames":[ { "RuleName":"my_database_rename_rule", "RuleActionType":"Rename", "RuleTargetType":"Schema" } ] } ]
        self.table_mappings = table_mappings
        # The list of synchronization object transformation rule definitions.
        # 
        # >  [ { "RuleName":"my_database_rename_rule", "RuleActionType":"Rename", "RuleTargetType":"Schema", "RuleExpression":"{"expression":"${srcDatasoureName}_${srcDatabaseName}"}" } ]
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
        # *   DefinePrimaryKey
        # *   Rename
        # *   AddColumn
        # *   HandleDml
        # *   DefineIncrementalCondition
        # *   DefineCycleScheduleSettings
        # *   DefinePartitionKey
        self.rule_action_type = rule_action_type
        # The rule expression in JSON string format.
        # 
        # 1.  Rename rule
        # 
        # *   Example: {"expression":"${srcDatasourceName}_${srcDatabaseName}_0922" }
        # *   expression: The rename transformation expression. Supported variables include: ${srcDatasourceName} (source data source name), ${srcDatabaseName} (source database name), and ${srcTableName} (source table name).
        # 
        # 2.  AddColumn rule
        # 
        # *   Example: {"columns":[{"columnName":"my_add_column","columnValueType":"Constant","columnValue":"123"}]}
        # *   If not specified, the default behavior is to not add columns.
        # *   columnName: The name of the column to add.
        # *   columnValueType: The value type of the column to add. Valid values: Constant and Variable.
        # *   columnValue: The value of the column to add. When columnValueType is set to Constant, the value is a custom constant of the string type. When columnValueType is set to Variable, the value is a built-in variable. Built-in variables include: EXECUTE_TIME (execution time, long type), DB_NAME_SRC (source database name, string type), DATASOURCE_NAME_SRC (source data source name, string type), TABLE_NAME_SRC (source table name, string type), DB_NAME_DEST (destination database name, string type), DATASOURCE_NAME_DEST (destination data source name, string type), TABLE_NAME_DEST (destination table name, string type), and DB_NAME_SRC_TRANSED (transformed source database name, string type).
        # 
        # 3.  DefinePrimaryKey
        # 
        # *   Example: {"columns":["ukcolumn1","ukcolumn2"]}
        # *   If not specified, the source primary key columns are used by default.
        # *   When the destination table already exists: Data Integration does not modify the destination table structure. If the specified primary key columns are not in the destination table, the task fails to start.
        # *   When the destination table is auto-created: Data Integration automatically creates the destination table structure with the defined primary key columns. If the specified primary key columns are not in the destination table, the task fails to start.
        # 
        # 4.  HandleDml rule
        # 
        # *   Example of a rule used to process DML messages: {"dmlPolicies":[{"dmlType":"Delete","dmlAction":"Filter","filterCondition":"id > 1"}]}.
        # *   If not specified, the default rule is Normal for Insert, Update, and Delete.
        # *   dmlType: The DML operation type. Valid values: Insert, Update, and Delete.
        # *   dmlAction: The DML handling policy. Valid values: Normal, Ignore, Filter (conditional processing, used when dmlType is Update or Delete), and LogicalDelete.
        # *   filterCondition: The DML filter condition. This parameter is used when dmlAction is set to Filter.
        # 
        # 5.  DefineIncrementalCondition
        # 
        # *   Example: {"where":"id > 0"}
        # *   Specifies the incremental filter condition.
        # 
        # 6.  DefineCycleScheduleSettings
        # 
        # *   Example: {"cronExpress":" \\* \\* \\* \\* \\* \\*", "cycleType":"1"}
        # *   Specifies the scheduled task parameters.
        # 
        # 7.  DefinePartitionKey
        # 
        # *   Example: {"columns":["id"]}
        # *   Specifies the partition key.
        self.rule_expression = rule_expression
        # The rule name. When the action type and target type are the same, the rule name must be unique. The name cannot exceed 50 characters.
        self.rule_name = rule_name
        # The target type for the action. Valid values:
        # 
        # *   Table
        # *   Schema
        # *   Database
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
        # Each rule can select a set of source objects to synchronize. Multiple rules together select a table.
        self.source_object_selection_rules = source_object_selection_rules
        # The list of synchronization object transformation rule definitions. Each element represents a single transformation rule definition.
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
        # *   DefinePrimaryKey
        # *   Rename
        # *   AddColumn
        # *   HandleDml
        # *   DefineIncrementalCondition
        # *   DefineCycleScheduleSettings
        # *   DefinePartitionKey
        self.rule_action_type = rule_action_type
        # The rule name. The rule name must be unique for a given combination of action type and target type. The name cannot exceed 50 characters.
        self.rule_name = rule_name
        # The target type for the action. Valid values:
        # 
        # *   Table
        # *   Schema
        # *   Database
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
        # The selection action. Valid values: Include and Exclude.
        self.action = action
        # The expression.
        self.expression = expression
        # The expression type. Valid values: Exact and Regex.
        self.expression_type = expression_type
        # The object type. Valid values:
        # 
        # *   Table
        # *   Schema
        # *   Database
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
        # The data source name.
        self.data_source_name = data_source_name
        # The data source properties.
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
        encoding: str = None,
        timezone: str = None,
    ):
        # The database encoding.
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
        if self.encoding is not None:
            result['Encoding'] = self.encoding

        if self.timezone is not None:
            result['Timezone'] = self.timezone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
        # The batch synchronization resources.
        self.offline_resource_settings = offline_resource_settings
        # The real-time synchronization resources.
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
        # The CU of the scheduling resource group for batch synchronization tasks.
        self.requested_cu = requested_cu
        # The name of the scheduling resource group for batch synchronization tasks.
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
        # The CU of the Data Integration resource group used for real-time synchronization.
        self.requested_cu = requested_cu
        # The name of the Data Integration resource group used for real-time synchronization.
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
        # The CU of the Data Integration resource group used for batch synchronization.
        self.requested_cu = requested_cu
        # The name of the Data Integration resource group used for batch synchronization.
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
        # The channel-specific settings. You can configure special settings for specific channels. Currently supported: Holo2Holo (Hologres to Hologres) and Holo2Kafka (Hologres to Kafka).
        # 
        # 1.  Holo2Kafka
        # 
        # *   Example: {"destinationChannelSettings":{"kafkaClientProperties":[{"key":"linger.ms","value":"100"}],"keyColumns":["col3"],"writeMode":"canal"}} kafkaClientProperties: Kafka producer parameters used when writing to Kafka.
        # *   keyColumns: The columns to write to Kafka.
        # *   writeMode: The Kafka write format. Valid values: json and canal.
        # 
        # 2.  Holo2Holo
        # 
        # *   Example: {"destinationChannelSettings":{"conflictMode":"replace","dynamicColumnAction":"replay","writeMode":"replay"}}
        # *   conflictMode: The conflict handling policy when writing to Hologres. Valid values: replace (overwrite) and ignore.
        # *   writeMode: The write mode for Hologres. Valid values: replay and insert.
        # *   dynamicColumnAction: The dynamic column handling mode when writing to Hologres. Valid values: replay, insert, and ignore.
        self.channel_settings = channel_settings
        # The array of column type mappings.
        # 
        # >  ["ColumnDataTypeSettings":[ { "SourceDataType":"Bigint", "DestinationDataType":"Text" } ]
        self.column_data_type_settings = column_data_type_settings
        # The scheduled task settings.
        self.cycle_schedule_settings = cycle_schedule_settings
        # The array of DDL handling settings.
        # 
        # >  ["DDLHandlingSettings":[ { "Type":"Insert", "Action":"Normal" } ]
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
        # The setting name. Valid values:
        # 
        # *   src.offline.datasource.max.connection: Specifies the maximum number of connections that are allowed for reading data from the source of a batch synchronization task.
        # *   dst.offline.truncate: Specifies whether to clear the destination table before data writing.
        # *   runtime.offline.speed.limit.enable: Specifies whether throttling is enabled for a batch synchronization task.
        # *   runtime.offline.concurrent: Specifies the maximum number of parallel threads that are allowed for a batch synchronization task.
        # *   runtime.enable.auto.create.schema: Specifies whether schemas are automatically created in the destination of a synchronization task.
        # *   runtime.realtime.concurrent: Specifies the maximum number of parallel threads that are allowed for a real-time synchronization task.
        # *   runtime.realtime.failover.minute.dataxcdc: Specifies the maximum waiting duration before a synchronization task retries the next restart if the previous restart fails after failover occurs. Unit: minutes.
        # *   runtime.realtime.failover.times.dataxcdc: Specifies the maximum number of failures that are allowed for restarting a synchronization task after failovers occur.
        self.name = name
        # The setting value.
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
        # Valid values:
        # 
        # *   Ignore
        # *   Critical: Fail the task
        # *   Normal
        self.action = action
        # The DDL type. Valid values:
        # 
        # *   RenameColumn
        # *   ModifyColumn
        # *   CreateTable
        # *   TruncateTable
        # *   DropTable
        # *   DropColumn
        # *   AddColumn
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
        # The synchronization type that requires scheduling. Valid values:
        # 
        # *   Full: Full synchronization
        # *   OfflineIncremental: Batch incremental synchronization
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
        # The destination type, such as bigint, boolean, string, text, datetime, timestamp, decimal, or binary. Different data sources may have different types.
        self.destination_data_type = destination_data_type
        # The source type, such as bigint, boolean, string, text, datetime, timestamp, decimal, or binary. Different data sources may have different types.
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
    ):
        # The data source name.
        self.data_source_name = data_source_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_source_name is not None:
            result['DataSourceName'] = self.data_source_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceName') is not None:
            self.data_source_name = m.get('DataSourceName')

        return self

