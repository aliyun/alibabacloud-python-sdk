# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_qualitycheck20190115 import models as main_models
from darabonba.model import DaraModel

class VerifySentenceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.VerifySentenceResponseBodyData = None,
        incorrect_words: int = None,
        message: str = None,
        request_id: str = None,
        source_role: int = None,
        success: bool = None,
        target_role: int = None,
    ):
        self.code = code
        self.data = data
        self.incorrect_words = incorrect_words
        self.message = message
        self.request_id = request_id
        self.source_role = source_role
        self.success = success
        self.target_role = target_role

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

        if self.incorrect_words is not None:
            result['IncorrectWords'] = self.incorrect_words

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.source_role is not None:
            result['SourceRole'] = self.source_role

        if self.success is not None:
            result['Success'] = self.success

        if self.target_role is not None:
            result['TargetRole'] = self.target_role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.VerifySentenceResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('IncorrectWords') is not None:
            self.incorrect_words = m.get('IncorrectWords')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SourceRole') is not None:
            self.source_role = m.get('SourceRole')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TargetRole') is not None:
            self.target_role = m.get('TargetRole')

        return self

class VerifySentenceResponseBodyData(DaraModel):
    def __init__(
        self,
        delta: List[main_models.VerifySentenceResponseBodyDataDelta] = None,
    ):
        self.delta = delta

    def validate(self):
        if self.delta:
            for v1 in self.delta:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Delta'] = []
        if self.delta is not None:
            for k1 in self.delta:
                result['Delta'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.delta = []
        if m.get('Delta') is not None:
            for k1 in m.get('Delta'):
                temp_model = main_models.VerifySentenceResponseBodyDataDelta()
                self.delta.append(temp_model.from_map(k1))

        return self

class VerifySentenceResponseBodyDataDelta(DaraModel):
    def __init__(
        self,
        source: main_models.VerifySentenceResponseBodyDataDeltaSource = None,
        target: main_models.VerifySentenceResponseBodyDataDeltaTarget = None,
        type: str = None,
    ):
        self.source = source
        self.target = target
        self.type = type

    def validate(self):
        if self.source:
            self.source.validate()
        if self.target:
            self.target.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.source is not None:
            result['Source'] = self.source.to_map()

        if self.target is not None:
            result['Target'] = self.target.to_map()

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Source') is not None:
            temp_model = main_models.VerifySentenceResponseBodyDataDeltaSource()
            self.source = temp_model.from_map(m.get('Source'))

        if m.get('Target') is not None:
            temp_model = main_models.VerifySentenceResponseBodyDataDeltaTarget()
            self.target = temp_model.from_map(m.get('Target'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class VerifySentenceResponseBodyDataDeltaTarget(DaraModel):
    def __init__(
        self,
        line: main_models.VerifySentenceResponseBodyDataDeltaTargetLine = None,
        position: int = None,
    ):
        self.line = line
        self.position = position

    def validate(self):
        if self.line:
            self.line.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.line is not None:
            result['Line'] = self.line.to_map()

        if self.position is not None:
            result['Position'] = self.position

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Line') is not None:
            temp_model = main_models.VerifySentenceResponseBodyDataDeltaTargetLine()
            self.line = temp_model.from_map(m.get('Line'))

        if m.get('Position') is not None:
            self.position = m.get('Position')

        return self

class VerifySentenceResponseBodyDataDeltaTargetLine(DaraModel):
    def __init__(
        self,
        line: List[str] = None,
    ):
        self.line = line

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.line is not None:
            result['Line'] = self.line

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Line') is not None:
            self.line = m.get('Line')

        return self

class VerifySentenceResponseBodyDataDeltaSource(DaraModel):
    def __init__(
        self,
        line: main_models.VerifySentenceResponseBodyDataDeltaSourceLine = None,
        position: int = None,
    ):
        self.line = line
        self.position = position

    def validate(self):
        if self.line:
            self.line.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.line is not None:
            result['Line'] = self.line.to_map()

        if self.position is not None:
            result['Position'] = self.position

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Line') is not None:
            temp_model = main_models.VerifySentenceResponseBodyDataDeltaSourceLine()
            self.line = temp_model.from_map(m.get('Line'))

        if m.get('Position') is not None:
            self.position = m.get('Position')

        return self

class VerifySentenceResponseBodyDataDeltaSourceLine(DaraModel):
    def __init__(
        self,
        line: List[str] = None,
    ):
        self.line = line

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.line is not None:
            result['Line'] = self.line

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Line') is not None:
            self.line = m.get('Line')

        return self

