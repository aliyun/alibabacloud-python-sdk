# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSkillsRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        order_by: str = None,
        owner: str = None,
        page_no: int = None,
        page_size: int = None,
        scope: str = None,
        search: str = None,
        skill_name: str = None,
    ):
        # The maximum number of entries to return per page.
        self.max_results = max_results
        # The pagination token for the next page.
        self.next_token = next_token
        # The sort field. The value download_count is supported. Default value: gmt_modified.
        self.order_by = order_by
        # Filters results by owner.
        self.owner = owner
        # The page number. Default value: 1.
        self.page_no = page_no
        # The number of entries per page. Default value: 10. Maximum value: 50.
        self.page_size = page_size
        # Filters results by visibility. Valid values:
        # - PUBLIC
        # - PRIVATE
        self.scope = scope
        # The search mode. Valid values:
        # - accurate: exact match.
        # - blur: fuzzy match.
        self.search = search
        # The filter keyword.
        self.skill_name = skill_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.order_by is not None:
            result['orderBy'] = self.order_by

        if self.owner is not None:
            result['owner'] = self.owner

        if self.page_no is not None:
            result['pageNo'] = self.page_no

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.scope is not None:
            result['scope'] = self.scope

        if self.search is not None:
            result['search'] = self.search

        if self.skill_name is not None:
            result['skillName'] = self.skill_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')

        if m.get('owner') is not None:
            self.owner = m.get('owner')

        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('scope') is not None:
            self.scope = m.get('scope')

        if m.get('search') is not None:
            self.search = m.get('search')

        if m.get('skillName') is not None:
            self.skill_name = m.get('skillName')

        return self

