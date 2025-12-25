# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRCDeploymentSetResponseBody(DaraModel):
    def __init__(
        self,
        deployment_set_id: str = None,
        request_id: str = None,
    ):
        # The deployment set ID.
        self.deployment_set_id = deployment_set_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deployment_set_id is not None:
            result['DeploymentSetId'] = self.deployment_set_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeploymentSetId') is not None:
            self.deployment_set_id = m.get('DeploymentSetId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

