# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteJobRecordsShrinkRequest(DaraModel):
    def __init__(
        self,
        job_ids_shrink: str = None,
    ):
        # The list of job IDs.
        self.job_ids_shrink = job_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_ids_shrink is not None:
            result['JobIds'] = self.job_ids_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobIds') is not None:
            self.job_ids_shrink = m.get('JobIds')

        return self

