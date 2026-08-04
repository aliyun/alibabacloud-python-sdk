# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aicontent20240611 import models as main_models
from darabonba.model import DaraModel

class ModelRouterBatchCreateModelRequest(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        base_url: str = None,
        models: List[main_models.BatchCreateModelItemDTO] = None,
        symbol: str = None,
    ):
        # The API key. This parameter is required. The key is shared by the same provider and reused by all models.
        # 
        # This parameter is required.
        self.api_key = api_key
        # The base URL. This parameter is optional. Specify this parameter when you use a custom gateway address. If you do not specify this parameter, the default address of the provider is used.
        self.base_url = base_url
        # The list of models to create in batches. This parameter is required. At least one item must be specified.
        # 
        # This parameter is required.
        self.models = models
        # The provider symbol. This parameter is required. All models items share the same provider.
        # 
        # This parameter is required.
        self.symbol = symbol

    def validate(self):
        if self.models:
            for v1 in self.models:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['apiKey'] = self.api_key

        if self.base_url is not None:
            result['baseUrl'] = self.base_url

        result['models'] = []
        if self.models is not None:
            for k1 in self.models:
                result['models'].append(k1.to_map() if k1 else None)

        if self.symbol is not None:
            result['symbol'] = self.symbol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiKey') is not None:
            self.api_key = m.get('apiKey')

        if m.get('baseUrl') is not None:
            self.base_url = m.get('baseUrl')

        self.models = []
        if m.get('models') is not None:
            for k1 in m.get('models'):
                temp_model = main_models.BatchCreateModelItemDTO()
                self.models.append(temp_model.from_map(k1))

        if m.get('symbol') is not None:
            self.symbol = m.get('symbol')

        return self

