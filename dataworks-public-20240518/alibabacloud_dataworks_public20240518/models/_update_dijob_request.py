# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class UpdateDIJobRequest(DaraModel):
    def __init__(
        self,
        dijob_id: int = None,
        description: str = None,
        file_spec: str = None,
        id: int = None,
        job_settings: main_models.UpdateDIJobRequestJobSettings = None,
        owner: str = None,
        project_id: int = None,
        resource_settings: main_models.UpdateDIJobRequestResourceSettings = None,
        table_mappings: List[main_models.UpdateDIJobRequestTableMappings] = None,
        transformation_rules: List[main_models.UpdateDIJobRequestTransformationRules] = None,
    ):
        # This parameter is deprecated. Use the `Id` parameter instead.
        self.dijob_id = dijob_id
        # The description of the synchronization job.
        self.description = description
        # The job configuration in script mode.
        self.file_spec = file_spec
        # The ID of the synchronization job.
        self.id = id
        # The settings for the synchronization job. This includes DDL handling settings, data type mappings for columns between the source and destination, and runtime parameters.
        self.job_settings = job_settings
        # The owner of the synchronization job.
        self.owner = owner
        # The ID of the DataWorks workspace. You can call the [ListProjects](https://help.aliyun.com/document_detail/178393.html) operation to get the workspace ID.
        self.project_id = project_id
        # The resource settings.
        self.resource_settings = resource_settings
        # A list of object transformation mappings. Each mapping specifies a set of selection rules for source objects and a list of transformation rules that apply to the selected objects.
        # 
        # > [ { "SourceObjectSelectionRules":[ { "ObjectType":"Database", "Action":"Include", "ExpressionType":"Exact", "Expression":"biz_db" }, { "ObjectType":"Schema", "Action":"Include", "ExpressionType":"Exact", "Expression":"s1" }, { "ObjectType":"Table", "Action":"Include", "ExpressionType":"Exact", "Expression":"table1" } ], "TransformationRuleNames":[ { "RuleName":"my_database_rename_rule", "RuleActionType":"Rename", "RuleTargetType":"Schema" } ] } ]
        self.table_mappings = table_mappings
        # A list of transformation rule definitions.
        # 
        # > [ { "RuleName":"my_database_rename_rule", "RuleActionType":"Rename", "RuleTargetType":"Schema", "RuleExpression":"{"expression":"${srcDatasoureName}_${srcDatabaseName}"}" } ]
        self.transformation_rules = transformation_rules

    def validate(self):
        if self.job_settings:
            self.job_settings.validate()
        if self.resource_settings:
            self.resource_settings.validate()
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
        if self.dijob_id is not None:
            result['DIJobId'] = self.dijob_id

        if self.description is not None:
            result['Description'] = self.description

        if self.file_spec is not None:
            result['FileSpec'] = self.file_spec

        if self.id is not None:
            result['Id'] = self.id

        if self.job_settings is not None:
            result['JobSettings'] = self.job_settings.to_map()

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.resource_settings is not None:
            result['ResourceSettings'] = self.resource_settings.to_map()

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
        if m.get('DIJobId') is not None:
            self.dijob_id = m.get('DIJobId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FileSpec') is not None:
            self.file_spec = m.get('FileSpec')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('JobSettings') is not None:
            temp_model = main_models.UpdateDIJobRequestJobSettings()
            self.job_settings = temp_model.from_map(m.get('JobSettings'))

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ResourceSettings') is not None:
            temp_model = main_models.UpdateDIJobRequestResourceSettings()
            self.resource_settings = temp_model.from_map(m.get('ResourceSettings'))

        self.table_mappings = []
        if m.get('TableMappings') is not None:
            for k1 in m.get('TableMappings'):
                temp_model = main_models.UpdateDIJobRequestTableMappings()
                self.table_mappings.append(temp_model.from_map(k1))

        self.transformation_rules = []
        if m.get('TransformationRules') is not None:
            for k1 in m.get('TransformationRules'):
                temp_model = main_models.UpdateDIJobRequestTransformationRules()
                self.transformation_rules.append(temp_model.from_map(k1))

        return self

