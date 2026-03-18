# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aicontent20240611 import models as main_models
from darabonba.model import DaraModel

class ExecuteTextbookAssistantSuggestionResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ExecuteTextbookAssistantSuggestionResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        httpstatus_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.httpstatus_code = httpstatus_code
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

        if self.httpstatus_code is not None:
            result['httpstatusCode'] = self.httpstatus_code

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.ExecuteTextbookAssistantSuggestionResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')

        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')

        if m.get('httpstatusCode') is not None:
            self.httpstatus_code = m.get('httpstatusCode')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class ExecuteTextbookAssistantSuggestionResponseBodyData(DaraModel):
    def __init__(
        self,
        result: main_models.ExecuteTextbookAssistantSuggestionResponseBodyDataResult = None,
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
            temp_model = main_models.ExecuteTextbookAssistantSuggestionResponseBodyDataResult()
            self.result = temp_model.from_map(m.get('result'))

        return self

class ExecuteTextbookAssistantSuggestionResponseBodyDataResult(DaraModel):
    def __init__(
        self,
        chinese_result: str = None,
        english_result: str = None,
    ):
        self.chinese_result = chinese_result
        self.english_result = english_result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chinese_result is not None:
            result['chineseResult'] = self.chinese_result

        if self.english_result is not None:
            result['englishResult'] = self.english_result

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chineseResult') is not None:
            self.chinese_result = m.get('chineseResult')

        if m.get('englishResult') is not None:
            self.english_result = m.get('englishResult')

        return self

