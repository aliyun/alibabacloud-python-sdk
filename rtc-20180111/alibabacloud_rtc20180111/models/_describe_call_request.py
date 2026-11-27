# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCallRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        created_ts: int = None,
        destroyed_ts: int = None,
        ext_data_type: str = None,
        query_exp_info: bool = None,
    ):
        # The app ID.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The channel ID.
        # 
        # This parameter is required.
        self.channel_id = channel_id
        # The time when the channel was created. You can query data of the last 30 days. The time is a UNIX timestamp in seconds.
        # > The channel creation time must be exactly the same as the actual creation time (accurate to the second). You can call the [DescribeCallList](https://help.aliyun.com/document_detail/2655884.html) operation to view the channel creation time (the CreatedTS parameter in the response).
        # 
        # This parameter is required.
        self.created_ts = created_ts
        # The time when the channel was released. The time is a UNIX timestamp in seconds. If this parameter is left empty, the current time is used.
        # > If the specified channel release time is later than the actual release time, the data from the creation time to the actual release time is returned.
        self.destroyed_ts = destroyed_ts
        # The extended data type to query. Valid values:
        # - USER_DURATION_STAT: user duration statistics.
        self.ext_data_type = ext_data_type
        # Specifies whether to query the communication experience information. Default value: true.
        self.query_exp_info = query_exp_info

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

        if self.ext_data_type is not None:
            result['ExtDataType'] = self.ext_data_type

        if self.query_exp_info is not None:
            result['QueryExpInfo'] = self.query_exp_info

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

        if m.get('ExtDataType') is not None:
            self.ext_data_type = m.get('ExtDataType')

        if m.get('QueryExpInfo') is not None:
            self.query_exp_info = m.get('QueryExpInfo')

        return self

