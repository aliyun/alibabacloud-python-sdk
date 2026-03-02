# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListMicroServiceRequest(DaraModel):
    def __init__(
        self,
        order_by: str = None,
        order_direction: str = None,
        page_number: int = None,
        page_size: int = None,
        pbc_id: int = None,
        service_ids: str = None,
    ):
        self.order_by = order_by
        self.order_direction = order_direction
        self.page_number = page_number
        self.page_size = page_size
        self.pbc_id = pbc_id
        self.service_ids = service_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.service_ids is not None:
            result['serviceIds'] = self.service_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        if m.get('serviceIds') is not None:
            self.service_ids = m.get('serviceIds')

        return self

