# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetLogTicketResponseBody(DaraModel):
    def __init__(
        self,
        log_ticket: str = None,
        request_id: str = None,
    ):
        self.log_ticket = log_ticket
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.log_ticket is not None:
            result['LogTicket'] = self.log_ticket

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogTicket') is not None:
            self.log_ticket = m.get('LogTicket')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

