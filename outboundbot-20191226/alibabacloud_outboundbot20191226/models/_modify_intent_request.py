# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyIntentRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        intent_description: str = None,
        intent_id: str = None,
        intent_name: str = None,
        keywords: str = None,
        script_id: str = None,
        utterances: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.intent_description = intent_description
        # This parameter is required.
        self.intent_id = intent_id
        # This parameter is required.
        self.intent_name = intent_name
        self.keywords = keywords
        # This parameter is required.
        self.script_id = script_id
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

        if self.intent_id is not None:
            result['IntentId'] = self.intent_id

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

        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')

        if m.get('IntentName') is not None:
            self.intent_name = m.get('IntentName')

        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        if m.get('Utterances') is not None:
            self.utterances = m.get('Utterances')

        return self

