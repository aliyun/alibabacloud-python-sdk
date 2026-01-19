# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDemoInstanceRequest(DaraModel):
    def __init__(
        self,
        outbound_call_whitelist: str = None,
    ):
        # This parameter is required.
        self.outbound_call_whitelist = outbound_call_whitelist

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.outbound_call_whitelist is not None:
            result['OutboundCallWhitelist'] = self.outbound_call_whitelist

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutboundCallWhitelist') is not None:
            self.outbound_call_whitelist = m.get('OutboundCallWhitelist')

        return self

