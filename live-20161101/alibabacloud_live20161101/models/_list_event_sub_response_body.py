# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class ListEventSubResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        subscribers: List[main_models.ListEventSubResponseBodySubscribers] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The events.
        self.subscribers = subscribers

    def validate(self):
        if self.subscribers:
            for v1 in self.subscribers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Subscribers'] = []
        if self.subscribers is not None:
            for k1 in self.subscribers:
                result['Subscribers'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.subscribers = []
        if m.get('Subscribers') is not None:
            for k1 in m.get('Subscribers'):
                temp_model = main_models.ListEventSubResponseBodySubscribers()
                self.subscribers.append(temp_model.from_map(k1))

        return self

class ListEventSubResponseBodySubscribers(DaraModel):
    def __init__(
        self,
        callback_url: str = None,
        channel_id: str = None,
        create_time: str = None,
        events: List[str] = None,
        modify_time: str = None,
        roles: int = None,
        sub_id: str = None,
        users: List[str] = None,
    ):
        # The callback URL.
        self.callback_url = callback_url
        # The ID of the channel to which you subscribe.
        self.channel_id = channel_id
        # The time when the subscription was created. The time is displayed in UTC+8. Format: yyyy-MM-dd hh:mm:ss.
        self.create_time = create_time
        # The type of the event. Valid values:
        # 
        # *   ChannelEvent: channel event. For example, the channel is opened or closed.
        # *   UserEvent: user event. For example, a user joins or leaves the channel.
        self.events = events
        # The time when the subscription was modified. The time is displayed in UTC+8. Format: yyyy-MM-dd hh:mm:ss.
        self.modify_time = modify_time
        # The role of the user whose events are returned. Valid values:
        # 
        # *   1: streamer
        # *   2: viewer
        # 
        # An empty value or a value other than 1 and 2 indicates that events of all users in the channel are returned.
        # 
        # >  This parameter is deprecated. When you create a subscription, this parameter is no longer supported.
        self.roles = roles
        # The ID of the event.
        self.sub_id = sub_id
        # The user whose events are returned. We recommend that you use either this parameter or Roles.
        self.users = users

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.events is not None:
            result['Events'] = self.events

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.roles is not None:
            result['Roles'] = self.roles

        if self.sub_id is not None:
            result['SubId'] = self.sub_id

        if self.users is not None:
            result['Users'] = self.users

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Events') is not None:
            self.events = m.get('Events')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Roles') is not None:
            self.roles = m.get('Roles')

        if m.get('SubId') is not None:
            self.sub_id = m.get('SubId')

        if m.get('Users') is not None:
            self.users = m.get('Users')

        return self

