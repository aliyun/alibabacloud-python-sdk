# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class InsertInterveneRuleRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        intervene_rule_config: main_models.InsertInterveneRuleRequestInterveneRuleConfig = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.intervene_rule_config = intervene_rule_config

    def validate(self):
        if self.intervene_rule_config:
            self.intervene_rule_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.intervene_rule_config is not None:
            result['InterveneRuleConfig'] = self.intervene_rule_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('InterveneRuleConfig') is not None:
            temp_model = main_models.InsertInterveneRuleRequestInterveneRuleConfig()
            self.intervene_rule_config = temp_model.from_map(m.get('InterveneRuleConfig'))

        return self

class InsertInterveneRuleRequestInterveneRuleConfig(DaraModel):
    def __init__(
        self,
        answer_config: List[main_models.InsertInterveneRuleRequestInterveneRuleConfigAnswerConfig] = None,
        effect_config: main_models.InsertInterveneRuleRequestInterveneRuleConfigEffectConfig = None,
        intervene_config_list: List[main_models.InsertInterveneRuleRequestInterveneRuleConfigInterveneConfigList] = None,
        intervene_type: int = None,
        namespace_list: List[str] = None,
        rule_id: int = None,
        rule_name: str = None,
    ):
        self.answer_config = answer_config
        self.effect_config = effect_config
        self.intervene_config_list = intervene_config_list
        self.intervene_type = intervene_type
        self.namespace_list = namespace_list
        self.rule_id = rule_id
        self.rule_name = rule_name

    def validate(self):
        if self.answer_config:
            for v1 in self.answer_config:
                 if v1:
                    v1.validate()
        if self.effect_config:
            self.effect_config.validate()
        if self.intervene_config_list:
            for v1 in self.intervene_config_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AnswerConfig'] = []
        if self.answer_config is not None:
            for k1 in self.answer_config:
                result['AnswerConfig'].append(k1.to_map() if k1 else None)

        if self.effect_config is not None:
            result['EffectConfig'] = self.effect_config.to_map()

        result['InterveneConfigList'] = []
        if self.intervene_config_list is not None:
            for k1 in self.intervene_config_list:
                result['InterveneConfigList'].append(k1.to_map() if k1 else None)

        if self.intervene_type is not None:
            result['InterveneType'] = self.intervene_type

        if self.namespace_list is not None:
            result['NamespaceList'] = self.namespace_list

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.answer_config = []
        if m.get('AnswerConfig') is not None:
            for k1 in m.get('AnswerConfig'):
                temp_model = main_models.InsertInterveneRuleRequestInterveneRuleConfigAnswerConfig()
                self.answer_config.append(temp_model.from_map(k1))

        if m.get('EffectConfig') is not None:
            temp_model = main_models.InsertInterveneRuleRequestInterveneRuleConfigEffectConfig()
            self.effect_config = temp_model.from_map(m.get('EffectConfig'))

        self.intervene_config_list = []
        if m.get('InterveneConfigList') is not None:
            for k1 in m.get('InterveneConfigList'):
                temp_model = main_models.InsertInterveneRuleRequestInterveneRuleConfigInterveneConfigList()
                self.intervene_config_list.append(temp_model.from_map(k1))

        if m.get('InterveneType') is not None:
            self.intervene_type = m.get('InterveneType')

        if m.get('NamespaceList') is not None:
            self.namespace_list = m.get('NamespaceList')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        return self

class InsertInterveneRuleRequestInterveneRuleConfigInterveneConfigList(DaraModel):
    def __init__(
        self,
        id: str = None,
        operation_type: int = None,
        query: str = None,
    ):
        # id
        self.id = id
        self.operation_type = operation_type
        self.query = query

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.operation_type is not None:
            result['OperationType'] = self.operation_type

        if self.query is not None:
            result['Query'] = self.query

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        return self

class InsertInterveneRuleRequestInterveneRuleConfigEffectConfig(DaraModel):
    def __init__(
        self,
        effect_type: int = None,
        end_time: str = None,
        start_time: str = None,
    ):
        self.effect_type = effect_type
        self.end_time = end_time
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.effect_type is not None:
            result['EffectType'] = self.effect_type

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EffectType') is not None:
            self.effect_type = m.get('EffectType')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class InsertInterveneRuleRequestInterveneRuleConfigAnswerConfig(DaraModel):
    def __init__(
        self,
        answer_type: int = None,
        message: str = None,
        namespace: str = None,
    ):
        self.answer_type = answer_type
        self.message = message
        self.namespace = namespace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.answer_type is not None:
            result['AnswerType'] = self.answer_type

        if self.message is not None:
            result['Message'] = self.message

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnswerType') is not None:
            self.answer_type = m.get('AnswerType')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        return self

