# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyStreamingPropertyRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        task_id: str = None,
        view_content: str = None,
        view_subscribers: List[str] = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.channel_id = channel_id
        # This parameter is required.
        self.task_id = task_id
        self.view_content = view_content
        # ViewSubscribers。
        self.view_subscribers = view_subscribers

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.view_content is not None:
            result['ViewContent'] = self.view_content

        if self.view_subscribers is not None:
            result['ViewSubscribers'] = self.view_subscribers

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('ViewContent') is not None:
            self.view_content = m.get('ViewContent')

        if m.get('ViewSubscribers') is not None:
            self.view_subscribers = m.get('ViewSubscribers')

        return self

