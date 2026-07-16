# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ros20190910 import models as main_models
from darabonba.model import DaraModel

class ListStackGroupOperationResultsResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        stack_group_operation_results: List[main_models.ListStackGroupOperationResultsResponseBodyStackGroupOperationResults] = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The details of the results of the operation.
        self.stack_group_operation_results = stack_group_operation_results
        # The total number of results.
        self.total_count = total_count

    def validate(self):
        if self.stack_group_operation_results:
            for v1 in self.stack_group_operation_results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['StackGroupOperationResults'] = []
        if self.stack_group_operation_results is not None:
            for k1 in self.stack_group_operation_results:
                result['StackGroupOperationResults'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.stack_group_operation_results = []
        if m.get('StackGroupOperationResults') is not None:
            for k1 in m.get('StackGroupOperationResults'):
                temp_model = main_models.ListStackGroupOperationResultsResponseBodyStackGroupOperationResults()
                self.stack_group_operation_results.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListStackGroupOperationResultsResponseBodyStackGroupOperationResults(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        rd_folder_id: str = None,
        region_id: str = None,
        status: str = None,
        status_reason: str = None,
    ):
        # The ID of the account to which the stack instance belongs.
        # 
        # *   If the stack group has self-managed permissions, the stack instance belongs to an Alibaba Cloud account.
        # *   If the stack group has service-managed permissions, the stack instance belongs to a member account in the resource directory.
        # 
        # >  For more information about the account, see [Overview](https://help.aliyun.com/document_detail/154578.html).
        self.account_id = account_id
        # The folder ID of the resource directory.
        # 
        # >  This parameter is returned only when the stack group is granted service-managed permissions.
        self.rd_folder_id = rd_folder_id
        # The region ID of the stack instance.
        self.region_id = region_id
        # The status of the operation.
        # 
        # Valid values:
        # 
        # *   RUNNING: The operation is being performed.
        # *   SUCCEEDED: The operation succeeded.
        # *   FAILED: The operation failed.
        # *   STOPPING: The operation is being stopped.
        # *   STOPPED: The operation is stopped.
        self.status = status
        # The reason why the operation is in a specific state.
        # 
        # >  This parameter is returned only when stack instances are in the OUTDATED state.
        self.status_reason = status_reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.rd_folder_id is not None:
            result['RdFolderId'] = self.rd_folder_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('RdFolderId') is not None:
            self.rd_folder_id = m.get('RdFolderId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')

        return self

