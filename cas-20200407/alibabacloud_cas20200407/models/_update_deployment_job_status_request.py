# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDeploymentJobStatusRequest(DaraModel):
    def __init__(
        self,
        job_id: int = None,
        status: str = None,
    ):
        # The ID of the deployment task.
        # 
        # This parameter is required.
        self.job_id = job_id
        # The desired status.
        # 
        # Valid values:
        # 
        # *   pending
        # *   scheduling
        # *   editing
        # 
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

