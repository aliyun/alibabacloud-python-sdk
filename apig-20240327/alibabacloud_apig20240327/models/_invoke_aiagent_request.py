# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class InvokeAIAgentRequest(DaraModel):
    def __init__(
        self,
        agent_name: str = None,
        biz_params: Dict[str, str] = None,
        history: List[main_models.InvokeAIAgentRequestHistory] = None,
        output_language: str = None,
        prompt: str = None,
    ):
        # This parameter is required.
        self.agent_name = agent_name
        self.biz_params = biz_params
        self.history = history
        self.output_language = output_language
        self.prompt = prompt

    def validate(self):
        if self.history:
            for v1 in self.history:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_name is not None:
            result['agentName'] = self.agent_name

        if self.biz_params is not None:
            result['bizParams'] = self.biz_params

        result['history'] = []
        if self.history is not None:
            for k1 in self.history:
                result['history'].append(k1.to_map() if k1 else None)

        if self.output_language is not None:
            result['outputLanguage'] = self.output_language

        if self.prompt is not None:
            result['prompt'] = self.prompt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentName') is not None:
            self.agent_name = m.get('agentName')

        if m.get('bizParams') is not None:
            self.biz_params = m.get('bizParams')

        self.history = []
        if m.get('history') is not None:
            for k1 in m.get('history'):
                temp_model = main_models.InvokeAIAgentRequestHistory()
                self.history.append(temp_model.from_map(k1))

        if m.get('outputLanguage') is not None:
            self.output_language = m.get('outputLanguage')

        if m.get('prompt') is not None:
            self.prompt = m.get('prompt')

        return self

class InvokeAIAgentRequestHistory(DaraModel):
    def __init__(
        self,
        content: str = None,
        role: str = None,
    ):
        self.content = content
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.role is not None:
            result['role'] = self.role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('role') is not None:
            self.role = m.get('role')

        return self

