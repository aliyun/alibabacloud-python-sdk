# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_qualitycheck20190115 import models as main_models
from darabonba.model import DaraModel

class GraphFlowNode(DaraModel):
    def __init__(
        self,
        conditions: List[main_models.ConditionBasicInfo] = None,
        content: str = None,
        id: int = None,
        index: int = None,
        name: str = None,
        next_nodes: List[main_models.GraphFlowNodeNextNodes] = None,
        node_type: str = None,
        properties: main_models.GraphFlowNodeProperties = None,
        rid: int = None,
        use_conditions: bool = None,
    ):
        self.conditions = conditions
        self.content = content
        self.id = id
        self.index = index
        self.name = name
        self.next_nodes = next_nodes
        self.node_type = node_type
        self.properties = properties
        self.rid = rid
        self.use_conditions = use_conditions

    def validate(self):
        if self.conditions:
            for v1 in self.conditions:
                 if v1:
                    v1.validate()
        if self.next_nodes:
            for v1 in self.next_nodes:
                 if v1:
                    v1.validate()
        if self.properties:
            self.properties.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Conditions'] = []
        if self.conditions is not None:
            for k1 in self.conditions:
                result['Conditions'].append(k1.to_map() if k1 else None)

        if self.content is not None:
            result['Content'] = self.content

        if self.id is not None:
            result['Id'] = self.id

        if self.index is not None:
            result['Index'] = self.index

        if self.name is not None:
            result['Name'] = self.name

        result['NextNodes'] = []
        if self.next_nodes is not None:
            for k1 in self.next_nodes:
                result['NextNodes'].append(k1.to_map() if k1 else None)

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.properties is not None:
            result['Properties'] = self.properties.to_map()

        if self.rid is not None:
            result['Rid'] = self.rid

        if self.use_conditions is not None:
            result['UseConditions'] = self.use_conditions

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conditions = []
        if m.get('Conditions') is not None:
            for k1 in m.get('Conditions'):
                temp_model = main_models.ConditionBasicInfo()
                self.conditions.append(temp_model.from_map(k1))

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.next_nodes = []
        if m.get('NextNodes') is not None:
            for k1 in m.get('NextNodes'):
                temp_model = main_models.GraphFlowNodeNextNodes()
                self.next_nodes.append(temp_model.from_map(k1))

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('Properties') is not None:
            temp_model = main_models.GraphFlowNodeProperties()
            self.properties = temp_model.from_map(m.get('Properties'))

        if m.get('Rid') is not None:
            self.rid = m.get('Rid')

        if m.get('UseConditions') is not None:
            self.use_conditions = m.get('UseConditions')

        return self

class GraphFlowNodeProperties(DaraModel):
    def __init__(
        self,
        auto_review: int = None,
        branch_judge: bool = None,
        check_more_size: int = None,
        check_type: int = None,
        lambda_: str = None,
        role: str = None,
        rule_score_type: int = None,
        say_type: str = None,
        score_num: int = None,
        score_num_type: int = None,
        score_rule_hit_type: int = None,
        score_type: int = None,
        triggers: List[str] = None,
        type: str = None,
    ):
        self.auto_review = auto_review
        self.branch_judge = branch_judge
        self.check_more_size = check_more_size
        self.check_type = check_type
        self.lambda_ = lambda_
        self.role = role
        self.rule_score_type = rule_score_type
        self.say_type = say_type
        self.score_num = score_num
        self.score_num_type = score_num_type
        self.score_rule_hit_type = score_rule_hit_type
        self.score_type = score_type
        self.triggers = triggers
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_review is not None:
            result['AutoReview'] = self.auto_review

        if self.branch_judge is not None:
            result['BranchJudge'] = self.branch_judge

        if self.check_more_size is not None:
            result['CheckMoreSize'] = self.check_more_size

        if self.check_type is not None:
            result['CheckType'] = self.check_type

        if self.lambda_ is not None:
            result['Lambda'] = self.lambda_

        if self.role is not None:
            result['Role'] = self.role

        if self.rule_score_type is not None:
            result['RuleScoreType'] = self.rule_score_type

        if self.say_type is not None:
            result['SayType'] = self.say_type

        if self.score_num is not None:
            result['ScoreNum'] = self.score_num

        if self.score_num_type is not None:
            result['ScoreNumType'] = self.score_num_type

        if self.score_rule_hit_type is not None:
            result['ScoreRuleHitType'] = self.score_rule_hit_type

        if self.score_type is not None:
            result['ScoreType'] = self.score_type

        if self.triggers is not None:
            result['Triggers'] = self.triggers

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoReview') is not None:
            self.auto_review = m.get('AutoReview')

        if m.get('BranchJudge') is not None:
            self.branch_judge = m.get('BranchJudge')

        if m.get('CheckMoreSize') is not None:
            self.check_more_size = m.get('CheckMoreSize')

        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')

        if m.get('Lambda') is not None:
            self.lambda_ = m.get('Lambda')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('RuleScoreType') is not None:
            self.rule_score_type = m.get('RuleScoreType')

        if m.get('SayType') is not None:
            self.say_type = m.get('SayType')

        if m.get('ScoreNum') is not None:
            self.score_num = m.get('ScoreNum')

        if m.get('ScoreNumType') is not None:
            self.score_num_type = m.get('ScoreNumType')

        if m.get('ScoreRuleHitType') is not None:
            self.score_rule_hit_type = m.get('ScoreRuleHitType')

        if m.get('ScoreType') is not None:
            self.score_type = m.get('ScoreType')

        if m.get('Triggers') is not None:
            self.triggers = m.get('Triggers')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GraphFlowNodeNextNodes(DaraModel):
    def __init__(
        self,
        check_type: int = None,
        index: int = None,
        lambda_: str = None,
        name: str = None,
        next_node_id: int = None,
        triggers: List[str] = None,
    ):
        self.check_type = check_type
        self.index = index
        self.lambda_ = lambda_
        self.name = name
        self.next_node_id = next_node_id
        self.triggers = triggers

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_type is not None:
            result['CheckType'] = self.check_type

        if self.index is not None:
            result['Index'] = self.index

        if self.lambda_ is not None:
            result['Lambda'] = self.lambda_

        if self.name is not None:
            result['Name'] = self.name

        if self.next_node_id is not None:
            result['NextNodeId'] = self.next_node_id

        if self.triggers is not None:
            result['Triggers'] = self.triggers

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')

        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('Lambda') is not None:
            self.lambda_ = m.get('Lambda')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NextNodeId') is not None:
            self.next_node_id = m.get('NextNodeId')

        if m.get('Triggers') is not None:
            self.triggers = m.get('Triggers')

        return self

