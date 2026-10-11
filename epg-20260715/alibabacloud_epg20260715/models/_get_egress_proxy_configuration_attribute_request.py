# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetEgressProxyConfigurationAttributeRequest(DaraModel):
    def __init__(
        self,
        egress_proxy_configuration_id: str = None,
    ):
        # The ID of the egress proxy configuration.
        # 
        # This parameter is required.
        self.egress_proxy_configuration_id = egress_proxy_configuration_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.egress_proxy_configuration_id is not None:
            result['EgressProxyConfigurationId'] = self.egress_proxy_configuration_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EgressProxyConfigurationId') is not None:
            self.egress_proxy_configuration_id = m.get('EgressProxyConfigurationId')

        return self

