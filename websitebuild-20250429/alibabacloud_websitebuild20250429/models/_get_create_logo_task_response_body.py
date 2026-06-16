# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_websitebuild20250429 import models as main_models
from darabonba.model import DaraModel

class GetCreateLogoTaskResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
        task: main_models.GetCreateLogoTaskResponseBodyTask = None,
    ):
        # The error code. If the request is successful, this field is not returned. If the request fails, this field is returned. For more information, see the error code list in this topic.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success
        # The task information.
        self.task = task

    def validate(self):
        if self.task:
            self.task.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.task is not None:
            result['Task'] = self.task.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Task') is not None:
            temp_model = main_models.GetCreateLogoTaskResponseBodyTask()
            self.task = temp_model.from_map(m.get('Task'))

        return self

class GetCreateLogoTaskResponseBodyTask(DaraModel):
    def __init__(
        self,
        task_id: str = None,
        task_status: str = None,
        urls: List[str] = None,
    ):
        # The task ID.
        self.task_id = task_id
        # The current status of the task. Valid values:
        # 
        # - pending: pending execution
        # - configuring: being configured
        # - success: succeeded
        # - failed: failed
        # - partialFailed: partially failed.
        self.task_status = task_status
        # The URL of the prefetched resource.
        self.urls = urls

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.urls is not None:
            result['Urls'] = self.urls

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('Urls') is not None:
            self.urls = m.get('Urls')

        return self

