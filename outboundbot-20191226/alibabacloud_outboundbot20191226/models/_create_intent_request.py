# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateIntentRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        intent_description: str = None,
        intent_name: str = None,
        keywords: str = None,
        script_id: str = None,
        utterances: str = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # A description of the intent.
        self.intent_description = intent_description
        # The name of the intent. This name must be unique within the script.
        # 
        # This parameter is required.
        self.intent_name = intent_name
        # A JSON-formatted string containing an array of keywords that help identify the intent.
        self.keywords = keywords
        # The script ID.
        # 
        # This parameter is required.
        self.script_id = script_id
        # A JSON-formatted string containing an array of sample utterances that trigger this intent.
        # 
        # This parameter is required.
        self.utterances = utterances

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.intent_description is not None:
            result['IntentDescription'] = self.intent_description

        if self.intent_name is not None:
            result['IntentName'] = self.intent_name

        if self.keywords is not None:
            result['Keywords'] = self.keywords

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        if self.utterances is not None:
            result['Utterances'] = self.utterances

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IntentDescription') is not None:
            self.intent_description = m.get('IntentDescription')

        if m.get('IntentName') is not None:
            self.intent_name = m.get('IntentName')

        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        if m.get('Utterances') is not None:
            self.utterances = m.get('Utterances')

        return self

