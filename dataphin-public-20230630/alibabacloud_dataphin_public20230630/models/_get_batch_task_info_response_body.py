# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetBatchTaskInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_info: main_models.GetBatchTaskInfoResponseBodyTaskInfo = None,
    ):
        # The error code. A value of OK indicates that the request is successful.
        self.code = code
        # The HTTP status code returned by the backend.
        self.http_status_code = http_status_code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success
        # The task details.
        self.task_info = task_info

    def validate(self):
        if self.task_info:
            self.task_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.task_info is not None:
            result['TaskInfo'] = self.task_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TaskInfo') is not None:
            temp_model = main_models.GetBatchTaskInfoResponseBodyTaskInfo()
            self.task_info = temp_model.from_map(m.get('TaskInfo'))

        return self

class GetBatchTaskInfoResponseBodyTaskInfo(DaraModel):
    def __init__(
        self,
        base_schedule_template_id: int = None,
        base_schedule_template_name: str = None,
        code: str = None,
        code_template_id: str = None,
        code_template_version: int = None,
        condition_schedule_enable: bool = None,
        condition_schedule_param_list: List[main_models.GetBatchTaskInfoResponseBodyTaskInfoConditionScheduleParamList] = None,
        condition_schedule_template_id: int = None,
        condition_schedule_template_name: str = None,
        context_param_list: List[main_models.GetBatchTaskInfoResponseBodyTaskInfoContextParamList] = None,
        cpu_resource: str = None,
        cron_expression: str = None,
        custom_schedule_config: main_models.GetBatchTaskInfoResponseBodyTaskInfoCustomScheduleConfig = None,
        dag_id: str = None,
        data_source_catalog: str = None,
        data_source_id: str = None,
        data_source_schema: str = None,
        databricks_python_connect_info: main_models.GetBatchTaskInfoResponseBodyTaskInfoDatabricksPythonConnectInfo = None,
        dev_http_path: str = None,
        dev_resource_group_id: str = None,
        dev_resource_group_name: str = None,
        develop_owner_id: str = None,
        develop_owner_id_list: List[str] = None,
        develop_owner_name: str = None,
        develop_owner_name_list: List[str] = None,
        execute_rerun_config: main_models.GetBatchTaskInfoResponseBodyTaskInfoExecuteRerunConfig = None,
        execute_time_out_config: main_models.GetBatchTaskInfoResponseBodyTaskInfoExecuteTimeOutConfig = None,
        file_id: int = None,
        has_dev_node: bool = None,
        memory_resource: str = None,
        name: str = None,
        need_publish: bool = None,
        node_description: str = None,
        node_from: str = None,
        node_id: str = None,
        node_name: str = None,
        node_output_name_list: List[str] = None,
        node_status: int = None,
        operator_user_id: str = None,
        ops_owner_id: str = None,
        ops_owner_id_list: List[str] = None,
        ops_owner_name: str = None,
        ops_owner_name_list: List[str] = None,
        owner_name: str = None,
        owner_user_id: str = None,
        pai_config: main_models.GetBatchTaskInfoResponseBodyTaskInfoPaiConfig = None,
        param_list: List[main_models.GetBatchTaskInfoResponseBodyTaskInfoParamList] = None,
        paused: bool = None,
        priority: int = None,
        prod_http_path: str = None,
        project_id: int = None,
        published: bool = None,
        python_module_list: List[main_models.GetBatchTaskInfoResponseBodyTaskInfoPythonModuleList] = None,
        python_version: str = None,
        remark: str = None,
        rerunable: bool = None,
        resource_group_id: str = None,
        resource_group_name: str = None,
        retry_on_timeout_enable: bool = None,
        schedule_period: str = None,
        schedule_type: int = None,
        spark_client_info: main_models.GetBatchTaskInfoResponseBodyTaskInfoSparkClientInfo = None,
        spark_dynamic_resource_switch: bool = None,
        spark_resource_effect_scope: str = None,
        spark_sql_resource_config_map: str = None,
        spark_version: str = None,
        status: str = None,
        task_tag_list: List[str] = None,
        task_type: int = None,
        up_stream_list: List[main_models.GetBatchTaskInfoResponseBodyTaskInfoUpStreamList] = None,
        valid_end_date: str = None,
        valid_start_date: str = None,
    ):
        # The ID of the base schedule template. This parameter is returned when the configuration method is set to schedule template.
        self.base_schedule_template_id = base_schedule_template_id
        # The name of the base schedule template.
        self.base_schedule_template_name = base_schedule_template_name
        # The code of the node.
        self.code = code
        # The ID of the offline code template.
        self.code_template_id = code_template_id
        # The version of the offline code template.
        self.code_template_version = code_template_version
        # Specifies whether conditional scheduling is enabled.
        self.condition_schedule_enable = condition_schedule_enable
        # The details of the conditional scheduling configuration. This parameter has a value only when conditional scheduling is enabled.
        self.condition_schedule_param_list = condition_schedule_param_list
        # The ID of the conditional schedule template.
        self.condition_schedule_template_id = condition_schedule_template_id
        # The name of the conditional schedule template.
        self.condition_schedule_template_name = condition_schedule_template_name
        # The cross-node parameters. These are the output parameters declared by the current node for downstream nodes to reference in the format of ${#n_NodeID:ParameterName}.
        self.context_param_list = context_param_list
        # The current configuration of the node. When queried by version, this parameter returns the configuration of the corresponding version.
        self.cpu_resource = cpu_resource
        # The cron expression for automatic scheduling. You can refer to Linux cron expressions.
        self.cron_expression = cron_expression
        # The custom schedule interval configuration.
        self.custom_schedule_config = custom_schedule_config
        # The ID of the DAG to which the node belongs.
        self.dag_id = dag_id
        # The data source catalog for database SQL tasks. This parameter takes effect only for data source types that require a catalog, such as Presto.
        self.data_source_catalog = data_source_catalog
        # The data source ID for database SQL tasks.
        self.data_source_id = data_source_id
        # The data source schema for database SQL tasks. This parameter takes effect only for data source types that require a schema, such as Oracle.
        self.data_source_schema = data_source_schema
        # The Python connection information.
        self.databricks_python_connect_info = databricks_python_connect_info
        # The HTTP path for the development environment, used for Databricks tasks.
        self.dev_http_path = dev_http_path
        # The ID of the scheduling resource group for the development task.
        self.dev_resource_group_id = dev_resource_group_id
        # The name of the scheduling resource group for the development task.
        self.dev_resource_group_name = dev_resource_group_name
        # The user ID of the development owner.
        self.develop_owner_id = develop_owner_id
        # The list of user IDs of the development owners.
        self.develop_owner_id_list = develop_owner_id_list
        # The name of the development owner.
        self.develop_owner_name = develop_owner_name
        # The list of names of the development owners.
        self.develop_owner_name_list = develop_owner_name_list
        # The failure retry configuration. This is the current configuration of the task. If queried by version, this is the configuration of the corresponding version.
        self.execute_rerun_config = execute_rerun_config
        # The execution timeout configuration. This is the current configuration of the task. If queried by version, this is the configuration of the corresponding version.
        self.execute_time_out_config = execute_time_out_config
        # The ID of the node in the task directory tree.
        self.file_id = file_id
        # Indicates whether a development environment node exists.
        self.has_dev_node = has_dev_node
        # The current configuration of the node. When queried by version, this parameter returns the configuration of the corresponding version.
        self.memory_resource = memory_resource
        # The name of the task.
        self.name = name
        # Indicates whether the task needs to be published.
        self.need_publish = need_publish
        # The description of the task.
        self.node_description = node_description
        # The source of the node. This indicates the organization or application that created the node.
        self.node_from = node_from
        # The ID of the node.
        self.node_id = node_id
        # The name of the node.
        self.node_name = node_name
        # The list of node output names.
        self.node_output_name_list = node_output_name_list
        # The status of the node. Valid values: 1 (Normal), 2 (Paused), and 3 (Dry run).
        self.node_status = node_status
        # The user ID of the current operator.
        self.operator_user_id = operator_user_id
        # The user ID of the O&M owner.
        self.ops_owner_id = ops_owner_id
        # The list of user IDs of the O&M owners.
        self.ops_owner_id_list = ops_owner_id_list
        # The O&M owner name.
        self.ops_owner_name = ops_owner_name
        # The list of O&M owner names.
        self.ops_owner_name_list = ops_owner_name_list
        # The name of the node owner.
        self.owner_name = owner_name
        # The user ID of the node owner.
        self.owner_user_id = owner_user_id
        # The PAI configuration information.
        self.pai_config = pai_config
        # The list of custom parameters for the node.
        self.param_list = param_list
        # Indicates whether the scheduling of the node is paused.
        self.paused = paused
        # The scheduling priority of the task. Valid values: 1 to 9. A larger value indicates a lower priority.
        self.priority = priority
        # The HTTP path in the production environment. This parameter is used for Databricks tasks.
        self.prod_http_path = prod_http_path
        # The ID of the project.
        self.project_id = project_id
        # Indicates whether the task is published.
        self.published = published
        # The list of third-party packages that the Python task depends on.
        self.python_module_list = python_module_list
        # The Python version for the Python task, such as Python 3.7.
        self.python_version = python_version
        # The remark.
        self.remark = remark
        # Indicates whether the task can be rerun.
        self.rerunable = rerunable
        # The ID of the schedule resource group for the production task.
        self.resource_group_id = resource_group_id
        # The name of the schedule resource group for the production task.
        self.resource_group_name = resource_group_name
        # Specifies whether to retry the task upon timeout. This is the current configuration of the task. If you query by version, this is the configuration of the corresponding version.
        self.retry_on_timeout_enable = retry_on_timeout_enable
        # The scheduling period. Valid values:
        # - YEARLY: Yearly.
        # - MONTHLY: Monthly.
        # - WEEKLY: Weekly.
        # - DAILY: Daily.
        # - HOURLY: Hourly.
        # - MINUTELY: Minutely.
        self.schedule_period = schedule_period
        # The type of the node. Valid values: 
        # - 1: Periodic task.
        # - 3: Manual task.
        self.schedule_type = schedule_type
        # The Spark client information.
        self.spark_client_info = spark_client_info
        # The current configuration of the node. When queried by version, this parameter returns the configuration of the corresponding version.
        self.spark_dynamic_resource_switch = spark_dynamic_resource_switch
        # The effective scope of the Spark resource configuration. A value of ONLY_PROD indicates the production environment only, and a value of PROD_AND_DEV indicates the production and development environments. This is the current configuration of the task. If you query by version, this is the configuration of the corresponding version.
        self.spark_resource_effect_scope = spark_resource_effect_scope
        # The Spark SQL resource configuration. The key is the configuration item name, and the value is a string. The entire configuration is returned as a JSON string. This is the current configuration of the task. If you query by version, this is the configuration of the corresponding version.
        self.spark_sql_resource_config_map = spark_sql_resource_config_map
        # The MaxCompute Spark version.
        self.spark_version = spark_version
        # The publish status. Valid values: 0 (Draft), 1 (Submitted), and 100 (In development).
        self.status = status
        # The list of node tag names.
        self.task_tag_list = task_tag_list
        # The node type. For more information, see the API operation for creating an offline computing node.
        self.task_type = task_type
        # The upstream dependencies.
        self.up_stream_list = up_stream_list
        # The effective end date. Format: yyyy-MM-dd.
        self.valid_end_date = valid_end_date
        # The effective start date. Format: yyyy-MM-dd.
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
        if self.databricks_python_connect_info:
            self.databricks_python_connect_info.validate()
        if self.execute_rerun_config:
            self.execute_rerun_config.validate()
        if self.execute_time_out_config:
            self.execute_time_out_config.validate()
        if self.pai_config:
            self.pai_config.validate()
        if self.param_list:
            for v1 in self.param_list:
                 if v1:
                    v1.validate()
        if self.python_module_list:
            for v1 in self.python_module_list:
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

        if self.base_schedule_template_name is not None:
            result['BaseScheduleTemplateName'] = self.base_schedule_template_name

        if self.code is not None:
            result['Code'] = self.code

        if self.code_template_id is not None:
            result['CodeTemplateId'] = self.code_template_id

        if self.code_template_version is not None:
            result['CodeTemplateVersion'] = self.code_template_version

        if self.condition_schedule_enable is not None:
            result['ConditionScheduleEnable'] = self.condition_schedule_enable

        result['ConditionScheduleParamList'] = []
        if self.condition_schedule_param_list is not None:
            for k1 in self.condition_schedule_param_list:
                result['ConditionScheduleParamList'].append(k1.to_map() if k1 else None)

        if self.condition_schedule_template_id is not None:
            result['ConditionScheduleTemplateId'] = self.condition_schedule_template_id

        if self.condition_schedule_template_name is not None:
            result['ConditionScheduleTemplateName'] = self.condition_schedule_template_name

        result['ContextParamList'] = []
        if self.context_param_list is not None:
            for k1 in self.context_param_list:
                result['ContextParamList'].append(k1.to_map() if k1 else None)

        if self.cpu_resource is not None:
            result['CpuResource'] = self.cpu_resource

        if self.cron_expression is not None:
            result['CronExpression'] = self.cron_expression

        if self.custom_schedule_config is not None:
            result['CustomScheduleConfig'] = self.custom_schedule_config.to_map()

        if self.dag_id is not None:
            result['DagId'] = self.dag_id

        if self.data_source_catalog is not None:
            result['DataSourceCatalog'] = self.data_source_catalog

        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id

        if self.data_source_schema is not None:
            result['DataSourceSchema'] = self.data_source_schema

        if self.databricks_python_connect_info is not None:
            result['DatabricksPythonConnectInfo'] = self.databricks_python_connect_info.to_map()

        if self.dev_http_path is not None:
            result['DevHttpPath'] = self.dev_http_path

        if self.dev_resource_group_id is not None:
            result['DevResourceGroupId'] = self.dev_resource_group_id

        if self.dev_resource_group_name is not None:
            result['DevResourceGroupName'] = self.dev_resource_group_name

        if self.develop_owner_id is not None:
            result['DevelopOwnerId'] = self.develop_owner_id

        if self.develop_owner_id_list is not None:
            result['DevelopOwnerIdList'] = self.develop_owner_id_list

        if self.develop_owner_name is not None:
            result['DevelopOwnerName'] = self.develop_owner_name

        if self.develop_owner_name_list is not None:
            result['DevelopOwnerNameList'] = self.develop_owner_name_list

        if self.execute_rerun_config is not None:
            result['ExecuteRerunConfig'] = self.execute_rerun_config.to_map()

        if self.execute_time_out_config is not None:
            result['ExecuteTimeOutConfig'] = self.execute_time_out_config.to_map()

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.has_dev_node is not None:
            result['HasDevNode'] = self.has_dev_node

        if self.memory_resource is not None:
            result['MemoryResource'] = self.memory_resource

        if self.name is not None:
            result['Name'] = self.name

        if self.need_publish is not None:
            result['NeedPublish'] = self.need_publish

        if self.node_description is not None:
            result['NodeDescription'] = self.node_description

        if self.node_from is not None:
            result['NodeFrom'] = self.node_from

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.node_output_name_list is not None:
            result['NodeOutputNameList'] = self.node_output_name_list

        if self.node_status is not None:
            result['NodeStatus'] = self.node_status

        if self.operator_user_id is not None:
            result['OperatorUserId'] = self.operator_user_id

        if self.ops_owner_id is not None:
            result['OpsOwnerId'] = self.ops_owner_id

        if self.ops_owner_id_list is not None:
            result['OpsOwnerIdList'] = self.ops_owner_id_list

        if self.ops_owner_name is not None:
            result['OpsOwnerName'] = self.ops_owner_name

        if self.ops_owner_name_list is not None:
            result['OpsOwnerNameList'] = self.ops_owner_name_list

        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name

        if self.owner_user_id is not None:
            result['OwnerUserId'] = self.owner_user_id

        if self.pai_config is not None:
            result['PaiConfig'] = self.pai_config.to_map()

        result['ParamList'] = []
        if self.param_list is not None:
            for k1 in self.param_list:
                result['ParamList'].append(k1.to_map() if k1 else None)

        if self.paused is not None:
            result['Paused'] = self.paused

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.prod_http_path is not None:
            result['ProdHttpPath'] = self.prod_http_path

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.published is not None:
            result['Published'] = self.published

        result['PythonModuleList'] = []
        if self.python_module_list is not None:
            for k1 in self.python_module_list:
                result['PythonModuleList'].append(k1.to_map() if k1 else None)

        if self.python_version is not None:
            result['PythonVersion'] = self.python_version

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.rerunable is not None:
            result['Rerunable'] = self.rerunable

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name

        if self.retry_on_timeout_enable is not None:
            result['RetryOnTimeoutEnable'] = self.retry_on_timeout_enable

        if self.schedule_period is not None:
            result['SchedulePeriod'] = self.schedule_period

        if self.schedule_type is not None:
            result['ScheduleType'] = self.schedule_type

        if self.spark_client_info is not None:
            result['SparkClientInfo'] = self.spark_client_info.to_map()

        if self.spark_dynamic_resource_switch is not None:
            result['SparkDynamicResourceSwitch'] = self.spark_dynamic_resource_switch

        if self.spark_resource_effect_scope is not None:
            result['SparkResourceEffectScope'] = self.spark_resource_effect_scope

        if self.spark_sql_resource_config_map is not None:
            result['SparkSqlResourceConfigMap'] = self.spark_sql_resource_config_map

        if self.spark_version is not None:
            result['SparkVersion'] = self.spark_version

        if self.status is not None:
            result['Status'] = self.status

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

        if m.get('BaseScheduleTemplateName') is not None:
            self.base_schedule_template_name = m.get('BaseScheduleTemplateName')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CodeTemplateId') is not None:
            self.code_template_id = m.get('CodeTemplateId')

        if m.get('CodeTemplateVersion') is not None:
            self.code_template_version = m.get('CodeTemplateVersion')

        if m.get('ConditionScheduleEnable') is not None:
            self.condition_schedule_enable = m.get('ConditionScheduleEnable')

        self.condition_schedule_param_list = []
        if m.get('ConditionScheduleParamList') is not None:
            for k1 in m.get('ConditionScheduleParamList'):
                temp_model = main_models.GetBatchTaskInfoResponseBodyTaskInfoConditionScheduleParamList()
                self.condition_schedule_param_list.append(temp_model.from_map(k1))

        if m.get('ConditionScheduleTemplateId') is not None:
            self.condition_schedule_template_id = m.get('ConditionScheduleTemplateId')

        if m.get('ConditionScheduleTemplateName') is not None:
            self.condition_schedule_template_name = m.get('ConditionScheduleTemplateName')

        self.context_param_list = []
        if m.get('ContextParamList') is not None:
            for k1 in m.get('ContextParamList'):
                temp_model = main_models.GetBatchTaskInfoResponseBodyTaskInfoContextParamList()
                self.context_param_list.append(temp_model.from_map(k1))

        if m.get('CpuResource') is not None:
            self.cpu_resource = m.get('CpuResource')

        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')

        if m.get('CustomScheduleConfig') is not None:
            temp_model = main_models.GetBatchTaskInfoResponseBodyTaskInfoCustomScheduleConfig()
            self.custom_schedule_config = temp_model.from_map(m.get('CustomScheduleConfig'))

        if m.get('DagId') is not None:
            self.dag_id = m.get('DagId')

        if m.get('DataSourceCatalog') is not None:
            self.data_source_catalog = m.get('DataSourceCatalog')

        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('DataSourceSchema') is not None:
            self.data_source_schema = m.get('DataSourceSchema')

        if m.get('DatabricksPythonConnectInfo') is not None:
            temp_model = main_models.GetBatchTaskInfoResponseBodyTaskInfoDatabricksPythonConnectInfo()
            self.databricks_python_connect_info = temp_model.from_map(m.get('DatabricksPythonConnectInfo'))

        if m.get('DevHttpPath') is not None:
            self.dev_http_path = m.get('DevHttpPath')

        if m.get('DevResourceGroupId') is not None:
            self.dev_resource_group_id = m.get('DevResourceGroupId')

        if m.get('DevResourceGroupName') is not None:
            self.dev_resource_group_name = m.get('DevResourceGroupName')

        if m.get('DevelopOwnerId') is not None:
            self.develop_owner_id = m.get('DevelopOwnerId')

        if m.get('DevelopOwnerIdList') is not None:
            self.develop_owner_id_list = m.get('DevelopOwnerIdList')

        if m.get('DevelopOwnerName') is not None:
            self.develop_owner_name = m.get('DevelopOwnerName')

        if m.get('DevelopOwnerNameList') is not None:
            self.develop_owner_name_list = m.get('DevelopOwnerNameList')

        if m.get('ExecuteRerunConfig') is not None:
            temp_model = main_models.GetBatchTaskInfoResponseBodyTaskInfoExecuteRerunConfig()
            self.execute_rerun_config = temp_model.from_map(m.get('ExecuteRerunConfig'))

        if m.get('ExecuteTimeOutConfig') is not None:
            temp_model = main_models.GetBatchTaskInfoResponseBodyTaskInfoExecuteTimeOutConfig()
            self.execute_time_out_config = temp_model.from_map(m.get('ExecuteTimeOutConfig'))

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('HasDevNode') is not None:
            self.has_dev_node = m.get('HasDevNode')

        if m.get('MemoryResource') is not None:
            self.memory_resource = m.get('MemoryResource')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NeedPublish') is not None:
            self.need_publish = m.get('NeedPublish')

        if m.get('NodeDescription') is not None:
            self.node_description = m.get('NodeDescription')

        if m.get('NodeFrom') is not None:
            self.node_from = m.get('NodeFrom')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('NodeOutputNameList') is not None:
            self.node_output_name_list = m.get('NodeOutputNameList')

        if m.get('NodeStatus') is not None:
            self.node_status = m.get('NodeStatus')

        if m.get('OperatorUserId') is not None:
            self.operator_user_id = m.get('OperatorUserId')

        if m.get('OpsOwnerId') is not None:
            self.ops_owner_id = m.get('OpsOwnerId')

        if m.get('OpsOwnerIdList') is not None:
            self.ops_owner_id_list = m.get('OpsOwnerIdList')

        if m.get('OpsOwnerName') is not None:
            self.ops_owner_name = m.get('OpsOwnerName')

        if m.get('OpsOwnerNameList') is not None:
            self.ops_owner_name_list = m.get('OpsOwnerNameList')

        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')

        if m.get('OwnerUserId') is not None:
            self.owner_user_id = m.get('OwnerUserId')

        if m.get('PaiConfig') is not None:
            temp_model = main_models.GetBatchTaskInfoResponseBodyTaskInfoPaiConfig()
            self.pai_config = temp_model.from_map(m.get('PaiConfig'))

        self.param_list = []
        if m.get('ParamList') is not None:
            for k1 in m.get('ParamList'):
                temp_model = main_models.GetBatchTaskInfoResponseBodyTaskInfoParamList()
                self.param_list.append(temp_model.from_map(k1))

        if m.get('Paused') is not None:
            self.paused = m.get('Paused')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('ProdHttpPath') is not None:
            self.prod_http_path = m.get('ProdHttpPath')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Published') is not None:
            self.published = m.get('Published')

        self.python_module_list = []
        if m.get('PythonModuleList') is not None:
            for k1 in m.get('PythonModuleList'):
                temp_model = main_models.GetBatchTaskInfoResponseBodyTaskInfoPythonModuleList()
                self.python_module_list.append(temp_model.from_map(k1))

        if m.get('PythonVersion') is not None:
            self.python_version = m.get('PythonVersion')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('Rerunable') is not None:
            self.rerunable = m.get('Rerunable')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')

        if m.get('RetryOnTimeoutEnable') is not None:
            self.retry_on_timeout_enable = m.get('RetryOnTimeoutEnable')

        if m.get('SchedulePeriod') is not None:
            self.schedule_period = m.get('SchedulePeriod')

        if m.get('ScheduleType') is not None:
            self.schedule_type = m.get('ScheduleType')

        if m.get('SparkClientInfo') is not None:
            temp_model = main_models.GetBatchTaskInfoResponseBodyTaskInfoSparkClientInfo()
            self.spark_client_info = temp_model.from_map(m.get('SparkClientInfo'))

        if m.get('SparkDynamicResourceSwitch') is not None:
            self.spark_dynamic_resource_switch = m.get('SparkDynamicResourceSwitch')

        if m.get('SparkResourceEffectScope') is not None:
            self.spark_resource_effect_scope = m.get('SparkResourceEffectScope')

        if m.get('SparkSqlResourceConfigMap') is not None:
            self.spark_sql_resource_config_map = m.get('SparkSqlResourceConfigMap')

        if m.get('SparkVersion') is not None:
            self.spark_version = m.get('SparkVersion')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskTagList') is not None:
            self.task_tag_list = m.get('TaskTagList')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        self.up_stream_list = []
        if m.get('UpStreamList') is not None:
            for k1 in m.get('UpStreamList'):
                temp_model = main_models.GetBatchTaskInfoResponseBodyTaskInfoUpStreamList()
                self.up_stream_list.append(temp_model.from_map(k1))

        if m.get('ValidEndDate') is not None:
            self.valid_end_date = m.get('ValidEndDate')

        if m.get('ValidStartDate') is not None:
            self.valid_start_date = m.get('ValidStartDate')

        return self

