# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetOperationRecordDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        operation_record_detail_response: main_models.GetOperationRecordDetailResponseBodyOperationRecordDetailResponse = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The backend response code.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The backend exception details.
        self.message = message
        # The execution record detail response.
        self.operation_record_detail_response = operation_record_detail_response
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.operation_record_detail_response:
            self.operation_record_detail_response.validate()

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

        if self.operation_record_detail_response is not None:
            result['OperationRecordDetailResponse'] = self.operation_record_detail_response.to_map()

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

        if m.get('OperationRecordDetailResponse') is not None:
            temp_model = main_models.GetOperationRecordDetailResponseBodyOperationRecordDetailResponse()
            self.operation_record_detail_response = temp_model.from_map(m.get('OperationRecordDetailResponse'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetOperationRecordDetailResponseBodyOperationRecordDetailResponse(DaraModel):
    def __init__(
        self,
        file_id: int = None,
        log_content: str = None,
        operation_id: str = None,
        results: List[main_models.GetOperationRecordDetailResponseBodyOperationRecordDetailResponseResults] = None,
    ):
        # The file ID.
        self.file_id = file_id
        # The log content.
        self.log_content = log_content
        # The operation record ID.
        self.operation_id = operation_id
        # The list of execution results.
        self.results = results

    def validate(self):
        if self.results:
            for v1 in self.results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.log_content is not None:
            result['LogContent'] = self.log_content

        if self.operation_id is not None:
            result['OperationId'] = self.operation_id

        result['Results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['Results'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('LogContent') is not None:
            self.log_content = m.get('LogContent')

        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')

        self.results = []
        if m.get('Results') is not None:
            for k1 in m.get('Results'):
                temp_model = main_models.GetOperationRecordDetailResponseBodyOperationRecordDetailResponseResults()
                self.results.append(temp_model.from_map(k1))

        return self

class GetOperationRecordDetailResponseBodyOperationRecordDetailResponseResults(DaraModel):
    def __init__(
        self,
        index: int = None,
        result: str = None,
        sql: str = None,
        task_id: str = None,
        title: str = None,
    ):
        # The result index.
        self.index = index
        # The result content.
        self.result = result
        # The result SQL statement.
        self.sql = sql
        # The task ID.
        self.task_id = task_id
        # The result title.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.index is not None:
            result['Index'] = self.index

        if self.result is not None:
            result['Result'] = self.result

        if self.sql is not None:
            result['Sql'] = self.sql

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('Sql') is not None:
            self.sql = m.get('Sql')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

