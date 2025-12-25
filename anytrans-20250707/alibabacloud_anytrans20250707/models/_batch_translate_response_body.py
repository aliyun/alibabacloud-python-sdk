# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_anytrans20250707 import models as main_models
from darabonba.model import DaraModel

class BatchTranslateResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.BatchTranslateResponseBodyData = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.BatchTranslateResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class BatchTranslateResponseBodyData(DaraModel):
    def __init__(
        self,
        translation_list: List[main_models.BatchTranslateResponseBodyDataTranslationList] = None,
    ):
        self.translation_list = translation_list

    def validate(self):
        if self.translation_list:
            for v1 in self.translation_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['translationList'] = []
        if self.translation_list is not None:
            for k1 in self.translation_list:
                result['translationList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.translation_list = []
        if m.get('translationList') is not None:
            for k1 in m.get('translationList'):
                temp_model = main_models.BatchTranslateResponseBodyDataTranslationList()
                self.translation_list.append(temp_model.from_map(k1))

        return self

class BatchTranslateResponseBodyDataTranslationList(DaraModel):
    def __init__(
        self,
        code: int = None,
        index: str = None,
        message: str = None,
        translation: str = None,
        usage: main_models.BatchTranslateResponseBodyDataTranslationListUsage = None,
    ):
        self.code = code
        self.index = index
        self.message = message
        self.translation = translation
        self.usage = usage

    def validate(self):
        if self.usage:
            self.usage.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.index is not None:
            result['index'] = self.index

        if self.message is not None:
            result['message'] = self.message

        if self.translation is not None:
            result['translation'] = self.translation

        if self.usage is not None:
            result['usage'] = self.usage.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('index') is not None:
            self.index = m.get('index')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('translation') is not None:
            self.translation = m.get('translation')

        if m.get('usage') is not None:
            temp_model = main_models.BatchTranslateResponseBodyDataTranslationListUsage()
            self.usage = temp_model.from_map(m.get('usage'))

        return self

class BatchTranslateResponseBodyDataTranslationListUsage(DaraModel):
    def __init__(
        self,
        input_tokens: int = None,
        output_tokens: int = None,
        total_tokens: int = None,
    ):
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens
        self.total_tokens = total_tokens

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_tokens is not None:
            result['inputTokens'] = self.input_tokens

        if self.output_tokens is not None:
            result['outputTokens'] = self.output_tokens

        if self.total_tokens is not None:
            result['totalTokens'] = self.total_tokens

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('inputTokens') is not None:
            self.input_tokens = m.get('inputTokens')

        if m.get('outputTokens') is not None:
            self.output_tokens = m.get('outputTokens')

        if m.get('totalTokens') is not None:
            self.total_tokens = m.get('totalTokens')

        return self

