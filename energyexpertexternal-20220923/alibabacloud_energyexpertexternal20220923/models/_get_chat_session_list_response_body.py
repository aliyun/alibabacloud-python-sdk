# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_energyexpertexternal20220923 import models as main_models
from darabonba.model import DaraModel

class GetChatSessionListResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetChatSessionListResponseBodyData = None,
        request_id: str = None,
    ):
        # Returned data
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
            temp_model = main_models.GetChatSessionListResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetChatSessionListResponseBodyData(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        session_list: List[main_models.GetChatSessionListResponseBodyDataSessionList] = None,
        total: int = None,
        total_page: int = None,
    ):
        # Current page number.
        self.current_page = current_page
        # 分页大小。
        self.page_size = page_size
        # Session list.
        self.session_list = session_list
        # Total number of records.
        self.total = total
        # Total number of pages
        self.total_page = total_page

    def validate(self):
        if self.session_list:
            for v1 in self.session_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['currentPage'] = self.current_page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        result['sessionList'] = []
        if self.session_list is not None:
            for k1 in self.session_list:
                result['sessionList'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['total'] = self.total

        if self.total_page is not None:
            result['totalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        self.session_list = []
        if m.get('sessionList') is not None:
            for k1 in m.get('sessionList'):
                temp_model = main_models.GetChatSessionListResponseBodyDataSessionList()
                self.session_list.append(temp_model.from_map(k1))

        if m.get('total') is not None:
            self.total = m.get('total')

        if m.get('totalPage') is not None:
            self.total_page = m.get('totalPage')

        return self

class GetChatSessionListResponseBodyDataSessionList(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        folder_id: str = None,
        name: str = None,
        session_id: str = None,
        update_time: int = None,
        user_id: str = None,
    ):
        # Report creation timestamp, in milliseconds.
        self.create_time = create_time
        # Folder ID, used to specify the scope of documents to be queried.
        self.folder_id = folder_id
        # Session name
        self.name = name
        # Q&A session ID, used to record multiple Q&As of the same user.
        self.session_id = session_id
        # Modification time, in milliseconds.
        self.update_time = update_time
        # User ID of the current session.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.folder_id is not None:
            result['folderId'] = self.folder_id

        if self.name is not None:
            result['name'] = self.name

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('folderId') is not None:
            self.folder_id = m.get('folderId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

