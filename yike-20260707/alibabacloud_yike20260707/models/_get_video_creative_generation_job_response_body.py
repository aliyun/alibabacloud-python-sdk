# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yike20260707 import models as main_models
from darabonba.model import DaraModel

class GetVideoCreativeGenerationJobResponseBody(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        error_code: str = None,
        finish_time: str = None,
        job_id: str = None,
        job_result: List[main_models.GetVideoCreativeGenerationJobResponseBodyJobResult] = None,
        job_status: str = None,
        request_id: str = None,
        user_data: str = None,
    ):
        # The job creation time in UTC format (yyyy-MM-dd\\"T\\"HH:mm:ss\\"Z\\").
        self.create_time = create_time
        # The error code. This parameter is returned only when the job status is Failed.
        self.error_code = error_code
        # The job completion time in UTC format.
        self.finish_time = finish_time
        # The job ID.
        self.job_id = job_id
        # The task results of the node. This parameter is valid only when the job status is Succeeded. Each element represents the output for a single language.
        self.job_result = job_result
        # The job status. Valid values: Running, Succeeded, and Failed.
        self.job_status = job_status
        # Id of the request
        self.request_id = request_id
        # The custom user data, which is returned as-is.
        self.user_data = user_data

    def validate(self):
        if self.job_result:
            for v1 in self.job_result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.job_id is not None:
            result['JobId'] = self.job_id

        result['JobResult'] = []
        if self.job_result is not None:
            for k1 in self.job_result:
                result['JobResult'].append(k1.to_map() if k1 else None)

        if self.job_status is not None:
            result['JobStatus'] = self.job_status

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        self.job_result = []
        if m.get('JobResult') is not None:
            for k1 in m.get('JobResult'):
                temp_model = main_models.GetVideoCreativeGenerationJobResponseBodyJobResult()
                self.job_result.append(temp_model.from_map(k1))

        if m.get('JobStatus') is not None:
            self.job_status = m.get('JobStatus')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class GetVideoCreativeGenerationJobResponseBodyJobResult(DaraModel):
    def __init__(
        self,
        editing_project_id: str = None,
        media_id: str = None,
        output_language: str = None,
        output_url: str = None,
    ):
        # The online editing project ID.
        self.editing_project_id = editing_project_id
        # The media asset ID of the output video.
        self.media_id = media_id
        # The output language. Valid values: CN, EN, and YUE.
        self.output_language = output_language
        # The signed download URL of the output video. The URL is time-limited.
        self.output_url = output_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.editing_project_id is not None:
            result['EditingProjectId'] = self.editing_project_id

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.output_language is not None:
            result['OutputLanguage'] = self.output_language

        if self.output_url is not None:
            result['OutputUrl'] = self.output_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EditingProjectId') is not None:
            self.editing_project_id = m.get('EditingProjectId')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('OutputLanguage') is not None:
            self.output_language = m.get('OutputLanguage')

        if m.get('OutputUrl') is not None:
            self.output_url = m.get('OutputUrl')

        return self

