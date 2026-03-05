# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryUnionTaskListRequest(DaraModel):
    def __init__(
        self,
        brand_user_id: int = None,
        brand_user_nick: str = None,
        channel_id: str = None,
        page_index: int = None,
        page_size: int = None,
        proxy_user_id: int = None,
    ):
        self.brand_user_id = brand_user_id
        self.brand_user_nick = brand_user_nick
        # This parameter is required.
        self.channel_id = channel_id
        # This parameter is required.
        self.page_index = page_index
        # This parameter is required.
        self.page_size = page_size
        # This parameter is required.
        self.proxy_user_id = proxy_user_id

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

        if self.page_index is not None:
            result['PageIndex'] = self.page_index

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.proxy_user_id is not None:
            result['ProxyUserId'] = self.proxy_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BrandUserId') is not None:
            self.brand_user_id = m.get('BrandUserId')

        if m.get('BrandUserNick') is not None:
            self.brand_user_nick = m.get('BrandUserNick')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProxyUserId') is not None:
            self.proxy_user_id = m.get('ProxyUserId')

        return self

