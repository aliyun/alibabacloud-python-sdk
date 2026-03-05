# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryContentListRequest(DaraModel):
    def __init__(
        self,
        brand_user_id: int = None,
        brand_user_nick: str = None,
        channel_id: str = None,
        proxy_user_id: int = None,
        task_biz_type: str = None,
        task_type: str = None,
    ):
        self.brand_user_id = brand_user_id
        self.brand_user_nick = brand_user_nick
        # This parameter is required.
        self.channel_id = channel_id
        # This parameter is required.
        self.proxy_user_id = proxy_user_id
        # This parameter is required.
        self.task_biz_type = task_biz_type
        # This parameter is required.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.brand_user_id is not None:
            result['BrandUserId'] = self.brand_user_id

        if self.brand_user_nick is not None:
            result['BrandUserNick'] = self.brand_user_nick

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.proxy_user_id is not None:
            result['ProxyUserId'] = self.proxy_user_id

        if self.task_biz_type is not None:
            result['TaskBizType'] = self.task_biz_type

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BrandUserId') is not None:
            self.brand_user_id = m.get('BrandUserId')

        if m.get('BrandUserNick') is not None:
            self.brand_user_nick = m.get('BrandUserNick')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('ProxyUserId') is not None:
            self.proxy_user_id = m.get('ProxyUserId')

        if m.get('TaskBizType') is not None:
            self.task_biz_type = m.get('TaskBizType')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

