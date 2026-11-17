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
        # The JSON array string of additional input events. Supports DTMF key press events (dataType=DTMF, dtmf is the key content), Silence events (dataType=Silence), and RuntimePrompts events (dataType=RuntimePrompts, prompts is the prompt text, persistent specifies whether to persist). For example, a silence event is [{"dataType":"Silence"}]. This parameter is optional when no additional events are present.
        self.extras = extras
        # The instance identity of the associated product. You must use an instance that the invoker has permission to access and that actually exists. It must be consistent with the instance to which the scenario, channel, and session belong. The maximum length is subject to the current POP parameter definition.
        self.instance_id = instance_id
        # The ID of the conversation scenario under the instance. Specify an existing scenario. Subsequent conversations and end requests for the same text session must use the scenario specified when the session was initiated.
        self.script_id = script_id
        # The session ID used to uniquely associate this interaction. For a text session, it is the text- identifier returned when the session is initiated. For web voice, it is the ws- identifier. For real number outbound call tests, it is the test- identifier. Subsequent calls must use the actual returned value.
        self.session_id = session_id
        # The text input content of the user for the current round. For normal conversations, pass the actual text of the user. Events such as key presses or silence can be passed through Extras. The processing method is determined by the scenario and the engine.
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

