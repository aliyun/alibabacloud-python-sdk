# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_outboundbot20191226 import models as main_models
from darabonba.model import DaraModel

class ModifyBeebotIntentRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        intent_definition: main_models.ModifyBeebotIntentRequestIntentDefinition = None,
        intent_id: int = None,
        script_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.intent_definition = intent_definition
        # This parameter is required.
        self.intent_id = intent_id
        # This parameter is required.
        self.script_id = script_id

    def validate(self):
        if self.intent_definition:
            self.intent_definition.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.intent_definition is not None:
            result['IntentDefinition'] = self.intent_definition.to_map()

        if self.intent_id is not None:
            result['IntentId'] = self.intent_id

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IntentDefinition') is not None:
            temp_model = main_models.ModifyBeebotIntentRequestIntentDefinition()
            self.intent_definition = temp_model.from_map(m.get('IntentDefinition'))

        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        return self

class ModifyBeebotIntentRequestIntentDefinition(DaraModel):
    def __init__(
        self,
        alias_name: str = None,
        intent_name: str = None,
    ):
        self.alias_name = alias_name
        # This parameter is required.
        self.intent_name = intent_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name

        if self.intent_name is not None:
            result['IntentName'] = self.intent_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')

        if m.get('IntentName') is not None:
            self.intent_name = m.get('IntentName')

        return self

