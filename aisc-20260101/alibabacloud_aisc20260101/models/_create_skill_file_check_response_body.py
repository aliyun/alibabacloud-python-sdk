# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aisc20260101 import models as main_models
from darabonba.model import DaraModel

class CreateSkillFileCheckResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.CreateSkillFileCheckResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.CreateSkillFileCheckResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateSkillFileCheckResponseBodyData(DaraModel):
    def __init__(
        self,
        fail_count: int = None,
        root_task_id: str = None,
        success_count: int = None,
        upload_results: List[main_models.CreateSkillFileCheckResponseBodyDataUploadResults] = None,
    ):
        self.fail_count = fail_count
        self.root_task_id = root_task_id
        self.success_count = success_count
        self.upload_results = upload_results

    def validate(self):
        if self.upload_results:
            for v1 in self.upload_results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fail_count is not None:
            result['FailCount'] = self.fail_count

        if self.root_task_id is not None:
            result['RootTaskId'] = self.root_task_id

        if self.success_count is not None:
            result['SuccessCount'] = self.success_count

        result['UploadResults'] = []
        if self.upload_results is not None:
            for k1 in self.upload_results:
                result['UploadResults'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailCount') is not None:
            self.fail_count = m.get('FailCount')

        if m.get('RootTaskId') is not None:
            self.root_task_id = m.get('RootTaskId')

        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')

        self.upload_results = []
        if m.get('UploadResults') is not None:
            for k1 in m.get('UploadResults'):
                temp_model = main_models.CreateSkillFileCheckResponseBodyDataUploadResults()
                self.upload_results.append(temp_model.from_map(k1))

        return self

class CreateSkillFileCheckResponseBodyDataUploadResults(DaraModel):
    def __init__(
        self,
        error_msg: str = None,
        file_hash: str = None,
        file_name: str = None,
        identify_id: str = None,
        success: bool = None,
    ):
        self.error_msg = error_msg
        self.file_hash = file_hash
        self.file_name = file_name
        self.identify_id = identify_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.file_hash is not None:
            result['FileHash'] = self.file_hash

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.identify_id is not None:
            result['IdentifyId'] = self.identify_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('FileHash') is not None:
            self.file_hash = m.get('FileHash')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('IdentifyId') is not None:
            self.identify_id = m.get('IdentifyId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

