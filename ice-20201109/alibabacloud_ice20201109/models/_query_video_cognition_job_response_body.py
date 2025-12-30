# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class QueryVideoCognitionJobResponseBody(DaraModel):
    def __init__(
        self,
        job_status: str = None,
        request_id: str = None,
        results: main_models.QueryVideoCognitionJobResponseBodyResults = None,
        user_data: str = None,
    ):
        # The status of the task. Valid values:
        # 
        # *   **Success**
        # *   **Fail**
        # *   **Processing**
        # *   **Submitted**
        self.job_status = job_status
        # The request ID.
        self.request_id = request_id
        # An array of analysis result objects.
        self.results = results
        # The user-defined data.
        self.user_data = user_data

    def validate(self):
        if self.results:
            self.results.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_status is not None:
            result['JobStatus'] = self.job_status

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.results is not None:
            result['Results'] = self.results.to_map()

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobStatus') is not None:
            self.job_status = m.get('JobStatus')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Results') is not None:
            temp_model = main_models.QueryVideoCognitionJobResponseBodyResults()
            self.results = temp_model.from_map(m.get('Results'))

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
        # A JSON string containing the detailed analysis data. The structure of this data depends on the Type field. For details, see the Result parameters section below.
        self.data = data
        # The type of analysis result. Valid values:
        # 
        # 1.  TextLabel: Tags from text content.
        # 2.  VideoLabel: Tags from video content.
        # 3.  ASR: Raw speech recognition results. Not returned by default.
        # 4.  OCR: Raw text recognition results. Not returned by default.
        # 5.  NLP: Natural Language Processing results. Not returned by default.
        # 6.  Process: URL to the raw algorithm output. Not returned by default.
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

