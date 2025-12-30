# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListChannelsRequest(DaraModel):
    def __init__(
        self,
        channel_name: str = None,
        channel_tier: str = None,
        page_no: int = None,
        page_size: int = None,
        playback_mode: str = None,
        sort_by: str = None,
        sort_by_modified_time: str = None,
        state: int = None,
    ):
        # The name of the channel.
        self.channel_name = channel_name
        # The tier of the channel. Valid values: basic and standard.
        self.channel_tier = channel_tier
        # The page number. Default value: 1.
        self.page_no = page_no
        # The number of entries per page. Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size
        # The playback mode. Valid values: loop and linear.
        self.playback_mode = playback_mode
        # The sorting order by creation time. Valid values: asc and desc.
        self.sort_by = sort_by
        # The sorting order by modification time. Valid values: asc and desc.
        self.sort_by_modified_time = sort_by_modified_time
        # The channel status. A value of 0 specifies stopped. A value of 1 specifies started.
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_name is not None:
            result['ChannelName'] = self.channel_name

        if self.channel_tier is not None:
            result['ChannelTier'] = self.channel_tier

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.playback_mode is not None:
            result['PlaybackMode'] = self.playback_mode

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.sort_by_modified_time is not None:
            result['SortByModifiedTime'] = self.sort_by_modified_time

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelName') is not None:
            self.channel_name = m.get('ChannelName')

        if m.get('ChannelTier') is not None:
            self.channel_tier = m.get('ChannelTier')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PlaybackMode') is not None:
            self.playback_mode = m.get('PlaybackMode')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('SortByModifiedTime') is not None:
            self.sort_by_modified_time = m.get('SortByModifiedTime')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

