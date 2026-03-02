# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListComponentsRequest(DaraModel):
    def __init__(
        self,
        company_id: int = None,
        env: str = None,
        name: str = None,
        order_by: str = None,
        order_direction: str = None,
        page_number: int = None,
        page_size: int = None,
        product_id: int = None,
        template_id: int = None,
        type: str = None,
    ):
        # This parameter is required.
        self.company_id = company_id
        self.env = env
        self.name = name
        self.order_by = order_by
        self.order_direction = order_direction
        self.page_number = page_number
        self.page_size = page_size
        # This parameter is required.
        self.product_id = product_id
        self.template_id = template_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.company_id is not None:
            result['companyId'] = self.company_id

        if self.env is not None:
            result['env'] = self.env

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

        if self.product_id is not None:
            result['productId'] = self.product_id

        if self.template_id is not None:
            result['templateId'] = self.template_id

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('companyId') is not None:
            self.company_id = m.get('companyId')

        if m.get('env') is not None:
            self.env = m.get('env')

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

        if m.get('productId') is not None:
            self.product_id = m.get('productId')

        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

