# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetEgressProxyIpPoolAttributeRequest(DaraModel):
    def __init__(
        self,
        egress_proxy_ip_pool_id: str = None,
    ):
        # This parameter is required.
        self.egress_proxy_ip_pool_id = egress_proxy_ip_pool_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.egress_proxy_ip_pool_id is not None:
            result['EgressProxyIpPoolId'] = self.egress_proxy_ip_pool_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EgressProxyIpPoolId') is not None:
            self.egress_proxy_ip_pool_id = m.get('EgressProxyIpPoolId')

        return self

