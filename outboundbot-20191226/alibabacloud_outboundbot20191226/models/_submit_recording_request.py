# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitRecordingRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        merged_recording: str = None,
        resource_recording: str = None,
        task_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.merged_recording = merged_recording
        self.resource_recording = resource_recording
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

        if self.merged_recording is not None:
            result['MergedRecording'] = self.merged_recording

        if self.resource_recording is not None:
            result['ResourceRecording'] = self.resource_recording

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MergedRecording') is not None:
            self.merged_recording = m.get('MergedRecording')

        if m.get('ResourceRecording') is not None:
            self.resource_recording = m.get('ResourceRecording')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

