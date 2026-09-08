# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SaveAgentDataSemanticsShrinkRequest(DaraModel):
    def __init__(
        self,
        agent_name: str = None,
        examples_shrink: str = None,
        joins_shrink: str = None,
        metrics_shrink: str = None,
        text_shrink: str = None,
    ):
        # The name of the agent.
        # 
        # This parameter is required.
        self.agent_name = agent_name
        # The SQL example knowledge. If this parameter is specified, the current content is saved. If this parameter is not specified, the existing content is cleared. A maximum of 50 entries are supported, and the maximum size of each knowledge category is 16 KB.
        self.examples_shrink = examples_shrink
        # The data association knowledge. If this parameter is specified, the current content is saved. If this parameter is not specified, the existing content is cleared. A maximum of 100 entries are supported, and the maximum size of each knowledge category is 16 KB.
        self.joins_shrink = joins_shrink
        # The SQL expression knowledge. If this parameter is specified, the current content is saved. If this parameter is not specified, the existing content is cleared. A maximum of 100 entries are supported, and the maximum size of each knowledge category is 16 KB.
        self.metrics_shrink = metrics_shrink
        # The text knowledge in Markdown format. If this parameter is specified, the current content is saved. If this parameter is not specified, the existing content is cleared. The maximum size of each knowledge category is 16 KB.
        self.text_shrink = text_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_name is not None:
            result['AgentName'] = self.agent_name

        if self.examples_shrink is not None:
            result['Examples'] = self.examples_shrink

        if self.joins_shrink is not None:
            result['Joins'] = self.joins_shrink

        if self.metrics_shrink is not None:
            result['Metrics'] = self.metrics_shrink

        if self.text_shrink is not None:
            result['Text'] = self.text_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')

        if m.get('Examples') is not None:
            self.examples_shrink = m.get('Examples')

        if m.get('Joins') is not None:
            self.joins_shrink = m.get('Joins')

        if m.get('Metrics') is not None:
            self.metrics_shrink = m.get('Metrics')

        if m.get('Text') is not None:
            self.text_shrink = m.get('Text')

        return self

