# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EvaluateTicketRequest(DaraModel):
    def __init__(
        self,
        content: str = None,
        score: str = None,
        solved: bool = None,
        ticket_id: str = None,
        uid: str = None,
    ):
        # The content of the evaluation.
        self.content = content
        # The rating, from 1 to 5 stars.
        # 
        # This parameter is required.
        self.score = score
        # Indicates whether the issue was resolved.
        # 
        # This parameter is required.
        self.solved = solved
        # The ticket ID.
        # 
        # This parameter is required.
        self.ticket_id = ticket_id
        # The UID.
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.score is not None:
            result['Score'] = self.score

        if self.solved is not None:
            result['Solved'] = self.solved

        if self.ticket_id is not None:
            result['TicketId'] = self.ticket_id

        if self.uid is not None:
            result['Uid'] = self.uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('Solved') is not None:
            self.solved = m.get('Solved')

        if m.get('TicketId') is not None:
            self.ticket_id = m.get('TicketId')

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        return self

