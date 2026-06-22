# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteMaliciousNoteRequest(DaraModel):
    def __init__(
        self,
        note_id: int = None,
    ):
        # The ID of the note record.
        # >Call the [ListAgentlessMaliciousFiles](~~ListAgentlessMaliciousFiles~~) operation to obtain this parameter from the NoteId field.
        self.note_id = note_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.note_id is not None:
            result['NoteId'] = self.note_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NoteId') is not None:
            self.note_id = m.get('NoteId')

        return self

