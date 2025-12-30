# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DetectAudioForCustomizedVoiceJobRequest(DaraModel):
    def __init__(
        self,
        audio_record_id: int = None,
        record_url: str = None,
        voice_id: str = None,
    ):
        # The sequence number of the recording file.
        # 
        # This parameter is required.
        self.audio_record_id = audio_record_id
        # The URL of the recording file.
        # 
        # > : The URL must be an Object Storage Service (OSS) URL within your Alibaba Cloud account. The OSS bucket must be in the same region in which IMS is activated.
        # 
        # > : The audio file must be in the WAV or PCM format and must be a 16-bit mono audio file at 48000 Hz.
        # 
        # This parameter is required.
        self.record_url = record_url
        # The voice ID.
        # 
        # This parameter is required.
        self.voice_id = voice_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio_record_id is not None:
            result['AudioRecordId'] = self.audio_record_id

        if self.record_url is not None:
            result['RecordUrl'] = self.record_url

        if self.voice_id is not None:
            result['VoiceId'] = self.voice_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioRecordId') is not None:
            self.audio_record_id = m.get('AudioRecordId')

        if m.get('RecordUrl') is not None:
            self.record_url = m.get('RecordUrl')

        if m.get('VoiceId') is not None:
            self.voice_id = m.get('VoiceId')

        return self

