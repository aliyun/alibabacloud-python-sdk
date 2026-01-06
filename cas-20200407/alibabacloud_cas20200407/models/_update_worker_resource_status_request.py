# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateWorkerResourceStatusRequest(DaraModel):
    def __init__(
        self,
        job_id: int = None,
        status: str = None,
        worker_id: int = None,
    ):
        # The ID of the deployment task. You can call the [CreateDeploymentJob](https://help.aliyun.com/document_detail/2712234.html) operation to obtain the ID of a deployment task from the **JobId** parameter. You can also call the [ListDeploymentJob](https://help.aliyun.com/document_detail/2712223.html) operation to obtain the ID of a deployment task.
        # 
        # This parameter is required.
        self.job_id = job_id
        # The desired status.
        # 
        # Valid values:
        # 
        # *   rollback
        # 
        # This parameter is required.
        self.status = status
        # The ID of the worker task. You can call the [ListWorkerResource](https://help.aliyun.com/document_detail/2712224.html) operation to obtain the ID of a worker task.
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

        if self.status is not None:
            result['Status'] = self.status

        if self.worker_id is not None:
            result['WorkerId'] = self.worker_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('WorkerId') is not None:
            self.worker_id = m.get('WorkerId')

        return self

