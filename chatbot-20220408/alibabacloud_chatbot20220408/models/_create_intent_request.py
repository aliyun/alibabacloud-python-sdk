# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_chatbot20220408 import models as main_models
from darabonba.model import DaraModel

class CreateIntentRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        instance_id: str = None,
        intent_definition: main_models.CreateIntentRequestIntentDefinition = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.instance_id = instance_id
        self.intent_definition = intent_definition

    def validate(self):
        if self.intent_definition:
            self.intent_definition.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.intent_definition is not None:
            result['IntentDefinition'] = self.intent_definition.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IntentDefinition') is not None:
            temp_model = main_models.CreateIntentRequestIntentDefinition()
            self.intent_definition = temp_model.from_map(m.get('IntentDefinition'))

        return self

class CreateIntentRequestIntentDefinition(DaraModel):
    def __init__(
        self,
        alias_name: str = None,
        intent_name: str = None,
        slot_infos: List[main_models.CreateIntentRequestIntentDefinitionSlotInfos] = None,
    ):
        self.alias_name = alias_name
        # This parameter is required.
        self.intent_name = intent_name
        self.slot_infos = slot_infos

    def validate(self):
        if self.slot_infos:
            for v1 in self.slot_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name

        if self.intent_name is not None:
            result['IntentName'] = self.intent_name

        result['SlotInfos'] = []
        if self.slot_infos is not None:
            for k1 in self.slot_infos:
                result['SlotInfos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')

        if m.get('IntentName') is not None:
            self.intent_name = m.get('IntentName')

        self.slot_infos = []
        if m.get('SlotInfos') is not None:
            for k1 in m.get('SlotInfos'):
                temp_model = main_models.CreateIntentRequestIntentDefinitionSlotInfos()
                self.slot_infos.append(temp_model.from_map(k1))

        return self

class CreateIntentRequestIntentDefinitionSlotInfos(DaraModel):
    def __init__(
        self,
        array: bool = None,
        encrypt: bool = None,
        interactive: bool = None,
        name: str = None,
        slot_id: str = None,
        value: str = None,
    ):
        self.array = array
        self.encrypt = encrypt
        self.interactive = interactive
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.slot_id = slot_id
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.array is not None:
            result['Array'] = self.array

        if self.encrypt is not None:
            result['Encrypt'] = self.encrypt

        if self.interactive is not None:
            result['Interactive'] = self.interactive

        if self.name is not None:
            result['Name'] = self.name

        if self.slot_id is not None:
            result['SlotId'] = self.slot_id

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Array') is not None:
            self.array = m.get('Array')

        if m.get('Encrypt') is not None:
            self.encrypt = m.get('Encrypt')

        if m.get('Interactive') is not None:
            self.interactive = m.get('Interactive')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SlotId') is not None:
            self.slot_id = m.get('SlotId')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

