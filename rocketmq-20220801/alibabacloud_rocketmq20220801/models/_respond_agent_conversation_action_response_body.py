# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RespondAgentConversationActionResponseBody(DaraModel):
    def __init__(
        self,
        accepted: bool = None,
        continuation_created: bool = None,
        run_id: str = None,
    ):
        self.accepted = accepted
        self.continuation_created = continuation_created
        self.run_id = run_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accepted is not None:
            result['accepted'] = self.accepted

        if self.continuation_created is not None:
            result['continuationCreated'] = self.continuation_created

        if self.run_id is not None:
            result['runId'] = self.run_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accepted') is not None:
            self.accepted = m.get('accepted')

        if m.get('continuationCreated') is not None:
            self.continuation_created = m.get('continuationCreated')

        if m.get('runId') is not None:
            self.run_id = m.get('runId')

        return self

