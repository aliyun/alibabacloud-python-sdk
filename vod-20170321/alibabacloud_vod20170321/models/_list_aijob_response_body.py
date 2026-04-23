# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class ListAIJobResponseBody(DaraModel):
    def __init__(
        self,
        aijob_list: main_models.ListAIJobResponseBodyAIJobList = None,
        non_exist_aijob_ids: main_models.ListAIJobResponseBodyNonExistAIJobIds = None,
        request_id: str = None,
    ):
        self.aijob_list = aijob_list
        self.non_exist_aijob_ids = non_exist_aijob_ids
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.aijob_list:
            self.aijob_list.validate()
        if self.non_exist_aijob_ids:
            self.non_exist_aijob_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aijob_list is not None:
            result['AIJobList'] = self.aijob_list.to_map()

        if self.non_exist_aijob_ids is not None:
            result['NonExistAIJobIds'] = self.non_exist_aijob_ids.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AIJobList') is not None:
            temp_model = main_models.ListAIJobResponseBodyAIJobList()
            self.aijob_list = temp_model.from_map(m.get('AIJobList'))

        if m.get('NonExistAIJobIds') is not None:
            temp_model = main_models.ListAIJobResponseBodyNonExistAIJobIds()
            self.non_exist_aijob_ids = temp_model.from_map(m.get('NonExistAIJobIds'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListAIJobResponseBodyNonExistAIJobIds(DaraModel):
    def __init__(
        self,
        string: List[str] = None,
    ):
        self.string = string

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.string is not None:
            result['String'] = self.string

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('String') is not None:
            self.string = m.get('String')

        return self

class ListAIJobResponseBodyAIJobList(DaraModel):
    def __init__(
        self,
        aijob: List[main_models.ListAIJobResponseBodyAIJobListAIJob] = None,
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
                temp_model = main_models.ListAIJobResponseBodyAIJobListAIJob()
                self.aijob.append(temp_model.from_map(k1))

        return self

class ListAIJobResponseBodyAIJobListAIJob(DaraModel):
    def __init__(
        self,
        code: str = None,
        complete_time: str = None,
        creation_time: str = None,
        data: str = None,
        job_id: str = None,
        media_id: str = None,
        message: str = None,
        status: str = None,
        type: str = None,
    ):
        self.code = code
        self.complete_time = complete_time
        self.creation_time = creation_time
        self.data = data
        self.job_id = job_id
        self.media_id = media_id
        self.message = message
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.data is not None:
            result['Data'] = self.data

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.message is not None:
            result['Message'] = self.message

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

