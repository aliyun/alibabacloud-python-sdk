# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateLivePackageChannelRequest(DaraModel):
    def __init__(
        self,
        channel_name: str = None,
        description: str = None,
        group_name: str = None,
        protocol: str = None,
        segment_count: int = None,
        segment_duration: int = None,
    ):
        # The channel name. It can contain letters, digits, hyphens (-), and underscores (_). The name must be 1 to 200 characters in length. Format: [A-Za-z0-9_-]+
        # 
        # This parameter is required.
        self.channel_name = channel_name
        # The channel description. It can be up to 1,000 characters in length.
        self.description = description
        # The channel group name. It can contain letters, digits, hyphens (-), and underscores (_). The name must be 1 to 200 characters in length. Format: [A-Za-z0-9_-]+
        # 
        # This parameter is required.
        self.group_name = group_name
        # The ingest protocol. Only HLS is supported.
        # 
        # This parameter is required.
        self.protocol = protocol
        # The number of M3U8 segments. Valid values: 2 to 100.
        # 
        # This parameter is required.
        self.segment_count = segment_count
        # The segment duration. Valid values: 1 to 30.
        # 
        # This parameter is required.
        self.segment_duration = segment_duration

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_name is not None:
            result['ChannelName'] = self.channel_name

        if self.description is not None:
            result['Description'] = self.description

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.segment_count is not None:
            result['SegmentCount'] = self.segment_count

        if self.segment_duration is not None:
            result['SegmentDuration'] = self.segment_duration

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelName') is not None:
            self.channel_name = m.get('ChannelName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('SegmentCount') is not None:
            self.segment_count = m.get('SegmentCount')

        if m.get('SegmentDuration') is not None:
            self.segment_duration = m.get('SegmentDuration')

        return self

