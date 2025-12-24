# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class ListMessageGroupUserResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.ListMessageGroupUserResponseBodyResult = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The returned result.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.ListMessageGroupUserResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class ListMessageGroupUserResponseBodyResult(DaraModel):
    def __init__(
        self,
        has_more: bool = None,
        total: int = None,
        user_list: List[main_models.ListMessageGroupUserResponseBodyResultUserList] = None,
    ):
        # Indicates whether the current page is followed by another page. Valid values:
        # 
        # *   true: The current page is followed by another page.
        # *   false: The current page is not followed by another page.
        self.has_more = has_more
        # The total number of users in the message group.
        self.total = total
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
        if self.has_more is not None:
            result['HasMore'] = self.has_more

        if self.total is not None:
            result['Total'] = self.total

        result['UserList'] = []
        if self.user_list is not None:
            for k1 in self.user_list:
                result['UserList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        self.user_list = []
        if m.get('UserList') is not None:
            for k1 in m.get('UserList'):
                temp_model = main_models.ListMessageGroupUserResponseBodyResultUserList()
                self.user_list.append(temp_model.from_map(k1))

        return self

class ListMessageGroupUserResponseBodyResultUserList(DaraModel):
    def __init__(
        self,
        join_time: int = None,
        user_id: str = None,
    ):
        # The time when the user joined the message group. The value is a UTC timestamp.
        self.join_time = join_time
        # The ID of the user.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.join_time is not None:
            result['JoinTime'] = self.join_time

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

