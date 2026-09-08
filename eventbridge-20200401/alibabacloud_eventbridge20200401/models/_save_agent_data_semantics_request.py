# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class SaveAgentDataSemanticsRequest(DaraModel):
    def __init__(
        self,
        agent_name: str = None,
        examples: List[main_models.AgentDataSemanticsExample] = None,
        joins: List[main_models.AgentDataSemanticsJoin] = None,
        metrics: List[main_models.AgentDataSemanticsMetric] = None,
        text: main_models.AgentDataSemanticsText = None,
    ):
        # The name of the agent.
        # 
        # This parameter is required.
        self.agent_name = agent_name
        # The SQL example knowledge. If this parameter is specified, the current content is saved. If this parameter is not specified, the existing content is cleared. A maximum of 50 entries are supported, and the maximum size of each knowledge category is 16 KB.
        self.examples = examples
        # The data association knowledge. If this parameter is specified, the current content is saved. If this parameter is not specified, the existing content is cleared. A maximum of 100 entries are supported, and the maximum size of each knowledge category is 16 KB.
        self.joins = joins
        # The SQL expression knowledge. If this parameter is specified, the current content is saved. If this parameter is not specified, the existing content is cleared. A maximum of 100 entries are supported, and the maximum size of each knowledge category is 16 KB.
        self.metrics = metrics
        # The text knowledge in Markdown format. If this parameter is specified, the current content is saved. If this parameter is not specified, the existing content is cleared. The maximum size of each knowledge category is 16 KB.
        self.text = text

    def validate(self):
        if self.examples:
            for v1 in self.examples:
                 if v1:
                    v1.validate()
        if self.joins:
            for v1 in self.joins:
                 if v1:
                    v1.validate()
        if self.metrics:
            for v1 in self.metrics:
                 if v1:
                    v1.validate()
        if self.text:
            self.text.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_name is not None:
            result['AgentName'] = self.agent_name

        result['Examples'] = []
        if self.examples is not None:
            for k1 in self.examples:
                result['Examples'].append(k1.to_map() if k1 else None)

        result['Joins'] = []
        if self.joins is not None:
            for k1 in self.joins:
                result['Joins'].append(k1.to_map() if k1 else None)

        result['Metrics'] = []
        if self.metrics is not None:
            for k1 in self.metrics:
                result['Metrics'].append(k1.to_map() if k1 else None)

        if self.text is not None:
            result['Text'] = self.text.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')

        self.examples = []
        if m.get('Examples') is not None:
            for k1 in m.get('Examples'):
                temp_model = main_models.AgentDataSemanticsExample()
                self.examples.append(temp_model.from_map(k1))

        self.joins = []
        if m.get('Joins') is not None:
            for k1 in m.get('Joins'):
                temp_model = main_models.AgentDataSemanticsJoin()
                self.joins.append(temp_model.from_map(k1))

        self.metrics = []
        if m.get('Metrics') is not None:
            for k1 in m.get('Metrics'):
                temp_model = main_models.AgentDataSemanticsMetric()
                self.metrics.append(temp_model.from_map(k1))

        if m.get('Text') is not None:
            temp_model = main_models.AgentDataSemanticsText()
            self.text = temp_model.from_map(m.get('Text'))

        return self

