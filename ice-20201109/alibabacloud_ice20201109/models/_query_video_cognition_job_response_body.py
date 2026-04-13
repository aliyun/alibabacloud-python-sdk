# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class QueryVideoCognitionJobResponseBody(DaraModel):
    def __init__(
        self,
        input: main_models.QueryVideoCognitionJobResponseBodyInput = None,
        job_status: str = None,
        params: str = None,
        request_id: str = None,
        results: main_models.QueryVideoCognitionJobResponseBodyResults = None,
        template_id: str = None,
        user_data: str = None,
    ):
        self.input = input
        # The status of the task. Valid values:
        # 
        # *   **Success**
        # *   **Fail**
        # *   **Processing**
        # *   **Submitted**
        self.job_status = job_status
        self.params = params
        # The request ID.
        self.request_id = request_id
        self.results = results
        self.template_id = template_id
        # The user-defined data.
        self.user_data = user_data

    def validate(self):
        if self.input:
            self.input.validate()
        if self.results:
            self.results.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input is not None:
            result['Input'] = self.input.to_map()

        if self.job_status is not None:
            result['JobStatus'] = self.job_status

        if self.params is not None:
            result['Params'] = self.params

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.results is not None:
            result['Results'] = self.results.to_map()

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Input') is not None:
            temp_model = main_models.QueryVideoCognitionJobResponseBodyInput()
            self.input = temp_model.from_map(m.get('Input'))

        if m.get('JobStatus') is not None:
            self.job_status = m.get('JobStatus')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Results') is not None:
            temp_model = main_models.QueryVideoCognitionJobResponseBodyResults()
            self.results = temp_model.from_map(m.get('Results'))

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class QueryVideoCognitionJobResponseBodyResults(DaraModel):
    def __init__(
        self,
        result: List[main_models.QueryVideoCognitionJobResponseBodyResultsResult] = None,
    ):
        self.result = result

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['result'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('result') is not None:
            for k1 in m.get('result'):
                temp_model = main_models.QueryVideoCognitionJobResponseBodyResultsResult()
                self.result.append(temp_model.from_map(k1))

        return self

class QueryVideoCognitionJobResponseBodyResultsResult(DaraModel):
    def __init__(
        self,
        data: str = None,
        type: str = None,
    ):
        self.data = data
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class QueryVideoCognitionJobResponseBodyInput(DaraModel):
    def __init__(
        self,
        media: str = None,
        type: str = None,
    ):
        self.media = media
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media is not None:
            result['Media'] = self.media

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Media') is not None:
            self.media = m.get('Media')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

