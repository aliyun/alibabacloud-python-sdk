# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_intelligentcreation20240313 import models as main_models
from darabonba.model import DaraModel

class BatchCreateAICoachTaskRequest(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        script_record_id: str = None,
        student_ids: List[str] = None,
        student_list: List[main_models.BatchCreateAICoachTaskRequestStudentList] = None,
    ):
        self.request_id = request_id
        self.script_record_id = script_record_id
        self.student_ids = student_ids
        self.student_list = student_list

    def validate(self):
        if self.student_list:
            for v1 in self.student_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.script_record_id is not None:
            result['scriptRecordId'] = self.script_record_id

        if self.student_ids is not None:
            result['studentIds'] = self.student_ids

        result['studentList'] = []
        if self.student_list is not None:
            for k1 in self.student_list:
                result['studentList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('scriptRecordId') is not None:
            self.script_record_id = m.get('scriptRecordId')

        if m.get('studentIds') is not None:
            self.student_ids = m.get('studentIds')

        self.student_list = []
        if m.get('studentList') is not None:
            for k1 in m.get('studentList'):
                temp_model = main_models.BatchCreateAICoachTaskRequestStudentList()
                self.student_list.append(temp_model.from_map(k1))

        return self



class BatchCreateAICoachTaskRequestStudentList(DaraModel):
    def __init__(
        self,
        student_audio_url: str = None,
        student_id: str = None,
    ):
        self.student_audio_url = student_audio_url
        self.student_id = student_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.student_audio_url is not None:
            result['studentAudioUrl'] = self.student_audio_url

        if self.student_id is not None:
            result['studentId'] = self.student_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('studentAudioUrl') is not None:
            self.student_audio_url = m.get('studentAudioUrl')

        if m.get('studentId') is not None:
            self.student_id = m.get('studentId')

        return self

