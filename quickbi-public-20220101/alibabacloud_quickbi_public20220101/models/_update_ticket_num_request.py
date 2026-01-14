# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateTicketNumRequest(DaraModel):
    def __init__(
        self,
        ticket: str = None,
        ticket_num: int = None,
    ):
        # The value of the third-party embedded ticket, that is, the accessTicket value in the URL.
        # 
        # This parameter is required.
        self.ticket = ticket
        # The number of bills.
        # 
        # *   Valid values: 1 to 99998. Recommended value: 1.
        # 
        # This parameter is required.
        self.ticket_num = ticket_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ticket is not None:
            result['Ticket'] = self.ticket

        if self.ticket_num is not None:
            result['TicketNum'] = self.ticket_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ticket') is not None:
            self.ticket = m.get('Ticket')

        if m.get('TicketNum') is not None:
            self.ticket_num = m.get('TicketNum')

        return self

