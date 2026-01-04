# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateNetworkAccessEndpointResponseBody(DaraModel):
    def __init__(
        self,
        network_access_endpoint_id: str = None,
        request_id: str = None,
    ):
        # The unique identifier of the network access endpoint.
        self.network_access_endpoint_id = network_access_endpoint_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.network_access_endpoint_id is not None:
            result['NetworkAccessEndpointId'] = self.network_access_endpoint_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkAccessEndpointId') is not None:
            self.network_access_endpoint_id = m.get('NetworkAccessEndpointId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

