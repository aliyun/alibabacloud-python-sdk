# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class SubmitAIJobResponseBody(DaraModel):
    def __init__(
        self,
        aijob_list: main_models.SubmitAIJobResponseBodyAIJobList = None,
        request_id: str = None,
    ):
        self.aijob_list = aijob_list
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.aijob_list:
            self.aijob_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aijob_list is not None:
            result['AIJobList'] = self.aijob_list.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AIJobList') is not None:
            temp_model = main_models.SubmitAIJobResponseBodyAIJobList()
            self.aijob_list = temp_model.from_map(m.get('AIJobList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class SubmitAIJobResponseBodyAIJobList(DaraModel):
    def __init__(
        self,
        aijob: List[main_models.SubmitAIJobResponseBodyAIJobListAIJob] = None,
    ):
        self.aijob = aijob

    def validate(self):
        if self.aijob:
            for v1 in self.aijob:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AIJob'] = []
        if self.aijob is not None:
            for k1 in self.aijob:
                result['AIJob'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.aijob = []
        if m.get('AIJob') is not None:
            for k1 in m.get('AIJob'):
                temp_model = main_models.SubmitAIJobResponseBodyAIJobListAIJob()
                self.aijob.append(temp_model.from_map(k1))

        return self

class SubmitAIJobResponseBodyAIJobListAIJob(DaraModel):
    def __init__(
        self,
        job_id: str = None,
        media_id: str = None,
        type: str = None,
    ):
        self.job_id = job_id
        self.media_id = media_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

