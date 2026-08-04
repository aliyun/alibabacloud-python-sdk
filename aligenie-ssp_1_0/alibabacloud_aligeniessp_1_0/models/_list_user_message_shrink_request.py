# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListUserMessageShrinkRequest(DaraModel):
    def __init__(
        self,
        before_time: str = None,
        user_info_shrink: str = None,
        limit: int = None,
    ):
        # After a specific point in time
        self.before_time = before_time
        # User identifier information
        # 
        # This parameter is required.
        self.user_info_shrink = user_info_shrink
        # Number of records to query
        self.limit = limit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.before_time is not None:
            result['BeforeTime'] = self.before_time

        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink

        if self.limit is not None:
            result['limit'] = self.limit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeforeTime') is not None:
            self.before_time = m.get('BeforeTime')

        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')

        if m.get('limit') is not None:
            self.limit = m.get('limit')

        return self

