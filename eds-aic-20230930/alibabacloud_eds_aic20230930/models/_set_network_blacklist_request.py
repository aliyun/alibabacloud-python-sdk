# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SetNetworkBlacklistRequest(DaraModel):
    def __init__(
        self,
        domain_blacklist: List[str] = None,
        ip_blacklist: List[str] = None,
    ):
        self.domain_blacklist = domain_blacklist
        self.ip_blacklist = ip_blacklist

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_blacklist is not None:
            result['DomainBlacklist'] = self.domain_blacklist

        if self.ip_blacklist is not None:
            result['IpBlacklist'] = self.ip_blacklist

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainBlacklist') is not None:
            self.domain_blacklist = m.get('DomainBlacklist')

        if m.get('IpBlacklist') is not None:
            self.ip_blacklist = m.get('IpBlacklist')

        return self

