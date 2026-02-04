# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetHandshakeRequest(DaraModel):
    def __init__(
        self,
        handshake_id: str = None,
    ):
        # The ID of the invitation.
        # 
        # This parameter is required.
        self.handshake_id = handshake_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.handshake_id is not None:
            result['HandshakeId'] = self.handshake_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HandshakeId') is not None:
            self.handshake_id = m.get('HandshakeId')

        return self

