# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetOperationRecordByIdResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        operation_log_dto: main_models.GetOperationRecordByIdResponseBodyOperationLogDTO = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.operation_log_dto = operation_log_dto
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.operation_log_dto:
            self.operation_log_dto.validate()

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

        if self.operation_log_dto is not None:
            result['OperationLogDTO'] = self.operation_log_dto.to_map()

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

        if m.get('OperationLogDTO') is not None:
            temp_model = main_models.GetOperationRecordByIdResponseBodyOperationLogDTO()
            self.operation_log_dto = temp_model.from_map(m.get('OperationLogDTO'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetOperationRecordByIdResponseBodyOperationLogDTO(DaraModel):
    def __init__(
        self,
        begin_time: str = None,
        code_type: int = None,
        duration: int = None,
        id: int = None,
        name: str = None,
        object_type: str = None,
        operation_id: int = None,
        project_id: int = None,
        relation_tables: List[str] = None,
        runner: str = None,
        runner_name: str = None,
        status: int = None,
        tenant_id: int = None,
    ):
        self.begin_time = begin_time
        self.code_type = code_type
        self.duration = duration
        self.id = id
        self.name = name
        self.object_type = object_type
        self.operation_id = operation_id
        self.project_id = project_id
        self.relation_tables = relation_tables
        self.runner = runner
        self.runner_name = runner_name
        self.status = status
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        if self.code_type is not None:
            result['CodeType'] = self.code_type

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.object_type is not None:
            result['ObjectType'] = self.object_type

        if self.operation_id is not None:
            result['OperationId'] = self.operation_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.relation_tables is not None:
            result['RelationTables'] = self.relation_tables

        if self.runner is not None:
            result['Runner'] = self.runner

        if self.runner_name is not None:
            result['RunnerName'] = self.runner_name

        if self.status is not None:
            result['Status'] = self.status

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('CodeType') is not None:
            self.code_type = m.get('CodeType')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')

        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RelationTables') is not None:
            self.relation_tables = m.get('RelationTables')

        if m.get('Runner') is not None:
            self.runner = m.get('Runner')

        if m.get('RunnerName') is not None:
            self.runner_name = m.get('RunnerName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        return self

