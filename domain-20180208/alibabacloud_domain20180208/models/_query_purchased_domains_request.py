# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryPurchasedDomainsRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        domain_name: str = None,
        end_operation_time: str = None,
        op_time_order: bool = None,
        operation_status: int = None,
        page_size: int = None,
        product_type: int = None,
        start_operation_time: str = None,
        update_time_order: bool = None,
    ):
        self.current_page = current_page
        self.domain_name = domain_name
        self.end_operation_time = end_operation_time
        self.op_time_order = op_time_order
        self.operation_status = operation_status
        self.page_size = page_size
        self.product_type = product_type
        self.start_operation_time = start_operation_time
        self.update_time_order = update_time_order

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.end_operation_time is not None:
            result['EndOperationTime'] = self.end_operation_time

        if self.op_time_order is not None:
            result['OpTimeOrder'] = self.op_time_order

        if self.operation_status is not None:
            result['OperationStatus'] = self.operation_status

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.start_operation_time is not None:
            result['StartOperationTime'] = self.start_operation_time

        if self.update_time_order is not None:
            result['UpdateTimeOrder'] = self.update_time_order

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EndOperationTime') is not None:
            self.end_operation_time = m.get('EndOperationTime')

        if m.get('OpTimeOrder') is not None:
            self.op_time_order = m.get('OpTimeOrder')

        if m.get('OperationStatus') is not None:
            self.operation_status = m.get('OperationStatus')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('StartOperationTime') is not None:
            self.start_operation_time = m.get('StartOperationTime')

        if m.get('UpdateTimeOrder') is not None:
            self.update_time_order = m.get('UpdateTimeOrder')

        return self

