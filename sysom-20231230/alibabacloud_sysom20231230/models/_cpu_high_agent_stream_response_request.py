# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CpuHighAgentStreamResponseRequest(DaraModel):
    def __init__(
        self,
        llm_param_string: str = None,
    ):
        # Input parameter for interfacing with the high-CPU agent service. Refer to the standard LLM API input parameter dictionary, convert it into a string, and pass it in the `llmParamString` field.
        self.llm_param_string = llm_param_string

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.llm_param_string is not None:
            result['llmParamString'] = self.llm_param_string

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('llmParamString') is not None:
            self.llm_param_string = m.get('llmParamString')

        return self

