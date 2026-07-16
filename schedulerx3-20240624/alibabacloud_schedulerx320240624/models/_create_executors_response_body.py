# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_schedulerx320240624 import models as main_models
from darabonba.model import DaraModel

class CreateExecutorsResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.CreateExecutorsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code.
        self.code = code
        # The returned data.
        self.data = data
        # The response message.
        self.message = message
        # The unique ID of the request.
        self.request_id = request_id
        # Indicates whether the request succeeded.
        # 
        # - true: The request succeeded.
        # 
        # - false: The request failed.
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
            temp_model = main_models.CreateExecutorsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CreateExecutorsResponseBodyData(DaraModel):
    def __init__(
        self,
        app_group_id: int = None,
        app_type: int = None,
        failed_service: str = None,
        worker_id: int = None,
        worker_type: str = None,
        workers: str = None,
    ):
        # The App Group ID.
        self.app_group_id = app_group_id
        # The application type.
        self.app_type = app_type
        # A list of Kubernetes Services that failed to import.
        self.failed_service = failed_service
        # The ID of the worker. You can obtain this ID by calling the [ListWorkerResource](https://help.aliyun.com/document_detail/2712224.html) operation.
        self.worker_id = worker_id
        # The worker type.
        self.worker_type = worker_type
        # A JSON string that represents the list of imported workers.
        self.workers = workers

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_group_id is not None:
            result['AppGroupId'] = self.app_group_id

        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.failed_service is not None:
            result['FailedService'] = self.failed_service

        if self.worker_id is not None:
            result['WorkerId'] = self.worker_id

        if self.worker_type is not None:
            result['WorkerType'] = self.worker_type

        if self.workers is not None:
            result['Workers'] = self.workers

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppGroupId') is not None:
            self.app_group_id = m.get('AppGroupId')

        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('FailedService') is not None:
            self.failed_service = m.get('FailedService')

        if m.get('WorkerId') is not None:
            self.worker_id = m.get('WorkerId')

        if m.get('WorkerType') is not None:
            self.worker_type = m.get('WorkerType')

        if m.get('Workers') is not None:
            self.workers = m.get('Workers')

        return self

