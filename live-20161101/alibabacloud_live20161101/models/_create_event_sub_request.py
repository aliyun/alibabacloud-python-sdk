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
        # The ID of the application to subscribe to. You can view your application IDs by navigating to **ApsaraVideo Live > Live+ > ApsaraVideo Real-time Communication > Application Management**. If no application exists, create one by clicking [Create Application].
        # 
        # This parameter is required.
        self.app_id = app_id
        # The callback URL. For the callback content, see the callback content examples below.
        # 
        # This parameter is required.
        self.callback_url = callback_url
        # The ID of the channel to subscribe to. You can call the [ListEventSub](https://help.aliyun.com/document_detail/2848210.html) operation to query the subscribed channel IDs.
        # 
        # >- If the Users.N parameter is not empty, this parameter is required.
        # >- If ChannelId is set to \\* or left empty, all channels are subscribed. Each AppId allows only one all-channel subscription.
        # >- Each AppId allows a maximum of 20 subscriptions at the same time.
        self.channel_id = channel_id
        # The subscription events.
        # 
        # This parameter is required.
        self.events = events
        # The users whose messages you want to subscribe to. If this parameter is empty, all users in the channel (including streamers and viewers) are subscribed. Format:
        # 
        # ```
        # Users.1=****
        # Users.2=****
        # ......
        # ```
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

