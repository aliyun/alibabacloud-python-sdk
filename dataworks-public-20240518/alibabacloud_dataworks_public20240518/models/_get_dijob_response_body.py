# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetDIJobResponseBody(DaraModel):
    def __init__(
        self,
        paging_info: main_models.GetDIJobResponseBodyPagingInfo = None,
        request_id: str = None,
    ):
        # The pagination information.
        self.paging_info = paging_info
        # The request ID. You can use the ID to locate logs and troubleshoot issues.
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
            temp_model = main_models.GetDIJobResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m.get('PagingInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetDIJobResponseBodyPagingInfo(DaraModel):
    def __init__(
        self,
        dijob_id: str = None,
        description: str = None,
        destination_data_source_settings: List[main_models.GetDIJobResponseBodyPagingInfoDestinationDataSourceSettings] = None,
        destination_data_source_type: str = None,
        id: int = None,
        job_name: str = None,
        job_settings: main_models.GetDIJobResponseBodyPagingInfoJobSettings = None,
        job_status: str = None,
        job_type: str = None,
        migration_type: str = None,
        owner: str = None,
        project_id: int = None,
        resource_settings: main_models.GetDIJobResponseBodyPagingInfoResourceSettings = None,
        source_data_source_settings: List[main_models.GetDIJobResponseBodyPagingInfoSourceDataSourceSettings] = None,
        source_data_source_type: str = None,
        table_mappings: List[main_models.GetDIJobResponseBodyPagingInfoTableMappings] = None,
        transformation_rules: List[main_models.GetDIJobResponseBodyPagingInfoTransformationRules] = None,
    ):
        # **[Deprecated]** This field is deprecated. Use the Id field instead.
        self.dijob_id = dijob_id
        # The description.
        self.description = description
        # The list of destination data source properties.
        self.destination_data_source_settings = destination_data_source_settings
        # The type of the destination data source. Valid values: Hologres, OSS-HDFS, OSS, MaxCompute, LogHub, StarRocks, DataHub, AnalyticDB_For_MySQL, Kafka, and Hive.
        self.destination_data_source_type = destination_data_source_type
        # The task ID.
        self.id = id
        # The task name.
        self.job_name = job_name
        # The runtime settings.
        self.job_settings = job_settings
        # The task status. Valid values:
        # - Finished: the task ran successfully and has finished.
        # - Failed: the task failed to run.
        # - Running: the task is running.
        # - Initialized: the task is initialized but not started.
        # - Stopping: the task is being stopped.
        # - Stop: the task is stopped.
        self.job_status = job_status
        # The task type. Valid values:
        # - DatabaseRealtimeMigration: performs stream synchronization for multiple tables across multiple source databases. Supports full data only, incremental data only, or both full and incremental data.
        # - DatabaseOfflineMigration: performs batch synchronization for multiple tables across multiple source databases. Supports full data only, incremental data only, or both full and incremental data.
        # - SingleTableRealtimeMigration: performs stream synchronization for a single source table.
        self.job_type = job_type
        # The synchronization type. Valid values:
        # - FullAndRealtimeIncremental: full and real-time incremental synchronization (real-time synchronization for the entire database).
        # - RealtimeIncremental: real-time incremental synchronization (real-time synchronization for a single table).
        # - Full: full data synchronization (batch synchronization for the entire database).
        # - OfflineIncremental: batch incremental synchronization (batch synchronization for the entire database).
        # - FullAndOfflineIncremental: full and batch incremental synchronization (batch synchronization for the entire database).
        self.migration_type = migration_type
        # The task owner.
        self.owner = owner
        # The ID of the DataWorks workspace. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the workspace configuration page to obtain the workspace ID.
        # 
        # This parameter specifies the DataWorks workspace used for this API call.
        self.project_id = project_id
        # The resource settings.
        self.resource_settings = resource_settings
        # The array of source data source settings.
        self.source_data_source_settings = source_data_source_settings
        # The type of the source data source. Valid values: PolarDB, MySQL, Kafka, LogHub, Hologres, Oracle, OceanBase, MongoDB, RedShift, Hive, SQLServer, Doris, and ClickHouse.
        self.source_data_source_type = source_data_source_type
        # The list of synchronization object transformation mappings. Each element in the list describes a set of source object selection rules and a list of transformation rules applied to the selected synchronization objects.
        # 
        # > [
        #   {
        #     "SourceObjectSelectionRules":[
        #       {
        #         "ObjectType":"Database",
        #         "Action":"Include",
        #         "ExpressionType":"Exact",
        #         "Expression":"biz_db"
        #       },
        #     {
        #         "ObjectType":"Schema",
        #         "Action":"Include",
        #         "ExpressionType":"Exact",
        #         "Expression":"s1"
        #       }, 
        #     {
        #         "ObjectType":"Table",
        #         "Action":"Include",
        #         "ExpressionType":"Exact",
        #         "Expression":"table1"
        #       }
        #     ],
        #     "TransformationRuleNames":[
        #       {
        #         "RuleName":"my_database_rename_rule",
        #         "RuleActionType":"Rename",
        #         "RuleTargetType":"Schema"
        #   		}
        #     ]
        #   }
        # ]
        self.table_mappings = table_mappings
        # The list of transformation rule definitions for synchronization objects.
        # 
        # > [
        #   {
        #     "RuleName":"my_database_rename_rule",
        #     "RuleActionType":"Rename",
        #     "RuleTargetType":"Schema",
        #     "RuleExpression":"{\\"expression\\":\\"${srcDatasoureName}_${srcDatabaseName}\\"}"
        #   }
        # ]
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
        if self.dijob_id is not None:
            result['DIJobId'] = self.dijob_id

        if self.description is not None:
            result['Description'] = self.description

        result['DestinationDataSourceSettings'] = []
        if self.destination_data_source_settings is not None:
            for k1 in self.destination_data_source_settings:
                result['DestinationDataSourceSettings'].append(k1.to_map() if k1 else None)

        if self.destination_data_source_type is not None:
            result['DestinationDataSourceType'] = self.destination_data_source_type

        if self.id is not None:
            result['Id'] = self.id

        if self.job_name is not None:
            result['JobName'] = self.job_name

        if self.job_settings is not None:
            result['JobSettings'] = self.job_settings.to_map()

        if self.job_status is not None:
            result['JobStatus'] = self.job_status

        if self.job_type is not None:
            result['JobType'] = self.job_type

        if self.migration_type is not None:
            result['MigrationType'] = self.migration_type

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
        if m.get('DIJobId') is not None:
            self.dijob_id = m.get('DIJobId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.destination_data_source_settings = []
        if m.get('DestinationDataSourceSettings') is not None:
            for k1 in m.get('DestinationDataSourceSettings'):
                temp_model = main_models.GetDIJobResponseBodyPagingInfoDestinationDataSourceSettings()
                self.destination_data_source_settings.append(temp_model.from_map(k1))

        if m.get('DestinationDataSourceType') is not None:
            self.destination_data_source_type = m.get('DestinationDataSourceType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        if m.get('JobSettings') is not None:
            temp_model = main_models.GetDIJobResponseBodyPagingInfoJobSettings()
            self.job_settings = temp_model.from_map(m.get('JobSettings'))

        if m.get('JobStatus') is not None:
            self.job_status = m.get('JobStatus')

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        if m.get('MigrationType') is not None:
            self.migration_type = m.get('MigrationType')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ResourceSettings') is not None:
            temp_model = main_models.GetDIJobResponseBodyPagingInfoResourceSettings()
            self.resource_settings = temp_model.from_map(m.get('ResourceSettings'))

        self.source_data_source_settings = []
        if m.get('SourceDataSourceSettings') is not None:
            for k1 in m.get('SourceDataSourceSettings'):
                temp_model = main_models.GetDIJobResponseBodyPagingInfoSourceDataSourceSettings()
                self.source_data_source_settings.append(temp_model.from_map(k1))

        if m.get('SourceDataSourceType') is not None:
            self.source_data_source_type = m.get('SourceDataSourceType')

        self.table_mappings = []
        if m.get('TableMappings') is not None:
            for k1 in m.get('TableMappings'):
                temp_model = main_models.GetDIJobResponseBodyPagingInfoTableMappings()
                self.table_mappings.append(temp_model.from_map(k1))

        self.transformation_rules = []
        if m.get('TransformationRules') is not None:
            for k1 in m.get('TransformationRules'):
                temp_model = main_models.GetDIJobResponseBodyPagingInfoTransformationRules()
                self.transformation_rules.append(temp_model.from_map(k1))

        return self

class GetDIJobResponseBodyPagingInfoTransformationRules(DaraModel):
    def __init__(
        self,
        rule_action_type: str = None,
        rule_expression: str = None,
        rule_name: str = None,
        rule_target_type: str = None,
    ):
        # The action type. Valid values:
        # - DefinePrimaryKey: defines the primary key.
        # - Rename: renames the object.
        # - AddColumn: adds a column.
        # - HandleDml: handles DML operations.
        # - DefineIncrementalCondition: defines the incremental condition.
        # - DefineCycleScheduleSettings: defines the periodic scheduling settings.
        # - DefinePartitionKey: defines the partition key.
        self.rule_action_type = rule_action_type
        # The rule expression in JSON string format.
        # 
        # 1. Rename rule (Rename)
        # - Example: {"expression":"${srcDatasourceName}_${srcDatabaseName}_0922"}
        # - expression: the expression for the rename transformation rule. Supported variables in the expression include: ${srcDatasourceName} (source data source name), ${srcDatabaseName} (source database name), and ${srcTableName} (source table name).
        # 
        # 2. Add column rule (AddColumn)
        # - Example: {"columns":[{"columnName":"my_add_column","columnValueType":"Constant","columnValue":"123"}]}
        # - If not specified, the default rule is to add no columns and perform no replication.
        # - columnName: the name of the appended column.
        # - columnValueType: the value type of the appended column. Valid values: Constant and Variable.
        # - columnValue: the value of the appended column. When columnValueType is Constant, the value is a custom constant of the String type. When columnValueType is Variable, the value is a built-in variable. Valid built-in variables include: EXECUTE_TIME (execution time, Long type), DB_NAME_SRC (source database name, String type), DATASOURCE_NAME_SRC (source data source name, String type), TABLE_NAME_SRC (source table name, String type), DB_NAME_DEST (destination database name, String type), DATASOURCE_NAME_DEST (destination data source name, String type), TABLE_NAME_DEST (destination table name, String type), and DB_NAME_SRC_TRANSED (transformed database name, String type).
        # 
        # 3. Specify the primary key column names for the destination table (DefinePrimaryKey)
        # - Example: {"columns":["ukcolumn1","ukcolumn2"]}
        # - If not specified, the source primary key columns are used by default.
        # - When the destination is an existing table: the data integration system does not modify the destination table schema. If the specified primary key columns are not in the destination column set, an error is reported when the task starts.
        # - When the destination is a table to be created automatically: the data integration system automatically creates the destination table schema, which includes the defined primary key columns. If the specified primary key columns are not in the destination column set, an error is reported when the task starts.
        # 
        # 4. DML handling rule (HandleDml)
        # - Example:
        # {"dmlPolicies":[{"dmlType":"Delete","dmlAction":"Filter","filterCondition":"id > 1"}]}
        # - If not specified, the default rule is Normal for Insert, Update, and Delete.
        # - dmlType: the DML operations type. Valid values: Insert, Update, and Delete.
        # - dmlAction: the DML handling policy. Valid values: Normal (normal processing), Ignore (ignore), Filter (conditional normal processing, used when dmlType is Update or Delete), and LogicalDelete (logical deletion).
        # - filterCondition: the DML filter condition, used when dmlAction is Filter.
        # 
        # 5. Incremental condition (DefineIncrementalCondition)
        # - Example:
        # {"where":"id > 0"}
        # - Specifies the incremental filter condition.
        # 
        # 6. Periodic scheduling parameters (DefineCycleScheduleSettings)
        # - Example:
        # {"cronExpress":" * * * * * *", "cycleType":"1"}
        # - Specifies the scheduling parameters for the scheduled task.
        # 
        # 7. Specify the partition key (DefinePartitionKey)
        # - Example:
        # {"columns":["id"]}
        # - Specifies the partition key.
        self.rule_expression = rule_expression
        # The rule name. The rule name must be unique under a specific combination of action type and target type.
        self.rule_name = rule_name
        # The target type of the action. Valid values:
        # - Table: table.
        # - Schema: schema.
        # - Database: database.
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

class GetDIJobResponseBodyPagingInfoTableMappings(DaraModel):
    def __init__(
        self,
        source_object_selection_rules: List[main_models.GetDIJobResponseBodyPagingInfoTableMappingsSourceObjectSelectionRules] = None,
        transformation_rules: List[main_models.GetDIJobResponseBodyPagingInfoTableMappingsTransformationRules] = None,
    ):
        # Each rule selects a set of source objects to be synchronized. Multiple rules combine to select a single table.
        self.source_object_selection_rules = source_object_selection_rules
        # The list of transformation rule definitions for synchronization objects. Each element in the list is a transformation rule definition.
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
                temp_model = main_models.GetDIJobResponseBodyPagingInfoTableMappingsSourceObjectSelectionRules()
                self.source_object_selection_rules.append(temp_model.from_map(k1))

        self.transformation_rules = []
        if m.get('TransformationRules') is not None:
            for k1 in m.get('TransformationRules'):
                temp_model = main_models.GetDIJobResponseBodyPagingInfoTableMappingsTransformationRules()
                self.transformation_rules.append(temp_model.from_map(k1))

        return self

class GetDIJobResponseBodyPagingInfoTableMappingsTransformationRules(DaraModel):
    def __init__(
        self,
        rule_action_type: str = None,
        rule_name: str = None,
        rule_target_type: str = None,
    ):
        # The action type. Valid values:
        # - DefinePrimaryKey: defines the primary key.
        # - Rename: renames the object.
        # - AddColumn: adds a column.
        # - HandleDml: handles DML operations.
        self.rule_action_type = rule_action_type
        # The rule name. The rule name must be unique when the action type and the target type of the action are the same.
        self.rule_name = rule_name
        # The target type of the action. Valid values:
        # - Table: table.
        # - Schema: schema.
        # - Database: database.
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

class GetDIJobResponseBodyPagingInfoTableMappingsSourceObjectSelectionRules(DaraModel):
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
        # - Table: table.
        # - Schema: schema.
        # - Database: database.
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

class GetDIJobResponseBodyPagingInfoSourceDataSourceSettings(DaraModel):
    def __init__(
        self,
        data_source_name: str = None,
        data_source_properties: main_models.GetDIJobResponseBodyPagingInfoSourceDataSourceSettingsDataSourceProperties = None,
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
            temp_model = main_models.GetDIJobResponseBodyPagingInfoSourceDataSourceSettingsDataSourceProperties()
            self.data_source_properties = temp_model.from_map(m.get('DataSourceProperties'))

        return self

class GetDIJobResponseBodyPagingInfoSourceDataSourceSettingsDataSourceProperties(DaraModel):
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

class GetDIJobResponseBodyPagingInfoResourceSettings(DaraModel):
    def __init__(
        self,
        offline_resource_settings: main_models.GetDIJobResponseBodyPagingInfoResourceSettingsOfflineResourceSettings = None,
        realtime_resource_settings: main_models.GetDIJobResponseBodyPagingInfoResourceSettingsRealtimeResourceSettings = None,
        schedule_resource_settings: main_models.GetDIJobResponseBodyPagingInfoResourceSettingsScheduleResourceSettings = None,
    ):
        # The batch synchronization resources.
        self.offline_resource_settings = offline_resource_settings
        # The real-time synchronization resources.
        self.realtime_resource_settings = realtime_resource_settings
        # The scheduling resource.
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
            temp_model = main_models.GetDIJobResponseBodyPagingInfoResourceSettingsOfflineResourceSettings()
            self.offline_resource_settings = temp_model.from_map(m.get('OfflineResourceSettings'))

        if m.get('RealtimeResourceSettings') is not None:
            temp_model = main_models.GetDIJobResponseBodyPagingInfoResourceSettingsRealtimeResourceSettings()
            self.realtime_resource_settings = temp_model.from_map(m.get('RealtimeResourceSettings'))

        if m.get('ScheduleResourceSettings') is not None:
            temp_model = main_models.GetDIJobResponseBodyPagingInfoResourceSettingsScheduleResourceSettings()
            self.schedule_resource_settings = temp_model.from_map(m.get('ScheduleResourceSettings'))

        return self

class GetDIJobResponseBodyPagingInfoResourceSettingsScheduleResourceSettings(DaraModel):
    def __init__(
        self,
        requested_cu: float = None,
        resource_group_identifier: str = None,
    ):
        # The number of CUs of the data integration resource group used by the batch scheduling task.
        self.requested_cu = requested_cu
        # The name of the scheduling resource group used by the batch scheduling task.
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

class GetDIJobResponseBodyPagingInfoResourceSettingsRealtimeResourceSettings(DaraModel):
    def __init__(
        self,
        requested_cu: float = None,
        resource_group_identifier: str = None,
    ):
        # The number of CUs of the data integration resource group used for real-time synchronization.
        self.requested_cu = requested_cu
        # The name of the data integration resource group used for real-time tasks.
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

class GetDIJobResponseBodyPagingInfoResourceSettingsOfflineResourceSettings(DaraModel):
    def __init__(
        self,
        requested_cu: float = None,
        resource_group_identifier: str = None,
    ):
        # The number of compute units (CUs) of the scheduling resource group used by the batch synchronization task.
        self.requested_cu = requested_cu
        # The name of the data integration resource group used for batch synchronization.
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

class GetDIJobResponseBodyPagingInfoJobSettings(DaraModel):
    def __init__(
        self,
        channel_settings: str = None,
        column_data_type_settings: List[main_models.GetDIJobResponseBodyPagingInfoJobSettingsColumnDataTypeSettings] = None,
        cycle_schedule_settings: main_models.GetDIJobResponseBodyPagingInfoJobSettingsCycleScheduleSettings = None,
        ddl_handling_settings: List[main_models.GetDIJobResponseBodyPagingInfoJobSettingsDdlHandlingSettings] = None,
        runtime_settings: List[main_models.GetDIJobResponseBodyPagingInfoJobSettingsRuntimeSettings] = None,
    ):
        # The channel-related task settings. You can configure specific channels. Currently, Holo2Holo (synchronization from Hologres to Hologres) and Holo2Kafka (synchronization from Hologres to Kafka) are supported.
        # 1. Holo2Kafka
        # - Example: {"destinationChannelSettings":{"kafkaClientProperties":[{"key":"linger.ms","value":"100"}],"keyColumns":["col3"],"writeMode":"canal"}}
        # - kafkaClientProperties: the Kafka producer parameters used when writing data to Kafka.
        # - keyColumns: the Kafka columns to which data is written.
        # - writeMode: the format in which data is written to Kafka. Valid values: json and canal.
        # 
        # 2. Holo2Holo
        # - Example: {"destinationChannelSettings":{"conflictMode":"replace","dynamicColumnAction":"replay","writeMode":"replay"}}
        # - conflictMode: the conflict handling policy when writing data to Hologres. Valid values: replace (overwrite) and ignore (ignore).
        # - writeMode: the method used to write data to Hologres. Valid values: replay and insert.
        # - dynamicColumnAction: the method used to write dynamic columns to Hologres. Valid values: replay, insert, and ignore.
        self.channel_settings = channel_settings
        # The column type mappings.
        self.column_data_type_settings = column_data_type_settings
        # The periodic scheduling settings.
        self.cycle_schedule_settings = cycle_schedule_settings
        # The array of DDL handling settings, which includes a list of DDL types to be handled and their corresponding rules.
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
                temp_model = main_models.GetDIJobResponseBodyPagingInfoJobSettingsColumnDataTypeSettings()
                self.column_data_type_settings.append(temp_model.from_map(k1))

        if m.get('CycleScheduleSettings') is not None:
            temp_model = main_models.GetDIJobResponseBodyPagingInfoJobSettingsCycleScheduleSettings()
            self.cycle_schedule_settings = temp_model.from_map(m.get('CycleScheduleSettings'))

        self.ddl_handling_settings = []
        if m.get('DdlHandlingSettings') is not None:
            for k1 in m.get('DdlHandlingSettings'):
                temp_model = main_models.GetDIJobResponseBodyPagingInfoJobSettingsDdlHandlingSettings()
                self.ddl_handling_settings.append(temp_model.from_map(k1))

        self.runtime_settings = []
        if m.get('RuntimeSettings') is not None:
            for k1 in m.get('RuntimeSettings'):
                temp_model = main_models.GetDIJobResponseBodyPagingInfoJobSettingsRuntimeSettings()
                self.runtime_settings.append(temp_model.from_map(k1))

        return self

class GetDIJobResponseBodyPagingInfoJobSettingsRuntimeSettings(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The setting name. Valid values:
        # - src.offline.datasource.max.connection: the maximum number of connections to the source for batch tasks.
        # - dst.offline.truncate: specifies whether to truncate the destination table.
        # - runtime.offline.speed.limit.enable: specifies whether to enable throttling for batch tasks.
        # - runtime.offline.concurrent: the concurrency of batch synchronization tasks.
        # - runtime.enable.auto.create.schema: specifies whether to automatically create a schema at the destination.
        # - runtime.realtime.concurrent: the concurrency of real-time tasks.
        # - runtime.realtime.failover.minute.dataxcdc: the wait time in minutes before restarting after a failover failure.
        # - runtime.realtime.failover.times.dataxcdc: the number of restart attempts after a failover failure.
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

class GetDIJobResponseBodyPagingInfoJobSettingsDdlHandlingSettings(DaraModel):
    def __init__(
        self,
        action: str = None,
        type: str = None,
    ):
        # The handling action. Valid values:
        # - Ignore: ignores the DDL statement.
        # - Critical: reports an error.
        # - Normal: processes the DDL statement normally.
        self.action = action
        # The DDL type. Valid values:
        # - RenameColumn: renames a column.
        # - ModifyColumn: modifies a column.
        # - CreateTable: creates a table.
        # - TruncateTable: truncates a table.
        # - DropTable: drops a table.
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

class GetDIJobResponseBodyPagingInfoJobSettingsCycleScheduleSettings(DaraModel):
    def __init__(
        self,
        cycle_migration_type: str = None,
        schedule_parameters: str = None,
    ):
        # The synchronization type that requires periodic scheduling. Valid values:
        # - Full: full data synchronization.
        # - OfflineIncremental: batch incremental synchronization.
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

class GetDIJobResponseBodyPagingInfoJobSettingsColumnDataTypeSettings(DaraModel):
    def __init__(
        self,
        destination_data_type: str = None,
        source_data_type: str = None,
    ):
        # The destination data type, such as bigint, boolean, string, text, datetime, timestamp, decimal, and binary. Data types vary based on the data source type.
        self.destination_data_type = destination_data_type
        # The source data type, such as bigint, boolean, string, text, datetime, timestamp, decimal, and binary. Data types vary based on the data source type.
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

class GetDIJobResponseBodyPagingInfoDestinationDataSourceSettings(DaraModel):
    def __init__(
        self,
        data_source_name: str = None,
    ):
        # The name of the destination data source.
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

