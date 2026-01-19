# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeEventTaskHistoryResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_object: List[main_models.DescribeEventTaskHistoryResponseBodyResultObject] = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Return object
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            for v1 in self.result_object:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['resultObject'] = []
        if self.result_object is not None:
            for k1 in self.result_object:
                result['resultObject'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result_object = []
        if m.get('resultObject') is not None:
            for k1 in m.get('resultObject'):
                temp_model = main_models.DescribeEventTaskHistoryResponseBodyResultObject()
                self.result_object.append(temp_model.from_map(k1))

        return self

class DescribeEventTaskHistoryResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        task_code: str = None,
        task_name: str = None,
        task_status: str = None,
        url: str = None,
    ):
        # Task code.
        self.task_code = task_code
        # Task name
        self.task_name = task_name
        # Task status.
        self.task_status = task_status
        # OSS download URL
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.task_code is not None:
            result['taskCode'] = self.task_code

        if self.task_name is not None:
            result['taskName'] = self.task_name

        if self.task_status is not None:
            result['taskStatus'] = self.task_status

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskCode') is not None:
            self.task_code = m.get('taskCode')

        if m.get('taskName') is not None:
            self.task_name = m.get('taskName')

        if m.get('taskStatus') is not None:
            self.task_status = m.get('taskStatus')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

