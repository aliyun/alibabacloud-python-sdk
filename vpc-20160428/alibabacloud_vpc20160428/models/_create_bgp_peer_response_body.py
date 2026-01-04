# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateBgpPeerResponseBody(DaraModel):
    def __init__(
        self,
        bgp_peer_id: str = None,
        request_id: str = None,
    ):
        # The ID of the BGP peer.
        self.bgp_peer_id = bgp_peer_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bgp_peer_id is not None:
            result['BgpPeerId'] = self.bgp_peer_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BgpPeerId') is not None:
            self.bgp_peer_id = m.get('BgpPeerId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

