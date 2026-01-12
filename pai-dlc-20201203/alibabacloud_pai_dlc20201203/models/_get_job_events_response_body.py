# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetJobEventsResponseBody(DaraModel):
    def __init__(
        self,
        events: List[str] = None,
        job_id: str = None,
        request_id: str = None,
    ):
        # The events.
        self.events = events
        # The job ID.
        self.job_id = job_id
        # The request ID, which can be used for troubleshooting.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.events is not None:
            result['Events'] = self.events

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Events') is not None:
            self.events = m.get('Events')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

