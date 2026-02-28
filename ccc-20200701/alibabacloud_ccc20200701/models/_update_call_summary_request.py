# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateCallSummaryRequest(DaraModel):
    def __init__(
        self,
        context: str = None,
        instance_id: str = None,
        ticket_id: str = None,
    ):
        self.context = context
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.ticket_id = ticket_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.context is not None:
            result['Context'] = self.context

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.ticket_id is not None:
            result['TicketId'] = self.ticket_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Context') is not None:
            self.context = m.get('Context')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('TicketId') is not None:
            self.ticket_id = m.get('TicketId')

        return self

