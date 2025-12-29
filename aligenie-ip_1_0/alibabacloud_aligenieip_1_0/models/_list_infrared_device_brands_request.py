# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListInfraredDeviceBrandsRequest(DaraModel):
    def __init__(
        self,
        category: str = None,
        service_provider: str = None,
    ):
        # This parameter is required.
        self.category = category
        self.service_provider = service_provider

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.service_provider is not None:
            result['ServiceProvider'] = self.service_provider

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('ServiceProvider') is not None:
            self.service_provider = m.get('ServiceProvider')

        return self

