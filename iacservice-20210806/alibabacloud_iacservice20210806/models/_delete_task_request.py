# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteTaskRequest(DaraModel):
    def __init__(
        self,
        resource_retention_policy: str = None,
    ):
        # The data retention policy. If this parameter is not specified, the policy is unconfirmed. If the node has resources or the resource status is unknown, the operation returns a confirmation fault. Set this parameter to RETAIN to delete only the node management record and retain the cloud resources.
        self.resource_retention_policy = resource_retention_policy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_retention_policy is not None:
            result['resourceRetentionPolicy'] = self.resource_retention_policy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceRetentionPolicy') is not None:
            self.resource_retention_policy = m.get('resourceRetentionPolicy')

        return self

