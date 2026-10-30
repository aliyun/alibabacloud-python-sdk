# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sysom20231230 import models as main_models
from darabonba.model import DaraModel

class GetHotfixTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetHotfixTaskResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code.
        # - If `code` is `Success`, the authorization is successful.
        # - Other status codes indicate that the authorization failed. If the authorization fails, check the `message` field for the detailed fault information.
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        # - If `code` is `Success`, this field is empty.
        # - Otherwise, this field contains the request error message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetHotfixTaskResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetHotfixTaskResponseBodyData(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        cve_id: str = None,
        finished_at: str = None,
        jobs: List[main_models.GetHotfixTaskResponseBodyDataJobs] = None,
        operation: str = None,
        status: str = None,
        task_id: str = None,
    ):
        # The time when the task was created.
        self.created_at = created_at
        # CVE ID
        self.cve_id = cve_id
        # The time when the task was completed.
        self.finished_at = finished_at
        # The list of instance tasks.
        self.jobs = jobs
        # The operation type of the task.
        self.operation = operation
        # The status of the task.
        self.status = status
        # The ID of the asynchronous task.
        self.task_id = task_id

    def validate(self):
        if self.jobs:
            for v1 in self.jobs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.cve_id is not None:
            result['cveId'] = self.cve_id

        if self.finished_at is not None:
            result['finishedAt'] = self.finished_at

        result['jobs'] = []
        if self.jobs is not None:
            for k1 in self.jobs:
                result['jobs'].append(k1.to_map() if k1 else None)

        if self.operation is not None:
            result['operation'] = self.operation

        if self.status is not None:
            result['status'] = self.status

        if self.task_id is not None:
            result['taskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('cveId') is not None:
            self.cve_id = m.get('cveId')

        if m.get('finishedAt') is not None:
            self.finished_at = m.get('finishedAt')

        self.jobs = []
        if m.get('jobs') is not None:
            for k1 in m.get('jobs'):
                temp_model = main_models.GetHotfixTaskResponseBodyDataJobs()
                self.jobs.append(temp_model.from_map(k1))

        if m.get('operation') is not None:
            self.operation = m.get('operation')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        return self

class GetHotfixTaskResponseBodyDataJobs(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        hotfix_status: str = None,
        instance: str = None,
        region: str = None,
        status: str = None,
    ):
        # The unified error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The hotfix status.
        self.hotfix_status = hotfix_status
        # The ID of the instance.
        self.instance = instance
        # The region ID.
        self.region = region
        # The status of the instance task.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.hotfix_status is not None:
            result['hotfixStatus'] = self.hotfix_status

        if self.instance is not None:
            result['instance'] = self.instance

        if self.region is not None:
            result['region'] = self.region

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('hotfixStatus') is not None:
            self.hotfix_status = m.get('hotfixStatus')

        if m.get('instance') is not None:
            self.instance = m.get('instance')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

