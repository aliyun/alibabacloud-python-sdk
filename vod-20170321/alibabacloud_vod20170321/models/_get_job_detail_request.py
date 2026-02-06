# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetJobDetailRequest(DaraModel):
    def __init__(
        self,
        job_id: str = None,
        job_type: str = None,
    ):
        # The ID of the task.
        # 
        # This parameter is required.
        self.job_id = job_id
        # The task type. Valid values:
        # 
        # *   transcode
        # *   snapshot
        # *   ai
        # 
        # This parameter is required.
        self.job_type = job_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.job_type is not None:
            result['JobType'] = self.job_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        return self

