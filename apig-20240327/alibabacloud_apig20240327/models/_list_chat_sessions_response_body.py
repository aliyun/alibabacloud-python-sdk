# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class ListChatSessionsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListChatSessionsResponseBodyData = None,
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
        # The pagination token for the next page. An empty value indicates that the last page has been reached.
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
            temp_model = main_models.ListChatSessionsResponseBodyData()
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

class ListChatSessionsResponseBodyData(DaraModel):
    def __init__(
        self,
        content: List[main_models.ListChatSessionsResponseBodyDataContent] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The list of chat sessions. Each element in the list is named session and represents a chat session.
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
                temp_model = main_models.ListChatSessionsResponseBodyDataContent()
                self.content.append(temp_model.from_map(k1))

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListChatSessionsResponseBodyDataContent(DaraModel):
    def __init__(
        self,
        name: str = None,
        products: List[str] = None,
        session_id: str = None,
        talk_type: str = None,
    ):
        # The name of the chat session.
        self.name = name
        # The list of API products associated with the session. Each element in the list is named product.
        self.products = products
        # The ID of the chat session. You can use this ID to locate the session in API operations such as UpdateChatSession, DeleteChatSession, and ListConversations.
        self.session_id = session_id
        # The conversation type of the session. Valid values: MODEL and AGENT. These values are defined in the talkType enumeration of the CreateChatSession request parameter, and this response parameter does not have the @enums annotation.
        self.talk_type = talk_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.products is not None:
            result['products'] = self.products

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.talk_type is not None:
            result['talkType'] = self.talk_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('products') is not None:
            self.products = m.get('products')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('talkType') is not None:
            self.talk_type = m.get('talkType')

        return self