class UpdateDIJobRequestTransformationRules(DaraModel):
    def __init__(
        self,
        rule_action_type: str = None,
        rule_expression: str = None,
        rule_name: str = None,
        rule_target_type: str = None,
    ):
        # The type of the action. Valid values:
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
        # 1. Rename rule (`Rename`)
        # 
        # - Example: `{"expression":"${srcDatasourceName}_${srcDatabaseName}_0922"}`
        # 
        # - `expression`: The expression for the rename transformation rule. The expression supports variables, including `${srcDatasourceName}` (source data source name), `${srcDatabaseName}` (source database name), and `${srcTableName}` (source table name).
        # 
        # 2. Add column rule (`AddColumn`)
        # 
        # - Example: `{"columns":[{"columnName":"my_add_column","columnValueType":"Constant","columnValue":"123"}]}`
        # 
        # - If this rule is not specified, no columns are added.
        # 
        # - `columnName`: The name of the column to add.
        # 
        # - `columnValueType`: The value type of the added column. Valid values: `Constant` and `Variable`.
        # 
        # - `columnValue`: The value of the added column. If `columnValueType` is `Constant`, the value is a custom constant of the string type. If `columnValueType` is `Variable`, the value is a built-in variable. Valid built-in variables: `EXECUTE_TIME` (execution time, Long type), `DB_NAME_SRC` (source database name, String type), `DATASOURCE_NAME_SRC` (source data source name, String type), `TABLE_NAME_SRC` (source table name, String type), `DB_NAME_DEST` (destination database name, String type), `DATASOURCE_NAME_DEST` (destination data source name, String type), `TABLE_NAME_DEST` (destination table name, String type), and `DB_NAME_SRC_TRANSED` (transformed database name, String type).
        # 
        # 3. Define primary key rule (`DefinePrimaryKey`)
        # 
        # - Example: `{"columns":["ukcolumn1","ukcolumn2"]}`
        # 
        # - If this rule is not specified, the primary key of the source is used by default.
        # 
        # - Data Integration does not modify the structure of an existing destination table. If a specified primary key column does not exist in the table, the synchronization job fails.
        # 
        # - When a destination table is automatically created, Data Integration includes the defined primary key columns in the structure. If a specified primary key column is not in the destination column set, the synchronization job fails.
        # 
        # 4. DML handling rule (`HandleDml`)
        # 
        # - Example: `{"dmlPolicies":[{"dmlType":"Delete","dmlAction":"Filter","filterCondition":"id > 1"}]}`
        # 
        # - If this rule is not specified, the default action for `Insert`, `Update`, and `Delete` operations is `Normal`.
        # 
        # - `dmlType`: The DML operation type. Valid values: `Insert`, `Update`, and `Delete`.
        # 
        # - `dmlAction`: The DML handling policy. Valid values: `Normal` (process the operation), `Ignore` (ignore the operation), `Filter` (conditionally process the operation, used when `dmlType` is `Update` or `Delete`), and `LogicalDelete` (perform a logical delete).
        # 
        # - `filterCondition`: The DML filter condition, used when `dmlAction` is `Filter`.
        # 
        # 5. Incremental condition rule (`DefineIncrementalCondition`)
        # 
        # - Example: `{"where":"id > 0"}`
        # 
        # - The `WHERE` clause for the incremental condition.
        # 
        # 6. Periodic scheduling rule (`DefineCycleScheduleSettings`)
        # 
        # - Example: `{"cronExpress":" * * * * * *", "cycleType":"1"}`
        # 
        # - Specifies the scheduling parameters for a periodic job.
        # 
        # 7. Define partition key rule (`DefinePartitionKey`)
        # 
        # - Example: `{"columns":["id"]}`
        # 
        # - Specifies the partition key.
        self.rule_expression = rule_expression
        # The name of the transformation rule. The name must be unique for a specific combination of `RuleActionType` and `RuleTargetType` and can be up to 50 characters long.
        self.rule_name = rule_name
        # The type of the target object. Valid values:
        # 
        # - `Table` (table)
        # 
        # - `Schema` (schema)
        # 
        # - `Database` (database)
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

