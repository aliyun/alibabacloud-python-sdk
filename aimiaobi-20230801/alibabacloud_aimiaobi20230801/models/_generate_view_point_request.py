# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class GenerateViewPointRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        reference_data: main_models.GenerateViewPointRequestReferenceData = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.reference_data = reference_data

    def validate(self):
        if self.reference_data:
            self.reference_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.reference_data is not None:
            result['ReferenceData'] = self.reference_data.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('ReferenceData') is not None:
            temp_model = main_models.GenerateViewPointRequestReferenceData()
            self.reference_data = temp_model.from_map(m.get('ReferenceData'))

        return self

class GenerateViewPointRequestReferenceData(DaraModel):
    def __init__(
        self,
        mini_doc: List[str] = None,
    ):
        self.mini_doc = mini_doc

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mini_doc is not None:
            result['MiniDoc'] = self.mini_doc

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MiniDoc') is not None:
            self.mini_doc = m.get('MiniDoc')

        return self

