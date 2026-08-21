# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CancelUrlUploadJobsResponseBody(DaraModel):
    def __init__(
        self,
        canceled_jobs: List[str] = None,
        non_exists: List[str] = None,
        request_id: str = None,
    ):
        # The list of tasks that were successfully canceled.
        self.canceled_jobs = canceled_jobs
        # The list of tasks that do not exist.
        self.non_exists = non_exists
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.canceled_jobs is not None:
            result['CanceledJobs'] = self.canceled_jobs

        if self.non_exists is not None:
            result['NonExists'] = self.non_exists

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanceledJobs') is not None:
            self.canceled_jobs = m.get('CanceledJobs')

        if m.get('NonExists') is not None:
            self.non_exists = m.get('NonExists')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

