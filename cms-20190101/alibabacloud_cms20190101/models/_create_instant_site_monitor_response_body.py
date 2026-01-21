# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class CreateInstantSiteMonitorResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        create_result_list: List[main_models.CreateInstantSiteMonitorResponseBodyCreateResultList] = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The error code.
        # 
        # > The status code 200 indicates that the call was successful.
        self.code = code
        # The results for creating the instant test task.
        self.create_result_list = create_result_list
        # The returned message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        if self.create_result_list:
            for v1 in self.create_result_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['CreateResultList'] = []
        if self.create_result_list is not None:
            for k1 in self.create_result_list:
                result['CreateResultList'].append(k1.to_map() if k1 else None)

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

        self.create_result_list = []
        if m.get('CreateResultList') is not None:
            for k1 in m.get('CreateResultList'):
                temp_model = main_models.CreateInstantSiteMonitorResponseBodyCreateResultList()
                self.create_result_list.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CreateInstantSiteMonitorResponseBodyCreateResultList(DaraModel):
    def __init__(
        self,
        task_id: str = None,
        task_name: str = None,
    ):
        # The ID of the instant test task.
        self.task_id = task_id
        # The name of the instant test task.
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        return self

