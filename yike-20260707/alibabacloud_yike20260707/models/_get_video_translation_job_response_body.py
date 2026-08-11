# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_yike20260707 import models as main_models
from darabonba.model import DaraModel

class GetVideoTranslationJobResponseBody(DaraModel):
    def __init__(
        self,
        job: main_models.GetVideoTranslationJobResponseBodyJob = None,
        request_id: str = None,
    ):
        # The video translation task.
        self.job = job
        # The request ID.
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
            temp_model = main_models.GetVideoTranslationJobResponseBodyJob()
            self.job = temp_model.from_map(m.get('Job'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetVideoTranslationJobResponseBodyJob(DaraModel):
    def __init__(
        self,
        duration: float = None,
        editing_project_id: str = None,
        error_code: str = None,
        error_message: str = None,
        input: str = None,
        job_id: str = None,
        job_parameters: str = None,
        job_type: str = None,
        output: str = None,
        status: str = None,
    ):
        # The duration of the input video, in seconds.
        self.duration = duration
        # The editing project ID.
        self.editing_project_id = editing_project_id
        # Optional. The error code returned when the task ultimately fails.
        self.error_code = error_code
        # Optional. The error message returned when the task ultimately fails.
        self.error_message = error_message
        # The normalized Input JSON.
        self.input = input
        # The task ID.
        self.job_id = job_id
        # The normalized JobParameters JSON, including default values.
        self.job_parameters = job_parameters
        # The normalized task type.
        self.job_type = job_type
        # The JSON string of the final task result.
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
        if self.duration is not None:
            result['Duration'] = self.duration

        if self.editing_project_id is not None:
            result['EditingProjectId'] = self.editing_project_id

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
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('EditingProjectId') is not None:
            self.editing_project_id = m.get('EditingProjectId')

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

