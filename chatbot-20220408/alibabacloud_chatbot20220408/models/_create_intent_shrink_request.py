# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateIntentShrinkRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        instance_id: str = None,
        intent_definition_shrink: str = None,
    ):
        # The key of the business space. If you do not specify this parameter, the default business space is used. You can get the key from the business management page of your main account.
        self.agent_key = agent_key
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The intent definition.
        self.intent_definition_shrink = intent_definition_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.intent_definition_shrink is not None:
            result['IntentDefinition'] = self.intent_definition_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IntentDefinition') is not None:
            self.intent_definition_shrink = m.get('IntentDefinition')

        return self

