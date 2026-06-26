# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRecordingRequest(DaraModel):
    def __init__(
        self,
        conversation_id: str = None,
        instance_id: str = None,
        need_voice_slice_recording: bool = None,
    ):
        # The conversation ID.
        # 
        # This parameter is required.
        self.conversation_id = conversation_id
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.need_voice_slice_recording = need_voice_slice_recording

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.need_voice_slice_recording is not None:
            result['NeedVoiceSliceRecording'] = self.need_voice_slice_recording

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NeedVoiceSliceRecording') is not None:
            self.need_voice_slice_recording = m.get('NeedVoiceSliceRecording')

        return self

