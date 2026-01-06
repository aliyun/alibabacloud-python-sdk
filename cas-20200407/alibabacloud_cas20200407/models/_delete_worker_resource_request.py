# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteWorkerResourceRequest(DaraModel):
    def __init__(
        self,
        job_id: int = None,
        worker_id: int = None,
    ):
        # The ID of the deployment task.
        # 
        # This parameter is required.
        self.job_id = job_id
        # The ID of the worker for the deployment task.
        # 
        # This parameter is required.
        self.worker_id = worker_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.worker_id is not None:
            result['WorkerId'] = self.worker_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('WorkerId') is not None:
            self.worker_id = m.get('WorkerId')

        return self

