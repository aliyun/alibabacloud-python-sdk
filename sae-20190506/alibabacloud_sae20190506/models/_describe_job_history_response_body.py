# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class DescribeJobHistoryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeJobHistoryResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        # The HTTP status code returned. Valid values:
        # 
        # *   **2xx**: The call was successful.
        # *   **3xx**: The call was redirected.
        # *   **4xx**: The call failed.
        # *   **5xx**: A server error occurred.
        self.code = code
        # The returned data.
        self.data = data
        # The error code returned. Take note of the following rules:
        # 
        # *   If the call is successful, the **ErrorCode** parameter is not returned.
        # *   If the call fails, the **ErrorCode** parameter is returned. For more information, see the "**Error codes**" section in this topic.
        self.error_code = error_code
        # The message returned. Take note of the following rules:
        # 
        # *   If the call is successful, **success** is returned.
        # *   If the call fails, an error code is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success
        # The trace ID that is used to query the details of the request.
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.DescribeJobHistoryResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        return self

class DescribeJobHistoryResponseBodyData(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        jobs: List[main_models.DescribeJobHistoryResponseBodyDataJobs] = None,
        page_size: int = None,
        total_size: int = None,
    ):
        # The page number of the returned page.
        self.current_page = current_page
        # The jobs.
        self.jobs = jobs
        # The number of entries to return on each page. Valid values: 0 to 10000.
        self.page_size = page_size
        # The total number of jobs.
        self.total_size = total_size

    def validate(self):
        if self.jobs:
            for v1 in self.jobs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        result['Jobs'] = []
        if self.jobs is not None:
            for k1 in self.jobs:
                result['Jobs'].append(k1.to_map() if k1 else None)

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_size is not None:
            result['TotalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.jobs = []
        if m.get('Jobs') is not None:
            for k1 in m.get('Jobs'):
                temp_model = main_models.DescribeJobHistoryResponseBodyDataJobs()
                self.jobs.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        return self

class DescribeJobHistoryResponseBodyDataJobs(DaraModel):
    def __init__(
        self,
        active: int = None,
        completion_time: int = None,
        failed: int = None,
        job_id: str = None,
        message: str = None,
        start_time: int = None,
        state: str = None,
        succeeded: int = None,
    ):
        # The number of running instances.
        self.active = active
        # The time when the job was executed.
        self.completion_time = completion_time
        # The number of instances that failed to run.
        self.failed = failed
        # The job ID.
        self.job_id = job_id
        # The message returned if exceptions occur during job running.
        self.message = message
        # The time when the job was created.
        self.start_time = start_time
        # The status of the job. Valid values:
        # 
        # *   **0**: The job was not executed.
        # *   **1**: The job was executed.
        # *   **2**: The job failed to be executed.
        # *   **3**: The job is being executed.
        self.state = state
        # The number of instances that are successfully run.
        self.succeeded = succeeded

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active is not None:
            result['Active'] = self.active

        if self.completion_time is not None:
            result['CompletionTime'] = self.completion_time

        if self.failed is not None:
            result['Failed'] = self.failed

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.message is not None:
            result['Message'] = self.message

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.state is not None:
            result['State'] = self.state

        if self.succeeded is not None:
            result['Succeeded'] = self.succeeded

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')

        if m.get('CompletionTime') is not None:
            self.completion_time = m.get('CompletionTime')

        if m.get('Failed') is not None:
            self.failed = m.get('Failed')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Succeeded') is not None:
            self.succeeded = m.get('Succeeded')

        return self

