# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListPdpServicesRequest(DaraModel):
    def __init__(
        self,
        alias: str = None,
        enterprise_id: int = None,
        name: str = None,
        order_by: str = None,
        order_direction: str = None,
        page_number: int = None,
        page_size: int = None,
        pbc_id: int = None,
        pdp_service_ids: List[int] = None,
        product_id: int = None,
    ):
        self.alias = alias
        self.enterprise_id = enterprise_id
        self.name = name
        self.order_by = order_by
        self.order_direction = order_direction
        self.page_number = page_number
        self.page_size = page_size
        self.pbc_id = pbc_id
        self.pdp_service_ids = pdp_service_ids
        self.product_id = product_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['alias'] = self.alias

        if self.enterprise_id is not None:
            result['enterpriseId'] = self.enterprise_id

        if self.name is not None:
            result['name'] = self.name

        if self.order_by is not None:
            result['orderBy'] = self.order_by

        if self.order_direction is not None:
            result['orderDirection'] = self.order_direction

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.pbc_id is not None:
            result['pbcId'] = self.pbc_id

        if self.pdp_service_ids is not None:
            result['pdpServiceIds'] = self.pdp_service_ids

        if self.product_id is not None:
            result['productId'] = self.product_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alias') is not None:
            self.alias = m.get('alias')

        if m.get('enterpriseId') is not None:
            self.enterprise_id = m.get('enterpriseId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')

        if m.get('orderDirection') is not None:
            self.order_direction = m.get('orderDirection')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('pbcId') is not None:
            self.pbc_id = m.get('pbcId')

        if m.get('pdpServiceIds') is not None:
            self.pdp_service_ids = m.get('pdpServiceIds')

        if m.get('productId') is not None:
            self.product_id = m.get('productId')

        return self

