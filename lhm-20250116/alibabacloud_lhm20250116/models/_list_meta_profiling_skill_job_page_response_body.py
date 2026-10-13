# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_lhm20250116 import models as main_models
from darabonba.model import DaraModel

class ListMetaProfilingSkillJobPageResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListMetaProfilingSkillJobPageResponseBodyData] = None,
        err_code: str = None,
        err_message: str = None,
        page_index: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The list of profiling tasks. For the element structure, see the descriptions of the child fields.
        self.data = data
        # The error code. This parameter is an empty string if the call is successful.
        self.err_code = err_code
        # The error message. This parameter is an empty string if the call is successful.
        self.err_message = err_message
        # The current page number, starting from 1.
        self.page_index = page_index
        # The number of records to return per page.
        self.page_size = page_size
        # The request ID used to locate and troubleshoot issues for this call.
        self.request_id = request_id
        # Indicates whether the call was successful. A value of true indicates success, and a value of false indicates failure. If the call fails, troubleshoot the issue based on the errCode and errMessage parameters.
        self.success = success
        # The total number of records that meet the specified conditions.
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.err_code is not None:
            result['errCode'] = self.err_code

        if self.err_message is not None:
            result['errMessage'] = self.err_message

        if self.page_index is not None:
            result['pageIndex'] = self.page_index

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.ListMetaProfilingSkillJobPageResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')

        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')

        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListMetaProfilingSkillJobPageResponseBodyData(DaraModel):
    def __init__(
        self,
        component_id: int = None,
        current_task_status: int = None,
        dc_name: str = None,
        dc_status: int = None,
        dc_type: str = None,
        diff_node_num: int = None,
        diff_partition_num: int = None,
        diff_table_num: int = None,
        diff_workflow_num: int = None,
        ds_category_type: str = None,
        gmt_create: str = None,
        has_increment_changes: bool = None,
        id: int = None,
        job_desc: str = None,
        job_name: str = None,
        job_status: int = None,
        last_batch_id: str = None,
        last_task_id: int = None,
        next_cron_time: str = None,
        profiling_enable: int = None,
        profiling_schema_list: List[str] = None,
        task_exec_result: int = None,
        task_finish_time: str = None,
        task_type: str = None,
    ):
        # The component ID, which is the primary key identifier of the data source component.
        self.component_id = component_id
        # The identifier of the current execution status of the task.
        self.current_task_status = current_task_status
        # The data component name.
        self.dc_name = dc_name
        # The status identifier of the data component.
        self.dc_status = dc_status
        # The type identifier of the data component.
        self.dc_type = dc_type
        # The number of differing nodes.
        self.diff_node_num = diff_node_num
        # The number of differing partitions.
        self.diff_partition_num = diff_partition_num
        # The number of differing tables.
        self.diff_table_num = diff_table_num
        # The number of differing workflows.
        self.diff_workflow_num = diff_workflow_num
        # The category type identifier of the data source.
        self.ds_category_type = ds_category_type
        # The time when the record was created.
        self.gmt_create = gmt_create
        # Indicates whether incremental changes exist.
        self.has_increment_changes = has_increment_changes
        # The primary key ID of the object.
        self.id = id
        # The description of the profiling task.
        self.job_desc = job_desc
        # The profiling task name.
        self.job_name = job_name
        # The status identifier of the profiling task.
        self.job_status = job_status
        # The ID of the most recent execution batch.
        self.last_batch_id = last_batch_id
        # The ID of the most recently executed task.
        self.last_task_id = last_task_id
        # The estimated time for the next scheduled execution.
        self.next_cron_time = next_cron_time
        # Indicates whether data profiling is enabled.
        self.profiling_enable = profiling_enable
        # The list of schemas (databases) to be profiled.
        self.profiling_schema_list = profiling_schema_list
        # The identifier of the task execution result.
        self.task_exec_result = task_exec_result
        # The time when the task execution was completed.
        self.task_finish_time = task_finish_time
        # The type identifier of the task.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_id is not None:
            result['componentId'] = self.component_id

        if self.current_task_status is not None:
            result['currentTaskStatus'] = self.current_task_status

        if self.dc_name is not None:
            result['dcName'] = self.dc_name

        if self.dc_status is not None:
            result['dcStatus'] = self.dc_status

        if self.dc_type is not None:
            result['dcType'] = self.dc_type

        if self.diff_node_num is not None:
            result['diffNodeNum'] = self.diff_node_num

        if self.diff_partition_num is not None:
            result['diffPartitionNum'] = self.diff_partition_num

        if self.diff_table_num is not None:
            result['diffTableNum'] = self.diff_table_num

        if self.diff_workflow_num is not None:
            result['diffWorkflowNum'] = self.diff_workflow_num

        if self.ds_category_type is not None:
            result['dsCategoryType'] = self.ds_category_type

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.has_increment_changes is not None:
            result['hasIncrementChanges'] = self.has_increment_changes

        if self.id is not None:
            result['id'] = self.id

        if self.job_desc is not None:
            result['jobDesc'] = self.job_desc

        if self.job_name is not None:
            result['jobName'] = self.job_name

        if self.job_status is not None:
            result['jobStatus'] = self.job_status

        if self.last_batch_id is not None:
            result['lastBatchId'] = self.last_batch_id

        if self.last_task_id is not None:
            result['lastTaskId'] = self.last_task_id

        if self.next_cron_time is not None:
            result['nextCronTime'] = self.next_cron_time

        if self.profiling_enable is not None:
            result['profilingEnable'] = self.profiling_enable

        if self.profiling_schema_list is not None:
            result['profilingSchemaList'] = self.profiling_schema_list

        if self.task_exec_result is not None:
            result['taskExecResult'] = self.task_exec_result

        if self.task_finish_time is not None:
            result['taskFinishTime'] = self.task_finish_time

        if self.task_type is not None:
            result['taskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('componentId') is not None:
            self.component_id = m.get('componentId')

        if m.get('currentTaskStatus') is not None:
            self.current_task_status = m.get('currentTaskStatus')

        if m.get('dcName') is not None:
            self.dc_name = m.get('dcName')

        if m.get('dcStatus') is not None:
            self.dc_status = m.get('dcStatus')

        if m.get('dcType') is not None:
            self.dc_type = m.get('dcType')

        if m.get('diffNodeNum') is not None:
            self.diff_node_num = m.get('diffNodeNum')

        if m.get('diffPartitionNum') is not None:
            self.diff_partition_num = m.get('diffPartitionNum')

        if m.get('diffTableNum') is not None:
            self.diff_table_num = m.get('diffTableNum')

        if m.get('diffWorkflowNum') is not None:
            self.diff_workflow_num = m.get('diffWorkflowNum')

        if m.get('dsCategoryType') is not None:
            self.ds_category_type = m.get('dsCategoryType')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('hasIncrementChanges') is not None:
            self.has_increment_changes = m.get('hasIncrementChanges')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('jobDesc') is not None:
            self.job_desc = m.get('jobDesc')

        if m.get('jobName') is not None:
            self.job_name = m.get('jobName')

        if m.get('jobStatus') is not None:
            self.job_status = m.get('jobStatus')

        if m.get('lastBatchId') is not None:
            self.last_batch_id = m.get('lastBatchId')

        if m.get('lastTaskId') is not None:
            self.last_task_id = m.get('lastTaskId')

        if m.get('nextCronTime') is not None:
            self.next_cron_time = m.get('nextCronTime')

        if m.get('profilingEnable') is not None:
            self.profiling_enable = m.get('profilingEnable')

        if m.get('profilingSchemaList') is not None:
            self.profiling_schema_list = m.get('profilingSchemaList')

        if m.get('taskExecResult') is not None:
            self.task_exec_result = m.get('taskExecResult')

        if m.get('taskFinishTime') is not None:
            self.task_finish_time = m.get('taskFinishTime')

        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')

        return self

