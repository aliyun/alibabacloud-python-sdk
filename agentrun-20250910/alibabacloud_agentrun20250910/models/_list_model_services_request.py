# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListModelServicesRequest(DaraModel):
    def __init__(
        self,
        model_type: str = None,
        page_number: int = None,
        page_size: int = None,
        provider: str = None,
        provider_type: str = None,
    ):
        # This parameter is required.
        self.model_type = model_type
        self.page_number = page_number
        self.page_size = page_size
        self.provider = provider
        self.provider_type = provider_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_type is not None:
            result['modelType'] = self.model_type

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.provider is not None:
            result['provider'] = self.provider

        if self.provider_type is not None:
            result['providerType'] = self.provider_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('modelType') is not None:
            self.model_type = m.get('modelType')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('provider') is not None:
            self.provider = m.get('provider')

        if m.get('providerType') is not None:
            self.provider_type = m.get('providerType')

        return self

