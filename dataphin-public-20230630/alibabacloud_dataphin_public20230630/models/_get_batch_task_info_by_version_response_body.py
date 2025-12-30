# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetBatchTaskInfoByVersionResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_info: main_models.GetBatchTaskInfoByVersionResponseBodyTaskInfo = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success
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
            temp_model = main_models.GetBatchTaskInfoByVersionResponseBodyTaskInfo()
            self.task_info = temp_model.from_map(m.get('TaskInfo'))

        return self

class GetBatchTaskInfoByVersionResponseBodyTaskInfo(DaraModel):
    def __init__(
        self,
        code: str = None,
        cron_expression: str = None,
        custom_schedule_config: main_models.GetBatchTaskInfoByVersionResponseBodyTaskInfoCustomScheduleConfig = None,
        dag_id: str = None,
        data_source_catalog: str = None,
        data_source_id: str = None,
        data_source_schema: str = None,
        file_id: int = None,
        has_dev_node: bool = None,
        name: str = None,
        need_publish: bool = None,
        node_description: str = None,
        node_from: str = None,
        node_id: str = None,
        node_name: str = None,
        node_output_name_list: List[str] = None,
        node_status: int = None,
        operator_user_id: str = None,
        owner_name: str = None,
        owner_user_id: str = None,
        param_list: List[main_models.GetBatchTaskInfoByVersionResponseBodyTaskInfoParamList] = None,
        paused: bool = None,
        priority: int = None,
        project_id: int = None,
        published: bool = None,
        remark: str = None,
        rerunable: bool = None,
        schedule_period: str = None,
        schedule_type: int = None,
        spark_client_info: main_models.GetBatchTaskInfoByVersionResponseBodyTaskInfoSparkClientInfo = None,
        status: str = None,
        task_type: int = None,
        up_stream_list: List[main_models.GetBatchTaskInfoByVersionResponseBodyTaskInfoUpStreamList] = None,
    ):
        self.code = code
        self.cron_expression = cron_expression
        self.custom_schedule_config = custom_schedule_config
        self.dag_id = dag_id
        self.data_source_catalog = data_source_catalog
        self.data_source_id = data_source_id
        self.data_source_schema = data_source_schema
        self.file_id = file_id
        self.has_dev_node = has_dev_node
        self.name = name
        self.need_publish = need_publish
        self.node_description = node_description
        self.node_from = node_from
        self.node_id = node_id
        self.node_name = node_name
        self.node_output_name_list = node_output_name_list
        self.node_status = node_status
        self.operator_user_id = operator_user_id
        self.owner_name = owner_name
        self.owner_user_id = owner_user_id
        self.param_list = param_list
        self.paused = paused
        self.priority = priority
        self.project_id = project_id
        self.published = published
        self.remark = remark
        self.rerunable = rerunable
        self.schedule_period = schedule_period
        self.schedule_type = schedule_type
        self.spark_client_info = spark_client_info
        self.status = status
        self.task_type = task_type
        self.up_stream_list = up_stream_list

    def validate(self):
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
        if self.code is not None:
            result['Code'] = self.code

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

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.has_dev_node is not None:
            result['HasDevNode'] = self.has_dev_node

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

        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name

        if self.owner_user_id is not None:
            result['OwnerUserId'] = self.owner_user_id

        result['ParamList'] = []
        if self.param_list is not None:
            for k1 in self.param_list:
                result['ParamList'].append(k1.to_map() if k1 else None)

        if self.paused is not None:
            result['Paused'] = self.paused

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.published is not None:
            result['Published'] = self.published

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.rerunable is not None:
            result['Rerunable'] = self.rerunable

        if self.schedule_period is not None:
            result['SchedulePeriod'] = self.schedule_period

        if self.schedule_type is not None:
            result['ScheduleType'] = self.schedule_type

        if self.spark_client_info is not None:
            result['SparkClientInfo'] = self.spark_client_info.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        result['UpStreamList'] = []
        if self.up_stream_list is not None:
            for k1 in self.up_stream_list:
                result['UpStreamList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')

        if m.get('CustomScheduleConfig') is not None:
            temp_model = main_models.GetBatchTaskInfoByVersionResponseBodyTaskInfoCustomScheduleConfig()
            self.custom_schedule_config = temp_model.from_map(m.get('CustomScheduleConfig'))

        if m.get('DagId') is not None:
            self.dag_id = m.get('DagId')

        if m.get('DataSourceCatalog') is not None:
            self.data_source_catalog = m.get('DataSourceCatalog')

        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('DataSourceSchema') is not None:
            self.data_source_schema = m.get('DataSourceSchema')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('HasDevNode') is not None:
            self.has_dev_node = m.get('HasDevNode')

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

        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')

        if m.get('OwnerUserId') is not None:
            self.owner_user_id = m.get('OwnerUserId')

        self.param_list = []
        if m.get('ParamList') is not None:
            for k1 in m.get('ParamList'):
                temp_model = main_models.GetBatchTaskInfoByVersionResponseBodyTaskInfoParamList()
                self.param_list.append(temp_model.from_map(k1))

        if m.get('Paused') is not None:
            self.paused = m.get('Paused')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Published') is not None:
            self.published = m.get('Published')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('Rerunable') is not None:
            self.rerunable = m.get('Rerunable')

        if m.get('SchedulePeriod') is not None:
            self.schedule_period = m.get('SchedulePeriod')

        if m.get('ScheduleType') is not None:
            self.schedule_type = m.get('ScheduleType')

        if m.get('SparkClientInfo') is not None:
            temp_model = main_models.GetBatchTaskInfoByVersionResponseBodyTaskInfoSparkClientInfo()
            self.spark_client_info = temp_model.from_map(m.get('SparkClientInfo'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        self.up_stream_list = []
        if m.get('UpStreamList') is not None:
            for k1 in m.get('UpStreamList'):
                temp_model = main_models.GetBatchTaskInfoByVersionResponseBodyTaskInfoUpStreamList()
                self.up_stream_list.append(temp_model.from_map(k1))

        return self

class GetBatchTaskInfoByVersionResponseBodyTaskInfoUpStreamList(DaraModel):
    def __init__(
        self,
        depend_period: main_models.GetBatchTaskInfoByVersionResponseBodyTaskInfoUpStreamListDependPeriod = None,
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
        self.depend_period = depend_period
        self.depend_strategy = depend_strategy
        self.field_list = field_list
        self.node_type = node_type
        self.period_diff = period_diff
        self.source_node_enabled = source_node_enabled
        self.source_node_id = source_node_id
        self.source_node_name = source_node_name
        self.source_node_output_name = source_node_output_name
        self.source_node_user_name = source_node_user_name
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
            temp_model = main_models.GetBatchTaskInfoByVersionResponseBodyTaskInfoUpStreamListDependPeriod()
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

class GetBatchTaskInfoByVersionResponseBodyTaskInfoUpStreamListDependPeriod(DaraModel):
    def __init__(
        self,
        period_offset: int = None,
        period_type: str = None,
    ):
        self.period_offset = period_offset
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

class GetBatchTaskInfoByVersionResponseBodyTaskInfoSparkClientInfo(DaraModel):
    def __init__(
        self,
        spark_client_version: str = None,
    ):
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

class GetBatchTaskInfoByVersionResponseBodyTaskInfoParamList(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
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

class GetBatchTaskInfoByVersionResponseBodyTaskInfoCustomScheduleConfig(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        interval: int = None,
        interval_unit: str = None,
        schedule_period: str = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        self.interval = interval
        self.interval_unit = interval_unit
        self.schedule_period = schedule_period
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

