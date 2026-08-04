# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModelRouterQueryApiKeyListRequest(DaraModel):
    def __init__(
        self,
        client_id: int = None,
        group_by: str = None,
        include_member_keys: bool = None,
        keyword: str = None,
        max_results: int = None,
        member_user_ids: str = None,
        need_total_count: bool = None,
        next_token: str = None,
        order_by: str = None,
        order_direction: str = None,
        page_index: int = None,
        page_size: int = None,
        status: int = None,
    ):
        # The client ID used to filter the results.
        self.client_id = client_id
        # The field by which to group the results.
        self.group_by = group_by
        # Optional. If set to true, the keys of members under the department are also included when filtering by department.
        self.include_member_keys = include_member_keys
        # The search keyword.
        self.keyword = keyword
        # The maximum number of results to return.
        self.max_results = max_results
        # Optional. Filters by member IDs. Separate multiple member IDs with commas. If this parameter is not specified, the department and all its members are included. If an empty value is specified, only the department is included without members.
        self.member_user_ids = member_user_ids
        # Specifies whether to return the total count.
        self.need_total_count = need_total_count
        # The pagination token. An empty value indicates that no more pages are available.
        self.next_token = next_token
        # The field by which to sort the results.
        self.order_by = order_by
        # The sort direction.
        self.order_direction = order_direction
        # The page number.
        self.page_index = page_index
        # The number of entries per page.
        self.page_size = page_size
        # The status used to filter the results.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_id is not None:
            result['clientId'] = self.client_id

        if self.group_by is not None:
            result['groupBy'] = self.group_by

        if self.include_member_keys is not None:
            result['includeMemberKeys'] = self.include_member_keys

        if self.keyword is not None:
            result['keyword'] = self.keyword

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.member_user_ids is not None:
            result['memberUserIds'] = self.member_user_ids

        if self.need_total_count is not None:
            result['needTotalCount'] = self.need_total_count

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.order_by is not None:
            result['orderBy'] = self.order_by

        if self.order_direction is not None:
            result['orderDirection'] = self.order_direction

        if self.page_index is not None:
            result['pageIndex'] = self.page_index

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientId') is not None:
            self.client_id = m.get('clientId')

        if m.get('groupBy') is not None:
            self.group_by = m.get('groupBy')

        if m.get('includeMemberKeys') is not None:
            self.include_member_keys = m.get('includeMemberKeys')

        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('memberUserIds') is not None:
            self.member_user_ids = m.get('memberUserIds')

        if m.get('needTotalCount') is not None:
            self.need_total_count = m.get('needTotalCount')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')

        if m.get('orderDirection') is not None:
            self.order_direction = m.get('orderDirection')

        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

