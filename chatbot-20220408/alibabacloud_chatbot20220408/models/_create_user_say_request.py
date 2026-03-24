# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_chatbot20220408 import models as main_models
from darabonba.model import DaraModel

class CreateUserSayRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        instance_id: str = None,
        user_say_definition: main_models.CreateUserSayRequestUserSayDefinition = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.instance_id = instance_id
        self.user_say_definition = user_say_definition

    def validate(self):
        if self.user_say_definition:
            self.user_say_definition.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.user_say_definition is not None:
            result['UserSayDefinition'] = self.user_say_definition.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('UserSayDefinition') is not None:
            temp_model = main_models.CreateUserSayRequestUserSayDefinition()
            self.user_say_definition = temp_model.from_map(m.get('UserSayDefinition'))

        return self

class CreateUserSayRequestUserSayDefinition(DaraModel):
    def __init__(
        self,
        content: str = None,
        intent_id: int = None,
        slot_infos: List[main_models.CreateUserSayRequestUserSayDefinitionSlotInfos] = None,
    ):
        # This parameter is required.
        self.content = content
        # This parameter is required.
        self.intent_id = intent_id
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
        if self.content is not None:
            result['Content'] = self.content

        if self.intent_id is not None:
            result['IntentId'] = self.intent_id

        result['SlotInfos'] = []
        if self.slot_infos is not None:
            for k1 in self.slot_infos:
                result['SlotInfos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')

        self.slot_infos = []
        if m.get('SlotInfos') is not None:
            for k1 in m.get('SlotInfos'):
                temp_model = main_models.CreateUserSayRequestUserSayDefinitionSlotInfos()
                self.slot_infos.append(temp_model.from_map(k1))

        return self

class CreateUserSayRequestUserSayDefinitionSlotInfos(DaraModel):
    def __init__(
        self,
        end_index: int = None,
        slot_id: str = None,
        start_index: int = None,
    ):
        self.end_index = end_index
        self.slot_id = slot_id
        self.start_index = start_index

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_index is not None:
            result['EndIndex'] = self.end_index

        if self.slot_id is not None:
            result['SlotId'] = self.slot_id

        if self.start_index is not None:
            result['StartIndex'] = self.start_index

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndIndex') is not None:
            self.end_index = m.get('EndIndex')

        if m.get('SlotId') is not None:
            self.slot_id = m.get('SlotId')

        if m.get('StartIndex') is not None:
            self.start_index = m.get('StartIndex')

        return self

