# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListMigrationOperationsShrinkRequest(DaraModel):
    def __init__(
        self,
        business_status_shrink: str = None,
        filter: str = None,
        instance_id: str = None,
        operation_status_shrink: str = None,
        operation_type: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.business_status_shrink = business_status_shrink
        self.filter = filter
        self.instance_id = instance_id
        self.operation_status_shrink = operation_status_shrink
        # This parameter is required.
        self.operation_type = operation_type
        # This parameter is required.
        self.page_number = page_number
        # This parameter is required.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_status_shrink is not None:
            result['businessStatus'] = self.business_status_shrink

        if self.filter is not None:
            result['filter'] = self.filter

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.operation_status_shrink is not None:
            result['operationStatus'] = self.operation_status_shrink

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
            self.business_status_shrink = m.get('businessStatus')

        if m.get('filter') is not None:
            self.filter = m.get('filter')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('operationStatus') is not None:
            self.operation_status_shrink = m.get('operationStatus')

        if m.get('operationType') is not None:
            self.operation_type = m.get('operationType')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        return self

