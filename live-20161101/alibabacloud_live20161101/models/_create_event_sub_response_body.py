# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateEventSubResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        subscribe_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The subscription ID.
        self.subscribe_id = subscribe_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.subscribe_id is not None:
            result['SubscribeId'] = self.subscribe_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SubscribeId') is not None:
            self.subscribe_id = m.get('SubscribeId')

        return self

