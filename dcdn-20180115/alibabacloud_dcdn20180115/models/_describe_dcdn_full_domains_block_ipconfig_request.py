# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDcdnFullDomainsBlockIPConfigRequest(DaraModel):
    def __init__(
        self,
        iplist: str = None,
    ):
        # The IP address or CIDR block to query. Separate multiple values with commas (,). You can specify up to 50 IP addresses or CIDR blocks.
        self.iplist = iplist

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.iplist is not None:
            result['IPList'] = self.iplist

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IPList') is not None:
            self.iplist = m.get('IPList')

        return self

