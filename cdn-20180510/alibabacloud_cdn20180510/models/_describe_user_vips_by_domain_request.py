# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeUserVipsByDomainRequest(DaraModel):
    def __init__(
        self,
        available: str = None,
        domain_name: str = None,
    ):
        # Specifies whether to query the virtual IP addresses of only healthy CDN POPs. Valid values:
        # 
        # *   **on**: healthy CDN edge nodes.
        # *   **off**: all CDN edge nodes.
        self.available = available
        # The accelerated domain name. You can specify only one domain name.
        # 
        # This parameter is required.
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available is not None:
            result['Available'] = self.available

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Available') is not None:
            self.available = m.get('Available')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        return self

