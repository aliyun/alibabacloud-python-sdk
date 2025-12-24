# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class ListLiveMessageGroupUsersResponseBody(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        hasmore: bool = None,
        next_page_token: int = None,
        request_id: str = None,
        user_list: List[main_models.ListLiveMessageGroupUsersResponseBodyUserList] = None,
    ):
        # The ID of the group queried.
        self.group_id = group_id
        # Indicates whether the current page is followed by another page.
        self.hasmore = hasmore
        # The starting page number for the next query. A value of 0 indicates that no further pages can be queried.
        self.next_page_token = next_page_token
        # The request ID.
        self.request_id = request_id
        # Details about the users.
        self.user_list = user_list

    def validate(self):
        if self.user_list:
            for v1 in self.user_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.hasmore is not None:
            result['Hasmore'] = self.hasmore

        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['UserList'] = []
        if self.user_list is not None:
            for k1 in self.user_list:
                result['UserList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Hasmore') is not None:
            self.hasmore = m.get('Hasmore')

        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.user_list = []
        if m.get('UserList') is not None:
            for k1 in m.get('UserList'):
                temp_model = main_models.ListLiveMessageGroupUsersResponseBodyUserList()
                self.user_list.append(temp_model.from_map(k1))

        return self

class ListLiveMessageGroupUsersResponseBodyUserList(DaraModel):
    def __init__(
        self,
        user_id: str = None,
        user_info: str = None,
    ):
        # The ID of the user.
        self.user_id = user_id
        # The additional information about the user.
        self.user_info = user_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_info is not None:
            result['UserInfo'] = self.user_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserInfo') is not None:
            self.user_info = m.get('UserInfo')

        return self

