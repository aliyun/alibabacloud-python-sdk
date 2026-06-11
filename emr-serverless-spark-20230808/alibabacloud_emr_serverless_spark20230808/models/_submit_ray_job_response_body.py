# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitRayJobResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        submission_id: str = None,
    ):
        self.request_id = request_id
        self.submission_id = submission_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.submission_id is not None:
            result['submissionId'] = self.submission_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('submissionId') is not None:
            self.submission_id = m.get('submissionId')

        return self

