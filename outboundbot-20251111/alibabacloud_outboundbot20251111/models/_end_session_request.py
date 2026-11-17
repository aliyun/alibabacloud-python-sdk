# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EndSessionRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        script_id: str = None,
        session_id: str = None,
    ):
        # The instance identity of the associated product. You must use an existing instance that the invoker is authorized to access. The instance must match the instance to which the scenario, channel, and session belong. The maximum length is subject to the current POP parameter definitions.
        self.instance_id = instance_id
        # The ID of the dialog scenario under the instance. You must specify an existing scenario. Subsequent dialog and session termination requests for the same text session must use the same scenario that was used to start the session.
        self.script_id = script_id
        # The session ID used to uniquely identify the current interaction. For a text session, use the text- prefixed ID returned when the session is started. For web voice, use the ws- prefixed ID. For outbound call tests with real numbers, use the test- prefixed ID. Subsequent calls must use the actual returned values.
        # 
        # This parameter is required.
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        return self

