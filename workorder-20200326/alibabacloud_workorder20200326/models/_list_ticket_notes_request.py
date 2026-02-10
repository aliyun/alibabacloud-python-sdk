# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTicketNotesRequest(DaraModel):
    def __init__(
        self,
        language: str = None,
        ticket_id: str = None,
    ):
        self.language = language
        # This parameter is required.
        self.ticket_id = ticket_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.language is not None:
            result['Language'] = self.language

        if self.ticket_id is not None:
            result['TicketId'] = self.ticket_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('TicketId') is not None:
            self.ticket_id = m.get('TicketId')

        return self

