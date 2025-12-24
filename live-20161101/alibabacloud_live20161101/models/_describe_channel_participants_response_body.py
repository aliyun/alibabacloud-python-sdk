# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeChannelParticipantsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        times: int = None,
        total_num: int = None,
        total_page: int = None,
        user_list: List[str] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The time elapsed until the result was returned. Unit: seconds. The value is a UNIX timestamp.
        self.times = times
        # The number of entries returned.
        self.total_num = total_num
        # The page number of the returned page.
        self.total_page = total_page
        # The list of user IDs.
        self.user_list = user_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.times is not None:
            result['Times'] = self.times

        if self.total_num is not None:
            result['TotalNum'] = self.total_num

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        if self.user_list is not None:
            result['UserList'] = self.user_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Times') is not None:
            self.times = m.get('Times')

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        if m.get('UserList') is not None:
            self.user_list = m.get('UserList')

        return self

