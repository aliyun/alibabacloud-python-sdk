# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetOperationSubmitStatusResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        operation_submit_job: main_models.GetOperationSubmitStatusResponseBodyOperationSubmitJob = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.operation_submit_job = operation_submit_job
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.operation_submit_job:
            self.operation_submit_job.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.operation_submit_job is not None:
            result['OperationSubmitJob'] = self.operation_submit_job.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('OperationSubmitJob') is not None:
            temp_model = main_models.GetOperationSubmitStatusResponseBodyOperationSubmitJob()
            self.operation_submit_job = temp_model.from_map(m.get('OperationSubmitJob'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetOperationSubmitStatusResponseBodyOperationSubmitJob(DaraModel):
    def __init__(
        self,
        external_biz_id: str = None,
        job_id: str = None,
        operation: str = None,
        operation_status: str = None,
        operator: str = None,
        progress: str = None,
    ):
        self.external_biz_id = external_biz_id
        self.job_id = job_id
        self.operation = operation
        self.operation_status = operation_status
        self.operator = operator
        self.progress = progress

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.external_biz_id is not None:
            result['ExternalBizId'] = self.external_biz_id

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.operation is not None:
            result['Operation'] = self.operation

        if self.operation_status is not None:
            result['OperationStatus'] = self.operation_status

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.progress is not None:
            result['Progress'] = self.progress

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternalBizId') is not None:
            self.external_biz_id = m.get('ExternalBizId')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Operation') is not None:
            self.operation = m.get('Operation')

        if m.get('OperationStatus') is not None:
            self.operation_status = m.get('OperationStatus')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        return self