class UpdateDIJobRequestTableMappings(DaraModel):
    def __init__(
        self,
        source_object_selection_rules: List[main_models.UpdateDIJobRequestTableMappingsSourceObjectSelectionRules] = None,
        transformation_rules: List[main_models.UpdateDIJobRequestTableMappingsTransformationRules] = None,
    ):
        # The rules for selecting source objects. Each rule can select a different type of source object to synchronize, such as a source database or table.
        self.source_object_selection_rules = source_object_selection_rules
        # The transformation rules for the source objects.
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
                temp_model = main_models.UpdateDIJobRequestTableMappingsSourceObjectSelectionRules()
                self.source_object_selection_rules.append(temp_model.from_map(k1))

        self.transformation_rules = []
        if m.get('TransformationRules') is not None:
            for k1 in m.get('TransformationRules'):
                temp_model = main_models.UpdateDIJobRequestTableMappingsTransformationRules()
                self.transformation_rules.append(temp_model.from_map(k1))

        return self

class UpdateDIJobRequestTableMappingsTransformationRules(DaraModel):
    def __init__(
        self,
        rule_action_type: str = None,
        rule_name: str = None,
        rule_target_type: str = None,
    ):
        # The type of the action. Valid values:
        # 
        # - `DefinePrimaryKey`: Defines a primary key.
        # 
        # - `Rename`: Renames an object.
        # 
        # - `AddColumn`: Adds a column.
        # 
        # - `HandleDml`: Handles DML operations.
        self.rule_action_type = rule_action_type
        # The name of the transformation rule. The name must be unique for a specific combination of `RuleActionType` and `RuleTargetType` and can be up to 50 characters long.
        self.rule_name = rule_name
        # The type of the target object. Valid values:
        # 
        # - `Table` (table)
        # 
        # - `Schema` (schema)
        # 
        # - `Database` (database)
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

class UpdateDIJobRequestTableMappingsSourceObjectSelectionRules(DaraModel):
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
        # The type of the expression. Valid values: `Exact` and `Regex`.
        self.expression_type = expression_type
        # The object type. Valid values:
        # 
        # - `Table` (table)
        # 
        # - `Schema` (schema)
        # 
        # - `Database` (database)
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

class UpdateDIJobRequestResourceSettings(DaraModel):
    def __init__(
        self,
        offline_resource_settings: main_models.UpdateDIJobRequestResourceSettingsOfflineResourceSettings = None,
        realtime_resource_settings: main_models.UpdateDIJobRequestResourceSettingsRealtimeResourceSettings = None,
        schedule_resource_settings: main_models.UpdateDIJobRequestResourceSettingsScheduleResourceSettings = None,
    ):
        # The resource settings for the offline synchronization job.
        self.offline_resource_settings = offline_resource_settings
        # The resource settings for the real-time synchronization job.
        self.realtime_resource_settings = realtime_resource_settings
        # The scheduling resource settings.
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
            temp_model = main_models.UpdateDIJobRequestResourceSettingsOfflineResourceSettings()
            self.offline_resource_settings = temp_model.from_map(m.get('OfflineResourceSettings'))

        if m.get('RealtimeResourceSettings') is not None:
            temp_model = main_models.UpdateDIJobRequestResourceSettingsRealtimeResourceSettings()
            self.realtime_resource_settings = temp_model.from_map(m.get('RealtimeResourceSettings'))

        if m.get('ScheduleResourceSettings') is not None:
            temp_model = main_models.UpdateDIJobRequestResourceSettingsScheduleResourceSettings()
            self.schedule_resource_settings = temp_model.from_map(m.get('ScheduleResourceSettings'))

        return self

