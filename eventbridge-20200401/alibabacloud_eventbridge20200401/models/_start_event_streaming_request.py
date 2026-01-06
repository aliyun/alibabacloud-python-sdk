# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartEventStreamingRequest(DaraModel):
    def __init__(
        self,
        event_streaming_name: str = None,
    ):
        # The name of the event stream that you want to enable.
        # 
        # This parameter is required.
        self.event_streaming_name = event_streaming_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_streaming_name is not None:
            result['EventStreamingName'] = self.event_streaming_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventStreamingName') is not None:
            self.event_streaming_name = m.get('EventStreamingName')

        return self

