# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListModelProvidersRequest(DaraModel):
    def __init__(
        self,
        model_name: str = None,
        model_type: str = None,
        page_number: str = None,
        page_size: str = None,
        provider: str = None,
    ):
        self.model_name = model_name
        self.model_type = model_type
        self.page_number = page_number
        self.page_size = page_size
        self.provider = provider

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_name is not None:
            result['modelName'] = self.model_name

        if self.model_type is not None:
            result['modelType'] = self.model_type

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.provider is not None:
            result['provider'] = self.provider

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('modelName') is not None:
            self.model_name = m.get('modelName')

        if m.get('modelType') is not None:
            self.model_type = m.get('modelType')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('provider') is not None:
            self.provider = m.get('provider')

        return self

