# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAIAgentDialogueRequest(DaraModel):
    def __init__(
        self,
        dialogue_id: str = None,
        node_id: str = None,
        session_id: str = None,
    ):
        # The ID of the dialog that you want to delete.
        # 
        # This parameter is required.
        self.dialogue_id = dialogue_id
        self.node_id = node_id
        # The session ID.
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
        if self.dialogue_id is not None:
            result['DialogueId'] = self.dialogue_id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DialogueId') is not None:
            self.dialogue_id = m.get('DialogueId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        return self

