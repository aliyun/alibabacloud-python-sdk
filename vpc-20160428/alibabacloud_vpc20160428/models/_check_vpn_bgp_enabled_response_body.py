# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckVpnBgpEnabledResponseBody(DaraModel):
    def __init__(
        self,
        bgp_enabled: bool = None,
        request_id: str = None,
    ):
        # Indicates whether the region supports BGP.
        # 
        # *   **true**
        # *   **false**
        self.bgp_enabled = bgp_enabled
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bgp_enabled is not None:
            result['BgpEnabled'] = self.bgp_enabled

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BgpEnabled') is not None:
            self.bgp_enabled = m.get('BgpEnabled')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

