# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DelayTicketExpireTimeRequest(DaraModel):
    def __init__(
        self,
        expire_time: int = None,
        ticket: str = None,
    ):
        # The time to postpone.
        # 
        # *   Unit: minutes. Valid values: 0 to 240. Unit: minutes. Valid values: 4 hours.
        # *   Expired bills cannot be extended.
        # 
        # This parameter is required.
        self.expire_time = expire_time
        # The value of the third-party embedded ticket, that is, the accessTicket value in the URL.
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
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.ticket is not None:
            result['Ticket'] = self.ticket

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('Ticket') is not None:
            self.ticket = m.get('Ticket')

        return self

