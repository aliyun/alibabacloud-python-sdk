# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryQwenConferenceSgTicketPopRequest(DaraModel):
    def __init__(
        self,
        ticket_token: str = None,
    ):
        self.ticket_token = ticket_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ticket_token is not None:
            result['TicketToken'] = self.ticket_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TicketToken') is not None:
            self.ticket_token = m.get('TicketToken')

        return self

