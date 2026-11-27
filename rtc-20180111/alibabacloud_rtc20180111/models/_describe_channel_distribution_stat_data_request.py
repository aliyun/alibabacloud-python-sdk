# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeChannelDistributionStatDataRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        created_ts: int = None,
        destroyed_ts: int = None,
        stat_dim: str = None,
    ):
        # The app ID.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The channel ID.
        # 
        # This parameter is required.
        self.channel_id = channel_id
        # The timestamp when the channel was created. You can query data from the last 30 days. The value is a UNIX timestamp in seconds.
        # 
        # This parameter is required.
        self.created_ts = created_ts
        # The timestamp when the channel was released. The value is a UNIX timestamp in seconds. If this parameter is empty, the current time is used.
        # > If the specified channel release time is later than the actual release time, the data from the creation time to the actual release time is returned.
        self.destroyed_ts = destroyed_ts
        # The statistical dimension. Valid values:
        # - **OS**: Statistics by operating system.
        # - **SDK_VERSION**: Statistics by SDK version.
        # 
        # This parameter is required.
        self.stat_dim = stat_dim

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

        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts

        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts

        if self.stat_dim is not None:
            result['StatDim'] = self.stat_dim

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')

        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')

        if m.get('StatDim') is not None:
            self.stat_dim = m.get('StatDim')

        return self

