# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSecretsRequest(DaraModel):
    def __init__(
        self,
        gateway_type: str = None,
        name_like: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.gateway_type = gateway_type
        self.name_like = name_like
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gateway_type is not None:
            result['gatewayType'] = self.gateway_type

        if self.name_like is not None:
            result['nameLike'] = self.name_like

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gatewayType') is not None:
            self.gateway_type = m.get('gatewayType')

        if m.get('nameLike') is not None:
            self.name_like = m.get('nameLike')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        return self

