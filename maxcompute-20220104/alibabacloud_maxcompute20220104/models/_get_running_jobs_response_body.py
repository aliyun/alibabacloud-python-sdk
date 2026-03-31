# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_maxcompute20220104 import models as main_models
from darabonba.model import DaraModel

class GetRunningJobsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetRunningJobsResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # *   If the value of success was false, an error code was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # Indicates whether the request was successful. If this parameter was not empty and the value of this parameter was not 200, the request failed.
        self.http_code = http_code
        # The ID of the request.
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
            result['data'] = self.data.to_map()

        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg

        if self.http_code is not None:
            result['httpCode'] = self.http_code

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.GetRunningJobsResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')

        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetRunningJobsResponseBodyData(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        running_job_info_list: List[main_models.GetRunningJobsResponseBodyDataRunningJobInfoList] = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The list of jobs in the running state.
        self.running_job_info_list = running_job_info_list
        # The total number of returned entries.
        self.total_count = total_count

    def validate(self):
        if self.running_job_info_list:
            for v1 in self.running_job_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        result['runningJobInfoList'] = []
        if self.running_job_info_list is not None:
            for k1 in self.running_job_info_list:
                result['runningJobInfoList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        self.running_job_info_list = []
        if m.get('runningJobInfoList') is not None:
            for k1 in m.get('runningJobInfoList'):
                temp_model = main_models.GetRunningJobsResponseBodyDataRunningJobInfoList()
                self.running_job_info_list.append(temp_model.from_map(k1))

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class GetRunningJobsResponseBodyDataRunningJobInfoList(DaraModel):
    def __init__(
        self,
        cu_snapshot: float = None,
        instance_id: str = None,
        job_owner: str = None,
        memory_snapshot: float = None,
        progress: float = None,
        project: str = None,
        quota_nickname: str = None,
        running_at_time: int = None,
        submitted_at_time: int = None,
    ):
        # The compute unit (CU) snapshot proportion of the job.
        self.cu_snapshot = cu_snapshot
        # The instance ID.
        self.instance_id = instance_id
        # The account that submits the job.
        self.job_owner = job_owner
        # The memory snapshot proportion of the job.
        self.memory_snapshot = memory_snapshot
        # The progress of the job.
        self.progress = progress
        # The name of the MaxCompute project.
        self.project = project
        # The nickname of the quota that is used by the job.
        self.quota_nickname = quota_nickname
        # The time when the job starts to run.
        self.running_at_time = running_at_time
        # The time when the job is submitted.
        self.submitted_at_time = submitted_at_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cu_snapshot is not None:
            result['cuSnapshot'] = self.cu_snapshot

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.job_owner is not None:
            result['jobOwner'] = self.job_owner

        if self.memory_snapshot is not None:
            result['memorySnapshot'] = self.memory_snapshot

        if self.progress is not None:
            result['progress'] = self.progress

        if self.project is not None:
            result['project'] = self.project

        if self.quota_nickname is not None:
            result['quotaNickname'] = self.quota_nickname

        if self.running_at_time is not None:
            result['runningAtTime'] = self.running_at_time

        if self.submitted_at_time is not None:
            result['submittedAtTime'] = self.submitted_at_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cuSnapshot') is not None:
            self.cu_snapshot = m.get('cuSnapshot')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('jobOwner') is not None:
            self.job_owner = m.get('jobOwner')

        if m.get('memorySnapshot') is not None:
            self.memory_snapshot = m.get('memorySnapshot')

        if m.get('progress') is not None:
            self.progress = m.get('progress')

        if m.get('project') is not None:
            self.project = m.get('project')

        if m.get('quotaNickname') is not None:
            self.quota_nickname = m.get('quotaNickname')

        if m.get('runningAtTime') is not None:
            self.running_at_time = m.get('runningAtTime')

        if m.get('submittedAtTime') is not None:
            self.submitted_at_time = m.get('submittedAtTime')

        return self

