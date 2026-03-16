# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeGroupUserRequest(DaraModel):
    def __init__(
        self,
        biz_type: str = None,
        business_channel: str = None,
        filter: str = None,
        group_id: str = None,
        max_results: int = None,
        next_token: str = None,
        solution_id: str = None,
    ):
        # >  This parameter is not available for public use.
        self.biz_type = biz_type
        self.business_channel = business_channel
        # The fuzzy search string that matches the username (EndUserId) and email address (Email) of the regular user.
        self.filter = filter
        # The ID of the user group.
        self.group_id = group_id
        # The number of entries to return on each page.
        self.max_results = max_results
        # The token for the next query. You can obtain this parameter from the response parameters of the last call to this operation.
        self.next_token = next_token
        # >  This parameter is not available for public use.
        self.solution_id = solution_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.business_channel is not None:
            result['BusinessChannel'] = self.business_channel

        if self.filter is not None:
            result['Filter'] = self.filter

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.solution_id is not None:
            result['SolutionId'] = self.solution_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('BusinessChannel') is not None:
            self.business_channel = m.get('BusinessChannel')

        if m.get('Filter') is not None:
            self.filter = m.get('Filter')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('SolutionId') is not None:
            self.solution_id = m.get('SolutionId')

        return self

