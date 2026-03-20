# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_schedulerx220190430 import models as main_models
from darabonba.model import DaraModel

class GetWorkerListResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetWorkerListResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code that is returned.
        self.code = code
        # The job information.
        self.data = data
        # The additional information that is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call is successful. Valid values:
        # 
        # *   **true**: The call is successful.
        # *   **false**: The call fails.
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
            temp_model = main_models.GetWorkerListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetWorkerListResponseBodyData(DaraModel):
    def __init__(
        self,
        worker_infos: List[main_models.GetWorkerListResponseBodyDataWorkerInfos] = None,
    ):
        # The worker information.
        self.worker_infos = worker_infos

    def validate(self):
        if self.worker_infos:
            for v1 in self.worker_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['WorkerInfos'] = []
        if self.worker_infos is not None:
            for k1 in self.worker_infos:
                result['WorkerInfos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.worker_infos = []
        if m.get('WorkerInfos') is not None:
            for k1 in m.get('WorkerInfos'):
                temp_model = main_models.GetWorkerListResponseBodyDataWorkerInfos()
                self.worker_infos.append(temp_model.from_map(k1))

        return self

class GetWorkerListResponseBodyDataWorkerInfos(DaraModel):
    def __init__(
        self,
        ip: str = None,
        label: str = None,
        port: int = None,
        starter: str = None,
        version: str = None,
        worker_address: str = None,
    ):
        # The IP address of the worker.
        self.ip = ip
        # The label of the worker.
        self.label = label
        # The port number of the worker.
        self.port = port
        # The startup method of the worker.
        self.starter = starter
        # The version of the worker.
        self.version = version
        # The address of the worker. The address is in the format of ${worker_id}@${worker_ip}:${worker_port}.
        self.worker_address = worker_address

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip is not None:
            result['Ip'] = self.ip

        if self.label is not None:
            result['Label'] = self.label

        if self.port is not None:
            result['Port'] = self.port

        if self.starter is not None:
            result['Starter'] = self.starter

        if self.version is not None:
            result['Version'] = self.version

        if self.worker_address is not None:
            result['WorkerAddress'] = self.worker_address

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Starter') is not None:
            self.starter = m.get('Starter')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('WorkerAddress') is not None:
            self.worker_address = m.get('WorkerAddress')

        return self

