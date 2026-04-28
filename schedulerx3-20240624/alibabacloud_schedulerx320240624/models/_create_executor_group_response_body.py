# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_schedulerx320240624 import models as main_models
from darabonba.model import DaraModel

class CreateExecutorGroupResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.CreateExecutorGroupResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
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
            temp_model = main_models.CreateExecutorGroupResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CreateExecutorGroupResponseBodyData(DaraModel):
    def __init__(
        self,
        auth_type: str = None,
        description: str = None,
        failed_service: str = None,
        name: str = None,
        network: str = None,
        protocol: str = None,
        worker_id: int = None,
        worker_type: str = None,
        workers: str = None,
    ):
        self.auth_type = auth_type
        self.description = description
        self.failed_service = failed_service
        self.name = name
        self.network = network
        self.protocol = protocol
        self.worker_id = worker_id
        self.worker_type = worker_type
        self.workers = workers

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type

        if self.description is not None:
            result['Description'] = self.description

        if self.failed_service is not None:
            result['FailedService'] = self.failed_service

        if self.name is not None:
            result['Name'] = self.name

        if self.network is not None:
            result['Network'] = self.network

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.worker_id is not None:
            result['WorkerId'] = self.worker_id

        if self.worker_type is not None:
            result['WorkerType'] = self.worker_type

        if self.workers is not None:
            result['Workers'] = self.workers

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FailedService') is not None:
            self.failed_service = m.get('FailedService')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Network') is not None:
            self.network = m.get('Network')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('WorkerId') is not None:
            self.worker_id = m.get('WorkerId')

        if m.get('WorkerType') is not None:
            self.worker_type = m.get('WorkerType')

        if m.get('Workers') is not None:
            self.workers = m.get('Workers')

        return self

