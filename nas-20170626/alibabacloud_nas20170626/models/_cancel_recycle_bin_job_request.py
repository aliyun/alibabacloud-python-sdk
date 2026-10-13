# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CancelRecycleBinJobRequest(DaraModel):
    def __init__(
        self,
        job_id: str = None,
    ):
        # The ID of the task that you want to cancel.
        # 
        # You can call the [ListRecycleBinJobs](https://help.aliyun.com/document_detail/2412172.html) operation to query the task ID.
        # 
        # This parameter is required.
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_id is not None:
            result['JobId'] = self.job_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        return self

