# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AsyncResourcePlanOperationResult(DaraModel):
    def __init__(
        self,
        message: str = None,
        plan: str = None,
        ticket_status: str = None,
    ):
        # The information about the ticket. The value of this parameter is returned when the value of the ticketStatus parameter is FAILED or EXECUTING.
        self.message = message
        # The resource configuration plan of the deployment in expert mode. The value of this parameter is returned when the value of the ticketStatus parameter is FINISHED.
        self.plan = plan
        # The status of the ticket that applies for an asynchronous operation. Valid values:
        # 
        # *   EXECUTING
        # *   FINISHED
        # *   FAILED
        self.ticket_status = ticket_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['message'] = self.message

        if self.plan is not None:
            result['plan'] = self.plan

        if self.ticket_status is not None:
            result['ticketStatus'] = self.ticket_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('plan') is not None:
            self.plan = m.get('plan')

        if m.get('ticketStatus') is not None:
            self.ticket_status = m.get('ticketStatus')

        return self

