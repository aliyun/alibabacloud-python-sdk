# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateWorkspaceRoleResponseBody(DaraModel):
    def __init__(
        self,
        instance_job_id: str = None,
        request_id: str = None,
    ):
        # The job ID for the request.
        self.instance_job_id = instance_job_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_job_id is not None:
            result['InstanceJobId'] = self.instance_job_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceJobId') is not None:
            self.instance_job_id = m.get('InstanceJobId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

