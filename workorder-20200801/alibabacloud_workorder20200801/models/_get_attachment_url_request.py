# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAttachmentUrlRequest(DaraModel):
    def __init__(
        self,
        attach_name: str = None,
        note_id: str = None,
        ticket_id: str = None,
    ):
        # This parameter is required.
        self.attach_name = attach_name
        # This parameter is required.
        self.note_id = note_id
        # This parameter is required.
        self.ticket_id = ticket_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attach_name is not None:
            result['AttachName'] = self.attach_name

        if self.note_id is not None:
            result['NoteId'] = self.note_id

        if self.ticket_id is not None:
            result['TicketId'] = self.ticket_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachName') is not None:
            self.attach_name = m.get('AttachName')

        if m.get('NoteId') is not None:
            self.note_id = m.get('NoteId')

        if m.get('TicketId') is not None:
            self.ticket_id = m.get('TicketId')

        return self

