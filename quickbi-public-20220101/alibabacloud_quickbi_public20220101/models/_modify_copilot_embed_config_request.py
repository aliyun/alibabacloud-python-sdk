# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyCopilotEmbedConfigRequest(DaraModel):
    def __init__(
        self,
        agent_name: str = None,
        copilot_id: str = None,
        data_range: str = None,
        module_name: str = None,
    ):
        # Agent nickname.
        self.agent_name = agent_name
        # Embedding ID.
        # 
        # This parameter is required.
        self.copilot_id = copilot_id
        # Data range.
        # >Notice: The parameter type is jsonString, and only one switch between analysis themes and query resources can be effective. When the all-select switch is true, it takes precedence. It is recommended to pass only one parameter, with other notes
        self.data_range = data_range
        # Module name.
        self.module_name = module_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_name is not None:
            result['AgentName'] = self.agent_name

        if self.copilot_id is not None:
            result['CopilotId'] = self.copilot_id

        if self.data_range is not None:
            result['DataRange'] = self.data_range

        if self.module_name is not None:
            result['ModuleName'] = self.module_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')

        if m.get('CopilotId') is not None:
            self.copilot_id = m.get('CopilotId')

        if m.get('DataRange') is not None:
            self.data_range = m.get('DataRange')

        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')

        return self

