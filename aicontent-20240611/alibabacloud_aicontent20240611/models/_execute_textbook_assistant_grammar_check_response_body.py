# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aicontent20240611 import models as main_models
from darabonba.model import DaraModel

class ExecuteTextbookAssistantGrammarCheckResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ExecuteTextbookAssistantGrammarCheckResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.err_code is not None:
            result['errCode'] = self.err_code

        if self.err_message is not None:
            result['errMessage'] = self.err_message

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.ExecuteTextbookAssistantGrammarCheckResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')

        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class ExecuteTextbookAssistantGrammarCheckResponseBodyData(DaraModel):
    def __init__(
        self,
        result: main_models.ExecuteTextbookAssistantGrammarCheckResponseBodyDataResult = None,
    ):
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.result is not None:
            result['result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = main_models.ExecuteTextbookAssistantGrammarCheckResponseBodyDataResult()
            self.result = temp_model.from_map(m.get('result'))

        return self

class ExecuteTextbookAssistantGrammarCheckResponseBodyDataResult(DaraModel):
    def __init__(
        self,
        analysis: str = None,
        correction: str = None,
        correction_status: str = None,
    ):
        self.analysis = analysis
        self.correction = correction
        self.correction_status = correction_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.analysis is not None:
            result['analysis'] = self.analysis

        if self.correction is not None:
            result['correction'] = self.correction

        if self.correction_status is not None:
            result['correctionStatus'] = self.correction_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analysis') is not None:
            self.analysis = m.get('analysis')

        if m.get('correction') is not None:
            self.correction = m.get('correction')

        if m.get('correctionStatus') is not None:
            self.correction_status = m.get('correctionStatus')

        return self

