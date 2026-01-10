# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class ListModelProvidersResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListModelProvidersResponseBodyData = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.ListModelProvidersResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListModelProvidersResponseBodyData(DaraModel):
    def __init__(
        self,
        items: List[main_models.ListModelProvidersResponseBodyDataItems] = None,
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
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.ListModelProvidersResponseBodyDataItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListModelProvidersResponseBodyDataItems(DaraModel):
    def __init__(
        self,
        base_url: str = None,
        model_info_config: main_models.ModelInfoConfig = None,
        model_type: str = None,
        models: List[str] = None,
        provider_name: str = None,
    ):
        # baseUrl
        self.base_url = base_url
        # modelInfoConfig
        self.model_info_config = model_info_config
        self.model_type = model_type
        self.models = models
        self.provider_name = provider_name

    def validate(self):
        if self.model_info_config:
            self.model_info_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.base_url is not None:
            result['baseUrl'] = self.base_url

        if self.model_info_config is not None:
            result['modelInfoConfig'] = self.model_info_config.to_map()

        if self.model_type is not None:
            result['modelType'] = self.model_type

        if self.models is not None:
            result['models'] = self.models

        if self.provider_name is not None:
            result['providerName'] = self.provider_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('baseUrl') is not None:
            self.base_url = m.get('baseUrl')

        if m.get('modelInfoConfig') is not None:
            temp_model = main_models.ModelInfoConfig()
            self.model_info_config = temp_model.from_map(m.get('modelInfoConfig'))

        if m.get('modelType') is not None:
            self.model_type = m.get('modelType')

        if m.get('models') is not None:
            self.models = m.get('models')

        if m.get('providerName') is not None:
            self.provider_name = m.get('providerName')

        return self

