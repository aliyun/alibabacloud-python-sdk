# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_energyexpertexternal20220923 import models as main_models
from darabonba.model import DaraModel

class GetChatListResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetChatListResponseBodyData = None,
        request_id: str = None,
    ):
        # Returned data structure.
        self.data = data
        # Request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.GetChatListResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetChatListResponseBodyData(DaraModel):
    def __init__(
        self,
        chat_list: List[main_models.ChatItem] = None,
        current_page: int = None,
        page_size: int = None,
        total: int = None,
        total_page: int = None,
    ):
        # Q&A list.
        self.chat_list = chat_list
        # Current page number.
        self.current_page = current_page
        # Page size.
        self.page_size = page_size
        # Total number of records.
        self.total = total
        # Total number of pages.
        self.total_page = total_page

    def validate(self):
        if self.chat_list:
            for v1 in self.chat_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['chatList'] = []
        if self.chat_list is not None:
            for k1 in self.chat_list:
                result['chatList'].append(k1.to_map() if k1 else None)

        if self.current_page is not None:
            result['currentPage'] = self.current_page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.total is not None:
            result['total'] = self.total

        if self.total_page is not None:
            result['totalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.chat_list = []
        if m.get('chatList') is not None:
            for k1 in m.get('chatList'):
                temp_model = main_models.ChatItem()
                self.chat_list.append(temp_model.from_map(k1))

        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('total') is not None:
            self.total = m.get('total')

        if m.get('totalPage') is not None:
            self.total_page = m.get('totalPage')

        return self

