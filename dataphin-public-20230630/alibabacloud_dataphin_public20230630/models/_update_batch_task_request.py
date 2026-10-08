# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class UpdateBatchTaskRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        op_user_id: str = None,
        update_command: main_models.UpdateBatchTaskRequestUpdateCommand = None,
    ):
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # The ID of the operator user.
        self.op_user_id = op_user_id
        # The update request.
        # 
        # This parameter is required.
        self.update_command = update_command

    def validate(self):
        if self.update_command:
            self.update_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.op_user_id is not None:
            result['OpUserId'] = self.op_user_id

        if self.update_command is not None:
            result['UpdateCommand'] = self.update_command.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('OpUserId') is not None:
            self.op_user_id = m.get('OpUserId')

        if m.get('UpdateCommand') is not None:
            temp_model = main_models.UpdateBatchTaskRequestUpdateCommand()
            self.update_command = temp_model.from_map(m.get('UpdateCommand'))

        return self

class UpdateBatchTaskRequestUpdateCommand(DaraModel):
    def __init__(
        self,
        base_schedule_template_id: int = None,
        code: str = None,
        condition_schedule_enable: bool = None,
        condition_schedule_param_list: List[main_models.UpdateBatchTaskRequestUpdateCommandConditionScheduleParamList] = None,
        condition_schedule_template_id: int = None,
        context_param_list: List[main_models.UpdateBatchTaskRequestUpdateCommandContextParamList] = None,
        cron_expression: str = None,
        custom_schedule_config: main_models.UpdateBatchTaskRequestUpdateCommandCustomScheduleConfig = None,
        data_source_catalog: str = None,
        data_source_id: str = None,
        data_source_schema: str = None,
        dev_http_path: str = None,
        dev_resource_group_id: str = None,
        develop_owner_id_list: List[str] = None,
        engine: str = None,
        file_id: int = None,
        name: str = None,
        node_description: str = None,
        node_output_name_list: List[str] = None,
        node_status: int = None,
        ops_owner_id_list: List[str] = None,
        param_list: List[main_models.UpdateBatchTaskRequestUpdateCommandParamList] = None,
        priority: int = None,
        prod_http_path: str = None,
        project_id: int = None,
        python_module_list: List[str] = None,
        resource_group_id: str = None,
        schedule_period: str = None,
        spark_client_info: main_models.UpdateBatchTaskRequestUpdateCommandSparkClientInfo = None,
        task_tag_list: List[str] = None,
        task_type: int = None,
        up_stream_list: List[main_models.UpdateBatchTaskRequestUpdateCommandUpStreamList] = None,
        valid_end_date: str = None,
        valid_start_date: str = None,
    ):
        self.base_schedule_template_id = base_schedule_template_id
        # The code of the node.
        # 
        # This parameter is required.
        self.code = code
        self.condition_schedule_enable = condition_schedule_enable
        self.condition_schedule_param_list = condition_schedule_param_list
        self.condition_schedule_template_id = condition_schedule_template_id
        self.context_param_list = context_param_list
        # The cron expression for automatic scheduling. Refer to Linux cron expressions.
        self.cron_expression = cron_expression
        # The custom schedule interval configuration.
        self.custom_schedule_config = custom_schedule_config
        # The catalog for database SQL nodes. This parameter applies only to datasource types that require a catalog, such as Presto.
        self.data_source_catalog = data_source_catalog
        # The datasource ID for database SQL nodes.
        self.data_source_id = data_source_id
        # The schema for database SQL nodes. This parameter applies only to datasource types that require a schema, such as Oracle.
        self.data_source_schema = data_source_schema
        self.dev_http_path = dev_http_path
        self.dev_resource_group_id = dev_resource_group_id
        # The list of development owner IDs.
        self.develop_owner_id_list = develop_owner_id_list
        # The execution engine for the node, such as for Python nodes. Valid values:
        # - PYTHON2_7
        # - PYTHON3_7
        # - PYTHON3_11
        self.engine = engine
        # The node ID in the folder tree.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The name of the offline node.
        # 
        # This parameter is required.
        self.name = name
        # The description of the node.
        self.node_description = node_description
        # The list of node output names.
        self.node_output_name_list = node_output_name_list
        # The node status. Valid values:
        # - 1: Normal.
        # - 2: Paused.
        # - 3: Dry run.
        self.node_status = node_status
        self.ops_owner_id_list = ops_owner_id_list
        # The list of custom parameters.
        self.param_list = param_list
        # The scheduling priority of the node. Valid values: 1 to 9. A larger value indicates a lower priority.
        self.priority = priority
        self.prod_http_path = prod_http_path
        # The ID of the project to which the node belongs.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The third-party Python packages required by the node.
        self.python_module_list = python_module_list
        self.resource_group_id = resource_group_id
        # The schedule period. Valid values:
        # - YEARLY
        # - MONTHLY
        # - WEEKLY
        # - DAILY
        # - HOURLY
        # - MINUTELY
        self.schedule_period = schedule_period
        # The Spark client information.
        self.spark_client_info = spark_client_info
        self.task_tag_list = task_tag_list
        # The node type. Valid values:
        # - 1: Hive_SQL.
        # - 5: MaxCompute_SQL.
        # - 10: Shell.
        # - 21: Python.
        # 
        # This parameter is required.
        self.task_type = task_type
        # The upstream dependencies.
        self.up_stream_list = up_stream_list
        self.valid_end_date = valid_end_date
        self.valid_start_date = valid_start_date

    def validate(self):
        if self.condition_schedule_param_list:
            for v1 in self.condition_schedule_param_list:
                 if v1:
                    v1.validate()
        if self.context_param_list:
            for v1 in self.context_param_list:
                 if v1:
                    v1.validate()
        if self.custom_schedule_config:
            self.custom_schedule_config.validate()
        if self.param_list:
            for v1 in self.param_list:
                 if v1:
                    v1.validate()
        if self.spark_client_info:
            self.spark_client_info.validate()
        if self.up_stream_list:
            for v1 in self.up_stream_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.base_schedule_template_id is not None:
            result['BaseScheduleTemplateId'] = self.base_schedule_template_id

        if self.code is not None:
            result['Code'] = self.code

        if self.condition_schedule_enable is not None:
            result['ConditionScheduleEnable'] = self.condition_schedule_enable

        result['ConditionScheduleParamList'] = []
        if self.condition_schedule_param_list is not None:
            for k1 in self.condition_schedule_param_list:
                result['ConditionScheduleParamList'].append(k1.to_map() if k1 else None)

        if self.condition_schedule_template_id is not None:
            result['ConditionScheduleTemplateId'] = self.condition_schedule_template_id

        result['ContextParamList'] = []
        if self.context_param_list is not None:
            for k1 in self.context_param_list:
                result['ContextParamList'].append(k1.to_map() if k1 else None)

        if self.cron_expression is not None:
            result['CronExpression'] = self.cron_expression

        if self.custom_schedule_config is not None:
            result['CustomScheduleConfig'] = self.custom_schedule_config.to_map()

        if self.data_source_catalog is not None:
            result['DataSourceCatalog'] = self.data_source_catalog

        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id

        if self.data_source_schema is not None:
            result['DataSourceSchema'] = self.data_source_schema

        if self.dev_http_path is not None:
            result['DevHttpPath'] = self.dev_http_path

        if self.dev_resource_group_id is not None:
            result['DevResourceGroupId'] = self.dev_resource_group_id

        if self.develop_owner_id_list is not None:
            result['DevelopOwnerIdList'] = self.develop_owner_id_list

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.name is not None:
            result['Name'] = self.name

        if self.node_description is not None:
            result['NodeDescription'] = self.node_description

        if self.node_output_name_list is not None:
            result['NodeOutputNameList'] = self.node_output_name_list

        if self.node_status is not None:
            result['NodeStatus'] = self.node_status

        if self.ops_owner_id_list is not None:
            result['OpsOwnerIdList'] = self.ops_owner_id_list

        result['ParamList'] = []
        if self.param_list is not None:
            for k1 in self.param_list:
                result['ParamList'].append(k1.to_map() if k1 else None)

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.prod_http_path is not None:
            result['ProdHttpPath'] = self.prod_http_path

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.python_module_list is not None:
            result['PythonModuleList'] = self.python_module_list

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.schedule_period is not None:
            result['SchedulePeriod'] = self.schedule_period

        if self.spark_client_info is not None:
            result['SparkClientInfo'] = self.spark_client_info.to_map()

        if self.task_tag_list is not None:
            result['TaskTagList'] = self.task_tag_list

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        result['UpStreamList'] = []
        if self.up_stream_list is not None:
            for k1 in self.up_stream_list:
                result['UpStreamList'].append(k1.to_map() if k1 else None)

        if self.valid_end_date is not None:
            result['ValidEndDate'] = self.valid_end_date

        if self.valid_start_date is not None:
            result['ValidStartDate'] = self.valid_start_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseScheduleTemplateId') is not None:
            self.base_schedule_template_id = m.get('BaseScheduleTemplateId')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('ConditionScheduleEnable') is not None:
            self.condition_schedule_enable = m.get('ConditionScheduleEnable')

        self.condition_schedule_param_list = []
        if m.get('ConditionScheduleParamList') is not None:
            for k1 in m.get('ConditionScheduleParamList'):
                temp_model = main_models.UpdateBatchTaskRequestUpdateCommandConditionScheduleParamList()
                self.condition_schedule_param_list.append(temp_model.from_map(k1))

        if m.get('ConditionScheduleTemplateId') is not None:
            self.condition_schedule_template_id = m.get('ConditionScheduleTemplateId')

        self.context_param_list = []
        if m.get('ContextParamList') is not None:
            for k1 in m.get('ContextParamList'):
                temp_model = main_models.UpdateBatchTaskRequestUpdateCommandContextParamList()
                self.context_param_list.append(temp_model.from_map(k1))

        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')

        if m.get('CustomScheduleConfig') is not None:
            temp_model = main_models.UpdateBatchTaskRequestUpdateCommandCustomScheduleConfig()
            self.custom_schedule_config = temp_model.from_map(m.get('CustomScheduleConfig'))

        if m.get('DataSourceCatalog') is not None:
            self.data_source_catalog = m.get('DataSourceCatalog')

        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('DataSourceSchema') is not None:
            self.data_source_schema = m.get('DataSourceSchema')

        if m.get('DevHttpPath') is not None:
            self.dev_http_path = m.get('DevHttpPath')

        if m.get('DevResourceGroupId') is not None:
            self.dev_resource_group_id = m.get('DevResourceGroupId')

        if m.get('DevelopOwnerIdList') is not None:
            self.develop_owner_id_list = m.get('DevelopOwnerIdList')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NodeDescription') is not None:
            self.node_description = m.get('NodeDescription')

        if m.get('NodeOutputNameList') is not None:
            self.node_output_name_list = m.get('NodeOutputNameList')

        if m.get('NodeStatus') is not None:
            self.node_status = m.get('NodeStatus')

        if m.get('OpsOwnerIdList') is not None:
            self.ops_owner_id_list = m.get('OpsOwnerIdList')

        self.param_list = []
        if m.get('ParamList') is not None:
            for k1 in m.get('ParamList'):
                temp_model = main_models.UpdateBatchTaskRequestUpdateCommandParamList()
                self.param_list.append(temp_model.from_map(k1))

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('ProdHttpPath') is not None:
            self.prod_http_path = m.get('ProdHttpPath')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('PythonModuleList') is not None:
            self.python_module_list = m.get('PythonModuleList')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SchedulePeriod') is not None:
            self.schedule_period = m.get('SchedulePeriod')

        if m.get('SparkClientInfo') is not None:
            temp_model = main_models.UpdateBatchTaskRequestUpdateCommandSparkClientInfo()
            self.spark_client_info = temp_model.from_map(m.get('SparkClientInfo'))

        if m.get('TaskTagList') is not None:
            self.task_tag_list = m.get('TaskTagList')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        self.up_stream_list = []
        if m.get('UpStreamList') is not None:
            for k1 in m.get('UpStreamList'):
                temp_model = main_models.UpdateBatchTaskRequestUpdateCommandUpStreamList()
                self.up_stream_list.append(temp_model.from_map(k1))

        if m.get('ValidEndDate') is not None:
            self.valid_end_date = m.get('ValidEndDate')

        if m.get('ValidStartDate') is not None:
            self.valid_start_date = m.get('ValidStartDate')

        return self

