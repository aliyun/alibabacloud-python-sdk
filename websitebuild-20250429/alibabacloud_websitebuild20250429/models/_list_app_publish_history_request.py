# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAppPublishHistoryRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        keyword: str = None,
        max_results: int = None,
        next_token: str = None,
        page_num: int = None,
        page_size: int = None,
        sort: str = None,
        status: str = None,
        website_domain: str = None,
    ):
        self.biz_id = biz_id
        self.keyword = keyword
        self.max_results = max_results
        self.next_token = next_token
        self.page_num = page_num
        self.page_size = page_size
        self.sort = sort
        self.status = status
        self.website_domain = website_domain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sort is not None:
            result['Sort'] = self.sort

        if self.status is not None:
            result['Status'] = self.status

        if self.website_domain is not None:
            result['WebsiteDomain'] = self.website_domain

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Sort') is not None:
            self.sort = m.get('Sort')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('WebsiteDomain') is not None:
            self.website_domain = m.get('WebsiteDomain')

        return self

