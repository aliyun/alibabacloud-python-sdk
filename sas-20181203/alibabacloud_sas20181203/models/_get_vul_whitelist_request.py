# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetVulWhitelistRequest(DaraModel):
    def __init__(
        self,
        vul_whitelist_id: int = None,
    ):
        # The ID of the whitelist.
        self.vul_whitelist_id = vul_whitelist_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.vul_whitelist_id is not None:
            result['VulWhitelistId'] = self.vul_whitelist_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VulWhitelistId') is not None:
            self.vul_whitelist_id = m.get('VulWhitelistId')

        return self

