# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DownloadRecordingRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        need_voice_slice_recording: bool = None,
        task_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.need_voice_slice_recording = need_voice_slice_recording
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.need_voice_slice_recording is not None:
            result['NeedVoiceSliceRecording'] = self.need_voice_slice_recording

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NeedVoiceSliceRecording') is not None:
            self.need_voice_slice_recording = m.get('NeedVoiceSliceRecording')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

