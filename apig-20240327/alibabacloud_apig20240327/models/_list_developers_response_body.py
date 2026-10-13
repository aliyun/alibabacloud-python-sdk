# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class ListDevelopersResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListDevelopersResponseBodyData = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The response status code.
        self.code = code
        # The response data.
        self.data = data
        # The maximum number of entries on the current page.
        self.max_results = max_results
        # The response message.
        self.message = message
        # The cursor for the next page. An empty value indicates that the last page has been reached.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.message is not None:
            result['message'] = self.message

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.ListDevelopersResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListDevelopersResponseBodyData(DaraModel):
    def __init__(
        self,
        content: List[main_models.ListDevelopersResponseBodyDataContent] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The list of developers.
        self.content = content
        # The page number.
        self.page_number = page_number
        # The page size.
        self.page_size = page_size
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.content:
            for v1 in self.content:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['content'] = []
        if self.content is not None:
            for k1 in self.content:
                result['content'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content = []
        if m.get('content') is not None:
            for k1 in m.get('content'):
                temp_model = main_models.ListDevelopersResponseBodyDataContent()
                self.content.append(temp_model.from_map(k1))

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListDevelopersResponseBodyDataContent(DaraModel):
    def __init__(
        self,
        developer_id: str = None,
        portal_id: str = None,
        status: str = None,
        username: str = None,
    ):
        # The developer ID. You can use this ID to locate the developer in API operations such as SetHiMarketDeveloperStatus and DeleteHiMarketDeveloper.
        self.developer_id = developer_id
        # The ID of the portal to which the developer belongs. You can use this ID to locate the portal in API operations such as GetPortal, UpdatePortal, and DeletePortal.
        self.portal_id = portal_id
        # The status of the developer. Valid values: PENDING, APPROVED, and REJECTED.
        self.status = status
        # The logon username of the developer.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.developer_id is not None:
            result['developerId'] = self.developer_id

        if self.portal_id is not None:
            result['portalId'] = self.portal_id

        if self.status is not None:
            result['status'] = self.status

        if self.username is not None:
            result['username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('developerId') is not None:
            self.developer_id = m.get('developerId')

        if m.get('portalId') is not None:
            self.portal_id = m.get('portalId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('username') is not None:
            self.username = m.get('username')

        return self

