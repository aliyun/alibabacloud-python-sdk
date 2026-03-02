# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListPdpPbcsRequest(DaraModel):
    def __init__(
        self,
        company_id: int = None,
        developer_id: str = None,
        keyword: str = None,
        order_by: str = None,
        order_direction: str = None,
        page_number: int = None,
        page_size: int = None,
        pbc_ids: List[int] = None,
    ):
        self.company_id = company_id
        self.developer_id = developer_id
        self.keyword = keyword
        self.order_by = order_by
        self.order_direction = order_direction
        self.page_number = page_number
        self.page_size = page_size
        self.pbc_ids = pbc_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.company_id is not None:
            result['companyId'] = self.company_id

        if self.developer_id is not None:
            result['developerId'] = self.developer_id

        if self.keyword is not None:
            result['keyword'] = self.keyword

        if self.order_by is not None:
            result['orderBy'] = self.order_by

        if self.order_direction is not None:
            result['orderDirection'] = self.order_direction

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.pbc_ids is not None:
            result['pbcIds'] = self.pbc_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('companyId') is not None:
            self.company_id = m.get('companyId')

        if m.get('developerId') is not None:
            self.developer_id = m.get('developerId')

        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')

        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')

        if m.get('orderDirection') is not None:
            self.order_direction = m.get('orderDirection')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('pbcIds') is not None:
            self.pbc_ids = m.get('pbcIds')

        return self

