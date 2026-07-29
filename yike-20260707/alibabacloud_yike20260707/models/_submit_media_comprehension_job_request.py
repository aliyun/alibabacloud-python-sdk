# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitMediaComprehensionJobRequest(DaraModel):
    def __init__(
        self,
        input: str = None,
        job_params: str = None,
        job_type: str = None,
        user_data: str = None,
    ):
        self.input = input
        self.job_params = job_params
        self.job_type = job_type
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input is not None:
            result['Input'] = self.input

        if self.job_params is not None:
            result['JobParams'] = self.job_params

        if self.job_type is not None:
            result['JobType'] = self.job_type

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Input') is not None:
            self.input = m.get('Input')

        if m.get('JobParams') is not None:
            self.job_params = m.get('JobParams')

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

