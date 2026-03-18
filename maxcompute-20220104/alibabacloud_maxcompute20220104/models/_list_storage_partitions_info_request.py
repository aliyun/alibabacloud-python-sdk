# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListStoragePartitionsInfoRequest(DaraModel):
    def __init__(
        self,
        asc_order: bool = None,
        date: str = None,
        order_column: str = None,
        page_number: int = None,
        page_size: int = None,
        partition_prefix: str = None,
        region: str = None,
        schema: str = None,
        tenant_id: str = None,
        types: List[str] = None,
    ):
        self.asc_order = asc_order
        # This parameter is required.
        self.date = date
        self.order_column = order_column
        self.page_number = page_number
        self.page_size = page_size
        self.partition_prefix = partition_prefix
        self.region = region
        self.schema = schema
        self.tenant_id = tenant_id
        self.types = types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asc_order is not None:
            result['ascOrder'] = self.asc_order

        if self.date is not None:
            result['date'] = self.date

        if self.order_column is not None:
            result['orderColumn'] = self.order_column

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.partition_prefix is not None:
            result['partitionPrefix'] = self.partition_prefix

        if self.region is not None:
            result['region'] = self.region

        if self.schema is not None:
            result['schema'] = self.schema

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.types is not None:
            result['types'] = self.types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ascOrder') is not None:
            self.asc_order = m.get('ascOrder')

        if m.get('date') is not None:
            self.date = m.get('date')

        if m.get('orderColumn') is not None:
            self.order_column = m.get('orderColumn')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('partitionPrefix') is not None:
            self.partition_prefix = m.get('partitionPrefix')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('schema') is not None:
            self.schema = m.get('schema')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('types') is not None:
            self.types = m.get('types')

        return self

