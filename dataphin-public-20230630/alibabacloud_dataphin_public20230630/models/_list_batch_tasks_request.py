# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListBatchTasksRequest(DaraModel):
    def __init__(
        self,
        batch_task_query: main_models.ListBatchTasksRequestBatchTaskQuery = None,
        op_tenant_id: int = None,
        op_user_id: str = None,
    ):
        # The task query conditions.
        # 
        # This parameter is required.
        self.batch_task_query = batch_task_query
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # The ID of the user who performs the operation.
        self.op_user_id = op_user_id

    def validate(self):
        if self.batch_task_query:
            self.batch_task_query.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_task_query is not None:
            result['BatchTaskQuery'] = self.batch_task_query.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.op_user_id is not None:
            result['OpUserId'] = self.op_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchTaskQuery') is not None:
            temp_model = main_models.ListBatchTasksRequestBatchTaskQuery()
            self.batch_task_query = temp_model.from_map(m.get('BatchTaskQuery'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('OpUserId') is not None:
            self.op_user_id = m.get('OpUserId')

        return self

class ListBatchTasksRequestBatchTaskQuery(DaraModel):
    def __init__(
        self,
        condition_schedule_enable: bool = None,
        create_begin_time: int = None,
        create_end_time: int = None,
        develop_owner_list: List[str] = None,
        directory_list: List[str] = None,
        include_sub_directory: bool = None,
        keyword: str = None,
        last_submit_status_list: List[str] = None,
        lock_user_list: List[str] = None,
        modified_begin_time: int = None,
        modified_end_time: int = None,
        node_status_list: List[int] = None,
        ops_owner_list: List[str] = None,
        output_table_name_list: List[str] = None,
        page: int = None,
        page_size: int = None,
        project_id: int = None,
        published: bool = None,
        ref_code_template_id: str = None,
        schedule_interval_type_list: List[str] = None,
        task_status_list: List[int] = None,
        task_tag_list: List[str] = None,
        task_type_list: List[int] = None,
    ):
        # Specifies whether to enable conditional scheduling. If not specified, no filtering is applied.
        self.condition_schedule_enable = condition_schedule_enable
        # The start time of the creation time range, in milliseconds. Must be specified together with CreateEndTime.
        self.create_begin_time = create_begin_time
        # The end time of the creation time range, in milliseconds. Must be specified together with CreateBeginTime.
        self.create_end_time = create_end_time
        # The list of developer IDs. If multiple IDs are specified, the union is used. If empty or not specified, no filtering is applied.
        self.develop_owner_list = develop_owner_list
        # The list of task directories, such as ["/"]. If empty or not specified, no filtering is applied.
        self.directory_list = directory_list
        # Specifies whether to include tasks in the subdirectories of the directories specified in DirectoryList. Default value: false.
        self.include_sub_directory = include_sub_directory
        # The search keyword for fuzzy matching by task name or node ID. If empty or not specified, no filtering is applied.
        self.keyword = keyword
        # The list of recent submit statuses. Valid values: SUBMITTING, SUCCESS, FAILED, and WARNING. If empty or not specified, no filtering is applied.
        self.last_submit_status_list = last_submit_status_list
        # The list of locker IDs. If multiple IDs are specified, the union is used. If empty or not specified, no filtering by locker is applied.
        self.lock_user_list = lock_user_list
        # The start time of the last modification time range, in milliseconds. Must be specified together with ModifiedEndTime.
        self.modified_begin_time = modified_begin_time
        # The end time of the last modification time range, in milliseconds. Must be specified together with ModifiedBeginTime.
        self.modified_end_time = modified_end_time
        # The list of scheduling types. Valid values: 0 (Manual), 1 (Normal), 2 (Paused), and 3 (Dry run). If empty or not specified, no filtering is applied.
        self.node_status_list = node_status_list
        # The list of O&M owner IDs. If multiple IDs are specified, the union is used. If empty or not specified, no filtering is applied.
        self.ops_owner_list = ops_owner_list
        # The list of output table names for exact matching. If multiple table names are specified, the OR logical operator is used. If empty or not specified, no filtering is applied.
        self.output_table_name_list = output_table_name_list
        # The page number. Pages start from 1. Default value: 1.
        self.page = page
        # The number of entries per page. Default value: 20. Maximum value: 100.
        self.page_size = page_size
        # The project ID. The query scope is limited to this project.
        # 
        # This parameter is required.
        self.project_id = project_id
        # Specifies whether the task is published to the production environment. If not specified, no filtering is applied.
        self.published = published
        # The ID of the referenced offline code template. If empty or not specified, no filtering is applied.
        self.ref_code_template_id = ref_code_template_id
        # The list of scheduling intervals. Valid values: MINUTELY, HOURLY, DAILY, WEEKLY, and MONTHLY. If empty or not specified, no filtering is applied.
        self.schedule_interval_type_list = schedule_interval_type_list
        # The list of task statuses. Valid values: 0 (Draft), 1 (Submitting), 2 (Submitted), and 100 (In development). If empty or not specified, no filtering is applied.
        self.task_status_list = task_status_list
        # The list of task tag names. If empty or not specified, no filtering is applied.
        self.task_tag_list = task_tag_list
        # The list of task type codes. If empty or not specified, no filtering is applied.
        self.task_type_list = task_type_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.condition_schedule_enable is not None:
            result['ConditionScheduleEnable'] = self.condition_schedule_enable

        if self.create_begin_time is not None:
            result['CreateBeginTime'] = self.create_begin_time

        if self.create_end_time is not None:
            result['CreateEndTime'] = self.create_end_time

        if self.develop_owner_list is not None:
            result['DevelopOwnerList'] = self.develop_owner_list

        if self.directory_list is not None:
            result['DirectoryList'] = self.directory_list

        if self.include_sub_directory is not None:
            result['IncludeSubDirectory'] = self.include_sub_directory

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.last_submit_status_list is not None:
            result['LastSubmitStatusList'] = self.last_submit_status_list

        if self.lock_user_list is not None:
            result['LockUserList'] = self.lock_user_list

        if self.modified_begin_time is not None:
            result['ModifiedBeginTime'] = self.modified_begin_time

        if self.modified_end_time is not None:
            result['ModifiedEndTime'] = self.modified_end_time

        if self.node_status_list is not None:
            result['NodeStatusList'] = self.node_status_list

        if self.ops_owner_list is not None:
            result['OpsOwnerList'] = self.ops_owner_list

        if self.output_table_name_list is not None:
            result['OutputTableNameList'] = self.output_table_name_list

        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.published is not None:
            result['Published'] = self.published

        if self.ref_code_template_id is not None:
            result['RefCodeTemplateId'] = self.ref_code_template_id

        if self.schedule_interval_type_list is not None:
            result['ScheduleIntervalTypeList'] = self.schedule_interval_type_list

        if self.task_status_list is not None:
            result['TaskStatusList'] = self.task_status_list

        if self.task_tag_list is not None:
            result['TaskTagList'] = self.task_tag_list

        if self.task_type_list is not None:
            result['TaskTypeList'] = self.task_type_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConditionScheduleEnable') is not None:
            self.condition_schedule_enable = m.get('ConditionScheduleEnable')

        if m.get('CreateBeginTime') is not None:
            self.create_begin_time = m.get('CreateBeginTime')

        if m.get('CreateEndTime') is not None:
            self.create_end_time = m.get('CreateEndTime')

        if m.get('DevelopOwnerList') is not None:
            self.develop_owner_list = m.get('DevelopOwnerList')

        if m.get('DirectoryList') is not None:
            self.directory_list = m.get('DirectoryList')

        if m.get('IncludeSubDirectory') is not None:
            self.include_sub_directory = m.get('IncludeSubDirectory')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('LastSubmitStatusList') is not None:
            self.last_submit_status_list = m.get('LastSubmitStatusList')

        if m.get('LockUserList') is not None:
            self.lock_user_list = m.get('LockUserList')

        if m.get('ModifiedBeginTime') is not None:
            self.modified_begin_time = m.get('ModifiedBeginTime')

        if m.get('ModifiedEndTime') is not None:
            self.modified_end_time = m.get('ModifiedEndTime')

        if m.get('NodeStatusList') is not None:
            self.node_status_list = m.get('NodeStatusList')

        if m.get('OpsOwnerList') is not None:
            self.ops_owner_list = m.get('OpsOwnerList')

        if m.get('OutputTableNameList') is not None:
            self.output_table_name_list = m.get('OutputTableNameList')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Published') is not None:
            self.published = m.get('Published')

        if m.get('RefCodeTemplateId') is not None:
            self.ref_code_template_id = m.get('RefCodeTemplateId')

        if m.get('ScheduleIntervalTypeList') is not None:
            self.schedule_interval_type_list = m.get('ScheduleIntervalTypeList')

        if m.get('TaskStatusList') is not None:
            self.task_status_list = m.get('TaskStatusList')

        if m.get('TaskTagList') is not None:
            self.task_tag_list = m.get('TaskTagList')

        if m.get('TaskTypeList') is not None:
            self.task_type_list = m.get('TaskTypeList')

        return self

