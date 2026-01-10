# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class ListGatewaysOutput(DaraModel):
    def __init__(
        self,
        items: main_models.Gateway = None,
        page_number: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.items = items
        self.page_number = page_number
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.items is not None:
            result['items'] = self.items.to_map()

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('items') is not None:
            temp_model = main_models.Gateway()
            self.items = temp_model.from_map(m.get('items'))

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

