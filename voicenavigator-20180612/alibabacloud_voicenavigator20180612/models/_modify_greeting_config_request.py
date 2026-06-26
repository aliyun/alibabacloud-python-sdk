# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyGreetingConfigRequest(DaraModel):
    def __init__(
        self,
        greeting_words: str = None,
        instance_id: str = None,
        intent_trigger: str = None,
        source_type: str = None,
    ):
        # The greeting words.
        # 
        # This parameter is required.
        self.greeting_words = greeting_words
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The intent trigger.
        self.intent_trigger = intent_trigger
        # The type.
        # 
        # This parameter is required.
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.greeting_words is not None:
            result['GreetingWords'] = self.greeting_words

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.intent_trigger is not None:
            result['IntentTrigger'] = self.intent_trigger

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GreetingWords') is not None:
            self.greeting_words = m.get('GreetingWords')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IntentTrigger') is not None:
            self.intent_trigger = m.get('IntentTrigger')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        return self

