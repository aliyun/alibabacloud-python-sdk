# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class SubmitBatchTaskRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        submit_command: main_models.SubmitBatchTaskRequestSubmitCommand = None,
    ):
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # The submit request.
        # 
        # This parameter is required.
        self.submit_command = submit_command

    def validate(self):
        if self.submit_command:
            self.submit_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.submit_command is not None:
            result['SubmitCommand'] = self.submit_command.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('SubmitCommand') is not None:
            temp_model = main_models.SubmitBatchTaskRequestSubmitCommand()
            self.submit_command = temp_model.from_map(m.get('SubmitCommand'))

        return self

class SubmitBatchTaskRequestSubmitCommand(DaraModel):
    def __init__(
        self,
        code: str = None,
        code_template_version: int = None,
        comment: str = None,
        cron_expression: str = None,
        custom_schedule_config: main_models.SubmitBatchTaskRequestSubmitCommandCustomScheduleConfig = None,
        engine: str = None,
        file_id: int = None,
        name: str = None,
        node_description: str = None,
        node_output_name_list: List[str] = None,
        node_status: int = None,
        offline_code_template_id: str = None,
        offline_code_template_params: List[main_models.SubmitBatchTaskRequestSubmitCommandOfflineCodeTemplateParams] = None,
        param_list: List[main_models.SubmitBatchTaskRequestSubmitCommandParamList] = None,
        priority: int = None,
        project_id: int = None,
        python_module_list: List[str] = None,
        schedule_period: str = None,
        spark_client_info: main_models.SubmitBatchTaskRequestSubmitCommandSparkClientInfo = None,
        up_stream_list: List[main_models.SubmitBatchTaskRequestSubmitCommandUpStreamList] = None,
    ):
        # The code of the node.
        # 
        # This parameter is required.
        self.code = code
        self.code_template_version = code_template_version
        # The comment for the submit operation.
        # 
        # This parameter is required.
        self.comment = comment
        # The cron expression for automatic scheduling. Refer to the Linux cron expression syntax.
        self.cron_expression = cron_expression
        # The custom schedule interval configuration.
        self.custom_schedule_config = custom_schedule_config
        # The execution engine for the node, such as for Python tasks. Valid values:
        # - PYTHON2_7
        # - PYTHON3_7
        # - PYTHON3_11
        self.engine = engine
        # The node ID in the directory tree.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The name of the batch task.
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
        self.offline_code_template_id = offline_code_template_id
        self.offline_code_template_params = offline_code_template_params
        # The list of custom parameters.
        self.param_list = param_list
        # The scheduling priority of the node. Valid values: 1 to 9. A larger value indicates a lower priority.
        self.priority = priority
        # The ID of the project to which the node belongs.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The Python third-party packages that the node depends on.
        self.python_module_list = python_module_list
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
        # The upstream dependencies.
        self.up_stream_list = up_stream_list

    def validate(self):
        if self.custom_schedule_config:
            self.custom_schedule_config.validate()
        if self.offline_code_template_params:
            for v1 in self.offline_code_template_params:
                 if v1:
                    v1.validate()
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
        if self.code is not None:
            result['Code'] = self.code

        if self.code_template_version is not None:
            result['CodeTemplateVersion'] = self.code_template_version

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.cron_expression is not None:
            result['CronExpression'] = self.cron_expression

        if self.custom_schedule_config is not None:
            result['CustomScheduleConfig'] = self.custom_schedule_config.to_map()

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

        if self.offline_code_template_id is not None:
            result['OfflineCodeTemplateId'] = self.offline_code_template_id

        result['OfflineCodeTemplateParams'] = []
        if self.offline_code_template_params is not None:
            for k1 in self.offline_code_template_params:
                result['OfflineCodeTemplateParams'].append(k1.to_map() if k1 else None)

        result['ParamList'] = []
        if self.param_list is not None:
            for k1 in self.param_list:
                result['ParamList'].append(k1.to_map() if k1 else None)

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.python_module_list is not None:
            result['PythonModuleList'] = self.python_module_list

        if self.schedule_period is not None:
            result['SchedulePeriod'] = self.schedule_period

        if self.spark_client_info is not None:
            result['SparkClientInfo'] = self.spark_client_info.to_map()

        result['UpStreamList'] = []
        if self.up_stream_list is not None:
            for k1 in self.up_stream_list:
                result['UpStreamList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CodeTemplateVersion') is not None:
            self.code_template_version = m.get('CodeTemplateVersion')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')

        if m.get('CustomScheduleConfig') is not None:
            temp_model = main_models.SubmitBatchTaskRequestSubmitCommandCustomScheduleConfig()
            self.custom_schedule_config = temp_model.from_map(m.get('CustomScheduleConfig'))

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

        if m.get('OfflineCodeTemplateId') is not None:
            self.offline_code_template_id = m.get('OfflineCodeTemplateId')

        self.offline_code_template_params = []
        if m.get('OfflineCodeTemplateParams') is not None:
            for k1 in m.get('OfflineCodeTemplateParams'):
                temp_model = main_models.SubmitBatchTaskRequestSubmitCommandOfflineCodeTemplateParams()
                self.offline_code_template_params.append(temp_model.from_map(k1))

        self.param_list = []
        if m.get('ParamList') is not None:
            for k1 in m.get('ParamList'):
                temp_model = main_models.SubmitBatchTaskRequestSubmitCommandParamList()
                self.param_list.append(temp_model.from_map(k1))

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('PythonModuleList') is not None:
            self.python_module_list = m.get('PythonModuleList')

        if m.get('SchedulePeriod') is not None:
            self.schedule_period = m.get('SchedulePeriod')

        if m.get('SparkClientInfo') is not None:
            temp_model = main_models.SubmitBatchTaskRequestSubmitCommandSparkClientInfo()
            self.spark_client_info = temp_model.from_map(m.get('SparkClientInfo'))

        self.up_stream_list = []
        if m.get('UpStreamList') is not None:
            for k1 in m.get('UpStreamList'):
                temp_model = main_models.SubmitBatchTaskRequestSubmitCommandUpStreamList()
                self.up_stream_list.append(temp_model.from_map(k1))

        return self

