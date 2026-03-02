# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListMetadataInfosRequest(DaraModel):
    def __init__(
        self,
        env: str = None,
        namespace_id: int = None,
        namespace_name: str = None,
        order_by: str = None,
        order_direction: str = None,
        org_id: int = None,
        page_number: int = None,
        page_size: int = None,
        pbc_id: int = None,
    ):
        self.env = env
        self.namespace_id = namespace_id
        self.namespace_name = namespace_name
        self.order_by = order_by
        self.order_direction = order_direction
        self.org_id = org_id
        self.page_number = page_number
        self.page_size = page_size
        # This parameter is required.
        self.pbc_id = pbc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.env is not None:
            result['env'] = self.env

        if self.namespace_id is not None:
            result['namespace_id'] = self.namespace_id

        if self.namespace_name is not None:
            result['namespace_name'] = self.namespace_name

        if self.order_by is not None:
            result['order_by'] = self.order_by

        if self.order_direction is not None:
            result['order_direction'] = self.order_direction

        if self.org_id is not None:
            result['org_id'] = self.org_id

        if self.page_number is not None:
            result['page_number'] = self.page_number

        if self.page_size is not None:
            result['page_size'] = self.page_size

        if self.pbc_id is not None:
            result['pbc_id'] = self.pbc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('env') is not None:
            self.env = m.get('env')

        if m.get('namespace_id') is not None:
            self.namespace_id = m.get('namespace_id')

        if m.get('namespace_name') is not None:
            self.namespace_name = m.get('namespace_name')

        if m.get('order_by') is not None:
            self.order_by = m.get('order_by')

        if m.get('order_direction') is not None:
            self.order_direction = m.get('order_direction')

        if m.get('org_id') is not None:
            self.org_id = m.get('org_id')

        if m.get('page_number') is not None:
            self.page_number = m.get('page_number')

        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')

        if m.get('pbc_id') is not None:
            self.pbc_id = m.get('pbc_id')

        return self

