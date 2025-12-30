# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSnapshotUrlsRequest(DaraModel):
    def __init__(
        self,
        job_id: str = None,
        order_by: str = None,
        page_number: int = None,
        page_size: int = None,
        timeout: int = None,
    ):
        # The job ID.
        self.job_id = job_id
        # The order that you use to sort the query results. Valid values: Asc and Desc.
        # 
        # - Asc
        # 
        # - Desc
        self.order_by = order_by
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 30. Default value: 10.
        self.page_size = page_size
        # The authentication timeout period. Unit: seconds Default value: 3600. Maximum value: 129600 (36 hours).
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        return self

