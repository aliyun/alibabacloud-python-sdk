# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteEventStreamingRequest(DaraModel):
    def __init__(
        self,
        event_streaming_name: str = None,
        force: bool = None,
    ):
        # The name of the event stream to delete.
        # 
        # This parameter is required.
        self.event_streaming_name = event_streaming_name
        # Specifies whether to force delete the event stream. If set to true, system label-based deletion protection is bypassed. Default value: false.
        self.force = force

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_streaming_name is not None:
            result['EventStreamingName'] = self.event_streaming_name

        if self.force is not None:
            result['Force'] = self.force

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventStreamingName') is not None:
            self.event_streaming_name = m.get('EventStreamingName')

        if m.get('Force') is not None:
            self.force = m.get('Force')

        return self

