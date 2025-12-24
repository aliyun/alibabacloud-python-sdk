# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PlayChoosenShowResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        show_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The ID of the episode.
        self.show_id = show_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.show_id is not None:
            result['ShowId'] = self.show_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ShowId') is not None:
            self.show_id = m.get('ShowId')

        return self

