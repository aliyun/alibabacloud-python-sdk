# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTokenRequest(DaraModel):
    def __init__(
        self,
        expire_time: int = None,
        training_job_id: str = None,
    ):
        self.expire_time = expire_time
        # This parameter is required.
        self.training_job_id = training_job_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.training_job_id is not None:
            result['TrainingJobId'] = self.training_job_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('TrainingJobId') is not None:
            self.training_job_id = m.get('TrainingJobId')

        return self

