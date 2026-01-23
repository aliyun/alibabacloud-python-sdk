# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetPurchaseControlRecordRequest(DaraModel):
    def __init__(
        self,
        customer_uid: int = None,
        operation_time: str = None,
        page_no: int = None,
        page_size: int = None,
    ):
        # This parameter is required.
        self.customer_uid = customer_uid
        self.operation_time = operation_time
        # This parameter is required.
        self.page_no = page_no
        # This parameter is required.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.customer_uid is not None:
            result['CustomerUID'] = self.customer_uid

        if self.operation_time is not None:
            result['OperationTime'] = self.operation_time

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomerUID') is not None:
            self.customer_uid = m.get('CustomerUID')

        if m.get('OperationTime') is not None:
            self.operation_time = m.get('OperationTime')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