class UpdateBatchTaskRequestUpdateCommandUpStreamList(DaraModel):
    def __init__(
        self,
        depend_period: main_models.UpdateBatchTaskRequestUpdateCommandUpStreamListDependPeriod = None,
        depend_strategy: str = None,
        field_list: List[str] = None,
        node_type: str = None,
        period_diff: int = None,
        source_node_enabled: bool = None,
        source_node_id: str = None,
        source_node_output_name: str = None,
        source_table_name: str = None,
    ):
        # The dependency period.
        self.depend_period = depend_period
        # The dependency strategy. Valid values:
        # - ALL: all.
        # - FIRST: first.
        # - LAST: last.
        # - NEAR: nearest.
        self.depend_strategy = depend_strategy
        # The fields of the dependent logical table.
        self.field_list = field_list
        # The type of the upstream dependency node. Valid values:
        # - PHYSICAL: physical node.
        # - LOGICAL: logical table dependency.
        self.node_type = node_type
        # The period difference. A value of 0 indicates same-period dependency. A positive number indicates dependency on the previous N periods.
        # 
        # This parameter is required.
        self.period_diff = period_diff
        # Indicates whether the upstream node is enabled.
        self.source_node_enabled = source_node_enabled
        # The ID of the upstream node.
        self.source_node_id = source_node_id
        # The output name of the upstream node.
        # 
        # This parameter is required.
        self.source_node_output_name = source_node_output_name
        # The name of the input table.
        self.source_table_name = source_table_name

    def validate(self):
        if self.depend_period:
            self.depend_period.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.depend_period is not None:
            result['DependPeriod'] = self.depend_period.to_map()

        if self.depend_strategy is not None:
            result['DependStrategy'] = self.depend_strategy

        if self.field_list is not None:
            result['FieldList'] = self.field_list

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.period_diff is not None:
            result['PeriodDiff'] = self.period_diff

        if self.source_node_enabled is not None:
            result['SourceNodeEnabled'] = self.source_node_enabled

        if self.source_node_id is not None:
            result['SourceNodeId'] = self.source_node_id

        if self.source_node_output_name is not None:
            result['SourceNodeOutputName'] = self.source_node_output_name

        if self.source_table_name is not None:
            result['SourceTableName'] = self.source_table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DependPeriod') is not None:
            temp_model = main_models.UpdateBatchTaskRequestUpdateCommandUpStreamListDependPeriod()
            self.depend_period = temp_model.from_map(m.get('DependPeriod'))

        if m.get('DependStrategy') is not None:
            self.depend_strategy = m.get('DependStrategy')

        if m.get('FieldList') is not None:
            self.field_list = m.get('FieldList')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('PeriodDiff') is not None:
            self.period_diff = m.get('PeriodDiff')

        if m.get('SourceNodeEnabled') is not None:
            self.source_node_enabled = m.get('SourceNodeEnabled')

        if m.get('SourceNodeId') is not None:
            self.source_node_id = m.get('SourceNodeId')

        if m.get('SourceNodeOutputName') is not None:
            self.source_node_output_name = m.get('SourceNodeOutputName')

        if m.get('SourceTableName') is not None:
            self.source_table_name = m.get('SourceTableName')

        return self

