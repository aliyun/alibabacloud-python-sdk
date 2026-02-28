# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartChatShrinkRequest(DaraModel):
    def __init__(
        self,
        access_channel_id: str = None,
        instance_id: str = None,
        token: str = None,
        user_list_shrink: str = None,
    ):
        self.access_channel_id = access_channel_id
        self.instance_id = instance_id
        self.token = token
        # This parameter is required.
        self.user_list_shrink = user_list_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_channel_id is not None:
            result['AccessChannelId'] = self.access_channel_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.token is not None:
            result['Token'] = self.token

        if self.user_list_shrink is not None:
            result['UserList'] = self.user_list_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessChannelId') is not None:
            self.access_channel_id = m.get('AccessChannelId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        if m.get('UserList') is not None:
            self.user_list_shrink = m.get('UserList')

        return self

