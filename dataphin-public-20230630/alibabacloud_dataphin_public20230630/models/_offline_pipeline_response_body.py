# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class OfflinePipelineResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.OfflinePipelineResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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
            temp_model = main_models.OfflinePipelineResponseBodyData()
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

class OfflinePipelineResponseBodyData(DaraModel):
    def __init__(
        self,
        host_machine: str = None,
        node_id: str = None,
        pipeline_id: int = None,
        submit_id: int = None,
        version: str = None,
    ):
        self.host_machine = host_machine
        self.node_id = node_id
        self.pipeline_id = pipeline_id
        self.submit_id = submit_id
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.host_machine is not None:
            result['HostMachine'] = self.host_machine

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id

        if self.submit_id is not None:
            result['SubmitId'] = self.submit_id

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostMachine') is not None:
            self.host_machine = m.get('HostMachine')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')

        if m.get('SubmitId') is not None:
            self.submit_id = m.get('SubmitId')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

