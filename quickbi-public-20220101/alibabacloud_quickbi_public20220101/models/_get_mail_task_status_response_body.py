# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quickbi_public20220101 import models as main_models
from darabonba.model import DaraModel

class GetMailTaskStatusResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.GetMailTaskStatusResponseBodyResult] = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Return result.
        self.result = result
        # Indicates whether the request was successful. Possible values:
        # - true: The request was successful. 
        # - false: The request failed.
        self.success = success

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.GetMailTaskStatusResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetMailTaskStatusResponseBodyResult(DaraModel):
    def __init__(
        self,
        exec_time: str = None,
        mail_id: str = None,
        status: str = None,
        task_id: int = None,
    ):
        # Execution time, in the format yyyy-MM-dd HH:mm:ss
        self.exec_time = exec_time
        # Mail ID
        self.mail_id = mail_id
        # Mail status. Possible values:
        # 
        # - Success: SENT
        # - Failure: FAILED 
        # - In Progress: PROCESSING
        self.status = status
        # Task ID
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exec_time is not None:
            result['execTime'] = self.exec_time

        if self.mail_id is not None:
            result['mailId'] = self.mail_id

        if self.status is not None:
            result['status'] = self.status

        if self.task_id is not None:
            result['taskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('execTime') is not None:
            self.exec_time = m.get('execTime')

        if m.get('mailId') is not None:
            self.mail_id = m.get('mailId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        return self

