# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateNetworkDomainResponseBody(DaraModel):
    def __init__(
        self,
        network_domain_id: str = None,
        request_id: str = None,
    ):
        # The ID of the network domain.
        self.network_domain_id = network_domain_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.network_domain_id is not None:
            result['NetworkDomainId'] = self.network_domain_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkDomainId') is not None:
            self.network_domain_id = m.get('NetworkDomainId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

