# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StopUnionTaskRequest(DaraModel):
    def __init__(
        self,
        channel_id: str = None,
        proxy_user_id: int = None,
        task_id: int = None,
    ):
        self.channel_id = channel_id
        self.proxy_user_id = proxy_user_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.proxy_user_id is not None:
            result['ProxyUserId'] = self.proxy_user_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('ProxyUserId') is not None:
            self.proxy_user_id = m.get('ProxyUserId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

