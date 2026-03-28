# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDeploymentResponseBody(DaraModel):
    def __init__(
        self,
        deployment_id: str = None,
        request_id: str = None,
    ):
        # Deployment record ID.
        self.deployment_id = deployment_id
        # Request ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deployment_id is not None:
            result['DeploymentId'] = self.deployment_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeploymentId') is not None:
            self.deployment_id = m.get('DeploymentId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

