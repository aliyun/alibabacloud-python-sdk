# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteInstanceIpWhitelistShrinkRequest(DaraModel):
    def __init__(
        self,
        ip_whitelist: str = None,
        ip_whitelists_shrink: str = None,
    ):
        # The IP address whitelist.
        self.ip_whitelist = ip_whitelist
        # The IP address whitelist.
        self.ip_whitelists_shrink = ip_whitelists_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip_whitelist is not None:
            result['ipWhitelist'] = self.ip_whitelist

        if self.ip_whitelists_shrink is not None:
            result['ipWhitelists'] = self.ip_whitelists_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ipWhitelist') is not None:
            self.ip_whitelist = m.get('ipWhitelist')

        if m.get('ipWhitelists') is not None:
            self.ip_whitelists_shrink = m.get('ipWhitelists')

        return self

