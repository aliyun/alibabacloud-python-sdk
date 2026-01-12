# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_green20220302 import models as main_models
from darabonba.model import DaraModel

class MultiModalAgentResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.MultiModalAgentResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
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
            temp_model = main_models.MultiModalAgentResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class MultiModalAgentResponseBodyData(DaraModel):
    def __init__(
        self,
        data_id: str = None,
        result: List[main_models.MultiModalAgentResponseBodyDataResult] = None,
        risk_level: str = None,
        usage: main_models.MultiModalAgentResponseBodyDataUsage = None,
    ):
        self.data_id = data_id
        self.result = result
        self.risk_level = risk_level
        self.usage = usage

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()
        if self.usage:
            self.usage.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_id is not None:
            result['DataId'] = self.data_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.usage is not None:
            result['Usage'] = self.usage.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.MultiModalAgentResponseBodyDataResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('Usage') is not None:
            temp_model = main_models.MultiModalAgentResponseBodyDataUsage()
            self.usage = temp_model.from_map(m.get('Usage'))

        return self

class MultiModalAgentResponseBodyDataUsage(DaraModel):
    def __init__(
        self,
        agent_detail: Dict[str, Any] = None,
        content_length: int = None,
        prompt_length: int = None,
    ):
        self.agent_detail = agent_detail
        self.content_length = content_length
        self.prompt_length = prompt_length

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_detail is not None:
            result['AgentDetail'] = self.agent_detail

        if self.content_length is not None:
            result['ContentLength'] = self.content_length

        if self.prompt_length is not None:
            result['PromptLength'] = self.prompt_length

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentDetail') is not None:
            self.agent_detail = m.get('AgentDetail')

        if m.get('ContentLength') is not None:
            self.content_length = m.get('ContentLength')

        if m.get('PromptLength') is not None:
            self.prompt_length = m.get('PromptLength')

        return self

class MultiModalAgentResponseBodyDataResult(DaraModel):
    def __init__(
        self,
        description: str = None,
        label: str = None,
        reason: str = None,
    ):
        self.description = description
        self.label = label
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.label is not None:
            result['Label'] = self.label

        if self.reason is not None:
            result['Reason'] = self.reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        return self

