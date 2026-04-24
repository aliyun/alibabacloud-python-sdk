# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yike20260319 import models as main_models
from darabonba.model import DaraModel

class GetYikeVoiceNarratorJobResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        job_id: str = None,
        job_params: str = None,
        job_result: List[main_models.GetYikeVoiceNarratorJobResponseBodyJobResult] = None,
        job_status: str = None,
        request_id: str = None,
        user_data: str = None,
    ):
        self.error_code = error_code
        self.job_id = job_id
        self.job_params = job_params
        self.job_result = job_result
        self.job_status = job_status
        self.request_id = request_id
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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.job_params is not None:
            result['JobParams'] = self.job_params

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
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('JobParams') is not None:
            self.job_params = m.get('JobParams')

        self.job_result = []
        if m.get('JobResult') is not None:
            for k1 in m.get('JobResult'):
                temp_model = main_models.GetYikeVoiceNarratorJobResponseBodyJobResult()
                self.job_result.append(temp_model.from_map(k1))

        if m.get('JobStatus') is not None:
            self.job_status = m.get('JobStatus')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class GetYikeVoiceNarratorJobResponseBodyJobResult(DaraModel):
    def __init__(
        self,
        editing_project_id: str = None,
        media_id: str = None,
        output_language: str = None,
        output_url: str = None,
    ):
        self.editing_project_id = editing_project_id
        self.media_id = media_id
        self.output_language = output_language
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

