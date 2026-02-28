# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class DescribeChannelParticipantsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        timestamp: int = None,
        total_num: int = None,
        total_page: int = None,
        user_list: main_models.DescribeChannelParticipantsResponseBodyUserList = None,
    ):
        self.request_id = request_id
        self.timestamp = timestamp
        self.total_num = total_num
        self.total_page = total_page
        self.user_list = user_list

    def validate(self):
        if self.user_list:
            self.user_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.total_num is not None:
            result['TotalNum'] = self.total_num

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        if self.user_list is not None:
            result['UserList'] = self.user_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        if m.get('UserList') is not None:
            temp_model = main_models.DescribeChannelParticipantsResponseBodyUserList()
            self.user_list = temp_model.from_map(m.get('UserList'))

        return self

class DescribeChannelParticipantsResponseBodyUserList(DaraModel):
    def __init__(
        self,
        user: List[str] = None,
    ):
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user is not None:
            result['User'] = self.user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('User') is not None:
            self.user = m.get('User')

        return self

