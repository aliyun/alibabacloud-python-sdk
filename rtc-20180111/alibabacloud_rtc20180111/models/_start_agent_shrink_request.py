# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartAgentShrinkRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        rtc_config_shrink: str = None,
        task_id: str = None,
        template_id: str = None,
        voice_chat_config_shrink: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.channel_id = channel_id
        # This parameter is required.
        self.rtc_config_shrink = rtc_config_shrink
        # This parameter is required.
        self.task_id = task_id
        # This parameter is required.
        self.template_id = template_id
        self.voice_chat_config_shrink = voice_chat_config_shrink

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

        if self.rtc_config_shrink is not None:
            result['RtcConfig'] = self.rtc_config_shrink

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.voice_chat_config_shrink is not None:
            result['VoiceChatConfig'] = self.voice_chat_config_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('RtcConfig') is not None:
            self.rtc_config_shrink = m.get('RtcConfig')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('VoiceChatConfig') is not None:
            self.voice_chat_config_shrink = m.get('VoiceChatConfig')

        return self