class UpdateDIJobRequestResourceSettingsScheduleResourceSettings(DaraModel):
    def __init__(
        self,
        requested_cu: float = None,
        resource_group_identifier: str = None,
    ):
        # The number of CUs for the scheduling resource group used by the offline synchronization job.
        self.requested_cu = requested_cu
        # The name of the scheduling resource group used by the offline synchronization job.
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

class UpdateDIJobRequestResourceSettingsRealtimeResourceSettings(DaraModel):
    def __init__(
        self,
        requested_cu: float = None,
        resource_group_identifier: str = None,
    ):
        # The number of CUs for the Data Integration resource group used by the real-time synchronization job.
        self.requested_cu = requested_cu
        # The name of the Data Integration resource group used by the real-time synchronization job.
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

class UpdateDIJobRequestResourceSettingsOfflineResourceSettings(DaraModel):
    def __init__(
        self,
        requested_cu: float = None,
        resource_group_identifier: str = None,
    ):
        # The number of CUs for the Data Integration resource group used by the offline synchronization job.
        self.requested_cu = requested_cu
        # The name of the Data Integration resource group used by the offline synchronization job.
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

class UpdateDIJobRequestJobSettings(DaraModel):
    def __init__(
        self,
        channel_settings: str = None,
        column_data_type_settings: List[main_models.UpdateDIJobRequestJobSettingsColumnDataTypeSettings] = None,
        cycle_schedule_settings: main_models.UpdateDIJobRequestJobSettingsCycleScheduleSettings = None,
        ddl_handling_settings: List[main_models.UpdateDIJobRequestJobSettingsDdlHandlingSettings] = None,
        runtime_settings: List[main_models.UpdateDIJobRequestJobSettingsRuntimeSettings] = None,
    ):
        # The job settings for specific data synchronization channels. You can apply special configurations to certain channels. Currently, `Holo2Holo` (synchronization from Hologres to Hologres) and `Holo2Kafka` (synchronization from Hologres to Kafka) are supported.
        # 
        # 1. `Holo2Kafka`
        # 
        # - Example: `{"destinationChannelSettings":{"kafkaClientProperties":[{"key":"linger.ms","value":"100"}],"keyColumns":["col3"],"writeMode":"canal"}}`
        #   `kafkaClientProperties`: The Kafka producer parameters used when writing to Kafka.
        # 
        # - `keyColumns`: The columns whose values are written to the key of a Kafka message.
        # 
        # - `writeMode`: The format for writing data to Kafka. Valid values: `json` and `canal`.
        # 
        # 2. `Holo2Holo`
        # 
        # - Example: `{"destinationChannelSettings":{"conflictMode":"replace","dynamicColumnAction":"replay","writeMode":"replay"}}`
        # 
        # - `conflictMode`: The conflict handling policy for writing data to Hologres. Valid values: `replace` (overwrite) and `ignore` (ignore).
        # 
        # - `writeMode`: The method for writing data to Hologres. Valid values: `replay` and `insert`.
        # 
        # - `dynamicColumnAction`: The action for handling dynamic columns when writing data to Hologres. Valid values: `replay`, `insert`, and `ignore`.
        self.channel_settings = channel_settings
        # An array of column data type mappings.
        # 
        # > ["ColumnDataTypeSettings":[ { "SourceDataType":"Bigint", "DestinationDataType":"Text" } ]
        self.column_data_type_settings = column_data_type_settings
        # The settings for periodic scheduling.
        self.cycle_schedule_settings = cycle_schedule_settings
        # An array of DDL handling settings.
        # 
        # > ["DDLHandlingSettings":[ { "Type":"Insert", "Action":"Normal" } ]
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
                temp_model = main_models.UpdateDIJobRequestJobSettingsColumnDataTypeSettings()
                self.column_data_type_settings.append(temp_model.from_map(k1))

        if m.get('CycleScheduleSettings') is not None:
            temp_model = main_models.UpdateDIJobRequestJobSettingsCycleScheduleSettings()
            self.cycle_schedule_settings = temp_model.from_map(m.get('CycleScheduleSettings'))

        self.ddl_handling_settings = []
        if m.get('DdlHandlingSettings') is not None:
            for k1 in m.get('DdlHandlingSettings'):
                temp_model = main_models.UpdateDIJobRequestJobSettingsDdlHandlingSettings()
                self.ddl_handling_settings.append(temp_model.from_map(k1))

        self.runtime_settings = []
        if m.get('RuntimeSettings') is not None:
            for k1 in m.get('RuntimeSettings'):
                temp_model = main_models.UpdateDIJobRequestJobSettingsRuntimeSettings()
                self.runtime_settings.append(temp_model.from_map(k1))

        return self