class GetBatchTaskInfoResponseBodyTaskInfoUpStreamList(DaraModel):
    def __init__(
        self,
        depend_period: main_models.GetBatchTaskInfoResponseBodyTaskInfoUpStreamListDependPeriod = None,
        depend_strategy: str = None,
        field_list: List[str] = None,
        node_type: str = None,
        period_diff: int = None,
        source_node_enabled: bool = None,
        source_node_id: str = None,
        source_node_name: str = None,
        source_node_output_name: str = None,
        source_node_user_name: str = None,
        source_table_name: str = None,
    ):
        # The dependency period.
        self.depend_period = depend_period
        # The dependency strategy. Valid values: ALL, FIRST, LAST, and NEAR.
        self.depend_strategy = depend_strategy
        # The dependent logical table fields.
        self.field_list = field_list
        # The upstream dependency node type. Valid values:
        # - PHYSICAL: physical node.
        # - LOGICAL: logical table dependency.
        self.node_type = node_type
        # The period difference. A value of 0 indicates a same-period dependency. A positive number indicates a dependency on the previous N periods.
        self.period_diff = period_diff
        # Indicates whether the upstream node is enabled.
        self.source_node_enabled = source_node_enabled
        # The ID of the upstream node.
        self.source_node_id = source_node_id
        # The name of the upstream node.
        self.source_node_name = source_node_name
        # The output name of the upstream node.
        self.source_node_output_name = source_node_output_name
        # The upstream username.
        self.source_node_user_name = source_node_user_name
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

        if self.source_node_name is not None:
            result['SourceNodeName'] = self.source_node_name

        if self.source_node_output_name is not None:
            result['SourceNodeOutputName'] = self.source_node_output_name

        if self.source_node_user_name is not None:
            result['SourceNodeUserName'] = self.source_node_user_name

        if self.source_table_name is not None:
            result['SourceTableName'] = self.source_table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DependPeriod') is not None:
            temp_model = main_models.GetBatchTaskInfoResponseBodyTaskInfoUpStreamListDependPeriod()
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

        if m.get('SourceNodeName') is not None:
            self.source_node_name = m.get('SourceNodeName')

        if m.get('SourceNodeOutputName') is not None:
            self.source_node_output_name = m.get('SourceNodeOutputName')

        if m.get('SourceNodeUserName') is not None:
            self.source_node_user_name = m.get('SourceNodeUserName')

        if m.get('SourceTableName') is not None:
            self.source_table_name = m.get('SourceTableName')

        return self