class UpdateBatchTaskRequestUpdateCommandUpStreamListDependPeriod(DaraModel):
    def __init__(
        self,
        period_offset: int = None,
        period_type: str = None,
    ):
        # The period offset. This parameter is required when dependencyPeriodType is set to LAST_N_PERIOD.
        self.period_offset = period_offset
        # The type of the dependency period. Valid values:
        # - CURRENT_PERIOD: current period.
        # - LAST_PERIOD: previous period.
        # - LAST_N_PERIOD: last N days.
        # - LAST_24_HOUR: last 24 hours.
        # 
        # This parameter is required.
        self.period_type = period_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.period_offset is not None:
            result['PeriodOffset'] = self.period_offset

        if self.period_type is not None:
            result['PeriodType'] = self.period_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PeriodOffset') is not None:
            self.period_offset = m.get('PeriodOffset')

        if m.get('PeriodType') is not None:
            self.period_type = m.get('PeriodType')

        return self

class UpdateBatchTaskRequestUpdateCommandSparkClientInfo(DaraModel):
    def __init__(
        self,
        spark_client_version: str = None,
    ):
        # The version name of the Spark client.
        # 
        # This parameter is required.
        self.spark_client_version = spark_client_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.spark_client_version is not None:
            result['SparkClientVersion'] = self.spark_client_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SparkClientVersion') is not None:
            self.spark_client_version = m.get('SparkClientVersion')

        return self

