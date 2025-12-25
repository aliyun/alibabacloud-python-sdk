# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class FetchImageTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.FetchImageTaskResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

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
            temp_model = main_models.FetchImageTaskResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class FetchImageTaskResponseBodyData(DaraModel):
    def __init__(
        self,
        task_info_list: List[main_models.FetchImageTaskResponseBodyDataTaskInfoList] = None,
    ):
        self.task_info_list = task_info_list

    def validate(self):
        if self.task_info_list:
            for v1 in self.task_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TaskInfoList'] = []
        if self.task_info_list is not None:
            for k1 in self.task_info_list:
                result['TaskInfoList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.task_info_list = []
        if m.get('TaskInfoList') is not None:
            for k1 in m.get('TaskInfoList'):
                temp_model = main_models.FetchImageTaskResponseBodyDataTaskInfoList()
                self.task_info_list.append(temp_model.from_map(k1))

        return self

class FetchImageTaskResponseBodyDataTaskInfoList(DaraModel):
    def __init__(
        self,
        id: int = None,
        image_list: List[main_models.FetchImageTaskResponseBodyDataTaskInfoListImageList] = None,
        task_id: str = None,
        task_status: str = None,
    ):
        self.id = id
        self.image_list = image_list
        self.task_id = task_id
        self.task_status = task_status

    def validate(self):
        if self.image_list:
            for v1 in self.image_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        result['ImageList'] = []
        if self.image_list is not None:
            for k1 in self.image_list:
                result['ImageList'].append(k1.to_map() if k1 else None)

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        self.image_list = []
        if m.get('ImageList') is not None:
            for k1 in m.get('ImageList'):
                temp_model = main_models.FetchImageTaskResponseBodyDataTaskInfoListImageList()
                self.image_list.append(temp_model.from_map(k1))

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        return self

class FetchImageTaskResponseBodyDataTaskInfoListImageList(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        url: str = None,
    ):
        self.code = code
        self.message = message
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

