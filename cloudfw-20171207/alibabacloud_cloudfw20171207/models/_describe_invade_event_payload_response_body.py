# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeInvadeEventPayloadResponseBody(DaraModel):
    def __init__(
        self,
        assets_instance_id: str = None,
        event_uuid: str = None,
        highlight_end: int = None,
        highlight_start: int = None,
        payload: str = None,
        payload_len: int = None,
        request_id: str = None,
    ):
        # The instance ID of the asset to which the event belongs.
        self.assets_instance_id = assets_instance_id
        # The UUID of the event.
        self.event_uuid = event_uuid
        # The end position (character index) of the matched content in the payload.
        self.highlight_end = highlight_end
        # The start position (character index) of the matched content in the payload.
        self.highlight_start = highlight_start
        # The original packet payload of the intrusion event.
        self.payload = payload
        # The length of the payload in bytes.
        self.payload_len = payload_len
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assets_instance_id is not None:
            result['AssetsInstanceId'] = self.assets_instance_id

        if self.event_uuid is not None:
            result['EventUuid'] = self.event_uuid

        if self.highlight_end is not None:
            result['HighlightEnd'] = self.highlight_end

        if self.highlight_start is not None:
            result['HighlightStart'] = self.highlight_start

        if self.payload is not None:
            result['Payload'] = self.payload

        if self.payload_len is not None:
            result['PayloadLen'] = self.payload_len

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetsInstanceId') is not None:
            self.assets_instance_id = m.get('AssetsInstanceId')

        if m.get('EventUuid') is not None:
            self.event_uuid = m.get('EventUuid')

        if m.get('HighlightEnd') is not None:
            self.highlight_end = m.get('HighlightEnd')

        if m.get('HighlightStart') is not None:
            self.highlight_start = m.get('HighlightStart')

        if m.get('Payload') is not None:
            self.payload = m.get('Payload')

        if m.get('PayloadLen') is not None:
            self.payload_len = m.get('PayloadLen')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

