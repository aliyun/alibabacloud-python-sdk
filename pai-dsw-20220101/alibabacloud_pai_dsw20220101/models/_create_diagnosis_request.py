# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDiagnosisRequest(DaraModel):
    def __init__(
        self,
        gmt_failure_time: str = None,
        instance_id: str = None,
        problem_category: str = None,
    ):
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.gmt_failure_time = gmt_failure_time
        self.instance_id = instance_id
        # This parameter is required.
        self.problem_category = problem_category

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gmt_failure_time is not None:
            result['GmtFailureTime'] = self.gmt_failure_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.problem_category is not None:
            result['ProblemCategory'] = self.problem_category

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtFailureTime') is not None:
            self.gmt_failure_time = m.get('GmtFailureTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ProblemCategory') is not None:
            self.problem_category = m.get('ProblemCategory')

        return self

