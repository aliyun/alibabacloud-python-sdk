# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLiveStreamStateResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        stream_state: str = None,
        type: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The state of the stream. Valid values:
        # 
        # - online: The stream is active.
        # 
        # - offline: The stream is offline. This may mean the stream ingest has failed or ended. For specific details, use the data returned by the stream ingest callback. This operation does not provide a detailed breakdown of the offline status.
        self.stream_state = stream_state
        # The stream ingest method. Valid values:
        # 
        # - push
        # 
        # - pull
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.stream_state is not None:
            result['StreamState'] = self.stream_state

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StreamState') is not None:
            self.stream_state = m.get('StreamState')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

