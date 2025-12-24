# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeDesktopOversoldUserRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        end_user_id: str = None,
        max_results: int = None,
        next_token: str = None,
        oversold_group_id: str = None,
        user_desktop_ids: List[str] = None,
        user_group_id: str = None,
    ):
        self.client_token = client_token
        self.end_user_id = end_user_id
        self.max_results = max_results
        self.next_token = next_token
        self.oversold_group_id = oversold_group_id
        self.user_desktop_ids = user_desktop_ids
        self.user_group_id = user_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.oversold_group_id is not None:
            result['OversoldGroupId'] = self.oversold_group_id

        if self.user_desktop_ids is not None:
            result['UserDesktopIds'] = self.user_desktop_ids

        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OversoldGroupId') is not None:
            self.oversold_group_id = m.get('OversoldGroupId')

        if m.get('UserDesktopIds') is not None:
            self.user_desktop_ids = m.get('UserDesktopIds')

        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')

        return self

