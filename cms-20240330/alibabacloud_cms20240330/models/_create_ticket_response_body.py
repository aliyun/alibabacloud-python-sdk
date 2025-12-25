# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTicketResponseBody(DaraModel):
    def __init__(
        self,
        ticket: str = None,
    ):
        # 免登录票据。
        self.ticket = ticket

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ticket is not None:
            result['ticket'] = self.ticket

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ticket') is not None:
            self.ticket = m.get('ticket')

        return self

