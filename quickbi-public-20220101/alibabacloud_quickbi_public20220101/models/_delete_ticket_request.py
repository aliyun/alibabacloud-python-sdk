# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteTicketRequest(DaraModel):
    def __init__(
        self,
        ticket: str = None,
    ):
        # The value of the third-party embedded ticket, which is the `accessTicket` in the URL.
        # 
        # This parameter is required.
        self.ticket = ticket

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ticket is not None:
            result['Ticket'] = self.ticket

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ticket') is not None:
            self.ticket = m.get('Ticket')

        return self

