# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_outboundbot20191226 import models as main_models
from darabonba.model import DaraModel

class CreateBeebotIntentRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        intent_definition: main_models.CreateBeebotIntentRequestIntentDefinition = None,
        script_id: str = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The description of the intent.
        # 
        # This parameter is required.
        self.intent_definition = intent_definition
        # The scenario ID.
        # 
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

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IntentDefinition') is not None:
            temp_model = main_models.CreateBeebotIntentRequestIntentDefinition()
            self.intent_definition = temp_model.from_map(m.get('IntentDefinition'))

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        return self

class CreateBeebotIntentRequestIntentDefinition(DaraModel):
    def __init__(
        self,
        alias_name: str = None,
        intent_name: str = None,
    ):
        # The intent alias.
        self.alias_name = alias_name
        # The intent name.
        # 
        # > This is the intent code. It serves as a unique identifier.
        # 
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

