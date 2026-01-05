# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListTaskInstanceOperationLogsResponseBody(DaraModel):
    def __init__(
        self,
        paging_info: main_models.ListTaskInstanceOperationLogsResponseBodyPagingInfo = None,
        request_id: str = None,
    ):
        # The pagination information.
        self.paging_info = paging_info
        # The request ID. You can locate logs and troubleshoot issues based on the ID.
        self.request_id = request_id

    def validate(self):
        if self.paging_info:
            self.paging_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.paging_info is not None:
            result['PagingInfo'] = self.paging_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PagingInfo') is not None:
            temp_model = main_models.ListTaskInstanceOperationLogsResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m.get('PagingInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListTaskInstanceOperationLogsResponseBodyPagingInfo(DaraModel):
    def __init__(
        self,
        operation_logs: List[main_models.ListTaskInstanceOperationLogsResponseBodyPagingInfoOperationLogs] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The operation logs.
        self.operation_logs = operation_logs
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.operation_logs:
            for v1 in self.operation_logs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['OperationLogs'] = []
        if self.operation_logs is not None:
            for k1 in self.operation_logs:
                result['OperationLogs'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.operation_logs = []
        if m.get('OperationLogs') is not None:
            for k1 in m.get('OperationLogs'):
                temp_model = main_models.ListTaskInstanceOperationLogsResponseBodyPagingInfoOperationLogs()
                self.operation_logs.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListTaskInstanceOperationLogsResponseBodyPagingInfoOperationLogs(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        operation_content: str = None,
        operation_seq: int = None,
        task_instance_id: int = None,
        user: str = None,
    ):
        # The time when the operation log was generated.
        self.create_time = create_time
        # The operation content.
        self.operation_content = operation_content
        # The serial number of the operation.
        self.operation_seq = operation_seq
        # The ID of the instance on which the operation was performed.
        self.task_instance_id = task_instance_id
        # The account ID of the operator.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.operation_content is not None:
            result['OperationContent'] = self.operation_content

        if self.operation_seq is not None:
            result['OperationSeq'] = self.operation_seq

        if self.task_instance_id is not None:
            result['TaskInstanceId'] = self.task_instance_id

        if self.user is not None:
            result['User'] = self.user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('OperationContent') is not None:
            self.operation_content = m.get('OperationContent')

        if m.get('OperationSeq') is not None:
            self.operation_seq = m.get('OperationSeq')

        if m.get('TaskInstanceId') is not None:
            self.task_instance_id = m.get('TaskInstanceId')

        if m.get('User') is not None:
            self.user = m.get('User')

        return self

