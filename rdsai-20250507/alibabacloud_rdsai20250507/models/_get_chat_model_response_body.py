# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rdsai20250507 import models as main_models
from darabonba.model import DaraModel

class GetChatModelResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.GetChatModelResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetChatModelResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetChatModelResponseBodyData(DaraModel):
    def __init__(
        self,
        context_window: int = None,
        default: bool = None,
        features: List[str] = None,
        model_id: str = None,
        thinking_levels: List[str] = None,
    ):
        self.context_window = context_window
        self.default = default
        self.features = features
        self.model_id = model_id
        self.thinking_levels = thinking_levels

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.context_window is not None:
            result['ContextWindow'] = self.context_window

        if self.default is not None:
            result['Default'] = self.default

        if self.features is not None:
            result['Features'] = self.features

        if self.model_id is not None:
            result['ModelId'] = self.model_id

        if self.thinking_levels is not None:
            result['ThinkingLevels'] = self.thinking_levels

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContextWindow') is not None:
            self.context_window = m.get('ContextWindow')

        if m.get('Default') is not None:
            self.default = m.get('Default')

        if m.get('Features') is not None:
            self.features = m.get('Features')

        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')

        if m.get('ThinkingLevels') is not None:
            self.thinking_levels = m.get('ThinkingLevels')

        return self

