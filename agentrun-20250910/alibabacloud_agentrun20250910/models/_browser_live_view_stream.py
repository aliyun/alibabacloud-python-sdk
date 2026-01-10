# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BrowserLiveViewStream(DaraModel):
    def __init__(
        self,
        stream_endpoint: str = None,
    ):
        self.stream_endpoint = stream_endpoint

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.stream_endpoint is not None:
            result['streamEndpoint'] = self.stream_endpoint

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('streamEndpoint') is not None:
            self.stream_endpoint = m.get('streamEndpoint')

        return self

