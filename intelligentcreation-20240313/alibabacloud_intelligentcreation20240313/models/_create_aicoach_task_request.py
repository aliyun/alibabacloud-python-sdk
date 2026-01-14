# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAICoachTaskRequest(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        script_record_id: str = None,
        student_audio_url: str = None,
        student_id: str = None,
    ):
        self.request_id = request_id
        self.script_record_id = script_record_id
        self.student_audio_url = student_audio_url
        self.student_id = student_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.script_record_id is not None:
            result['scriptRecordId'] = self.script_record_id

        if self.student_audio_url is not None:
            result['studentAudioUrl'] = self.student_audio_url

        if self.student_id is not None:
            result['studentId'] = self.student_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('scriptRecordId') is not None:
            self.script_record_id = m.get('scriptRecordId')

        if m.get('studentAudioUrl') is not None:
            self.student_audio_url = m.get('studentAudioUrl')

        if m.get('studentId') is not None:
            self.student_id = m.get('studentId')

        return self

