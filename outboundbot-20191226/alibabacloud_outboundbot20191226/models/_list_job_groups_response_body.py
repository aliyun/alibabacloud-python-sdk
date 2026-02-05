# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20191226 import models as main_models
from darabonba.model import DaraModel

class ListJobGroupsResponseBody(DaraModel):
    def __init__(
        self,
        async_task_id: str = None,
        code: str = None,
        http_status_code: int = None,
        job_groups: main_models.ListJobGroupsResponseBodyJobGroups = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.async_task_id = async_task_id
        self.code = code
        self.http_status_code = http_status_code
        self.job_groups = job_groups
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.job_groups:
            self.job_groups.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.async_task_id is not None:
            result['AsyncTaskId'] = self.async_task_id

        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.job_groups is not None:
            result['JobGroups'] = self.job_groups.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsyncTaskId') is not None:
            self.async_task_id = m.get('AsyncTaskId')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('JobGroups') is not None:
            temp_model = main_models.ListJobGroupsResponseBodyJobGroups()
            self.job_groups = temp_model.from_map(m.get('JobGroups'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListJobGroupsResponseBodyJobGroups(DaraModel):
    def __init__(
        self,
        list: List[main_models.ListJobGroupsResponseBodyJobGroupsList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.list = list
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.ListJobGroupsResponseBodyJobGroupsList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListJobGroupsResponseBodyJobGroupsList(DaraModel):
    def __init__(
        self,
        creation_time: int = None,
        export_progress: main_models.ListJobGroupsResponseBodyJobGroupsListExportProgress = None,
        job_data_parsing_task_id: str = None,
        job_group_description: str = None,
        job_group_id: str = None,
        job_group_name: str = None,
        min_concurrency: int = None,
        modify_time: str = None,
        progress: main_models.ListJobGroupsResponseBodyJobGroupsListProgress = None,
        script_id: str = None,
        script_name: str = None,
        script_version: str = None,
        status: str = None,
        strategy: main_models.ListJobGroupsResponseBodyJobGroupsListStrategy = None,
        total_call_num: int = None,
    ):
        self.creation_time = creation_time
        self.export_progress = export_progress
        self.job_data_parsing_task_id = job_data_parsing_task_id
        self.job_group_description = job_group_description
        self.job_group_id = job_group_id
        self.job_group_name = job_group_name
        self.min_concurrency = min_concurrency
        self.modify_time = modify_time
        self.progress = progress
        self.script_id = script_id
        self.script_name = script_name
        self.script_version = script_version
        self.status = status
        self.strategy = strategy
        self.total_call_num = total_call_num

    def validate(self):
        if self.export_progress:
            self.export_progress.validate()
        if self.progress:
            self.progress.validate()
        if self.strategy:
            self.strategy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.export_progress is not None:
            result['ExportProgress'] = self.export_progress.to_map()

        if self.job_data_parsing_task_id is not None:
            result['JobDataParsingTaskId'] = self.job_data_parsing_task_id

        if self.job_group_description is not None:
            result['JobGroupDescription'] = self.job_group_description

        if self.job_group_id is not None:
            result['JobGroupId'] = self.job_group_id

        if self.job_group_name is not None:
            result['JobGroupName'] = self.job_group_name

        if self.min_concurrency is not None:
            result['MinConcurrency'] = self.min_concurrency

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.progress is not None:
            result['Progress'] = self.progress.to_map()

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        if self.script_name is not None:
            result['ScriptName'] = self.script_name

        if self.script_version is not None:
            result['ScriptVersion'] = self.script_version

        if self.status is not None:
            result['Status'] = self.status

        if self.strategy is not None:
            result['Strategy'] = self.strategy.to_map()

        if self.total_call_num is not None:
            result['TotalCallNum'] = self.total_call_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('ExportProgress') is not None:
            temp_model = main_models.ListJobGroupsResponseBodyJobGroupsListExportProgress()
            self.export_progress = temp_model.from_map(m.get('ExportProgress'))

        if m.get('JobDataParsingTaskId') is not None:
            self.job_data_parsing_task_id = m.get('JobDataParsingTaskId')

        if m.get('JobGroupDescription') is not None:
            self.job_group_description = m.get('JobGroupDescription')

        if m.get('JobGroupId') is not None:
            self.job_group_id = m.get('JobGroupId')

        if m.get('JobGroupName') is not None:
            self.job_group_name = m.get('JobGroupName')

        if m.get('MinConcurrency') is not None:
            self.min_concurrency = m.get('MinConcurrency')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Progress') is not None:
            temp_model = main_models.ListJobGroupsResponseBodyJobGroupsListProgress()
            self.progress = temp_model.from_map(m.get('Progress'))

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        if m.get('ScriptName') is not None:
            self.script_name = m.get('ScriptName')

        if m.get('ScriptVersion') is not None:
            self.script_version = m.get('ScriptVersion')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Strategy') is not None:
            temp_model = main_models.ListJobGroupsResponseBodyJobGroupsListStrategy()
            self.strategy = temp_model.from_map(m.get('Strategy'))

        if m.get('TotalCallNum') is not None:
            self.total_call_num = m.get('TotalCallNum')

        return self

class ListJobGroupsResponseBodyJobGroupsListStrategy(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        start_time: int = None,
    ):
        self.end_time = end_time
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

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class ListJobGroupsResponseBodyJobGroupsListProgress(DaraModel):
    def __init__(
        self,
        cancelled_num: int = None,
        duration: int = None,
        executing_num: int = None,
        failed_num: int = None,
        paused_num: int = None,
        scheduling: int = None,
        start_time: int = None,
        status: str = None,
        total_completed: int = None,
        total_jobs: int = None,
        total_not_answered: int = None,
    ):
        self.cancelled_num = cancelled_num
        self.duration = duration
        self.executing_num = executing_num
        self.failed_num = failed_num
        self.paused_num = paused_num
        self.scheduling = scheduling
        self.start_time = start_time
        self.status = status
        self.total_completed = total_completed
        self.total_jobs = total_jobs
        self.total_not_answered = total_not_answered

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cancelled_num is not None:
            result['CancelledNum'] = self.cancelled_num

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.executing_num is not None:
            result['ExecutingNum'] = self.executing_num

        if self.failed_num is not None:
            result['FailedNum'] = self.failed_num

        if self.paused_num is not None:
            result['PausedNum'] = self.paused_num

        if self.scheduling is not None:
            result['Scheduling'] = self.scheduling

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.total_completed is not None:
            result['TotalCompleted'] = self.total_completed

        if self.total_jobs is not None:
            result['TotalJobs'] = self.total_jobs

        if self.total_not_answered is not None:
            result['TotalNotAnswered'] = self.total_not_answered

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CancelledNum') is not None:
            self.cancelled_num = m.get('CancelledNum')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('ExecutingNum') is not None:
            self.executing_num = m.get('ExecutingNum')

        if m.get('FailedNum') is not None:
            self.failed_num = m.get('FailedNum')

        if m.get('PausedNum') is not None:
            self.paused_num = m.get('PausedNum')

        if m.get('Scheduling') is not None:
            self.scheduling = m.get('Scheduling')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TotalCompleted') is not None:
            self.total_completed = m.get('TotalCompleted')

        if m.get('TotalJobs') is not None:
            self.total_jobs = m.get('TotalJobs')

        if m.get('TotalNotAnswered') is not None:
            self.total_not_answered = m.get('TotalNotAnswered')

        return self

class ListJobGroupsResponseBodyJobGroupsListExportProgress(DaraModel):
    def __init__(
        self,
        file_http_url: str = None,
        progress: str = None,
        status: str = None,
    ):
        self.file_http_url = file_http_url
        self.progress = progress
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_http_url is not None:
            result['FileHttpUrl'] = self.file_http_url

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileHttpUrl') is not None:
            self.file_http_url = m.get('FileHttpUrl')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

