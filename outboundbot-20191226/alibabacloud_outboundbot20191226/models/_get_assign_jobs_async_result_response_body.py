# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetAssignJobsAsyncResultResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        job_group_id: str = None,
        jobs_id: List[str] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        timeout: bool = None,
        valid: bool = None,
    ):
        # The API status code.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The task group ID.
        self.job_group_id = job_group_id
        # The list of job IDs.
        self.jobs_id = jobs_id
        # The API message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the operation succeeded.
        self.success = success
        # Indicates whether the asynchronous task timed out.
        self.timeout = timeout
        # Indicates whether the result has been fully generated.
        self.valid = valid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.job_group_id is not None:
            result['JobGroupId'] = self.job_group_id

        if self.jobs_id is not None:
            result['JobsId'] = self.jobs_id

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        if self.valid is not None:
            result['Valid'] = self.valid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('JobGroupId') is not None:
            self.job_group_id = m.get('JobGroupId')

        if m.get('JobsId') is not None:
            self.jobs_id = m.get('JobsId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        if m.get('Valid') is not None:
            self.valid = m.get('Valid')

        return self

