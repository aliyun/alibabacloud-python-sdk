# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class KopilotFeedbackRequest(DaraModel):
    def __init__(
        self,
        comment: str = None,
        feedback: str = None,
        region_id: str = None,
        session_id: str = None,
        turn_id: str = None,
    ):
        self.comment = comment
        self.feedback = feedback
        # This parameter is required.
        self.region_id = region_id
        self.session_id = session_id
        self.turn_id = turn_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.feedback is not None:
            result['Feedback'] = self.feedback

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.turn_id is not None:
            result['TurnId'] = self.turn_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('Feedback') is not None:
            self.feedback = m.get('Feedback')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('TurnId') is not None:
            self.turn_id = m.get('TurnId')

        return self

