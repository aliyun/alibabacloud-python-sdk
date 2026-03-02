# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDevelopersShrinkRequest(DaraModel):
    def __init__(
        self,
        account_ids_shrink: str = None,
        enterprise_id: int = None,
        name: str = None,
        order_by: str = None,
        order_direction: str = None,
        page_number: int = None,
        page_size: int = None,
        role_id: int = None,
    ):
        self.account_ids_shrink = account_ids_shrink
        self.enterprise_id = enterprise_id
        self.name = name
        self.order_by = order_by
        self.order_direction = order_direction
        self.page_number = page_number
        self.page_size = page_size
        self.role_id = role_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_ids_shrink is not None:
            result['accountIds'] = self.account_ids_shrink

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

        if self.role_id is not None:
            result['roleId'] = self.role_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountIds') is not None:
            self.account_ids_shrink = m.get('accountIds')

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

        if m.get('roleId') is not None:
            self.role_id = m.get('roleId')

        return self

