# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateEventSubscribeRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        callback_url: str = None,
        channel_id: str = None,
        client_token: str = None,
        events: List[str] = None,
        need_callback_auth: bool = None,
        owner_id: int = None,
        role: int = None,
        users: List[str] = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.callback_url = callback_url
        self.channel_id = channel_id
        # This parameter is required.
        self.client_token = client_token
        # This parameter is required.
        self.events = events
        self.need_callback_auth = need_callback_auth
        self.owner_id = owner_id
        self.role = role
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

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.events is not None:
            result['Events'] = self.events

        if self.need_callback_auth is not None:
            result['NeedCallbackAuth'] = self.need_callback_auth

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.role is not None:
            result['Role'] = self.role

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

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Events') is not None:
            self.events = m.get('Events')

        if m.get('NeedCallbackAuth') is not None:
            self.need_callback_auth = m.get('NeedCallbackAuth')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('Users') is not None:
            self.users = m.get('Users')

        return self