class SubmitBatchTaskRequestSubmitCommandUpStreamList(DaraModel):
    def __init__(
        self,
        depend_period: main_models.SubmitBatchTaskRequestSubmitCommandUpStreamListDependPeriod = None,
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
        # - ALL: all
        # - FIRST: first
        # - LAST: last
        # - NEAR: nearest
        self.depend_strategy = depend_strategy
        # The dependent logical table fields.
        self.field_list = field_list
        # The type of the upstream dependency node. Valid values:
        # - PHYSICAL: physical node
        # - LOGICAL: logical table dependency
        self.node_type = node_type
        # The period difference. A value of 0 indicates a same-period dependency. A positive number indicates a dependency on the previous N periods.
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
            temp_model = main_models.SubmitBatchTaskRequestSubmitCommandUpStreamListDependPeriod()
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

class SubmitBatchTaskRequestSubmitCommandUpStreamListDependPeriod(DaraModel):
    def __init__(
        self,
        period_offset: int = None,
        period_type: str = None,
    ):
        # The period offset. This parameter is required when dependencyPeriodType is set to LAST_N_PERIOD.
        self.period_offset = period_offset
        # The dependency period type. Valid values:
        # - CURRENT_PERIOD: current period
        # - LAST_PERIOD: previous period
        # - LAST_N_PERIOD: last N days
        # - LAST_24_HOUR: last 24 hours
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

class SubmitBatchTaskRequestSubmitCommandSparkClientInfo(DaraModel):
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

class SubmitBatchTaskRequestSubmitCommandParamList(DaraModel):
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

class SubmitBatchTaskRequestSubmitCommandOfflineCodeTemplateParams(DaraModel):
    def __init__(
        self,
        description: str = None,
        encrypt_enabled: bool = None,
        key: str = None,
        value: str = None,
    ):
        self.description = description
        self.encrypt_enabled = encrypt_enabled
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.encrypt_enabled is not None:
            result['EncryptEnabled'] = self.encrypt_enabled

        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EncryptEnabled') is not None:
            self.encrypt_enabled = m.get('EncryptEnabled')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class SubmitBatchTaskRequestSubmitCommandCustomScheduleConfig(DaraModel):
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
        # - MINUTE: minute
        # - HOUR: hour
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

