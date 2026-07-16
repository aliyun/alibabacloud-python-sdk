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
        # The error code. A value of OK indicates that the request was successful.
        self.code = code
        # The HTTP status code returned by the backend.
        self.http_status_code = http_status_code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success
        # The node details.
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
        # The node code.
        self.code = code
        # The cron expression for automatic scheduling. For more information, refer to the Linux cron expression syntax.
        self.cron_expression = cron_expression
        # The custom scheduling interval configuration.
        self.custom_schedule_config = custom_schedule_config
        # The ID of the DAG to which the node belongs.
        self.dag_id = dag_id
        # The catalog for database SQL nodes. This parameter takes effect only for data source types that require a catalog, such as Presto.
        self.data_source_catalog = data_source_catalog
        # The data source ID for database SQL nodes.
        self.data_source_id = data_source_id
        # The schema for database SQL nodes. This parameter takes effect only for data source types that require a schema, such as Oracle.
        self.data_source_schema = data_source_schema
        # The node ID in the node directory tree.
        self.file_id = file_id
        # Indicates whether the node has a development environment node.
        self.has_dev_node = has_dev_node
        # The node name.
        self.name = name
        # Indicates whether the node needs to be published.
        self.need_publish = need_publish
        # The node description.
        self.node_description = node_description
        # The source of the node, indicating the organization or application that created the node.
        self.node_from = node_from
        # The node ID.
        self.node_id = node_id
        # The node name.
        self.node_name = node_name
        # The list of node output names.
        self.node_output_name_list = node_output_name_list
        # The node status. Valid values:
        # - 1: Normal.
        # - 2: Paused.
        # - 3: Dry run.
        self.node_status = node_status
        # The user ID of the current operator.
        self.operator_user_id = operator_user_id
        # The name of the node owner.
        self.owner_name = owner_name
        # The user ID of the node owner.
        self.owner_user_id = owner_user_id
        # The list of custom node parameters.
        self.param_list = param_list
        # Indicates whether the node scheduling is paused.
        self.paused = paused
        # The scheduling priority of the node. Valid values: 1 to 9. A larger value indicates a lower priority.
        self.priority = priority
        # The project ID.
        self.project_id = project_id
        # Indicates whether the node has been published.
        self.published = published
        # The remarks.
        self.remark = remark
        # Indicates whether the node can be rerun.
        self.rerunable = rerunable
        # The scheduling period. Valid values:
        # - YEARLY
        # - MONTHLY
        # - WEEKLY
        # - DAILY
        # - HOURLY
        # - MINUTELY.
        self.schedule_period = schedule_period
        # The scheduling type. Valid values:
        # - 1: periodic node.
        # - 3: manual node.
        self.schedule_type = schedule_type
        # The Spark client information.
        self.spark_client_info = spark_client_info
        # The publish status. Valid values:
        # - 0: draft.
        # - 1: submitted.
        # - 100: in development.
        self.status = status
        # The node type. For more information, see the API operation for creating a batch task.
        self.task_type = task_type
        # The upstream dependencies.
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
        # The dependency period.
        self.depend_period = depend_period
        # The dependency strategy. Valid values: ALL, FIRST, LAST, NEAR.
        self.depend_strategy = depend_strategy
        # The fields of the dependent logical table.
        self.field_list = field_list
        # The type of the upstream dependency node. Valid values:
        # - PHYSICAL: physical node.
        # - LOGICAL: logical table dependency.
        self.node_type = node_type
        # The period difference. A value of 0 indicates a same-period dependency. A positive number indicates a dependency on the previous N periods.
        self.period_diff = period_diff
        # Indicates whether the upstream node is enabled.
        self.source_node_enabled = source_node_enabled
        # The upstream node ID.
        self.source_node_id = source_node_id
        # The upstream node name.
        self.source_node_name = source_node_name
        # The output name of the upstream node.
        self.source_node_output_name = source_node_output_name
        # The username of the upstream node owner.
        self.source_node_user_name = source_node_user_name
        # The input table name.
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
        # The period offset. This parameter is required when PeriodType is set to LAST_N_PERIOD.
        self.period_offset = period_offset
        # The dependency period type. Valid values:
        # - CURRENT_PERIOD
        # - LAST_PERIOD
        # - LAST_N_PERIOD
        # - LAST_24_HOUR.
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
        # The Spark client version.
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
        # The parameter name.
        self.key = key
        # The parameter value.
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
        # The end time in the format of HH:mm.
        self.end_time = end_time
        # The custom interval.
        self.interval = interval
        # The interval unit. Valid values: MINUTE, HOUR.
        self.interval_unit = interval_unit
        # The scheduling period.
        self.schedule_period = schedule_period
        # The start time in the format of HH:mm.
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

