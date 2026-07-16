# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetJobRequest(DaraModel):
    def __init__(
        self,
        job_type: str = None,
    ):
        # Task Type. Currently, only DOWNLOWD_MARKRESULT_FLOW is available.
        self.job_type = job_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_type is not None:
            result['JobType'] = self.job_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        return self

