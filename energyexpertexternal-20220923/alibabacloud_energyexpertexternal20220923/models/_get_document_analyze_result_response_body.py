# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_energyexpertexternal20220923 import models as main_models
from darabonba.model import DaraModel

class GetDocumentAnalyzeResultResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetDocumentAnalyzeResultResponseBodyData = None,
        request_id: str = None,
    ):
        # Returned Data
        self.data = data
        # Request ID
        self.request_id = request_id

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

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.GetDocumentAnalyzeResultResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetDocumentAnalyzeResultResponseBodyData(DaraModel):
    def __init__(
        self,
        kv_list_info: List[main_models.GetDocumentAnalyzeResultResponseBodyDataKvListInfo] = None,
    ):
        # Document Parsing Result
        self.kv_list_info = kv_list_info

    def validate(self):
        if self.kv_list_info:
            for v1 in self.kv_list_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['kvListInfo'] = []
        if self.kv_list_info is not None:
            for k1 in self.kv_list_info:
                result['kvListInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.kv_list_info = []
        if m.get('kvListInfo') is not None:
            for k1 in m.get('kvListInfo'):
                temp_model = main_models.GetDocumentAnalyzeResultResponseBodyDataKvListInfo()
                self.kv_list_info.append(temp_model.from_map(k1))

        return self

class GetDocumentAnalyzeResultResponseBodyDataKvListInfo(DaraModel):
    def __init__(
        self,
        context: main_models.GetDocumentAnalyzeResultResponseBodyDataKvListInfoContext = None,
        key_name: str = None,
        key_value: str = None,
    ):
        # Recalled Content
        self.context = context
        # Field Key Name
        self.key_name = key_name
        # Field Key Value
        self.key_value = key_value

    def validate(self):
        if self.context:
            self.context.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.context is not None:
            result['context'] = self.context.to_map()

        if self.key_name is not None:
            result['keyName'] = self.key_name

        if self.key_value is not None:
            result['keyValue'] = self.key_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('context') is not None:
            temp_model = main_models.GetDocumentAnalyzeResultResponseBodyDataKvListInfoContext()
            self.context = temp_model.from_map(m.get('context'))

        if m.get('keyName') is not None:
            self.key_name = m.get('keyName')

        if m.get('keyValue') is not None:
            self.key_value = m.get('keyValue')

        return self

class GetDocumentAnalyzeResultResponseBodyDataKvListInfoContext(DaraModel):
    def __init__(
        self,
        confidence: main_models.GetDocumentAnalyzeResultResponseBodyDataKvListInfoContextConfidence = None,
        key: List[main_models.ContentItem] = None,
        value: List[main_models.ContentItem] = None,
    ):
        # Confidence
        self.confidence = confidence
        # Key Recall Information
        self.key = key
        # Value Recall Information
        self.value = value

    def validate(self):
        if self.confidence:
            self.confidence.validate()
        if self.key:
            for v1 in self.key:
                 if v1:
                    v1.validate()
        if self.value:
            for v1 in self.value:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.confidence is not None:
            result['confidence'] = self.confidence.to_map()

        result['key'] = []
        if self.key is not None:
            for k1 in self.key:
                result['key'].append(k1.to_map() if k1 else None)

        result['value'] = []
        if self.value is not None:
            for k1 in self.value:
                result['value'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('confidence') is not None:
            temp_model = main_models.GetDocumentAnalyzeResultResponseBodyDataKvListInfoContextConfidence()
            self.confidence = temp_model.from_map(m.get('confidence'))

        self.key = []
        if m.get('key') is not None:
            for k1 in m.get('key'):
                temp_model = main_models.ContentItem()
                self.key.append(temp_model.from_map(k1))

        self.value = []
        if m.get('value') is not None:
            for k1 in m.get('value'):
                temp_model = main_models.ContentItem()
                self.value.append(temp_model.from_map(k1))

        return self

class GetDocumentAnalyzeResultResponseBodyDataKvListInfoContextConfidence(DaraModel):
    def __init__(
        self,
        key_confidence: float = None,
        value_confidence: float = None,
    ):
        # Confidence of Key
        self.key_confidence = key_confidence
        # Confidence of Value
        self.value_confidence = value_confidence

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key_confidence is not None:
            result['keyConfidence'] = self.key_confidence

        if self.value_confidence is not None:
            result['valueConfidence'] = self.value_confidence

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyConfidence') is not None:
            self.key_confidence = m.get('keyConfidence')

        if m.get('valueConfidence') is not None:
            self.value_confidence = m.get('valueConfidence')

        return self

