# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAppConversationsRequest(DaraModel):
    def __init__(
        self,
        bot_id: str = None,
        end_modify_time: str = None,
        max_results: int = None,
        next_token: str = None,
        page_num: int = None,
        page_size: int = None,
        site_id: str = None,
        start_modify_time: str = None,
    ):
        self.bot_id = bot_id
        self.end_modify_time = end_modify_time
        self.max_results = max_results
        self.next_token = next_token
        self.page_num = page_num
        self.page_size = page_size
        self.site_id = site_id
        self.start_modify_time = start_modify_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bot_id is not None:
            result['BotId'] = self.bot_id

        if self.end_modify_time is not None:
            result['EndModifyTime'] = self.end_modify_time

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.start_modify_time is not None:
            result['StartModifyTime'] = self.start_modify_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BotId') is not None:
            self.bot_id = m.get('BotId')

        if m.get('EndModifyTime') is not None:
            self.end_modify_time = m.get('EndModifyTime')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('StartModifyTime') is not None:
            self.start_modify_time = m.get('StartModifyTime')

        return self

