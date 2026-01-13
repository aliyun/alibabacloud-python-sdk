# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartJobRunResponseBody(DaraModel):
    def __init__(
        self,
        job_run_id: str = None,
        request_id: str = None,
    ):
        # The job ID.
        self.job_run_id = job_run_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_run_id is not None:
            result['jobRunId'] = self.job_run_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('jobRunId') is not None:
            self.job_run_id = m.get('jobRunId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

