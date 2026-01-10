# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class Target(DaraModel):
    def __init__(
        self,
        llm_config: main_models.LLMAPIConfiguration = None,
        mcp_api: main_models.MCPAPI = None,
        target_type: str = None,
    ):
        self.llm_config = llm_config
        self.mcp_api = mcp_api
        self.target_type = target_type

    def validate(self):
        if self.llm_config:
            self.llm_config.validate()
        if self.mcp_api:
            self.mcp_api.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.llm_config is not None:
            result['llmConfig'] = self.llm_config.to_map()

        if self.mcp_api is not None:
            result['mcpAPI'] = self.mcp_api.to_map()

        if self.target_type is not None:
            result['targetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('llmConfig') is not None:
            temp_model = main_models.LLMAPIConfiguration()
            self.llm_config = temp_model.from_map(m.get('llmConfig'))

        if m.get('mcpAPI') is not None:
            temp_model = main_models.MCPAPI()
            self.mcp_api = temp_model.from_map(m.get('mcpAPI'))

        if m.get('targetType') is not None:
            self.target_type = m.get('targetType')

        return self

