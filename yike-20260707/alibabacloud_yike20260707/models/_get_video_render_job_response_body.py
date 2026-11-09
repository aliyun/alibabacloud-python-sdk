# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_yike20260707 import models as main_models
from darabonba.model import DaraModel

class GetVideoRenderJobResponseBody(DaraModel):
    def __init__(
        self,
        job: main_models.GetVideoRenderJobResponseBodyJob = None,
        request_id: str = None,
    ):
        # The video rendering and compositing task object.
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
            temp_model = main_models.GetVideoRenderJobResponseBodyJob()
            self.job = temp_model.from_map(m.get('Job'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetVideoRenderJobResponseBodyJob(DaraModel):
    def __init__(
        self,
        editing_project_id: str = None,
        error_code: str = None,
        error_message: str = None,
        job_id: str = None,
        language: str = None,
        result: str = None,
        status: str = None,
        user_data: str = None,
    ):
        # The ID of the online editing project, which can be used for secondary editing of the produced video.
        self.editing_project_id = editing_project_id
        # The error code. This parameter is returned when the job is in the Failed state.
        self.error_code = error_code
        # The error message. This parameter is returned when the job is in the Failed state.
        self.error_message = error_message
        # The job ID.
        self.job_id = job_id
        # The voiceover language of the produced video.
        self.language = language
        # The download URL of the rendered and composited video.
        self.result = result
        # The job status. Valid values:
        # 
        # - Created: The job is created.
        # - Executing: The job is being executed.
        # - Finished: The job is completed.
        # - Failed: The job failed.
        # - Deleted: The job is deleted.
        self.status = status
        # The user-defined parameter, which is a JSON-formatted string.
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.editing_project_id is not None:
            result['EditingProjectId'] = self.editing_project_id

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.language is not None:
            result['Language'] = self.language

        if self.result is not None:
            result['Result'] = self.result

        if self.status is not None:
            result['Status'] = self.status

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EditingProjectId') is not None:
            self.editing_project_id = m.get('EditingProjectId')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

