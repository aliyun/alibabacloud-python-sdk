# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateOperationTicketResponseBody(DaraModel):
    def __init__(
        self,
        operation_ticket_id: str = None,
        request_id: str = None,
    ):
        self.operation_ticket_id = operation_ticket_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.operation_ticket_id is not None:
            result['OperationTicketId'] = self.operation_ticket_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperationTicketId') is not None:
            self.operation_ticket_id = m.get('OperationTicketId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

