# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListHiMarketConsumersRequest(DaraModel):
    def __init__(
        self,
        developer_id: str = None,
        max_results: int = None,
        name: str = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        portal_id: str = None,
    ):
        # The developer ID. This parameter is used to filter consumers by developer.
        self.developer_id = developer_id
        # The maximum number of entries per page. The default value and valid values are not specified in the API definition.
        self.max_results = max_results
        # The search keyword for the consumer name.
        self.name = name
        # The pagination token. To retrieve the next page, pass the nextToken value returned in the previous response. Do not specify this parameter for the first query.
        self.next_token = next_token
        # The page number. Pages start from 1.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The portal ID. This parameter is used to filter consumers by portal.
        self.portal_id = portal_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.developer_id is not None:
            result['developerId'] = self.developer_id

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.name is not None:
            result['name'] = self.name

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.portal_id is not None:
            result['portalId'] = self.portal_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('developerId') is not None:
            self.developer_id = m.get('developerId')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('portalId') is not None:
            self.portal_id = m.get('portalId')

        return self

