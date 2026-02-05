# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDialogueFlowRequest(DaraModel):
    def __init__(
        self,
        dialogue_flow_type: str = None,
        dialogue_name: str = None,
        instance_id: str = None,
        script_id: str = None,
    ):
        # This parameter is required.
        self.dialogue_flow_type = dialogue_flow_type
        # This parameter is required.
        self.dialogue_name = dialogue_name
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.script_id = script_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dialogue_flow_type is not None:
            result['DialogueFlowType'] = self.dialogue_flow_type

        if self.dialogue_name is not None:
            result['DialogueName'] = self.dialogue_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DialogueFlowType') is not None:
            self.dialogue_flow_type = m.get('DialogueFlowType')

        if m.get('DialogueName') is not None:
            self.dialogue_name = m.get('DialogueName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        return self