class GetBatchTaskInfoResponseBodyTaskInfoUpStreamListDependPeriod(DaraModel):
    def __init__(
        self,
        period_offset: int = None,
        period_type: str = None,
    ):
        # The period offset. This parameter is required when the period type is LAST_N_PERIOD.
        self.period_offset = period_offset
        # The dependency period type. Valid values: 
        # - CURRENT_PERIOD
        # - LAST_PERIOD
        # - LAST_N_PERIOD
        # - LAST_24_HOUR
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

class GetBatchTaskInfoResponseBodyTaskInfoSparkClientInfo(DaraModel):
    def __init__(
        self,
        spark_client_version: str = None,
    ):
        # The version name of the Spark client.
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

class GetBatchTaskInfoResponseBodyTaskInfoPythonModuleList(DaraModel):
    def __init__(
        self,
        module_id: int = None,
        name: str = None,
        python_version: str = None,
        version: str = None,
    ):
        # The ID of the third-party package.
        self.module_id = module_id
        # The name of the third-party package.
        self.name = name
        # The Python version that the third-party package depends on.
        self.python_version = python_version
        # The version number of the third-party package.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.module_id is not None:
            result['ModuleId'] = self.module_id

        if self.name is not None:
            result['Name'] = self.name

        if self.python_version is not None:
            result['PythonVersion'] = self.python_version

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PythonVersion') is not None:
            self.python_version = m.get('PythonVersion')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class GetBatchTaskInfoResponseBodyTaskInfoParamList(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The name of the parameter.
        self.key = key
        # The value of the parameter.
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

class GetBatchTaskInfoResponseBodyTaskInfoPaiConfig(DaraModel):
    def __init__(
        self,
        experiment_id: str = None,
        region: str = None,
        work_space_id: str = None,
    ):
        # The ID of the PAI experiment.
        self.experiment_id = experiment_id
        # The PAI region.
        self.region = region
        # The ID of the PAI workspace.
        self.work_space_id = work_space_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id

        if self.region is not None:
            result['Region'] = self.region

        if self.work_space_id is not None:
            result['WorkSpaceId'] = self.work_space_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('WorkSpaceId') is not None:
            self.work_space_id = m.get('WorkSpaceId')

        return self

class GetBatchTaskInfoResponseBodyTaskInfoExecuteTimeOutConfig(DaraModel):
    def __init__(
        self,
        custom_values: str = None,
        follow_system: bool = None,
    ):
        # The custom timeout period.
        self.custom_values = custom_values
        # Specifies whether to inherit the system configuration.
        self.follow_system = follow_system

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_values is not None:
            result['CustomValues'] = self.custom_values

        if self.follow_system is not None:
            result['FollowSystem'] = self.follow_system

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomValues') is not None:
            self.custom_values = m.get('CustomValues')

        if m.get('FollowSystem') is not None:
            self.follow_system = m.get('FollowSystem')

        return self

class GetBatchTaskInfoResponseBodyTaskInfoExecuteRerunConfig(DaraModel):
    def __init__(
        self,
        custom_rerun_interval: str = None,
        custom_rerun_times: str = None,
        follow_system: bool = None,
    ):
        # The custom failure retry interval.
        self.custom_rerun_interval = custom_rerun_interval
        # The custom number of failure retries.
        self.custom_rerun_times = custom_rerun_times
        # Specifies whether to inherit the system configuration.
        self.follow_system = follow_system

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_rerun_interval is not None:
            result['CustomRerunInterval'] = self.custom_rerun_interval

        if self.custom_rerun_times is not None:
            result['CustomRerunTimes'] = self.custom_rerun_times

        if self.follow_system is not None:
            result['FollowSystem'] = self.follow_system

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomRerunInterval') is not None:
            self.custom_rerun_interval = m.get('CustomRerunInterval')

        if m.get('CustomRerunTimes') is not None:
            self.custom_rerun_times = m.get('CustomRerunTimes')

        if m.get('FollowSystem') is not None:
            self.follow_system = m.get('FollowSystem')

        return self

class GetBatchTaskInfoResponseBodyTaskInfoDatabricksPythonConnectInfo(DaraModel):
    def __init__(
        self,
        dev_http_path: str = None,
        enable_databricks_python_connect: bool = None,
        prod_http_path: str = None,
    ):
        # The HTTP path for the development environment.
        self.dev_http_path = dev_http_path
        # Specifies whether Databricks Python Connect is enabled.
        self.enable_databricks_python_connect = enable_databricks_python_connect
        # The HTTP path for the production environment.
        self.prod_http_path = prod_http_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dev_http_path is not None:
            result['DevHttpPath'] = self.dev_http_path

        if self.enable_databricks_python_connect is not None:
            result['EnableDatabricksPythonConnect'] = self.enable_databricks_python_connect

        if self.prod_http_path is not None:
            result['ProdHttpPath'] = self.prod_http_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DevHttpPath') is not None:
            self.dev_http_path = m.get('DevHttpPath')

        if m.get('EnableDatabricksPythonConnect') is not None:
            self.enable_databricks_python_connect = m.get('EnableDatabricksPythonConnect')

        if m.get('ProdHttpPath') is not None:
            self.prod_http_path = m.get('ProdHttpPath')

        return self

class GetBatchTaskInfoResponseBodyTaskInfoCustomScheduleConfig(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        interval: int = None,
        interval_unit: str = None,
        schedule_period: str = None,
        start_time: str = None,
    ):
        # The end time in the HH:mm format.
        self.end_time = end_time
        # The custom interval.
        self.interval = interval
        # The unit of the interval. Valid values: MINUTE and HOUR.
        self.interval_unit = interval_unit
        # The scheduling cycle.
        self.schedule_period = schedule_period
        # The start time in the HH:mm format.
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

class GetBatchTaskInfoResponseBodyTaskInfoContextParamList(DaraModel):
    def __init__(
        self,
        default_value: str = None,
        desc: str = None,
        param_key: str = None,
    ):
        # The default value.
        # 
        # This parameter is required.
        self.default_value = default_value
        # The parameter description.
        # 
        # This parameter is required.
        self.desc = desc
        # The name of the parameter.
        # 
        # This parameter is required.
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

class GetBatchTaskInfoResponseBodyTaskInfoConditionScheduleParamList(DaraModel):
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
        # The name of the condition.
        # 
        # This parameter is required.
        self.condition_name = condition_name
        # The cron expression used after the condition is met.
        # 
        # This parameter is required.
        self.cron_expression = cron_expression
        # Specifies whether the condition is enabled.
        # 
        # This parameter is required.
        self.enable = enable
        # Specifies whether to follow the main scheduling parameter.
        # 
        # This parameter is required.
        self.follow_schedule_param = follow_schedule_param
        # The scheduling status of the node after the condition is met. Valid values:
        # - 1: Normal.
        # - 2: Paused.
        # - 3: Dry run.
        # 
        # This parameter is required.
        self.node_status = node_status
        # The conditional expression tree in JSON string format. The key names are lower camel case characters and must be parsed by the invoker.
        # 
        # This parameter is required.
        self.schedule_condition_json = schedule_condition_json
        # The scheduling time used after the condition is met.
        # 
        # This parameter is required.
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

