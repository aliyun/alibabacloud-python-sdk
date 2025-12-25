# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_qualitycheck20190115 import models as main_models
from darabonba.model import DaraModel

class GetMiningTaskResultResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetMiningTaskResultResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetMiningTaskResultResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetMiningTaskResultResponseBodyData(DaraModel):
    def __init__(
        self,
        file_path: str = None,
        file_path_list: List[main_models.GetMiningTaskResultResponseBodyDataFilePathList] = None,
        file_path_md: str = None,
        task_id: str = None,
        task_status: str = None,
    ):
        self.file_path = file_path
        self.file_path_list = file_path_list
        self.file_path_md = file_path_md
        self.task_id = task_id
        self.task_status = task_status

    def validate(self):
        if self.file_path_list:
            for v1 in self.file_path_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_path is not None:
            result['FilePath'] = self.file_path

        result['FilePathList'] = []
        if self.file_path_list is not None:
            for k1 in self.file_path_list:
                result['FilePathList'].append(k1.to_map() if k1 else None)

        if self.file_path_md is not None:
            result['FilePathMd'] = self.file_path_md

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')

        self.file_path_list = []
        if m.get('FilePathList') is not None:
            for k1 in m.get('FilePathList'):
                temp_model = main_models.GetMiningTaskResultResponseBodyDataFilePathList()
                self.file_path_list.append(temp_model.from_map(k1))

        if m.get('FilePathMd') is not None:
            self.file_path_md = m.get('FilePathMd')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        return self

class GetMiningTaskResultResponseBodyDataFilePathList(DaraModel):
    def __init__(
        self,
        file_type: str = None,
        file_url: str = None,
    ):
        self.file_type = file_type
        self.file_url = file_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_type is not None:
            result['FileType'] = self.file_type

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        return self

