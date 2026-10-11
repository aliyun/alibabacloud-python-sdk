# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateEgressProxyConfigurationResponseBody(DaraModel):
    def __init__(
        self,
        egress_proxy_configuration_id: str = None,
        request_id: str = None,
    ):
        # The ID of the egress proxy configuration.
        self.egress_proxy_configuration_id = egress_proxy_configuration_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.egress_proxy_configuration_id is not None:
            result['EgressProxyConfigurationId'] = self.egress_proxy_configuration_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EgressProxyConfigurationId') is not None:
            self.egress_proxy_configuration_id = m.get('EgressProxyConfigurationId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

