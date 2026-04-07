# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class GetDIJobResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetDIJobResponseBodyData = None,
        request_id: str = None,
    ):
        # The information about the synchronization task.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetDIJobResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetDIJobResponseBodyData(DaraModel):
    def __init__(
        self,
        created_time: int = None,
        created_uid: str = None,
        dijob_id: int = None,
        description: str = None,
        destination_data_source_settings: List[main_models.GetDIJobResponseBodyDataDestinationDataSourceSettings] = None,
        destination_data_source_type: str = None,
        error_message: str = None,
        job_name: str = None,
        job_settings: main_models.GetDIJobResponseBodyDataJobSettings = None,
        job_status: str = None,
        migration_type: str = None,
        project_id: int = None,
        resource_settings: main_models.GetDIJobResponseBodyDataResourceSettings = None,
        run_stats: Dict[str, str] = None,
        source_data_source_settings: List[main_models.GetDIJobResponseBodyDataSourceDataSourceSettings] = None,
        source_data_source_type: str = None,
        started_time: int = None,
        started_uid: str = None,
        table_mappings: List[main_models.GetDIJobResponseBodyDataTableMappings] = None,
        transformation_rules: List[main_models.GetDIJobResponseBodyDataTransformationRules] = None,
        updated_time: int = None,
        updated_uid: str = None,
    ):
        # The timestamp when the synchronization task was created. The timestamp is accurate to the second.
        self.created_time = created_time
        # The ID of the user who creates the synchronization task.
        self.created_uid = created_uid
        # The ID of the synchronization task.
        self.dijob_id = dijob_id
        # The description of the synchronization task.
        self.description = description
        # The settings of the destination. Only a single destination is supported.
        self.destination_data_source_settings = destination_data_source_settings
        # The destination type. Valid values: Hologres and Hive.
        self.destination_data_source_type = destination_data_source_type
        # The error message returned if the value of the JobStatus parameter is Failed.
        self.error_message = error_message
        # The name of the synchronization task.
        self.job_name = job_name
        # The settings for the dimension of the synchronization task. The settings include processing policies for DDL messages, policies for data type mappings between source fields and destination fields, and runtime parameters of the synchronization task.
        self.job_settings = job_settings
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
        # The workspace ID.
        self.project_id = project_id
        # The resource settings.
        self.resource_settings = resource_settings
        # The information about the running of the synchronization task.
        self.run_stats = run_stats
        # The settings of the source. Only a single source is supported.
        self.source_data_source_settings = source_data_source_settings
        # The source type. The value MySQL is returned.
        self.source_data_source_type = source_data_source_type
        # The timestamp when the synchronization task was last started. The timestamp is accurate to the second.
        self.started_time = started_time
        # The ID of the user who last starts the synchronization task.
        self.started_uid = started_uid
        # The list of mappings between rules used to select synchronization objects in the source and transformation rules applied to the selected synchronization objects. Each entry in the list displays a mapping between a rule used to select synchronization objects and a transformation rule applied to the selected synchronization objects.
        self.table_mappings = table_mappings
        # The list of transformation rules that are applied to the synchronization objects selected from the source. Each entry in the list defines a transformation rule.
        self.transformation_rules = transformation_rules
        # The timestamp when the synchronization task was last modified. The timestamp is accurate to the second.
        self.updated_time = updated_time
        # The ID of the user who last modifies the synchronization task.
        self.updated_uid = updated_uid

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
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.created_uid is not None:
            result['CreatedUid'] = self.created_uid

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

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.job_name is not None:
            result['JobName'] = self.job_name

        if self.job_settings is not None:
            result['JobSettings'] = self.job_settings.to_map()

        if self.job_status is not None:
            result['JobStatus'] = self.job_status

        if self.migration_type is not None:
            result['MigrationType'] = self.migration_type

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.resource_settings is not None:
            result['ResourceSettings'] = self.resource_settings.to_map()

        if self.run_stats is not None:
            result['RunStats'] = self.run_stats

        result['SourceDataSourceSettings'] = []
        if self.source_data_source_settings is not None:
            for k1 in self.source_data_source_settings:
                result['SourceDataSourceSettings'].append(k1.to_map() if k1 else None)

        if self.source_data_source_type is not None:
            result['SourceDataSourceType'] = self.source_data_source_type

        if self.started_time is not None:
            result['StartedTime'] = self.started_time

        if self.started_uid is not None:
            result['StartedUid'] = self.started_uid

        result['TableMappings'] = []
        if self.table_mappings is not None:
            for k1 in self.table_mappings:
                result['TableMappings'].append(k1.to_map() if k1 else None)

        result['TransformationRules'] = []
        if self.transformation_rules is not None:
            for k1 in self.transformation_rules:
                result['TransformationRules'].append(k1.to_map() if k1 else None)

        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time

        if self.updated_uid is not None:
            result['UpdatedUid'] = self.updated_uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('CreatedUid') is not None:
            self.created_uid = m.get('CreatedUid')

        if m.get('DIJobId') is not None:
            self.dijob_id = m.get('DIJobId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.destination_data_source_settings = []
        if m.get('DestinationDataSourceSettings') is not None:
            for k1 in m.get('DestinationDataSourceSettings'):
                temp_model = main_models.GetDIJobResponseBodyDataDestinationDataSourceSettings()
                self.destination_data_source_settings.append(temp_model.from_map(k1))

        if m.get('DestinationDataSourceType') is not None:
            self.destination_data_source_type = m.get('DestinationDataSourceType')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        if m.get('JobSettings') is not None:
            temp_model = main_models.GetDIJobResponseBodyDataJobSettings()
            self.job_settings = temp_model.from_map(m.get('JobSettings'))

        if m.get('JobStatus') is not None:
            self.job_status = m.get('JobStatus')

        if m.get('MigrationType') is not None:
            self.migration_type = m.get('MigrationType')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ResourceSettings') is not None:
            temp_model = main_models.GetDIJobResponseBodyDataResourceSettings()
            self.resource_settings = temp_model.from_map(m.get('ResourceSettings'))

        if m.get('RunStats') is not None:
            self.run_stats = m.get('RunStats')

        self.source_data_source_settings = []
        if m.get('SourceDataSourceSettings') is not None:
            for k1 in m.get('SourceDataSourceSettings'):
                temp_model = main_models.GetDIJobResponseBodyDataSourceDataSourceSettings()
                self.source_data_source_settings.append(temp_model.from_map(k1))

        if m.get('SourceDataSourceType') is not None:
            self.source_data_source_type = m.get('SourceDataSourceType')

        if m.get('StartedTime') is not None:
            self.started_time = m.get('StartedTime')

        if m.get('StartedUid') is not None:
            self.started_uid = m.get('StartedUid')

        self.table_mappings = []
        if m.get('TableMappings') is not None:
            for k1 in m.get('TableMappings'):
                temp_model = main_models.GetDIJobResponseBodyDataTableMappings()
                self.table_mappings.append(temp_model.from_map(k1))

        self.transformation_rules = []
        if m.get('TransformationRules') is not None:
            for k1 in m.get('TransformationRules'):
                temp_model = main_models.GetDIJobResponseBodyDataTransformationRules()
                self.transformation_rules.append(temp_model.from_map(k1))

        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')

        if m.get('UpdatedUid') is not None:
            self.updated_uid = m.get('UpdatedUid')

        return self

class GetDIJobResponseBodyDataTransformationRules(DaraModel):
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
        # *   DefineRuntimeSettings
        # *   DefinePartitionKey
        self.rule_action_type = rule_action_type
        # The expression of the rule. The expression is a JSON string.
        # 
        # *   Example of a renaming rule: `{"expression":"${srcDatasourceName}_${srcDatabaseName}_0922","variables":[{"variableName":"srcDatabaseName","variableRules":[{"from":"fromdb","to":"todb"}\\]}\\]}`.
        # 
        #     *   expression: the expression of the renaming rule. The expression may contain the following variables:
        # 
        #         *   ${srcDatasourceName}
        #         *   ${srcDatabaseName}
        #         *   ${srcTableName}
        # 
        #     *   variables: the generation rule for a variable used in the expression of the renaming rule. The default value of the specified variable is the original value of the object indicated by the variable. A group of string replacement rules used to change the original values may be returned.
        # 
        #         *   variableName: the name of the variable. The variable name is not enclosed in ${}.
        #         *   variableRules: the string replacement rules for variables. The system runs the string replacement rules in sequence. from indicates the original string. to indicates the new string.
        # 
        # *   Example of a rule used to add a specific field to the destination and assign a value to the field: `{"columns":[{"columnName":"my_add_column","columnValueType":"Constant","columnValue":"123"}\\]}`.
        # 
        #     If no rule of this type is configured, no fields are added to the destination and no values are assigned by default.
        # 
        #     *   columnName: the name of the field that is added.
        # 
        #     *   columnValueType: the value type of the field. Valid values: Constant and Variable.
        # 
        #     *   columnValue: the value of the field.
        # 
        #         *   If the value of the columnValueType parameter is Constant, the value of the columnValue parameter is a constant of the STRING data type.
        #         *   If the value of the columnValueType parameter is Variable, the value of the columnValue parameter is a built-in variable. The following built-in variables are supported: EXECUTE_TIME (LONG data type), DB_NAME_SRC (STRING data type), DATASOURCE_NAME_SRC (STRING data type), TABLE_NAME_SRC (STRING data type), DB_NAME_DEST (STRING data type), DATASOURCE_NAME_DEST (STRING data type), TABLE_NAME_DEST (STRING data type), and DB_NAME_SRC_TRANSED (STRING data type). EXECUTE_TIME indicates the execution time. DB_NAME_SRC indicates the name of a source database. DATASOURCE_NAME_SRC indicates the name of the source. TABLE_NAME_SRC indicates the name of a source table. DB_NAME_DEST indicates the name of a destination database. DATASOURCE_NAME_DEST indicates the name of the destination. TABLE_NAME_DEST indicates the name of a destination table. DB_NAME_SRC_TRANSED indicates the database name obtained after a transformation.
        # 
        # *   Example of a rule used to specify primary key fields for a destination table: `{"columns":["ukcolumn1","ukcolumn2"\\]}`.
        # 
        #     If no rule of this type is configured, the primary key fields in the mapped source table are used for the destination table by default.
        # 
        #     *   If the destination table is an existing table, Data Integration does not modify the schema of the destination table. If the specified primary key fields do not exist in the destination table, an error is reported when the synchronization task starts to run.
        #     *   If the destination table is automatically created by the system, Data Integration automatically creates the schema of the destination table. The schema contains the primary key fields that you specify. If the specified primary key fields do not exist in the destination table, an error is reported when the synchronization task starts to run.
        # 
        # *   Example of a rule used to process DML messages: `{"dmlPolicies":[{"dmlType":"Delete","dmlAction":"Filter","filterCondition":"id > 1"}\\]}`.
        # 
        #     If no rule of this type is configured, the default processing policy for messages generated for insert, update, and delete operations is Normal.
        # 
        #     *   dmlType: the DML operation. Valid values: Insert, Update, and Delete.
        #     *   dmlAction: the processing policy for DML messages. Valid values: Normal, Ignore, Filter, and LogicalDelete. Filter indicates conditional processing. The value Filter is returned for the dmlAction parameter only when the value of the dmlType parameter is Update or Delete.
        #     *   filterCondition: the condition used to filter DML messages. This parameter is returned only when the value of the dmlAction parameter is Filter.
        self.rule_expression = rule_expression
        # The name of the rule. If the values of the RuleActionType parameter and the RuleTargetType parameter are the same for multiple transformation rules, you must make sure that the transformation rule names are unique.
        self.rule_name = rule_name
        # The type of the object on which the action is performed. Valid values:
        # 
        # *   Table
        # *   Schema
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

class GetDIJobResponseBodyDataTableMappings(DaraModel):
    def __init__(
        self,
        source_object_selection_rules: List[main_models.GetDIJobResponseBodyDataTableMappingsSourceObjectSelectionRules] = None,
        transformation_rules: List[main_models.GetDIJobResponseBodyDataTableMappingsTransformationRules] = None,
    ):
        # The list of rules used to select synchronization objects in the source.
        self.source_object_selection_rules = source_object_selection_rules
        # The list of transformation rules that are applied to the synchronization objects selected from the source.
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
                temp_model = main_models.GetDIJobResponseBodyDataTableMappingsSourceObjectSelectionRules()
                self.source_object_selection_rules.append(temp_model.from_map(k1))

        self.transformation_rules = []
        if m.get('TransformationRules') is not None:
            for k1 in m.get('TransformationRules'):
                temp_model = main_models.GetDIJobResponseBodyDataTableMappingsTransformationRules()
                self.transformation_rules.append(temp_model.from_map(k1))

        return self

class GetDIJobResponseBodyDataTableMappingsTransformationRules(DaraModel):
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
        # *   DefineRuntimeSettings
        # *   DefinePartitionKey
        self.rule_action_type = rule_action_type
        # The name of the rule. If the values of the RuleActionType parameter and the RuleTargetType parameter are the same for multiple transformation rules, you must make sure that the transformation rule names are unique.
        self.rule_name = rule_name
        # The type of the object on which the action is performed. Valid values:
        # 
        # *   Table
        # *   Schema
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

class GetDIJobResponseBodyDataTableMappingsSourceObjectSelectionRules(DaraModel):
    def __init__(
        self,
        expression: str = None,
        object_type: str = None,
    ):
        # The expression.
        self.expression = expression
        # The object type. Valid values:
        # 
        # *   Table
        # *   Database
        self.object_type = object_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expression is not None:
            result['Expression'] = self.expression

        if self.object_type is not None:
            result['ObjectType'] = self.object_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')

        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')

        return self

class GetDIJobResponseBodyDataSourceDataSourceSettings(DaraModel):
    def __init__(
        self,
        data_source_name: str = None,
        data_source_properties: Dict[str, str] = None,
    ):
        # The name of the data source.
        self.data_source_name = data_source_name
        # The properties of the data source.
        self.data_source_properties = data_source_properties

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_source_name is not None:
            result['DataSourceName'] = self.data_source_name

        if self.data_source_properties is not None:
            result['DataSourceProperties'] = self.data_source_properties

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceName') is not None:
            self.data_source_name = m.get('DataSourceName')

        if m.get('DataSourceProperties') is not None:
            self.data_source_properties = m.get('DataSourceProperties')

        return self

class GetDIJobResponseBodyDataResourceSettings(DaraModel):
    def __init__(
        self,
        offline_resource_settings: main_models.GetDIJobResponseBodyDataResourceSettingsOfflineResourceSettings = None,
        realtime_resource_settings: main_models.GetDIJobResponseBodyDataResourceSettingsRealtimeResourceSettings = None,
        requested_cu: float = None,
    ):
        # The resource used for batch synchronization.
        self.offline_resource_settings = offline_resource_settings
        # The resource used for real-time synchronization.
        self.realtime_resource_settings = realtime_resource_settings
        # The number of compute units (CUs) in the resource group that are used for incremental and full synchronization.
        self.requested_cu = requested_cu

    def validate(self):
        if self.offline_resource_settings:
            self.offline_resource_settings.validate()
        if self.realtime_resource_settings:
            self.realtime_resource_settings.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.offline_resource_settings is not None:
            result['OfflineResourceSettings'] = self.offline_resource_settings.to_map()

        if self.realtime_resource_settings is not None:
            result['RealtimeResourceSettings'] = self.realtime_resource_settings.to_map()

        if self.requested_cu is not None:
            result['RequestedCu'] = self.requested_cu

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OfflineResourceSettings') is not None:
            temp_model = main_models.GetDIJobResponseBodyDataResourceSettingsOfflineResourceSettings()
            self.offline_resource_settings = temp_model.from_map(m.get('OfflineResourceSettings'))

        if m.get('RealtimeResourceSettings') is not None:
            temp_model = main_models.GetDIJobResponseBodyDataResourceSettingsRealtimeResourceSettings()
            self.realtime_resource_settings = temp_model.from_map(m.get('RealtimeResourceSettings'))

        if m.get('RequestedCu') is not None:
            self.requested_cu = m.get('RequestedCu')

        return self

class GetDIJobResponseBodyDataResourceSettingsRealtimeResourceSettings(DaraModel):
    def __init__(
        self,
        resource_group_identifier: str = None,
    ):
        # The identifier of the resource group for Data Integration used for real-time synchronization.
        self.resource_group_identifier = resource_group_identifier

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_group_identifier is not None:
            result['ResourceGroupIdentifier'] = self.resource_group_identifier

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupIdentifier') is not None:
            self.resource_group_identifier = m.get('ResourceGroupIdentifier')

        return self

class GetDIJobResponseBodyDataResourceSettingsOfflineResourceSettings(DaraModel):
    def __init__(
        self,
        resource_group_identifier: str = None,
    ):
        # The identifier of the resource group for Data Integration used for batch synchronization.
        self.resource_group_identifier = resource_group_identifier

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_group_identifier is not None:
            result['ResourceGroupIdentifier'] = self.resource_group_identifier

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupIdentifier') is not None:
            self.resource_group_identifier = m.get('ResourceGroupIdentifier')

        return self

class GetDIJobResponseBodyDataJobSettings(DaraModel):
    def __init__(
        self,
        channel_settings: str = None,
        column_data_type_settings: List[main_models.GetDIJobResponseBodyDataJobSettingsColumnDataTypeSettings] = None,
        cycle_schedule_settings: main_models.GetDIJobResponseBodyDataJobSettingsCycleScheduleSettings = None,
        ddl_handling_settings: List[main_models.GetDIJobResponseBodyDataJobSettingsDdlHandlingSettings] = None,
        runtime_settings: List[main_models.GetDIJobResponseBodyDataJobSettingsRuntimeSettings] = None,
    ):
        # The channel control settings for the synchronization task. The value of this parameter is a JSON string.
        self.channel_settings = channel_settings
        # The settings for data type mappings between source fields and destination fields. The value of this parameter is an array.
        self.column_data_type_settings = column_data_type_settings
        # The settings for periodic scheduling.
        self.cycle_schedule_settings = cycle_schedule_settings
        # The settings for processing DDL messages. The value of this parameter is an array.
        self.ddl_handling_settings = ddl_handling_settings
        # The runtime settings. The value of this parameter is an array.
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
                temp_model = main_models.GetDIJobResponseBodyDataJobSettingsColumnDataTypeSettings()
                self.column_data_type_settings.append(temp_model.from_map(k1))

        if m.get('CycleScheduleSettings') is not None:
            temp_model = main_models.GetDIJobResponseBodyDataJobSettingsCycleScheduleSettings()
            self.cycle_schedule_settings = temp_model.from_map(m.get('CycleScheduleSettings'))

        self.ddl_handling_settings = []
        if m.get('DdlHandlingSettings') is not None:
            for k1 in m.get('DdlHandlingSettings'):
                temp_model = main_models.GetDIJobResponseBodyDataJobSettingsDdlHandlingSettings()
                self.ddl_handling_settings.append(temp_model.from_map(k1))

        self.runtime_settings = []
        if m.get('RuntimeSettings') is not None:
            for k1 in m.get('RuntimeSettings'):
                temp_model = main_models.GetDIJobResponseBodyDataJobSettingsRuntimeSettings()
                self.runtime_settings.append(temp_model.from_map(k1))

        return self

class GetDIJobResponseBodyDataJobSettingsRuntimeSettings(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name of the configuration item. Valid values:
        # 
        # *   runtime.offline.speed.limit.mb: indicates the maximum transmission rate that is allowed for a batch synchronization task. This configuration item takes effect only when runtime.offline.speed.limit.enable is set to true.
        # *   runtime.offline.speed.limit.enable: indicates whether throttling is enabled for a batch synchronization task.
        # *   dst.offline.connection.max: indicates the maximum number of connections that are allowed for writing data to the destination of a batch synchronization task.
        # *   runtime.offline.concurrent: indicates the maximum number of parallel threads that are allowed for a batch synchronization task.
        # *   dst.realtime.connection.max: indicates the maximum number of connections that are allowed for writing data to the destination of a real-time synchronization task.
        # *   runtime.enable.auto.create.schema: indicates whether schemas are automatically created in the destination of a synchronization task.
        # *   src.offline.datasource.max.connection: indicates the maximum number of connections that are allowed for reading data from the source of a batch synchronization task.
        # *   runtime.realtime.concurrent: indicates the maximum number of parallel threads that are allowed for a real-time synchronization task.
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

class GetDIJobResponseBodyDataJobSettingsDdlHandlingSettings(DaraModel):
    def __init__(
        self,
        action: str = None,
        type: str = None,
    ):
        # The processing policy. Valid values:
        # 
        # *   Ignore: ignores a DDL message.
        # *   Critical: reports an error for a DDL message.
        # *   Normal: normally processes a DDL message.
        self.action = action
        # The type of the DDL operation. Valid values:
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

class GetDIJobResponseBodyDataJobSettingsCycleScheduleSettings(DaraModel):
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

class GetDIJobResponseBodyDataJobSettingsColumnDataTypeSettings(DaraModel):
    def __init__(
        self,
        destination_data_type: str = None,
        source_data_type: str = None,
    ):
        # The data type of a destination field.
        self.destination_data_type = destination_data_type
        # The data type of a source field.
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

class GetDIJobResponseBodyDataDestinationDataSourceSettings(DaraModel):
    def __init__(
        self,
        data_source_name: str = None,
        data_source_properties: Dict[str, str] = None,
    ):
        # The name of the data source.
        self.data_source_name = data_source_name
        # The properties of the data source.
        self.data_source_properties = data_source_properties

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_source_name is not None:
            result['DataSourceName'] = self.data_source_name

        if self.data_source_properties is not None:
            result['DataSourceProperties'] = self.data_source_properties

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceName') is not None:
            self.data_source_name = m.get('DataSourceName')

        if m.get('DataSourceProperties') is not None:
            self.data_source_properties = m.get('DataSourceProperties')

        return self

