# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_green20220302 import models as main_models
from darabonba.model import DaraModel

class MultiModalGuardResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.MultiModalGuardResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.MultiModalGuardResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class MultiModalGuardResponseBodyData(DaraModel):
    def __init__(
        self,
        data_id: str = None,
        detail: List[main_models.MultiModalGuardResponseBodyDataDetail] = None,
        suggestion: str = None,
    ):
        self.data_id = data_id
        self.detail = detail
        self.suggestion = suggestion

    def validate(self):
        if self.detail:
            for v1 in self.detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_id is not None:
            result['DataId'] = self.data_id

        result['Detail'] = []
        if self.detail is not None:
            for k1 in self.detail:
                result['Detail'].append(k1.to_map() if k1 else None)

        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')

        self.detail = []
        if m.get('Detail') is not None:
            for k1 in m.get('Detail'):
                temp_model = main_models.MultiModalGuardResponseBodyDataDetail()
                self.detail.append(temp_model.from_map(k1))

        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')

        return self

class MultiModalGuardResponseBodyDataDetail(DaraModel):
    def __init__(
        self,
        level: str = None,
        result: List[main_models.MultiModalGuardResponseBodyDataDetailResult] = None,
        suggestion: str = None,
        type: str = None,
    ):
        self.level = level
        self.result = result
        self.suggestion = suggestion
        self.type = type

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
        if self.level is not None:
            result['Level'] = self.level

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Level') is not None:
            self.level = m.get('Level')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.MultiModalGuardResponseBodyDataDetailResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class MultiModalGuardResponseBodyDataDetailResult(DaraModel):
    def __init__(
        self,
        confidence: float = None,
        description: str = None,
        ext: Any = None,
        label: str = None,
        level: str = None,
    ):
        self.confidence = confidence
        self.description = description
        self.ext = ext
        self.label = label
        self.level = level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.confidence is not None:
            result['Confidence'] = self.confidence

        if self.description is not None:
            result['Description'] = self.description

        if self.ext is not None:
            result['Ext'] = self.ext

        if self.label is not None:
            result['Label'] = self.label

        if self.level is not None:
            result['Level'] = self.level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Ext') is not None:
            self.ext = m.get('Ext')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        return self

