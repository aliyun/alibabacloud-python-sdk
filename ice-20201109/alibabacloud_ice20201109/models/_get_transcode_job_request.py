# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTranscodeJobRequest(DaraModel):
    def __init__(
        self,
        parent_job_id: str = None,
    ):
        # The job ID.
        self.parent_job_id = parent_job_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.parent_job_id is not None:
            result['ParentJobId'] = self.parent_job_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParentJobId') is not None:
            self.parent_job_id = m.get('ParentJobId')

        return self

