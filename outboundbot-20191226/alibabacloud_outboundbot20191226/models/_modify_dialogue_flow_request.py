# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDialogueFlowRequest(DaraModel):
    def __init__(
        self,
        dialogue_flow_definition: str = None,
        dialogue_flow_id: str = None,
        instance_id: str = None,
        is_drafted: bool = None,
        script_id: str = None,
    ):
        # A JSON string that defines the structure and logic of the dialogue flow.
        # 
        # This parameter is required.
        self.dialogue_flow_definition = dialogue_flow_definition
        # The dialogue flow ID.
        # 
        # This parameter is required.
        self.dialogue_flow_id = dialogue_flow_id
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Specifies whether to save the changes as a draft.
        self.is_drafted = is_drafted
        # The script ID.
        # 
        # This parameter is required.
        self.script_id = script_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dialogue_flow_definition is not None:
            result['DialogueFlowDefinition'] = self.dialogue_flow_definition

        if self.dialogue_flow_id is not None:
            result['DialogueFlowId'] = self.dialogue_flow_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.is_drafted is not None:
            result['IsDrafted'] = self.is_drafted

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DialogueFlowDefinition') is not None:
            self.dialogue_flow_definition = m.get('DialogueFlowDefinition')

        if m.get('DialogueFlowId') is not None:
            self.dialogue_flow_id = m.get('DialogueFlowId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IsDrafted') is not None:
            self.is_drafted = m.get('IsDrafted')

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        return self

