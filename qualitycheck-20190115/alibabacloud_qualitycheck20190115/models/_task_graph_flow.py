# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_qualitycheck20190115 import models as main_models
from darabonba.model import DaraModel

class TaskGraphFlow(DaraModel):
    def __init__(
        self,
        flow_rule_score_type: int = None,
        id: int = None,
        nodes: List[main_models.GraphFlowNode] = None,
        rid: int = None,
        rule_name: str = None,
        show_properties: str = None,
        skip_when_first_session_node_miss: bool = None,
    ):
        self.flow_rule_score_type = flow_rule_score_type
        self.id = id
        self.nodes = nodes
        self.rid = rid
        self.rule_name = rule_name
        self.show_properties = show_properties
        self.skip_when_first_session_node_miss = skip_when_first_session_node_miss

    def validate(self):
        if self.nodes:
            for v1 in self.nodes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.flow_rule_score_type is not None:
            result['FlowRuleScoreType'] = self.flow_rule_score_type

        if self.id is not None:
            result['Id'] = self.id

        result['Nodes'] = []
        if self.nodes is not None:
            for k1 in self.nodes:
                result['Nodes'].append(k1.to_map() if k1 else None)

        if self.rid is not None:
            result['Rid'] = self.rid

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.show_properties is not None:
            result['ShowProperties'] = self.show_properties

        if self.skip_when_first_session_node_miss is not None:
            result['SkipWhenFirstSessionNodeMiss'] = self.skip_when_first_session_node_miss

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowRuleScoreType') is not None:
            self.flow_rule_score_type = m.get('FlowRuleScoreType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        self.nodes = []
        if m.get('Nodes') is not None:
            for k1 in m.get('Nodes'):
                temp_model = main_models.GraphFlowNode()
                self.nodes.append(temp_model.from_map(k1))

        if m.get('Rid') is not None:
            self.rid = m.get('Rid')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('ShowProperties') is not None:
            self.show_properties = m.get('ShowProperties')

        if m.get('SkipWhenFirstSessionNodeMiss') is not None:
            self.skip_when_first_session_node_miss = m.get('SkipWhenFirstSessionNodeMiss')

        return self

