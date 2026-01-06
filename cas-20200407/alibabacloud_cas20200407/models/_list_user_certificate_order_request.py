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
        # The number of the page to return.
        self.current_page = current_page
        # The domain name that is bound or the ID of the resource. Fuzzy match is supported.
        self.keyword = keyword
        # The type of the order. Default value: **CPACK**. Valid values:
        # 
        # *   **CPACK**: virtual resource order. If you set OrderType to CPACK, only the information about orders that are generated to consume the certificate quota is returned.
        # *   **BUY**: purchase order. If you set OrderType to BUY, only the information about purchase orders is returned. In most cases, this type of order can be ignored.
        # *   **UPLOAD**: uploaded certificate. If you set OrderType to UPLOAD, only uploaded certificates are returned.
        # *   **CERT**: certificate. If you set OrderType to CERT, both issued certificates and uploaded certificates are returned.
        self.order_type = order_type
        # The ID of the resource group. You can call the [ListResources](https://help.aliyun.com/document_detail/2716559.html) operation to obtain the ID.
        self.resource_group_id = resource_group_id
        # The number of entries to return on each page. Default value: 50.
        self.show_size = show_size
        # The certificate status of the order. Valid values:
        # 
        # *   **PAYED**: pending application. You can set Status to PAYED only if you set OrderType to CPACK or BUY.
        # *   **CHECKING**: validating. You can set Status to CHECKING only if you set OrderType to CPACK or BUY.
        # *   **CHECKED_FAIL**: validation failed. You can set Status to CHECKED_FAIL only if you set OrderType to CPACK or BUY.
        # *   **ISSUED**: issued.
        # *   **WILLEXPIRED**: about to expire.
        # *   **EXPIRED**: expired.
        # *   **NOTACTIVATED**: not activated. You can set Status to NOTACTIVATED only if you set OrderType to CPACK or BUY.
        # *   **REVOKED**: revoked. You can set Status to REVOKED only if you set OrderType to CPACK or BUY.
        # 
        # If you set OrderType to CERT or UPLOAD and Status is left empty, valid certificates are returned by default, including issued certificates and certificates that are about to expire. If you set OrderType to CPACK or BUY and Status is left empty, all orders are returned by default.
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

