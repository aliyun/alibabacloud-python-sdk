# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_green20220302 import multi_modal_guard_ws_models as main_models
from darabonba.model import DaraModel

class ResponseMessageEvent(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: main_models.ResponseMessageEventData = None,
    ):
        self.code = code
        self.message = message
        self.data = data

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

        if self.message is not None:
            result['Message'] = self.message

        if self.data is not None:
            result['Data'] = self.data.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Data') is not None:
            temp_model = main_models.ResponseMessageEventData()
            self.data = temp_model.from_map(m.get('Data'))

        return self

class ResponseMessageEventData(DaraModel):
    def __init__(
        self,
        detail: List[main_models.ResponseMessageEventDataDetail] = None,
        suggestion: str = None,
        data_id: str = None,
        seq_list: List[str] = None,
    ):
        self.detail = detail
        self.suggestion = suggestion
        self.data_id = data_id
        self.seq_list = seq_list

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
        result['Detail'] = []
        if self.detail is not None:
            for k1 in self.detail:
                result['Detail'].append(k1.to_map() if k1 else None)

        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion

        if self.data_id is not None:
            result['DataId'] = self.data_id

        if self.seq_list is not None:
            result['SeqList'] = self.seq_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detail = []
        if m.get('Detail') is not None:
            for k1 in m.get('Detail'):
                temp_model = main_models.ResponseMessageEventDataDetail()
                self.detail.append(temp_model.from_map(k1))

        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')

        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')

        if m.get('SeqList') is not None:
            self.seq_list = m.get('SeqList')

        return self

class ResponseMessageEventDataDetail(DaraModel):
    def __init__(
        self,
        result: List[main_models.ResponseMessageEventDataDetailResult] = None,
        type: str = None,
        level: str = None,
        suggestion: str = None,
    ):
        self.result = result
        self.type = type
        self.level = level
        self.suggestion = suggestion

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
        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        if self.level is not None:
            result['Level'] = self.level

        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ResponseMessageEventDataDetailResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')

        return self

class ResponseMessageEventDataDetailResult(DaraModel):
    def __init__(
        self,
        label: str = None,
        description: str = None,
        confidence: float = None,
        level: str = None,
        ext: Any = None,
    ):
        self.label = label
        self.description = description
        self.confidence = confidence
        self.level = level
        self.ext = ext

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label is not None:
            result['Label'] = self.label

        if self.description is not None:
            result['Description'] = self.description

        if self.confidence is not None:
            result['Confidence'] = self.confidence

        if self.level is not None:
            result['Level'] = self.level

        if self.ext is not None:
            result['Ext'] = self.ext

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Ext') is not None:
            self.ext = m.get('Ext')

        return self

