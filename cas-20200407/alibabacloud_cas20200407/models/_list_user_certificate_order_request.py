# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListUserCertificateOrderRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        keyword: str = None,
        order_type: str = None,
        resource_group_id: str = None,
        show_size: int = None,
        status: str = None,
    ):
        # The page number of the current page in a paginated query.
        self.current_page = current_page
        # The keyword for fuzzy search. Matches the domain name or the corresponding resource ID.
        self.keyword = keyword
        # The resource type. Default value: **CPACK**. Valid values:
        # 
        # - **CPACK**: resource virtual order. Only orders generated from quotas are returned.
        # - **BUY**: purchase order. Only orders generated from purchases are returned. You can ignore this type in most cases.
        # - **UPLOAD**: uploaded certificate. Only uploaded certificates are returned.
        # - **CERT**: certificate. Both issued certificates and uploaded certificates are returned.
        self.order_type = order_type
        # The resource group ID. You can obtain this ID by calling the [ListResources](https://help.aliyun.com/document_detail/2716559.html) operation.
        self.resource_group_id = resource_group_id
        # The number of entries per page in a paginated query. Default value: 50.
        self.show_size = show_size
        # The order status. Valid values:
        # 
        # - **PAYED**: Pending application. Valid when OrderType is set to CPACK or BUY.
        # - **CHECKING**: Under review. Valid when OrderType is set to CPACK or BUY.
        # - **CHECKED_FAIL**: Review failed. Valid when OrderType is set to CPACK or BUY.
        # - **ISSUED**: Issued.
        # - **WILLEXPIRED**: About to expire.
        # - **EXPIRED**: Expired.
        # - **NOTACTIVATED**: Not activated. Valid when OrderType is set to CPACK or BUY.
        # - **REVOKED**: Revoked. Valid when OrderType is set to CPACK or BUY.
        # 
        # If OrderType is set to CERT or UPLOAD and Status is empty, valid certificates are returned by default, including issued and about-to-expire certificates. If OrderType is set to CPACK or BUY and Status is empty, all orders are returned by default.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.show_size is not None:
            result['ShowSize'] = self.show_size

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

