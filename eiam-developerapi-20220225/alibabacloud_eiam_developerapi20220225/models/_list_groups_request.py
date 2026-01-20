# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListGroupsRequest(DaraModel):
    def __init__(
        self,
        group_name_start_with: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # The prefix of the group name.
        self.group_name_start_with = group_name_start_with
        # The number of entries per page. Default value: 20.
        self.max_results = max_results
        # nextToken
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_name_start_with is not None:
            result['groupNameStartWith'] = self.group_name_start_with

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupNameStartWith') is not None:
            self.group_name_start_with = m.get('groupNameStartWith')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        return self

