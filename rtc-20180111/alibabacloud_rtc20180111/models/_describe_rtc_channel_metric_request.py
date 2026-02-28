# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRtcChannelMetricRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        owner_id: int = None,
        time_point: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.channel_id = channel_id
        self.owner_id = owner_id
        # This parameter is required.
        self.time_point = time_point

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.time_point is not None:
            result['TimePoint'] = self.time_point

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('TimePoint') is not None:
            self.time_point = m.get('TimePoint')

        return self

