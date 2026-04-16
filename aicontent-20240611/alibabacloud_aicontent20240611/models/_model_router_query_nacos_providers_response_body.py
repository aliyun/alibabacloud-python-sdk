# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aicontent20240611 import models as main_models
from darabonba.model import DaraModel

class ModelRouterQueryNacosProvidersResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ModelRouterQueryNacosProvidersResponseBodyData] = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.err_code is not None:
            result['errCode'] = self.err_code

        if self.err_message is not None:
            result['errMessage'] = self.err_message

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.ModelRouterQueryNacosProvidersResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')

        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class ModelRouterQueryNacosProvidersResponseBodyData(DaraModel):
    def __init__(
        self,
        base_url: str = None,
        models: List[main_models.ModelRouterQueryNacosProvidersResponseBodyDataModels] = None,
        name: str = None,
        symbol: str = None,
    ):
        self.base_url = base_url
        self.models = models
        self.name = name
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
        if self.base_url is not None:
            result['baseUrl'] = self.base_url

        result['models'] = []
        if self.models is not None:
            for k1 in self.models:
                result['models'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['name'] = self.name

        if self.symbol is not None:
            result['symbol'] = self.symbol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('baseUrl') is not None:
            self.base_url = m.get('baseUrl')

        self.models = []
        if m.get('models') is not None:
            for k1 in m.get('models'):
                temp_model = main_models.ModelRouterQueryNacosProvidersResponseBodyDataModels()
                self.models.append(temp_model.from_map(k1))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('symbol') is not None:
            self.symbol = m.get('symbol')

        return self

class ModelRouterQueryNacosProvidersResponseBodyDataModels(DaraModel):
    def __init__(
        self,
        extensions: main_models.ModelRouterQueryNacosProvidersResponseBodyDataModelsExtensions = None,
        identifier: str = None,
        in_out: str = None,
        input_token: str = None,
        output_token: str = None,
        type: str = None,
    ):
        self.extensions = extensions
        self.identifier = identifier
        self.in_out = in_out
        self.input_token = input_token
        self.output_token = output_token
        self.type = type

    def validate(self):
        if self.extensions:
            self.extensions.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extensions is not None:
            result['extensions'] = self.extensions.to_map()

        if self.identifier is not None:
            result['identifier'] = self.identifier

        if self.in_out is not None:
            result['inOut'] = self.in_out

        if self.input_token is not None:
            result['inputToken'] = self.input_token

        if self.output_token is not None:
            result['outputToken'] = self.output_token

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('extensions') is not None:
            temp_model = main_models.ModelRouterQueryNacosProvidersResponseBodyDataModelsExtensions()
            self.extensions = temp_model.from_map(m.get('extensions'))

        if m.get('identifier') is not None:
            self.identifier = m.get('identifier')

        if m.get('inOut') is not None:
            self.in_out = m.get('inOut')

        if m.get('inputToken') is not None:
            self.input_token = m.get('inputToken')

        if m.get('outputToken') is not None:
            self.output_token = m.get('outputToken')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class ModelRouterQueryNacosProvidersResponseBodyDataModelsExtensions(DaraModel):
    def __init__(
        self,
        async_: bool = None,
    ):
        self.async_ = async_

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.async_ is not None:
            result['async'] = self.async_

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('async') is not None:
            self.async_ = m.get('async')

        return self

