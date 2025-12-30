# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class QueryVideoCognitionJobRequest(DaraModel):
    def __init__(
        self,
        include_results: main_models.QueryVideoCognitionJobRequestIncludeResults = None,
        job_id: str = None,
        params: str = None,
    ):
        # Specifies whether to include the full algorithm results in the response.
        self.include_results = include_results
        # The ID of the task to query. It is returned when you call the [SubmitSmarttagJob](https://help.aliyun.com/document_detail/478786.html) operation.
        # 
        # This parameter is required.
        self.job_id = job_id
        # Additional request parameters, provided as a JSON string.
        self.params = params

    def validate(self):
        if self.include_results:
            self.include_results.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.include_results is not None:
            result['IncludeResults'] = self.include_results.to_map()

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.params is not None:
            result['Params'] = self.params

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IncludeResults') is not None:
            temp_model = main_models.QueryVideoCognitionJobRequestIncludeResults()
            self.include_results = temp_model.from_map(m.get('IncludeResults'))

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        return self

class QueryVideoCognitionJobRequestIncludeResults(DaraModel):
    def __init__(
        self,
        need_asr: bool = None,
        need_ocr: bool = None,
        need_process: bool = None,
    ):
        # Specifies whether to include Automatic Speech Recognition (ASR) results.
        self.need_asr = need_asr
        # Specifies whether to include Optical Character Recognition (OCR) results.
        self.need_ocr = need_ocr
        # Specifies whether to include the URL to the raw output of the algorithm.
        self.need_process = need_process

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.need_asr is not None:
            result['NeedAsr'] = self.need_asr

        if self.need_ocr is not None:
            result['NeedOcr'] = self.need_ocr

        if self.need_process is not None:
            result['NeedProcess'] = self.need_process

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NeedAsr') is not None:
            self.need_asr = m.get('NeedAsr')

        if m.get('NeedOcr') is not None:
            self.need_ocr = m.get('NeedOcr')

        if m.get('NeedProcess') is not None:
            self.need_process = m.get('NeedProcess')

        return self

