# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_yike20260707 import models as main_models
from darabonba.model import DaraModel

class GetVideoDetextJobResponseBody(DaraModel):
    def __init__(
        self,
        job: main_models.GetVideoDetextJobResponseBodyJob = None,
        request_id: str = None,
    ):
        # The video text erasure task.
        self.job = job
        # The request ID, which is used for Tracing Analysis and troubleshooting.
        self.request_id = request_id

    def validate(self):
        if self.job:
            self.job.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job is not None:
            result['Job'] = self.job.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Job') is not None:
            temp_model = main_models.GetVideoDetextJobResponseBodyJob()
            self.job = temp_model.from_map(m.get('Job'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetVideoDetextJobResponseBodyJob(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        input: str = None,
        job_id: str = None,
        job_parameters: str = None,
        job_type: str = None,
        output: str = None,
        status: str = None,
    ):
        # The business error code returned when the task fails. This field is typically not returned for non-failure states.
        self.error_code = error_code
        # The business error message returned when the task fails. This field is typically not returned for non-failure states.
        self.error_message = error_message
        # The normalized input configuration JSON string saved at submission time.
        self.input = input
        # The video text erasure task ID.
        self.job_id = job_id
        # The normalized text erasure parameter JSON string.
        self.job_parameters = job_parameters
        # The task type. The value is fixed to VIDEO_DETEXT.
        self.job_type = job_type
        # The task output JSON string. When the task succeeds, AiResult.DetextVideoURL contains the URL of the video with text erased.
        self.output = output
        # The task status. Valid values: Created, Queuing, Executing, Finished, and Failed.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.input is not None:
            result['Input'] = self.input

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.job_parameters is not None:
            result['JobParameters'] = self.job_parameters

        if self.job_type is not None:
            result['JobType'] = self.job_type

        if self.output is not None:
            result['Output'] = self.output

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('Input') is not None:
            self.input = m.get('Input')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('JobParameters') is not None:
            self.job_parameters = m.get('JobParameters')

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        if m.get('Output') is not None:
            self.output = m.get('Output')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

