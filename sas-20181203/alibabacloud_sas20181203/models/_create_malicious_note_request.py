# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateMaliciousNoteRequest(DaraModel):
    def __init__(
        self,
        event_id: int = None,
        note: str = None,
    ):
        # The ID of the alert event to which you want to add remarks.
        # 
        # >  You can call the [ListAgentlessMaliciousFiles](~~ListAgentlessMaliciousFiles~~) operation to obtain the ID of the alert event from the NoteId parameter.
        # 
        # This parameter is required.
        self.event_id = event_id
        # The remarks that you want to add.
        # 
        # This parameter is required.
        self.note = note

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.note is not None:
            result['Note'] = self.note

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('Note') is not None:
            self.note = m.get('Note')

        return self

