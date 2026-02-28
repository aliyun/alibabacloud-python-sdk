# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeEndPointMetricDataRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        created_ts: int = None,
        destroyed_ts: int = None,
        metrics: str = None,
        pub_call_id_list: str = None,
        pub_user_id: str = None,
        sub_user_id: str = None,
    ):
        # APP ID。
        # 
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.channel_id = channel_id
        # This parameter is required.
        self.created_ts = created_ts
        self.destroyed_ts = destroyed_ts
        # This parameter is required.
        self.metrics = metrics
        self.pub_call_id_list = pub_call_id_list
        self.pub_user_id = pub_user_id
        self.sub_user_id = sub_user_id

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

        if self.metrics is not None:
            result['Metrics'] = self.metrics

        if self.pub_call_id_list is not None:
            result['PubCallIdList'] = self.pub_call_id_list

        if self.pub_user_id is not None:
            result['PubUserId'] = self.pub_user_id

        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id

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

        if m.get('Metrics') is not None:
            self.metrics = m.get('Metrics')

        if m.get('PubCallIdList') is not None:
            self.pub_call_id_list = m.get('PubCallIdList')

        if m.get('PubUserId') is not None:
            self.pub_user_id = m.get('PubUserId')

        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')

        return self

