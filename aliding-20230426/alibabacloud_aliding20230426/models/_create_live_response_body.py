# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateLiveResponseBody(DaraModel):
    def __init__(
        self,
        live_id: str = None,
        request_id: str = None,
    ):
        self.live_id = live_id
        # requestId
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.live_id is not None:
            result['liveId'] = self.live_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('liveId') is not None:
            self.live_id = m.get('liveId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

