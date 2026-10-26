# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListMigrationOperationsRequest(DaraModel):
    def __init__(
        self,
        business_status: List[str] = None,
        filter: str = None,
        instance_id: str = None,
        operation_status: List[str] = None,
        operation_type: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The operation business status.
        self.business_status = business_status
        # The filter condition for the query.
        # 
        # >
        # > - Supports filtering by operationKey, which is the topic name.
        self.filter = filter
        # The instance ID.
        self.instance_id = instance_id
        # The operation status.
        self.operation_status = operation_status
        # The operation type.
        # 
        # This parameter is required.
        self.operation_type = operation_type
        # The page number of the results to return.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The page size, which specifies the maximum number of results to return per page.
        # 
        # This parameter is required.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_status is not None:
            result['businessStatus'] = self.business_status

        if self.filter is not None:
            result['filter'] = self.filter

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.operation_status is not None:
            result['operationStatus'] = self.operation_status

        if self.operation_type is not None:
            result['operationType'] = self.operation_type

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('businessStatus') is not None:
            self.business_status = m.get('businessStatus')

        if m.get('filter') is not None:
            self.filter = m.get('filter')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('operationStatus') is not None:
            self.operation_status = m.get('operationStatus')

        if m.get('operationType') is not None:
            self.operation_type = m.get('operationType')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        return self

