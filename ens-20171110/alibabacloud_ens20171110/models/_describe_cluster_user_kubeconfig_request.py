# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeClusterUserKubeconfigRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        private_ip_address: bool = None,
    ):
        # This parameter is required.
        self.cluster_id = cluster_id
        self.private_ip_address = private_ip_address

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')

        return self

