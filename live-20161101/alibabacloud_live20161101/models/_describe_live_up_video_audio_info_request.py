# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLiveUpVideoAudioInfoRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        owner_id: int = None,
        region_id: str = None,
        start_time: str = None,
        stream: str = None,
    ):
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.end_time = end_time
        self.owner_id = owner_id
        self.region_id = region_id
        # The name of the stream that you want to query. Specify this parameter in the following format: `rtmp://Ingest domain/Application name/Stream name`.
        self.start_time = start_time
        # The operation that you want to perform. Set the value to **DescribeLiveUpVideoAudioInfo**.
        # 
        # This parameter is required.
        self.stream = stream

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.stream is not None:
            result['Stream'] = self.stream

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Stream') is not None:
            self.stream = m.get('Stream')

        return self

