# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeIpStatusRequest(DaraModel):
    def __init__(
        self,
        ips: str = None,
    ):
        # The IP addresses that you want to query. Separate IP addresses with underscores (_), such as Ips=ip1_ip2.
        # 
        # This parameter is required.
        self.ips = ips

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ips is not None:
            result['Ips'] = self.ips

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ips') is not None:
            self.ips = m.get('Ips')

        return self

