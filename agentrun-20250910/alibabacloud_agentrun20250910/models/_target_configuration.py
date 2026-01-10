# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class TargetConfiguration(DaraModel):
    def __init__(
        self,
        llm_apiconfig: main_models.LLMAPIConfiguration = None,
        mcp_apiconfig: main_models.MCPAPIConfiguration = None,
        target_type: str = None,
    ):
        self.llm_apiconfig = llm_apiconfig
        self.mcp_apiconfig = mcp_apiconfig
        self.target_type = target_type

    def validate(self):
        if self.llm_apiconfig:
            self.llm_apiconfig.validate()
        if self.mcp_apiconfig:
            self.mcp_apiconfig.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.llm_apiconfig is not None:
            result['llmAPIConfig'] = self.llm_apiconfig.to_map()

        if self.mcp_apiconfig is not None:
            result['mcpAPIConfig'] = self.mcp_apiconfig.to_map()

        if self.target_type is not None:
            result['targetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('llmAPIConfig') is not None:
            temp_model = main_models.LLMAPIConfiguration()
            self.llm_apiconfig = temp_model.from_map(m.get('llmAPIConfig'))

        if m.get('mcpAPIConfig') is not None:
            temp_model = main_models.MCPAPIConfiguration()
            self.mcp_apiconfig = temp_model.from_map(m.get('mcpAPIConfig'))

        if m.get('targetType') is not None:
            self.target_type = m.get('targetType')

        return self

