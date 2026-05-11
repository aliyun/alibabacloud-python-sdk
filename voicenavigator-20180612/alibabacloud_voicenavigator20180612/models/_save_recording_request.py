# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SaveRecordingRequest(DaraModel):
    def __init__(
        self,
        conversation_id: str = None,
        duration: str = None,
        file_name: str = None,
        file_path: str = None,
        instance_id: str = None,
        instance_owner_id: int = None,
        start_time: int = None,
        type: str = None,
        voice_slice_recording_list: str = None,
    ):
        # This parameter is required.
        self.conversation_id = conversation_id
        # This parameter is required.
        self.duration = duration
        # This parameter is required.
        self.file_name = file_name
        # This parameter is required.
        self.file_path = file_path
        # This parameter is required.
        self.instance_id = instance_id
        self.instance_owner_id = instance_owner_id
        # This parameter is required.
        self.start_time = start_time
        # This parameter is required.
        self.type = type
        self.voice_slice_recording_list = voice_slice_recording_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_path is not None:
            result['FilePath'] = self.file_path

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_owner_id is not None:
            result['InstanceOwnerId'] = self.instance_owner_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.type is not None:
            result['Type'] = self.type

        if self.voice_slice_recording_list is not None:
            result['VoiceSliceRecordingList'] = self.voice_slice_recording_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceOwnerId') is not None:
            self.instance_owner_id = m.get('InstanceOwnerId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('VoiceSliceRecordingList') is not None:
            self.voice_slice_recording_list = m.get('VoiceSliceRecordingList')

        return self

