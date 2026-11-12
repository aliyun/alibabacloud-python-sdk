# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RebuildSandboxRequest(DaraModel):
    def __init__(
        self,
        service_endpoint_id: str = None,
    ):
        # The service registration endpoint ID. This parameter is optional. If specified, the operation targets the runtime instance corresponding to the service registration endpoint under the agent. If omitted, the default latest runtime identity is used. Pass the service registration endpoint ID, not the service registration endpoint name. Keep this parameter consistent when querying instances, committing the rebuild, and querying nodes.
        self.service_endpoint_id = service_endpoint_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.service_endpoint_id is not None:
            result['serviceEndpointId'] = self.service_endpoint_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('serviceEndpointId') is not None:
            self.service_endpoint_id = m.get('serviceEndpointId')

        return self

