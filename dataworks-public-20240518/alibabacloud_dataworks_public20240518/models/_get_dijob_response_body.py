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
        # The request ID. You can use the ID to query logs and troubleshoot issues.
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
        project_id: int = None,
        resource_settings: main_models.GetDIJobResponseBodyPagingInfoResourceSettings = None,
        source_data_source_settings: List[main_models.GetDIJobResponseBodyPagingInfoSourceDataSourceSettings] = None,
        source_data_source_type: str = None,
        table_mappings: List[main_models.GetDIJobResponseBodyPagingInfoTableMappings] = None,
        transformation_rules: List[main_models.GetDIJobResponseBodyPagingInfoTransformationRules] = None,
    ):
        # This parameter is deprecated. Use the Id parameter instead.
        self.dijob_id = dijob_id
        # The description of the synchronization task.
        self.description = description
        # The properties of the destination.
        self.destination_data_source_settings = destination_data_source_settings
        # The destination type. Valid values: Hologres, OSS-HDFS, OSS, MaxCompute, LogHub, StarRocks, DataHub, AnalyticDB_For_MySQL, Kafka, Hive.
        self.destination_data_source_type = destination_data_source_type
        # The ID of the synchronization task.
        self.id = id
        # The name of the synchronization task.
        self.job_name = job_name
        # The runtime settings.
        self.job_settings = job_settings
        # The status of the job.
        self.job_status = job_status
        # 任务类型
        # 
        # - DatabaseRealtimeMigration(整库实时):将源端多个库的多个表进行流同步，支持仅全量，仅增量，或全量+增量。
        # 
        # - DatabaseOfflineMigration(整库离线):将源端多个库的多个表进行批同步，支持仅全量，仅增量，或全量+增量。
        # 
        # - SingleTableRealtimeMigration(单表实时):将源端单个表进行流同步。
        self.job_type = job_type
        # The synchronization type. Valid values:
        # 
        # *   FullAndRealtimeIncremental: full synchronization and real-time incremental synchronization of data in an entire database
        # *   RealtimeIncremental: real-time incremental synchronization of data in a single table
        # *   Full: full batch synchronization of data in an entire database
        # *   OfflineIncremental: batch incremental synchronization of data in an entire database
        # *   FullAndOfflineIncremental: full synchronization and batch incremental synchronization of data in an entire database
        self.migration_type = migration_type
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to query the ID.
        # 
        # This parameter indicates the DataWorks workspace to which the API operation is applied.
        self.project_id = project_id
        # The resource settings.
        self.resource_settings = resource_settings
        # The settings of the source. Only a single source is supported.
        self.source_data_source_settings = source_data_source_settings
        # The source type. Valid values: PolarDB, MySQL, Kafka, LogHub, Hologres, Oracle, OceanBase, MongoDB, RedShift, Hive, SQLServer, Doris, ClickHouse.
        self.source_data_source_type = source_data_source_type
        # The list of mappings between rules used to select synchronization objects in the source and transformation rules applied to the selected synchronization objects. Each entry in the list displays a mapping between a rule used to select synchronization objects and a transformation rule applied to the selected synchronization objects.
        # 
        # >  [ { "SourceObjectSelectionRules":[ { "ObjectType":"Database", "Action":"Include", "ExpressionType":"Exact", "Expression":"biz_db" }, { "ObjectType":"Schema", "Action":"Include", "ExpressionType":"Exact", "Expression":"s1" }, { "ObjectType":"Table", "Action":"Include", "ExpressionType":"Exact", "Expression":"table1" } ], "TransformationRuleNames":[ { "RuleName":"my_database_rename_rule", "RuleActionType":"Rename", "RuleTargetType":"Schema" } ] } ]
        self.table_mappings = table_mappings
        # The list of transformation rules that are applied to the synchronization objects selected from the source.
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
        # 
        # *   DefinePrimaryKey
        # *   Rename
        # *   AddColumn
        # *   HandleDml
        # *   DefineIncrementalCondition
        # *   DefineCycleScheduleSettings
        # *   DefinePartitionKey
        self.rule_action_type = rule_action_type
        # The expression of the rule. The expression is a JSON string.
        # 
        # 1.  Example of a renaming rule
        # 
        # *   Example: {"expression":"${srcDatasourceName}_${srcDatabaseName}_0922" }
        # *   expression: the expression of the renaming rule. You can use the following variables in an expression: ${srcDatasourceName}, ${srcDatabaseName}, and ${srcTableName}. ${srcDatasourceName} indicates the name of the source. ${srcDatabaseName} indicates the name of a source database. ${srcTableName} indicates the name of a source table.
        # 
        # 2.  Example of a column addition rule
        # 
        # *   Example: {"columns":[{"columnName":"my_add_column","columnValueType":"Constant","columnValue":"123"}]}
        # *   If no rule of this type is configured, no fields are added to the destination and no values are assigned by default.
        # *   columnName: the name of the field that is added.
        # *   columnValueType: the value type of the field. Valid values: Constant and Variable.
        # *   columnValue: the value of the field. If the columnValueType parameter is set to Constant, the value of the columnValue parameter is a constant of the STRING data type. If the columnValueType parameter is set to Variable, the value of the columnValue parameter is a built-in variable. The following built-in variables are supported: EXECUTE_TIME (LONG data type), DB_NAME_SRC (STRING data type), DATASOURCE_NAME_SRC (STRING data type), TABLE_NAME_SRC (STRING data type), DB_NAME_DEST (STRING data type), DATASOURCE_NAME_DEST (STRING data type), TABLE_NAME_DEST (STRING data type), and DB_NAME_SRC_TRANSED (STRING data type). EXECUTE_TIME indicates the execution time. DB_NAME_SRC indicates the name of a source database. DATASOURCE_NAME_SRC indicates the name of the source. TABLE_NAME_SRC indicates the name of a source table. DB_NAME_DEST indicates the name of a destination database. DATASOURCE_NAME_DEST indicates the name of the destination. TABLE_NAME_DEST indicates the name of a destination table. DB_NAME_SRC_TRANSED indicates the database name obtained after a transformation.
        # 
        # 3.  Example of a rule used to specify primary key fields for a destination table
        # 
        # *   Example: {"columns":["ukcolumn1","ukcolumn2"]}
        # *   If no rule of this type is configured, the primary key fields in the mapped source table are used for the destination table by default.
        # *   If the destination table is an existing table, Data Integration does not modify the schema of the destination table. If the specified primary key fields do not exist in the destination table, an error is reported when the synchronization task starts to run.
        # *   If the destination table is automatically created by the system, Data Integration automatically creates the schema of the destination table. The schema contains the primary key fields that you specify. If the specified primary key fields do not exist in the destination table, an error is reported when the synchronization task starts to run.
        # 
        # 4.  Example of a rule used to process DML messages
        # 
        # *   Example: {"dmlPolicies":[{"dmlType":"Delete","dmlAction":"Filter","filterCondition":"id > 1"}]}
        # *   If no rule of this type is configured, the default processing policy for messages generated for insert, update, and delete operations is Normal.
        # *   dmlType: the DML operation. Valid values: Insert, Update, and Delete.
        # *   dmlAction: the processing policy for DML messages. Valid values: Normal, Ignore, Filter, and LogicalDelete. Filter indicates conditional processing. The value Filter is returned for the dmlAction parameter only when the value of the dmlType parameter is Update or Delete.
        # *   filterCondition: the condition used to filter DML messages. This parameter is returned only when the value of the dmlAction parameter is Filter.
        # 
        # 5.  Example of a rule used to perform incremental synchronization
        # 
        # *   Example: {"where":"id > 0"}
        # *   The rule used to perform incremental synchronization is returned.
        # 
        # 6.  Example of a rule used to configure scheduling parameters for an auto triggered task
        # 
        # *   Example: {"cronExpress":" \\* \\* \\* \\* \\* \\*", "cycleType":"1"}
        # *   The rule used to configure scheduling parameters for an auto triggered task is returned.
        # 
        # 7.  Example of a rule used to specify a partition key
        # 
        # *   Example: {"columns":["id"]}
        # *   The rule used to specify a partition key is returned.
        self.rule_expression = rule_expression
        # The name of the rule. If the values of the RuleActionType parameter and the RuleTargetType parameter are the same for multiple transformation rules, you must make sure that the transformation rule names are unique.
        self.rule_name = rule_name
        # The type of the object on which the action is performed. Valid values:
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

