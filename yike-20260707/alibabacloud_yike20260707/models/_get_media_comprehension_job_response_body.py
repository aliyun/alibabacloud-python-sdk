# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yike20260707 import models as main_models
from darabonba.model import DaraModel

class GetMediaComprehensionJobResponseBody(DaraModel):
    def __init__(
        self,
        job: main_models.GetMediaComprehensionJobResponseBodyJob = None,
        media_comprehension_job: main_models.GetMediaComprehensionJobResponseBodyMediaComprehensionJob = None,
        request_id: str = None,
    ):
        # The media asset content understanding result object.
        self.job = job
        # The media asset content understanding object. This parameter is deprecated.
        self.media_comprehension_job = media_comprehension_job
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.job:
            self.job.validate()
        if self.media_comprehension_job:
            self.media_comprehension_job.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job is not None:
            result['Job'] = self.job.to_map()

        if self.media_comprehension_job is not None:
            result['MediaComprehensionJob'] = self.media_comprehension_job.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Job') is not None:
            temp_model = main_models.GetMediaComprehensionJobResponseBodyJob()
            self.job = temp_model.from_map(m.get('Job'))

        if m.get('MediaComprehensionJob') is not None:
            temp_model = main_models.GetMediaComprehensionJobResponseBodyMediaComprehensionJob()
            self.media_comprehension_job = temp_model.from_map(m.get('MediaComprehensionJob'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetMediaComprehensionJobResponseBodyMediaComprehensionJob(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        job_id: str = None,
        media_id: str = None,
        result: str = None,
        state: str = None,
        user_data: str = None,
    ):
        # The error code. This parameter is returned when the job is in the `Failed` state.
        self.error_code = error_code
        # The error message. This parameter is returned when the job is in the Failed state.
        self.error_message = error_message
        # The job ID.
        self.job_id = job_id
        # The media asset ID.
        self.media_id = media_id
        # The analysis result, which is a JSON string.
        self.result = result
        # The file status. Valid values:
        # 
        # - **Created**: Created.
        # - **Executing**: Executing.
        # - **Finished**: Finished.
        # - **Failed**: Failed.
        # - **Deleted**: Deleted.
        self.state = state
        # The user-defined parameter, which is a JSON-formatted string.
        self.user_data = user_data

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

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.result is not None:
            result['Result'] = self.result

        if self.state is not None:
            result['State'] = self.state

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

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class GetMediaComprehensionJobResponseBodyJob(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        media_ids: List[str] = None,
        result: str = None,
        status: str = None,
        user_data: str = None,
    ):
        # The error code. This parameter is returned when the job is in the Failed state.
        self.error_code = error_code
        # The error message. This parameter is returned when the job is in the Failed state.
        self.error_message = error_message
        # The list of media asset IDs. If the input is a URL, the media asset ID registered after input is returned.
        self.media_ids = media_ids
        # The URL of the analysis result file. The file content is in JSON format.
        self.result = result
        # The file status. Valid values:
        # 
        # - **Created**: Created.
        # - **Executing**: Executing.
        # - **Finished**: Finished.
        # - **Failed**: Failed.
        # - **Deleted**: Deleted.
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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.media_ids is not None:
            result['MediaIds'] = self.media_ids

        if self.result is not None:
            result['Result'] = self.result

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

        if m.get('MediaIds') is not None:
            self.media_ids = m.get('MediaIds')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

