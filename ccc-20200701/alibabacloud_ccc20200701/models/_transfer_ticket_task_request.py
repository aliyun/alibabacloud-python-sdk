# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TransferTicketTaskRequest(DaraModel):
    def __init__(
        self,
        assignee: str = None,
        comment: str = None,
        instance_id: str = None,
        task_id: str = None,
        ticket_id: str = None,
    ):
        # This parameter is required.
        self.assignee = assignee
        self.comment = comment
        # This parameter is required.
        self.instance_id = instance_id
        self.task_id = task_id
        self.ticket_id = ticket_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assignee is not None:
            result['Assignee'] = self.assignee

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.ticket_id is not None:
            result['TicketId'] = self.ticket_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Assignee') is not None:
            self.assignee = m.get('Assignee')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TicketId') is not None:
            self.ticket_id = m.get('TicketId')

        return self

