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
        # The API status code or POP error code. Valid values:
        # - **2xx**: Success.
        # - **3xx**: Redirect.
        # - **4xx**: Client error.
        # - **5xx**: Server error.
        self.code = code
        # The response data.
        self.data = data
        # The error code.
        # - If the request is successful, the **ErrorCode** parameter is not returned.
        # - If the request fails, the **ErrorCode** parameter is returned. For more information, see the **Error codes** section in this topic.
        self.error_code = error_code
        # The additional information.
        # - If the request is successful, **success** is returned.
        # - If the request fails, a specific error code is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the job status was queried successfully. Valid values:
        # - **true**: The query succeeded.
        # - **false**: The query failed.
        self.success = success
        # The trace ID used to query detailed call information.
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
        # The current page number.
        self.current_page = current_page
        # The list of jobs.
        self.jobs = jobs
        # The number of entries per page in the paging Settings for a paged query. Valid values: 0 to 10000.
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
        # The completion time of the job.
        self.completion_time = completion_time
        # The number of failed instances.
        self.failed = failed
        # The ID of the job.
        self.job_id = job_id
        # The additional information returned when an exception occurs during job execution.
        self.message = message
        # The creation time of the job.
        self.start_time = start_time
        # The running status of the job. Valid values:
        # - **0**: Not run.
        # - **1**: Succeeded.
        # - **2**: Failed.
        # - **3**: Running.
        self.state = state
        # The number of successful instances.
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

