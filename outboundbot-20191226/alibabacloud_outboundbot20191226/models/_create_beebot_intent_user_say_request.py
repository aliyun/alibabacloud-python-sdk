# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_outboundbot20191226 import models as main_models
from darabonba.model import DaraModel

class CreateBeebotIntentUserSayRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        script_id: str = None,
        user_say_definition: main_models.CreateBeebotIntentUserSayRequestUserSayDefinition = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.script_id = script_id
        # This parameter is required.
        self.user_say_definition = user_say_definition

    def validate(self):
        if self.user_say_definition:
            self.user_say_definition.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        if self.user_say_definition is not None:
            result['UserSayDefinition'] = self.user_say_definition.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        if m.get('UserSayDefinition') is not None:
            temp_model = main_models.CreateBeebotIntentUserSayRequestUserSayDefinition()
            self.user_say_definition = temp_model.from_map(m.get('UserSayDefinition'))

        return self

class CreateBeebotIntentUserSayRequestUserSayDefinition(DaraModel):
    def __init__(
        self,
        content: str = None,
        intent_id: int = None,
    ):
        # This parameter is required.
        self.content = content
        # This parameter is required.
        self.intent_id = intent_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.intent_id is not None:
            result['IntentId'] = self.intent_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')

        return self