class UpdateDIJobRequestJobSettingsRuntimeSettings(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name of the setting. Valid values:
        # 
        # - `src.offline.datasource.max.connection`: The maximum number of concurrent connections to the source for an offline synchronization job.
        # 
        # - `dst.offline.truncate`: Specifies whether to truncate the destination table before an offline synchronization job.
        # 
        # - `runtime.offline.speed.limit.enable`: Specifies whether to enable speed limiting for an offline synchronization job.
        # 
        # - `runtime.offline.concurrent`: The concurrency level for an offline synchronization job.
        # 
        # - `runtime.enable.auto.create.schema`: Specifies whether to automatically create a schema at the destination.
        # 
        # - `runtime.realtime.concurrent`: The concurrency level for a real-time synchronization job.
        # 
        # - `runtime.realtime.failover.minute.dataxcdc`: The number of minutes to wait before a failover retry.
        # 
        # - `runtime.realtime.failover.times.dataxcdc`: The number of failover retries.
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

class UpdateDIJobRequestJobSettingsDdlHandlingSettings(DaraModel):
    def __init__(
        self,
        action: str = None,
        type: str = None,
    ):
        # The handling action. Valid values:
        # 
        # - `Ignore`: Ignores the DDL message.
        # 
        # - `Critical`: Reports an error and terminates the synchronization job.
        # 
        # - `Normal`: Processes the DDL message normally.
        self.action = action
        # The DDL type. Valid values:
        # 
        # - `RenameColumn`
        # 
        # - `ModifyColumn`
        # 
        # - `CreateTable`
        # 
        # - `TruncateTable`
        # 
        # - `DropTable`
        # 
        # - `DropColumn`
        # 
        # - `AddColumn`
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

class UpdateDIJobRequestJobSettingsCycleScheduleSettings(DaraModel):
    def __init__(
        self,
        schedule_parameters: str = None,
    ):
        # The scheduling parameters.
        self.schedule_parameters = schedule_parameters

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.schedule_parameters is not None:
            result['ScheduleParameters'] = self.schedule_parameters

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ScheduleParameters') is not None:
            self.schedule_parameters = m.get('ScheduleParameters')

        return self

class UpdateDIJobRequestJobSettingsColumnDataTypeSettings(DaraModel):
    def __init__(
        self,
        destination_data_type: str = None,
        source_data_type: str = None,
    ):
        # The destination data type. Examples: `bigint`, `boolean`, `string`, `text`, `datetime`, `timestamp`, `decimal`, and `binary`. The supported data types depend on the destination data source.
        self.destination_data_type = destination_data_type
        # The source data type. Examples: `bigint`, `boolean`, `string`, `text`, `datetime`, `timestamp`, `decimal`, and `binary`. The supported data types depend on the source data source.
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

