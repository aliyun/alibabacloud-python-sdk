# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RescaleJobParam(DaraModel):
    def __init__(
        self,
        job_parallelism: int = None,
    ):
        self.job_parallelism = job_parallelism

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_parallelism is not None:
            result['jobParallelism'] = self.job_parallelism

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('jobParallelism') is not None:
            self.job_parallelism = m.get('jobParallelism')

        return self

