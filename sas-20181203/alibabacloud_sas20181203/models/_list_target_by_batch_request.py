# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTargetByBatchRequest(DaraModel):
    def __init__(
        self,
        batch_id: int = None,
        current_page: int = None,
        operation_base: int = None,
        page_size: int = None,
    ):
        # The ID of the release batch.
        self.batch_id = batch_id
        # The page number of the current page in a paginated query.
        # 
        # This parameter is required.
        self.current_page = current_page
        # Asset selection dimension. Values:
        # 
        # - **0**: Machine instance
        # - **1**: Machine group
        # - **2**: VPC instance ID
        self.operation_base = operation_base
        # The maximum number of items to return per page in a paginated query.
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
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.operation_base is not None:
            result['OperationBase'] = self.operation_base

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('OperationBase') is not None:
            self.operation_base = m.get('OperationBase')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

