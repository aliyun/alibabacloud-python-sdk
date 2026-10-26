# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListFeatureConsistencyCheckJobsRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        order: str = None,
        page_number: str = None,
        page_size: str = None,
        sort_by: str = None,
        status: str = None,
    ):
        # The ID of the instance. For information about how to obtain the instance ID, see [ListInstances](https://help.aliyun.com/document_detail/2411819.html).
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The sort order. Valid values:
        # - ASC: ascending order
        # - DESC: descending order
        self.order = order
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The sort field. Valid values:
        # - GmtCreateTime: sort by creation time
        # - GmtModifiedTime: sort by update time
        self.sort_by = sort_by
        # The job status. Valid values:
        # - ToRun: pending
        # - Running: running
        # - Success: successful
        # - Failure: failed
        # - Stopped: stopped or canceled
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.order is not None:
            result['Order'] = self.order

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

