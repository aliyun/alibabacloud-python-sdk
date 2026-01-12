# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pai_dlc20201203 import models as main_models
from darabonba.model import DaraModel

class GetJobSanityCheckResultResponseBody(DaraModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
        sanity_check_result: List[main_models.SanityCheckResultItem] = None,
    ):
        # The job ID.
        self.job_id = job_id
        # The request ID.
        self.request_id = request_id
        # The job sanity check result.
        self.sanity_check_result = sanity_check_result

    def validate(self):
        if self.sanity_check_result:
            for v1 in self.sanity_check_result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.request_id is not None:
            result['RequestID'] = self.request_id

        result['SanityCheckResult'] = []
        if self.sanity_check_result is not None:
            for k1 in self.sanity_check_result:
                result['SanityCheckResult'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('RequestID') is not None:
            self.request_id = m.get('RequestID')

        self.sanity_check_result = []
        if m.get('SanityCheckResult') is not None:
            for k1 in m.get('SanityCheckResult'):
                temp_model = main_models.SanityCheckResultItem()
                self.sanity_check_result.append(temp_model.from_map(k1))

        return self

