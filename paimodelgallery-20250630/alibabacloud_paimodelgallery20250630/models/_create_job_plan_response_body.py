# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateJobPlanResponseBody(DaraModel):
    def __init__(
        self,
        job_plan_id: str = None,
        request_id: str = None,
    ):
        # The job plan ID.
        self.job_plan_id = job_plan_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_plan_id is not None:
            result['JobPlanId'] = self.job_plan_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobPlanId') is not None:
            self.job_plan_id = m.get('JobPlanId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

