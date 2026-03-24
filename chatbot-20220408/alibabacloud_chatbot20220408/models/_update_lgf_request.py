# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_chatbot20220408 import models as main_models
from darabonba.model import DaraModel

class UpdateLgfRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        instance_id: str = None,
        lgf_definition: main_models.UpdateLgfRequestLgfDefinition = None,
        lgf_id: int = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.lgf_definition = lgf_definition
        # LGF ID
        # 
        # This parameter is required.
        self.lgf_id = lgf_id

    def validate(self):
        if self.lgf_definition:
            self.lgf_definition.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.lgf_definition is not None:
            result['LgfDefinition'] = self.lgf_definition.to_map()

        if self.lgf_id is not None:
            result['LgfId'] = self.lgf_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LgfDefinition') is not None:
            temp_model = main_models.UpdateLgfRequestLgfDefinition()
            self.lgf_definition = temp_model.from_map(m.get('LgfDefinition'))

        if m.get('LgfId') is not None:
            self.lgf_id = m.get('LgfId')

        return self

class UpdateLgfRequestLgfDefinition(DaraModel):
    def __init__(
        self,
        intent_id: int = None,
        rule_text: str = None,
    ):
        # This parameter is required.
        self.intent_id = intent_id
        # This parameter is required.
        self.rule_text = rule_text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id

        if self.rule_text is not None:
            result['RuleText'] = self.rule_text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')

        if m.get('RuleText') is not None:
            self.rule_text = m.get('RuleText')

        return self

