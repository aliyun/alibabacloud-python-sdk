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
        # The page number. Default value: 1.
        self.current_page = current_page
        # Performs a fuzzy query. The keyword can be a domain name or a resource ID.
        self.keyword = keyword
        # The resource type. Default value: **CPACK**. Valid values:
        # 
        # - **CPACK**: An order for a resource plan. Only orders created from a resource plan are returned.
        # 
        # - **BUY**: A direct purchase. Only orders created from direct purchases are returned. You can ignore this type in most cases.
        # 
        # - **UPLOAD**: An uploaded certificate. Only uploaded certificates are returned.
        # 
        # - **CERT**: A certificate. Both issued and uploaded certificates are returned.
        self.order_type = order_type
        # The ID of the resource group. For more information, see [ListResources](https://help.aliyun.com/document_detail/2716559.html).
        self.resource_group_id = resource_group_id
        # The number of entries to return on each page. Default value: 50.
        self.show_size = show_size
        # The status of the order. Valid values:
        # 
        # - **PAYED**: The certificate is pending application. This value is valid only when OrderType is set to CPACK or BUY.
        # 
        # - **CHECKING**: The certificate is under review. This value is valid only when OrderType is set to CPACK or BUY.
        # 
        # - **CHECKED_FAIL**: The review failed. This value is valid only when OrderType is set to CPACK or BUY.
        # 
        # - **ISSUED**: The certificate is issued.
        # 
        # - **WILLEXPIRED**: The certificate is about to expire.
        # 
        # - **EXPIRED**: The certificate has expired.
        # 
        # - **NOTACTIVATED**: The certificate is not activated. This value is valid only when OrderType is set to CPACK or BUY.
        # 
        # - **REVOKED**: The certificate is revoked. This value is valid only when OrderType is set to CPACK or BUY.
        # 
        # If OrderType is CERT or UPLOAD and you leave this parameter empty, active certificates are returned by default. Active certificates are those in the ISSUED or WILLEXPIRED state. If OrderType is CPACK or BUY and you leave this parameter empty, all orders are returned by default.
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

