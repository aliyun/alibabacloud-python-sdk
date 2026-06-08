# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListChangeSetsRequest(DaraModel):
    def __init__(
        self,
        change_set_id: str = None,
        change_set_name: List[str] = None,
        execution_status: List[str] = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        stack_id: str = None,
        status: List[str] = None,
    ):
        # The ID of the change set. If detailed information about the change set is not required, you can use this parameter to replace the GetChangeSet operation.
        self.change_set_id = change_set_id
        # The name of change set N. Maximum value of N: 5. You can use an asterisk (\\*) as a wildcard for fuzzy search.
        self.change_set_name = change_set_name
        # The execution status of change set N. Maximum value of N: 5. Valid values:
        # 
        # *   UNAVAILABLE
        # *   AVAILABLE
        # *   EXECUTE_IN_PROGRESS
        # *   EXECUTE_COMPLETE
        # *   EXECUTE_FAILED
        # *   OBSOLETE
        self.execution_status = execution_status
        # The page number.\\
        # Pages start from page 1.\\
        # Default value: 1.
        self.page_number = page_number
        # The number of entries per page.\\
        # Valid values: 1 to 50.\\
        # Default value: 10.
        self.page_size = page_size
        # The region ID of the change set. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/131035.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the stack.
        # 
        # This parameter is required.
        self.stack_id = stack_id
        # The status of change set N. Maximum value of N: 5. Valid values:
        # 
        # *   CREATE_PENDING
        # *   CREATE_IN_PROGRESS
        # *   CREATE_COMPLETE
        # *   CREATE_FAILED
        # *   DELETE_FAILED
        # *   DELETE_COMPLETE
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.change_set_id is not None:
            result['ChangeSetId'] = self.change_set_id

        if self.change_set_name is not None:
            result['ChangeSetName'] = self.change_set_name

        if self.execution_status is not None:
            result['ExecutionStatus'] = self.execution_status

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.stack_id is not None:
            result['StackId'] = self.stack_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeSetId') is not None:
            self.change_set_id = m.get('ChangeSetId')

        if m.get('ChangeSetName') is not None:
            self.change_set_name = m.get('ChangeSetName')

        if m.get('ExecutionStatus') is not None:
            self.execution_status = m.get('ExecutionStatus')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

