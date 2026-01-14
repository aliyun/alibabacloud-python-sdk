# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateInstanceIpWhitelistRequest(DaraModel):
    def __init__(
        self,
        ip_whitelists: List[str] = None,
    ):
        # The IP address whitelists.
        # 
        # This parameter is required.
        self.ip_whitelists = ip_whitelists

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip_whitelists is not None:
            result['ipWhitelists'] = self.ip_whitelists

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ipWhitelists') is not None:
            self.ip_whitelists = m.get('ipWhitelists')

        return self

