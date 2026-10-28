# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DialogueRequest(DaraModel):
    def __init__(
        self,
        extras: str = None,
        instance_id: str = None,
        script_id: str = None,
        session_id: str = None,
        utterance: str = None,
    ):
        # Extras.
        # For example, a silence timeout: [{"dataType":"Silence"}]
        # >Notice: Valid values for `dataType`: `DTMF`, `Silence`, or `RuntimePrompts`.
        # 
        # > - If `dataType` is `DTMF`, use the format: `[{"dataType":"DTMF","dtmf":"xxxx"}]`
        # >
        # > - If `dataType` is `Silence`, use the format: `[{"dataType":"Silence"}]`
        # >
        # > - If `dataType` is `RuntimePrompts`, use the format: `[{"dataType":"RuntimePrompts","prompts":"xxxx","persistent":false/true}]`
        self.extras = extras
        # The instance ID.
        self.instance_id = instance_id
        # The script ID.
        self.script_id = script_id
        # The session ID.
        self.session_id = session_id
        # The user\\"s input for the conversational turn.
        self.utterance = utterance

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extras is not None:
            result['Extras'] = self.extras

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.utterance is not None:
            result['Utterance'] = self.utterance

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extras') is not None:
            self.extras = m.get('Extras')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('Utterance') is not None:
            self.utterance = m.get('Utterance')

        return self

