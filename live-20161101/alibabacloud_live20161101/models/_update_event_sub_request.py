# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateEventSubRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        callback_url: str = None,
        channel_id: str = None,
        events: List[str] = None,
        subscribe_id: str = None,
        users: List[str] = None,
    ):
        # The application ID.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The callback URL. For more information about the callback content, see CreateEventSub.
        # 
        # This parameter is required.
        self.callback_url = callback_url
        # The channel ID. You can call the [ListEventSub](https://help.aliyun.com/document_detail/2848210.html) operation to query the channel ID.
        # 
        # > 
        # 
        # *   This parameter is required if you specify the Users.N parameter.
        # 
        # *   If you set this parameter to \\* or do not specify this parameter, all channels are subscribed to.
        # 
        # *   You can create up to 20 subscriptions for each application ID.
        self.channel_id = channel_id
        # The type of the events to which you want to subscribe.
        # 
        # This parameter is required.
        self.events = events
        # The subscription ID. You can obtain the ID from the response to the [CreateEventSub](https://help.aliyun.com/document_detail/2848209.html) operation.
        # 
        # This parameter is required.
        self.subscribe_id = subscribe_id
        # The user whose events you want to subscribe to.
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

        if self.subscribe_id is not None:
            result['SubscribeId'] = self.subscribe_id

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

        if m.get('SubscribeId') is not None:
            self.subscribe_id = m.get('SubscribeId')

        if m.get('Users') is not None:
            self.users = m.get('Users')

        return self

