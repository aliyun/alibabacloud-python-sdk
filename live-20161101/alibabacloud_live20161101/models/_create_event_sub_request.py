# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateEventSubRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        callback_url: str = None,
        channel_id: str = None,
        events: List[str] = None,
        users: List[str] = None,
    ):
        # The application ID.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The callback URL. For more information about the content of the messages that are sent to the callback URL, see the Callback section in this topic.
        # 
        # This parameter is required.
        self.callback_url = callback_url
        # The channel ID. You can call the [ListEventSub](https://help.aliyun.com/document_detail/2628135.html) operation to query the channel ID.
        # 
        # > 
        # 
        # *   This parameter is required if you specify the Users.N parameter.
        # 
        # *   If you set this parameter to \\* or do not specify this parameter, all channels are subscribed to.
        # 
        # *   Each application ID allows only one all-channel subscription.
        self.channel_id = channel_id
        # Subscribe to events.
        # 
        # This parameter is required.
        self.events = events
        # The user whose events you want to subscribe to. If you leave this parameter empty, the events of all users in the channel are subscribed to, including the events of the streamer and viewers. Specify this parameter in the following format:
        # 
        #     Users.1=****
        #     Users.2=****
        #     ......
        self.users = users

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.events is not None:
            result['Events'] = self.events

        if self.users is not None:
            result['Users'] = self.users

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('Events') is not None:
            self.events = m.get('Events')

        if m.get('Users') is not None:
            self.users = m.get('Users')

        return self

