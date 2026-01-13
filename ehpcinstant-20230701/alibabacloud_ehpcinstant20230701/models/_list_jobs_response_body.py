# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ehpcinstant20230701 import models as main_models
from darabonba.model import DaraModel

class ListJobsResponseBody(DaraModel):
    def __init__(
        self,
        job_list: List[main_models.ListJobsResponseBodyJobList] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of jobs.
        self.job_list = job_list
        # The current page number.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned. This parameter is optional and is not returned by default.
        self.total_count = total_count

    def validate(self):
        if self.job_list:
            for v1 in self.job_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['JobList'] = []
        if self.job_list is not None:
            for k1 in self.job_list:
                result['JobList'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.job_list = []
        if m.get('JobList') is not None:
            for k1 in m.get('JobList'):
                temp_model = main_models.ListJobsResponseBodyJobList()
                self.job_list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListJobsResponseBodyJobList(DaraModel):
    def __init__(
        self,
        app_extra_info: str = None,
        app_name: str = None,
        create_time: str = None,
        end_time: str = None,
        executor_count: int = None,
        job_description: str = None,
        job_id: str = None,
        job_name: str = None,
        owner_uid: str = None,
        start_time: str = None,
        status: str = None,
        tags: List[main_models.ListJobsResponseBodyJobListTags] = None,
        task_count: int = None,
        task_sustainable: bool = None,
    ):
        # The additional information about the application.
        self.app_extra_info = app_extra_info
        self.app_name = app_name
        # The time when the job was submitted.
        self.create_time = create_time
        # The end time of the job.
        self.end_time = end_time
        # The number of running nodes.
        self.executor_count = executor_count
        # The description of the job.
        self.job_description = job_description
        # The ID of the job.
        self.job_id = job_id
        # The job name.
        self.job_name = job_name
        # The UID of the creator.
        self.owner_uid = owner_uid
        # The start time of the job.
        self.start_time = start_time
        # The status of the job. Valid values:
        # 
        # *   Pending
        # *   Initing
        # *   Succeed
        # *   Failed
        # *   Running
        # *   Exception
        # *   Retrying
        # *   Expired
        # *   Deleting
        # *   Deleted
        self.status = status
        # The list of job tags.
        self.tags = tags
        # The number of tasks.
        self.task_count = task_count
        # Indicate whether the job is a long-running job.
        self.task_sustainable = task_sustainable

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_extra_info is not None:
            result['AppExtraInfo'] = self.app_extra_info

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.executor_count is not None:
            result['ExecutorCount'] = self.executor_count

        if self.job_description is not None:
            result['JobDescription'] = self.job_description

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.job_name is not None:
            result['JobName'] = self.job_name

        if self.owner_uid is not None:
            result['OwnerUid'] = self.owner_uid

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.task_count is not None:
            result['TaskCount'] = self.task_count

        if self.task_sustainable is not None:
            result['TaskSustainable'] = self.task_sustainable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppExtraInfo') is not None:
            self.app_extra_info = m.get('AppExtraInfo')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ExecutorCount') is not None:
            self.executor_count = m.get('ExecutorCount')

        if m.get('JobDescription') is not None:
            self.job_description = m.get('JobDescription')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        if m.get('OwnerUid') is not None:
            self.owner_uid = m.get('OwnerUid')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListJobsResponseBodyJobListTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TaskCount') is not None:
            self.task_count = m.get('TaskCount')

        if m.get('TaskSustainable') is not None:
            self.task_sustainable = m.get('TaskSustainable')

        return self

class ListJobsResponseBodyJobListTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The key of the job tag.
        self.tag_key = tag_key
        # The value of the job tag.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

