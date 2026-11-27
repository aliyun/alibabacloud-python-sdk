# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class NotifyAgentShrinkRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        background_music_shrink: str = None,
        channel_id: str = None,
        custom_attribute: str = None,
        interruptable: bool = None,
        message: str = None,
        priority: int = None,
        task_id: str = None,
    ):
        # The application ID. Create and query it in the console. Only a single ID is supported.
        self.app_id = app_id
        # Background audio.
        self.background_music_shrink = background_music_shrink
        # The channel to join. Only a single ID is supported.
        self.channel_id = channel_id
        # Custom parameters passed through to the client.
        self.custom_attribute = custom_attribute
        # Indicates whether the announcement can be interrupted. If false, the message cannot be interrupted by voice input, key presses, or other methods.
        self.interruptable = interruptable
        # The text content to announce.
        self.message = message
        # The priority level for inserting the announcement:
        # 1 — Interrupt the current interaction and announce immediately.
        # 2 — Announce after the current interaction ends.
        # 3 — Announce only if no interaction is active.
        self.priority = priority
        # The task ID.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.background_music_shrink is not None:
            result['BackgroundMusic'] = self.background_music_shrink

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.custom_attribute is not None:
            result['CustomAttribute'] = self.custom_attribute

        if self.interruptable is not None:
            result['Interruptable'] = self.interruptable

        if self.message is not None:
            result['Message'] = self.message

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('BackgroundMusic') is not None:
            self.background_music_shrink = m.get('BackgroundMusic')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('CustomAttribute') is not None:
            self.custom_attribute = m.get('CustomAttribute')

        if m.get('Interruptable') is not None:
            self.interruptable = m.get('Interruptable')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

