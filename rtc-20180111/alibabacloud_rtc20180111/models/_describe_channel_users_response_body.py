# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeChannelUsersResponseBody(DaraModel):
    def __init__(
        self,
        channel_profile: int = None,
        comm_total_num: int = None,
        interactive_user_list: List[str] = None,
        interactive_user_num: int = None,
        is_channel_exist: bool = None,
        live_user_list: List[str] = None,
        live_user_num: int = None,
        request_id: str = None,
        timestamp: int = None,
        user_list: List[str] = None,
    ):
        self.channel_profile = channel_profile
        self.comm_total_num = comm_total_num
        self.interactive_user_list = interactive_user_list
        self.interactive_user_num = interactive_user_num
        self.is_channel_exist = is_channel_exist
        self.live_user_list = live_user_list
        self.live_user_num = live_user_num
        self.request_id = request_id
        self.timestamp = timestamp
        self.user_list = user_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_profile is not None:
            result['ChannelProfile'] = self.channel_profile

        if self.comm_total_num is not None:
            result['CommTotalNum'] = self.comm_total_num

        if self.interactive_user_list is not None:
            result['InteractiveUserList'] = self.interactive_user_list

        if self.interactive_user_num is not None:
            result['InteractiveUserNum'] = self.interactive_user_num

        if self.is_channel_exist is not None:
            result['IsChannelExist'] = self.is_channel_exist

        if self.live_user_list is not None:
            result['LiveUserList'] = self.live_user_list

        if self.live_user_num is not None:
            result['LiveUserNum'] = self.live_user_num

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.user_list is not None:
            result['UserList'] = self.user_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelProfile') is not None:
            self.channel_profile = m.get('ChannelProfile')

        if m.get('CommTotalNum') is not None:
            self.comm_total_num = m.get('CommTotalNum')

        if m.get('InteractiveUserList') is not None:
            self.interactive_user_list = m.get('InteractiveUserList')

        if m.get('InteractiveUserNum') is not None:
            self.interactive_user_num = m.get('InteractiveUserNum')

        if m.get('IsChannelExist') is not None:
            self.is_channel_exist = m.get('IsChannelExist')

        if m.get('LiveUserList') is not None:
            self.live_user_list = m.get('LiveUserList')

        if m.get('LiveUserNum') is not None:
            self.live_user_num = m.get('LiveUserNum')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('UserList') is not None:
            self.user_list = m.get('UserList')

        return self

