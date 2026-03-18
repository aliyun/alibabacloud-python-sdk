# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aicontent20240611 import models as main_models
from darabonba.model import DaraModel

class ListTextbookAssistantGradeVolumesResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListTextbookAssistantGradeVolumesResponseBodyData] = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.err_code is not None:
            result['errCode'] = self.err_code

        if self.err_message is not None:
            result['errMessage'] = self.err_message

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.ListTextbookAssistantGradeVolumesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')

        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class ListTextbookAssistantGradeVolumesResponseBodyData(DaraModel):
    def __init__(
        self,
        grade_volumes: List[main_models.ListTextbookAssistantGradeVolumesResponseBodyDataGradeVolumes] = None,
        textbook_version: str = None,
    ):
        self.grade_volumes = grade_volumes
        self.textbook_version = textbook_version

    def validate(self):
        if self.grade_volumes:
            for v1 in self.grade_volumes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['gradeVolumes'] = []
        if self.grade_volumes is not None:
            for k1 in self.grade_volumes:
                result['gradeVolumes'].append(k1.to_map() if k1 else None)

        if self.textbook_version is not None:
            result['textbookVersion'] = self.textbook_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.grade_volumes = []
        if m.get('gradeVolumes') is not None:
            for k1 in m.get('gradeVolumes'):
                temp_model = main_models.ListTextbookAssistantGradeVolumesResponseBodyDataGradeVolumes()
                self.grade_volumes.append(temp_model.from_map(k1))

        if m.get('textbookVersion') is not None:
            self.textbook_version = m.get('textbookVersion')

        return self

class ListTextbookAssistantGradeVolumesResponseBodyDataGradeVolumes(DaraModel):
    def __init__(
        self,
        grade: str = None,
        volume: str = None,
    ):
        self.grade = grade
        self.volume = volume

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.grade is not None:
            result['grade'] = self.grade

        if self.volume is not None:
            result['volume'] = self.volume

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('grade') is not None:
            self.grade = m.get('grade')

        if m.get('volume') is not None:
            self.volume = m.get('volume')

        return self