class GetDIJobResponseBodyPagingInfoTableMappings(DaraModel):
    def __init__(
        self,
        source_object_selection_rules: List[main_models.GetDIJobResponseBodyPagingInfoTableMappingsSourceObjectSelectionRules] = None,
        transformation_rules: List[main_models.GetDIJobResponseBodyPagingInfoTableMappingsTransformationRules] = None,
    ):
        # The list of rules used to select synchronization objects in the source.
        self.source_object_selection_rules = source_object_selection_rules
        # The list of transformation rules that are applied to the synchronization objects selected from the source. Each entry in the list defines a transformation rule.
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
        # 
        # *   DefinePrimaryKey
        # *   Rename
        # *   AddColumn
        # *   HandleDml
        self.rule_action_type = rule_action_type
        # The name of the rule. If the values of the RuleActionType parameter and the RuleTargetType parameter are the same for multiple transformation rules, you must make sure that the transformation rule names are unique.
        self.rule_name = rule_name
        # The type of the object on which the action is performed. Valid values:
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

class GetDIJobResponseBodyPagingInfoTableMappingsSourceObjectSelectionRules(DaraModel):
    def __init__(
        self,
        action: str = None,
        expression: str = None,
        expression_type: str = None,
        object_type: str = None,
    ):
        # The operation that is performed to select objects. Valid values: Include and Exclude.
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
        # The encoding format of the database.
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
        # The resource used for batch synchronization.
        self.offline_resource_settings = offline_resource_settings
        # The resource used for real-time synchronization.
        self.realtime_resource_settings = realtime_resource_settings
        # The resource used for scheduling.
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
        # The number of CUs in the resource group for Data Integration that are used for scheduling.
        self.requested_cu = requested_cu
        # The identifier of the resource group for scheduling used by the synchronization task.
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
        # The number of CUs in the resource group for Data Integration that are used for real-time synchronization.
        self.requested_cu = requested_cu
        # The identifier of the resource group for Data Integration used for real-time synchronization.
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
        # The number of compute units (CUs) in the resource group for scheduling that are used for batch synchronization.
        self.requested_cu = requested_cu
        # The identifier of the resource group for Data Integration used for batch synchronization.
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
        # The channel control settings for the synchronization task. You can configure special channel control settings for the following synchronization links: data synchronization between Hologres data sources and data synchronization from Hologres to Kafka.
        # 
        # 1.  Holo2Kafka
        # 
        # *   Example: {"destinationChannelSettings":{"kafkaClientProperties":[{"key":"linger.ms","value":"100"}],"keyColumns":["col3"],"writeMode":"canal"}}
        # *   kafkaClientProperties: the parameters related to a Kafka producer, which are used when you write data to a Kafka data source.
        # *   keyColumns: the names of Kafka columns to which data is written.
        # *   writeMode: the writing format. Valid values: json and canal.
        # 
        # 2.  Holo2Holo
        # 
        # *   Example: {"destinationChannelSettings":{"conflictMode":"replace","dynamicColumnAction":"replay","writeMode":"replay"}}
        # *   conflictMode: the policy used to handle a conflict that occurs during data writing to Hologres. Valid values: replace and ignore.
        # *   writeMode: the mode in which data is written to Hologres. Valid values: replay and insert.
        # *   dynamicColumnAction: the mode in which data is written to dynamic columns in a Hologres table. Valid values: replay, insert, and ignore.
        self.channel_settings = channel_settings
        # The data type mappings between source fields and destination fields.
        self.column_data_type_settings = column_data_type_settings
        # The settings for periodic scheduling.
        self.cycle_schedule_settings = cycle_schedule_settings
        # The DDL operation types. Valid values:
        # 
        # *   RenameColumn
        # *   ModifyColumn
        # *   CreateTable
        # *   TruncateTable
        # *   DropTable
        # *   DropColumn
        # *   AddColumn
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
        # The name of the configuration item. Valid values:
        # 
        # *   src.offline.datasource.max.connection: indicates the maximum number of connections that are allowed for reading data from the source of a batch synchronization task.
        # *   dst.offline.truncate: indicates whether to clear the destination table before data writing.
        # *   runtime.offline.speed.limit.enable: indicates whether throttling is enabled for a batch synchronization task.
        # *   runtime.offline.concurrent: indicates the maximum number of parallel threads that are allowed for a batch synchronization task.
        # *   runtime.enable.auto.create.schema: indicates whether schemas are automatically created in the destination of a synchronization task.
        # *   runtime.realtime.concurrent: indicates the maximum number of parallel threads that are allowed for a real-time synchronization task.
        # *   runtime.realtime.failover.minute.dataxcdc: indicates the maximum waiting duration before a synchronization task retries the next restart if the previous restart fails after failover occurs. Unit: minutes.
        # *   runtime.realtime.failover.times.dataxcdc: indicates the maximum number of failures that are allowed for restarting a synchronization task after failovers occur.
        self.name = name
        # The value of the configuration item.
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
        # The processing policy for a specific type of DDL message. Valid values:
        # 
        # *   Ignore: ignores a DDL message.
        # *   Critical: reports an error for a DDL message.
        # *   Normal: normally processes a DDL message.
        self.action = action
        # The DDL operation type. Valid values:
        # 
        # *   RenameColumn
        # *   ModifyColumn
        # *   CreateTable
        # *   TruncateTable
        # *   DropTable
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
        # 
        # *   Full: full synchronization
        # *   OfflineIncremental: batch incremental synchronization
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
        # The data type of the destination field. Valid values: bigint, boolean, string, text, datetime, timestamp, decimal, and binary. Different types of data sources support different data types.
        self.destination_data_type = destination_data_type
        # The data type of the source field. Valid values: bigint, boolean, string, text, datetime, timestamp, decimal, and binary. Different types of data sources support different data types.
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
        # The name of the data source.
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

