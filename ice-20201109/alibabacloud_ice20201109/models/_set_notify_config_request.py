# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetNotifyConfigRequest(DaraModel):
    def __init__(
        self,
        aiagent_id: str = None,
        audio_oss_path: str = None,
        callback_url: str = None,
        enable_audio_recording: bool = None,
        enable_notify: bool = None,
        event_types: str = None,
        token: str = None,
    ):
        # The ID of the AI agent.
        # 
        # This parameter is required.
        self.aiagent_id = aiagent_id
        self.audio_oss_path = audio_oss_path
        # The URL for receiving callback notifications. By default, this parameter is left empty.
        self.callback_url = callback_url
        self.enable_audio_recording = enable_audio_recording
        # Specifies whether to enable event notifications.
        # 
        # This parameter is required.
        self.enable_notify = enable_notify
        # The event types. If you do not specify this parameter, all event types are selected.
        # 
        # *   agent_start
        # *   agent_stop
        # *   error
        self.event_types = event_types
        # The authentication token for callback. The token is carried in the Authorization header of a callback request. By default, this parameter is left empty.
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aiagent_id is not None:
            result['AIAgentId'] = self.aiagent_id

        if self.audio_oss_path is not None:
            result['AudioOssPath'] = self.audio_oss_path

        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url

        if self.enable_audio_recording is not None:
            result['EnableAudioRecording'] = self.enable_audio_recording

        if self.enable_notify is not None:
            result['EnableNotify'] = self.enable_notify

        if self.event_types is not None:
            result['EventTypes'] = self.event_types

        if self.token is not None:
            result['Token'] = self.token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AIAgentId') is not None:
            self.aiagent_id = m.get('AIAgentId')

        if m.get('AudioOssPath') is not None:
            self.audio_oss_path = m.get('AudioOssPath')

        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')

        if m.get('EnableAudioRecording') is not None:
            self.enable_audio_recording = m.get('EnableAudioRecording')

        if m.get('EnableNotify') is not None:
            self.enable_notify = m.get('EnableNotify')

        if m.get('EventTypes') is not None:
            self.event_types = m.get('EventTypes')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        return self

