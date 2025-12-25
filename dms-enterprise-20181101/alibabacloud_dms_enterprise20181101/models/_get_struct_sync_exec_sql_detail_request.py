# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetStructSyncExecSqlDetailRequest(DaraModel):
    def __init__(
        self,
        order_id: int = None,
        page_number: int = None,
        page_size: int = None,
        tid: int = None,
    ):
        # The ID of the ticket.
        # 
        # This parameter is required.
        self.order_id = order_id
        # The number of the page to return.
        self.page_number = page_number
        # The number of entries to return on each page.
        self.page_size = page_size
        # The ID of the tenant.
        # 
        # > To view the tenant ID, move the pointer over the profile picture in the upper-right corner of the Data Management (DMS) console. For more information, see [Manage DMS tenants](https://help.aliyun.com/document_detail/181330.html).
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