class UpdateBatchTaskRequestUpdateCommandParamList(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The parameter name.
        # 
        # This parameter is required.
        self.key = key
        # The parameter value.
        # 
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class UpdateBatchTaskRequestUpdateCommandCustomScheduleConfig(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        interval: int = None,
        interval_unit: str = None,
        schedule_period: str = None,
        start_time: str = None,
    ):
        # The end time in the format of HH:mm.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The custom interval.
        # 
        # This parameter is required.
        self.interval = interval
        # The interval unit. Valid values:
        # - MINUTE: minute.
        # - HOUR: hour.
        # 
        # This parameter is required.
        self.interval_unit = interval_unit
        # The schedule period. Valid values:
        # - YEARLY
        # - MONTHLY
        # - WEEKLY
        # - DAILY
        # - HOURLY
        # - MINUTELY
        # 
        # This parameter is required.
        self.schedule_period = schedule_period
        # The start time in the format of HH:mm.
        # 
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.interval_unit is not None:
            result['IntervalUnit'] = self.interval_unit

        if self.schedule_period is not None:
            result['SchedulePeriod'] = self.schedule_period

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('IntervalUnit') is not None:
            self.interval_unit = m.get('IntervalUnit')

        if m.get('SchedulePeriod') is not None:
            self.schedule_period = m.get('SchedulePeriod')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class UpdateBatchTaskRequestUpdateCommandContextParamList(DaraModel):
    def __init__(
        self,
        default_value: str = None,
        desc: str = None,
        param_key: str = None,
    ):
        self.default_value = default_value
        self.desc = desc
        self.param_key = param_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value

        if self.desc is not None:
            result['Desc'] = self.desc

        if self.param_key is not None:
            result['ParamKey'] = self.param_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')

        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        if m.get('ParamKey') is not None:
            self.param_key = m.get('ParamKey')

        return self

class UpdateBatchTaskRequestUpdateCommandConditionScheduleParamList(DaraModel):
    def __init__(
        self,
        condition_name: str = None,
        cron_expression: str = None,
        enable: bool = None,
        follow_schedule_param: bool = None,
        node_status: int = None,
        schedule_condition_json: str = None,
        schedule_time: str = None,
    ):
        self.condition_name = condition_name
        self.cron_expression = cron_expression
        self.enable = enable
        self.follow_schedule_param = follow_schedule_param
        self.node_status = node_status
        self.schedule_condition_json = schedule_condition_json
        self.schedule_time = schedule_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.condition_name is not None:
            result['ConditionName'] = self.condition_name

        if self.cron_expression is not None:
            result['CronExpression'] = self.cron_expression

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.follow_schedule_param is not None:
            result['FollowScheduleParam'] = self.follow_schedule_param

        if self.node_status is not None:
            result['NodeStatus'] = self.node_status

        if self.schedule_condition_json is not None:
            result['ScheduleConditionJson'] = self.schedule_condition_json

        if self.schedule_time is not None:
            result['ScheduleTime'] = self.schedule_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConditionName') is not None:
            self.condition_name = m.get('ConditionName')

        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('FollowScheduleParam') is not None:
            self.follow_schedule_param = m.get('FollowScheduleParam')

        if m.get('NodeStatus') is not None:
            self.node_status = m.get('NodeStatus')

        if m.get('ScheduleConditionJson') is not None:
            self.schedule_condition_json = m.get('ScheduleConditionJson')

        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')

        return self

