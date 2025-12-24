# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeUserConnectTimeRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        end_user_id: str = None,
        max_results: int = None,
        next_token: str = None,
        oversold_group_id: str = None,
        start_time: str = None,
        user_desktop_id: str = None,
        user_group_id: str = None,
    ):
        self.end_time = end_time
        self.end_user_id = end_user_id
        self.max_results = max_results
        self.next_token = next_token
        self.oversold_group_id = oversold_group_id
        self.start_time = start_time
        self.user_desktop_id = user_desktop_id
        self.user_group_id = user_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.oversold_group_id is not None:
            result['OversoldGroupId'] = self.oversold_group_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.user_desktop_id is not None:
            result['UserDesktopId'] = self.user_desktop_id

        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OversoldGroupId') is not None:
            self.oversold_group_id = m.get('OversoldGroupId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('UserDesktopId') is not None:
            self.user_desktop_id = m.get('UserDesktopId')

        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')

        return self

