# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPdpImageRequest(DaraModel):
    def __init__(
        self,
        order_by: str = None,
        order_direction: str = None,
        page_number: int = None,
        page_size: int = None,
        service_group_id: int = None,
    ):
        self.order_by = order_by
        self.order_direction = order_direction
        self.page_number = page_number
        self.page_size = page_size
        # This parameter is required.
        self.service_group_id = service_group_id

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

        if self.service_group_id is not None:
            result['serviceGroupId'] = self.service_group_id

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

        if m.get('serviceGroupId') is not None:
            self.service_group_id = m.get('serviceGroupId')

        return self

