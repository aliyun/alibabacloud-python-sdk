# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeChannelUsersResponseBody(DaraModel):
    def __init__(
        self,
        interactive_user_list: List[str] = None,
        interactive_user_number: int = None,
        is_channel_exists: bool = None,
        live_user_list: List[str] = None,
        live_user_number: int = None,
        request_id: str = None,
        timestamp: int = None,
    ):
        # The list of streamers/co-streamers.
        self.interactive_user_list = interactive_user_list
        # The number of co-streamers.
        self.interactive_user_number = interactive_user_number
        # Indicates whether the channel exists. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # > After all users leave the channel, the system requires a few seconds to clear the cache. If you call the operation during this period, the value of this parameter is true, and the value of InteractiveUserNumber and LiveUserNumber is 0.
        self.is_channel_exists = is_channel_exists
        # The list of viewers.
        self.live_user_list = live_user_list
        # The number of viewers.
        self.live_user_number = live_user_number
        # The ID of the request.
        self.request_id = request_id
        # The UTC timestamp when the response is returned.
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.interactive_user_list is not None:
            result['InteractiveUserList'] = self.interactive_user_list

        if self.interactive_user_number is not None:
            result['InteractiveUserNumber'] = self.interactive_user_number

        if self.is_channel_exists is not None:
            result['IsChannelExists'] = self.is_channel_exists

        if self.live_user_list is not None:
            result['LiveUserList'] = self.live_user_list

        if self.live_user_number is not None:
            result['LiveUserNumber'] = self.live_user_number

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InteractiveUserList') is not None:
            self.interactive_user_list = m.get('InteractiveUserList')

        if m.get('InteractiveUserNumber') is not None:
            self.interactive_user_number = m.get('InteractiveUserNumber')

        if m.get('IsChannelExists') is not None:
            self.is_channel_exists = m.get('IsChannelExists')

        if m.get('LiveUserList') is not None:
            self.live_user_list = m.get('LiveUserList')

        if m.get('LiveUserNumber') is not None:
            self.live_user_number = m.get('LiveUserNumber')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

