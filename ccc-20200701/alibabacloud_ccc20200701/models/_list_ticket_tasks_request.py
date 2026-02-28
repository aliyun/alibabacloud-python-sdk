# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTicketTasksRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        ticket_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.ticket_id = ticket_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.ticket_id is not None:
            result['TicketId'] = self.ticket_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('TicketId') is not None:
            self.ticket_id = m.get('TicketId')

        return self

