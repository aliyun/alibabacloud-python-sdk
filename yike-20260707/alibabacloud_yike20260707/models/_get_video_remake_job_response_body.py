# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yike20260707 import models as main_models
from darabonba.model import DaraModel

class GetVideoRemakeJobResponseBody(DaraModel):
    def __init__(
        self,
        job: main_models.GetVideoRemakeJobResponseBodyJob = None,
        request_id: str = None,
    ):
        # The unified remake task details.
        self.job = job
        # The request tracking identifier.
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
            temp_model = main_models.GetVideoRemakeJobResponseBodyJob()
            self.job = temp_model.from_map(m.get('Job'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetVideoRemakeJobResponseBodyJob(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        job_id: str = None,
        job_result: main_models.GetVideoRemakeJobResponseBodyJobJobResult = None,
        media_ids: List[str] = None,
        status: str = None,
        user_data: str = None,
    ):
        # The error code for the failed asynchronous task. This parameter has a value only when the task status is Failed.
        self.error_code = error_code
        # The error message for the failed asynchronous task. This parameter has a value only when the task status is Failed.
        self.error_message = error_message
        # The unified remake task ID.
        self.job_id = job_id
        # The content understanding and script outputs returned when the status is Finished. This is not the rendered video.
        self.job_result = job_result
        # The list of input media asset IDs.
        self.media_ids = media_ids
        # The task status. Valid values: Created, Executing, Finished, and Failed. Finished indicates that content understanding and script generation are completed. If the status is Failed, check ErrorCode and ErrorMessage. If the task has been deleted, the query returns RecordNotFound.
        self.status = status
        # The UserData JSON string submitted with the task, returned as is.
        self.user_data = user_data

    def validate(self):
        if self.job_result:
            self.job_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.job_result is not None:
            result['JobResult'] = self.job_result.to_map()

        if self.media_ids is not None:
            result['MediaIds'] = self.media_ids

        if self.status is not None:
            result['Status'] = self.status

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('JobResult') is not None:
            temp_model = main_models.GetVideoRemakeJobResponseBodyJobJobResult()
            self.job_result = temp_model.from_map(m.get('JobResult'))

        if m.get('MediaIds') is not None:
            self.media_ids = m.get('MediaIds')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class GetVideoRemakeJobResponseBodyJobJobResult(DaraModel):
    def __init__(
        self,
        ai_result: str = None,
        script: str = None,
    ):
        # The download URL of the JSON file for the content understanding result.
        self.ai_result = ai_result
        # The download URL of the JSON file for the creative script. Use the file content as the Script parameter for SubmitVideoRenderJob.
        self.script = script

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ai_result is not None:
            result['AiResult'] = self.ai_result

        if self.script is not None:
            result['Script'] = self.script

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AiResult') is not None:
            self.ai_result = m.get('AiResult')

        if m.get('Script') is not None:
            self.script = m.get('Script')

        return self

