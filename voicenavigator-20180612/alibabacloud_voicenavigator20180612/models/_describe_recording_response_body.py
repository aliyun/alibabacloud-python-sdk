# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRecordingResponseBody(DaraModel):
    def __init__(
        self,
        file_name: str = None,
        file_path: str = None,
        request_id: str = None,
        voice_slice_recording_list_json: str = None,
    ):
        # The file name.
        self.file_name = file_name
        # The file download URL.
        self.file_path = file_path
        # The request ID.
        self.request_id = request_id
        self.voice_slice_recording_list_json = voice_slice_recording_list_json

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_path is not None:
            result['FilePath'] = self.file_path

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.voice_slice_recording_list_json is not None:
            result['VoiceSliceRecordingListJson'] = self.voice_slice_recording_list_json

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('VoiceSliceRecordingListJson') is not None:
            self.voice_slice_recording_list_json = m.get('VoiceSliceRecordingListJson')

        return self

