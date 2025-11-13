# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_farui20240628 import models as main_models
from darabonba.model import DaraModel

class RunContractResultGenerationRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        assistant: main_models.RunContractResultGenerationRequestAssistant = None,
        stream: bool = None,
    ):
        self.app_id = app_id
        self.assistant = assistant
        self.stream = stream

    def validate(self):
        if self.assistant:
            self.assistant.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['appId'] = self.app_id

        if self.assistant is not None:
            result['assistant'] = self.assistant.to_map()

        if self.stream is not None:
            result['stream'] = self.stream

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')

        if m.get('assistant') is not None:
            temp_model = main_models.RunContractResultGenerationRequestAssistant()
            self.assistant = temp_model.from_map(m.get('assistant'))

        if m.get('stream') is not None:
            self.stream = m.get('stream')

        return self

class RunContractResultGenerationRequestAssistant(DaraModel):
    def __init__(
        self,
        meta_data: main_models.RunContractResultGenerationRequestAssistantMetaData = None,
        type: str = None,
        version: str = None,
    ):
        self.meta_data = meta_data
        self.type = type
        self.version = version

    def validate(self):
        if self.meta_data:
            self.meta_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.meta_data is not None:
            result['metaData'] = self.meta_data.to_map()

        if self.type is not None:
            result['type'] = self.type

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('metaData') is not None:
            temp_model = main_models.RunContractResultGenerationRequestAssistantMetaData()
            self.meta_data = temp_model.from_map(m.get('metaData'))

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

class RunContractResultGenerationRequestAssistantMetaData(DaraModel):
    def __init__(
        self,
        custom_rule_config: main_models.RunContractResultGenerationRequestAssistantMetaDataCustomRuleConfig = None,
        file_id: str = None,
        position: str = None,
        rule_task_id: str = None,
        rules: List[main_models.RunContractResultGenerationRequestAssistantMetaDataRules] = None,
    ):
        self.custom_rule_config = custom_rule_config
        self.file_id = file_id
        self.position = position
        self.rule_task_id = rule_task_id
        self.rules = rules

    def validate(self):
        if self.custom_rule_config:
            self.custom_rule_config.validate()
        if self.rules:
            for v1 in self.rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_rule_config is not None:
            result['customRuleConfig'] = self.custom_rule_config.to_map()

        if self.file_id is not None:
            result['fileId'] = self.file_id

        if self.position is not None:
            result['position'] = self.position

        if self.rule_task_id is not None:
            result['ruleTaskId'] = self.rule_task_id

        result['rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['rules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('customRuleConfig') is not None:
            temp_model = main_models.RunContractResultGenerationRequestAssistantMetaDataCustomRuleConfig()
            self.custom_rule_config = temp_model.from_map(m.get('customRuleConfig'))

        if m.get('fileId') is not None:
            self.file_id = m.get('fileId')

        if m.get('position') is not None:
            self.position = m.get('position')

        if m.get('ruleTaskId') is not None:
            self.rule_task_id = m.get('ruleTaskId')

        self.rules = []
        if m.get('rules') is not None:
            for k1 in m.get('rules'):
                temp_model = main_models.RunContractResultGenerationRequestAssistantMetaDataRules()
                self.rules.append(temp_model.from_map(k1))

        return self

class RunContractResultGenerationRequestAssistantMetaDataRules(DaraModel):
    def __init__(
        self,
        risk_level: str = None,
        rule_sequence: str = None,
        rule_tag: str = None,
        rule_title: str = None,
    ):
        self.risk_level = risk_level
        self.rule_sequence = rule_sequence
        self.rule_tag = rule_tag
        self.rule_title = rule_title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.risk_level is not None:
            result['riskLevel'] = self.risk_level

        if self.rule_sequence is not None:
            result['ruleSequence'] = self.rule_sequence

        if self.rule_tag is not None:
            result['ruleTag'] = self.rule_tag

        if self.rule_title is not None:
            result['ruleTitle'] = self.rule_title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('riskLevel') is not None:
            self.risk_level = m.get('riskLevel')

        if m.get('ruleSequence') is not None:
            self.rule_sequence = m.get('ruleSequence')

        if m.get('ruleTag') is not None:
            self.rule_tag = m.get('ruleTag')

        if m.get('ruleTitle') is not None:
            self.rule_title = m.get('ruleTitle')

        return self

class RunContractResultGenerationRequestAssistantMetaDataCustomRuleConfig(DaraModel):
    def __init__(
        self,
        custom_rules: List[main_models.RunContractResultGenerationRequestAssistantMetaDataCustomRuleConfigCustomRules] = None,
    ):
        self.custom_rules = custom_rules

    def validate(self):
        if self.custom_rules:
            for v1 in self.custom_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['customRules'] = []
        if self.custom_rules is not None:
            for k1 in self.custom_rules:
                result['customRules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.custom_rules = []
        if m.get('customRules') is not None:
            for k1 in m.get('customRules'):
                temp_model = main_models.RunContractResultGenerationRequestAssistantMetaDataCustomRuleConfigCustomRules()
                self.custom_rules.append(temp_model.from_map(k1))

        return self

class RunContractResultGenerationRequestAssistantMetaDataCustomRuleConfigCustomRules(DaraModel):
    def __init__(
        self,
        risk_level: str = None,
        rule_desc: str = None,
        rule_title: str = None,
    ):
        self.risk_level = risk_level
        self.rule_desc = rule_desc
        self.rule_title = rule_title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.risk_level is not None:
            result['riskLevel'] = self.risk_level

        if self.rule_desc is not None:
            result['ruleDesc'] = self.rule_desc

        if self.rule_title is not None:
            result['ruleTitle'] = self.rule_title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('riskLevel') is not None:
            self.risk_level = m.get('riskLevel')

        if m.get('ruleDesc') is not None:
            self.rule_desc = m.get('ruleDesc')

        if m.get('ruleTitle') is not None:
            self.rule_title = m.get('ruleTitle')

        return self

