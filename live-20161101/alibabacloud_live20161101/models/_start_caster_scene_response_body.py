# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartCasterSceneResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        stream_url: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The streaming URL of the scene. It is used for playback, but not for stream relay.
        self.stream_url = stream_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.stream_url is not None:
            result['StreamUrl'] = self.stream_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StreamUrl') is not None:
            self.stream_url = m.get('StreamUrl')

        return self

