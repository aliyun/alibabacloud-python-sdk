# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sysom20231230 import models as main_models
from darabonba.model import DaraModel

class ListVmcoreDiagnosisTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListVmcoreDiagnosisTaskResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        total: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.total = total

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
        if self.code is not None:
            result['code'] = self.code

        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.ListVmcoreDiagnosisTaskResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListVmcoreDiagnosisTaskResponseBodyData(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        error_msg: str = None,
        task_id: str = None,
        task_status: str = None,
        task_type: str = None,
    ):
        self.created_at = created_at
        self.error_msg = error_msg
        self.task_id = task_id
        self.task_status = task_status
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg

        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.task_status is not None:
            result['taskStatus'] = self.task_status

        if self.task_type is not None:
            result['taskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('taskStatus') is not None:
            self.task_status = m.get('taskStatus')

        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')

        return self

