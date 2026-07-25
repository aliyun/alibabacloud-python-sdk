# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetYikeAgentJobEstimatedCreditRequest(DaraModel):
    def __init__(
        self,
        job_action: str = None,
        job_params: str = None,
    ):
        # This parameter is required.
        self.job_action = job_action
        # This parameter is required.
        self.job_params = job_params

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_action is not None:
            result['JobAction'] = self.job_action

        if self.job_params is not None:
            result['JobParams'] = self.job_params

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobAction') is not None:
            self.job_action = m.get('JobAction')

        if m.get('JobParams') is not None:
            self.job_params = m.get('JobParams')

        return self

