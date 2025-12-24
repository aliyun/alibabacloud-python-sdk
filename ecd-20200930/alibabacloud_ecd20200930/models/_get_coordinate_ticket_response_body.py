# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCoordinateTicketResponseBody(DaraModel):
    def __init__(
        self,
        co_id: str = None,
        request_id: str = None,
        task_id: str = None,
        task_status: str = None,
        ticket: str = None,
    ):
        # The ID of the stream collaboration.
        self.co_id = co_id
        # The request ID.
        self.request_id = request_id
        # The ID of the cloud computer connection task.
        self.task_id = task_id
        # The task status.
        # 
        # Possible values:
        # 
        # *   Finished
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Failed
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Running
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.task_status = task_status
        # The credentials of the stream collaboration.
        self.ticket = ticket

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.co_id is not None:
            result['CoId'] = self.co_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.ticket is not None:
            result['Ticket'] = self.ticket

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoId') is not None:
            self.co_id = m.get('CoId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('Ticket') is not None:
            self.ticket = m.get('Ticket')

        return self

