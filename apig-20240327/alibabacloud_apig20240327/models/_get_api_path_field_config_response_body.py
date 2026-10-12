# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class GetApiPathFieldConfigResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetApiPathFieldConfigResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response status code.
        self.code = code
        # The response data.
        self.data = data
        # The response message.
        self.message = message
        # The request ID.
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

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetApiPathFieldConfigResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetApiPathFieldConfigResponseBodyData(DaraModel):
    def __init__(
        self,
        api_id: str = None,
        gateway_id: str = None,
        path_configs: List[main_models.GetApiPathFieldConfigResponseBodyDataPathConfigs] = None,
    ):
        # The ID of the HTTP API.
        self.api_id = api_id
        # The ID of the cloud-native API gateway.
        self.gateway_id = gateway_id
        # The list of field configurations grouped by API request path.
        self.path_configs = path_configs

    def validate(self):
        if self.path_configs:
            for v1 in self.path_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_id is not None:
            result['apiId'] = self.api_id

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        result['pathConfigs'] = []
        if self.path_configs is not None:
            for k1 in self.path_configs:
                result['pathConfigs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiId') is not None:
            self.api_id = m.get('apiId')

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        self.path_configs = []
        if m.get('pathConfigs') is not None:
            for k1 in m.get('pathConfigs'):
                temp_model = main_models.GetApiPathFieldConfigResponseBodyDataPathConfigs()
                self.path_configs.append(temp_model.from_map(k1))

        return self

class GetApiPathFieldConfigResponseBodyDataPathConfigs(DaraModel):
    def __init__(
        self,
        field_paths: Dict[str, List[main_models.DataPathConfigsFieldPathsValue]] = None,
        path: str = None,
    ):
        # The collection of field configurations under the path, grouped by mapping key, where each group represents a set of field configuration items.
        self.field_paths = field_paths
        # The request path of the API.
        self.path = path

    def validate(self):
        if self.field_paths:
            for v1 in self.field_paths.values():
                for v2 in v1:
                     if v2:
                        v2.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['fieldPaths'] = {}
        if self.field_paths is not None:
            for k1, v1 in self.field_paths.items():
                l1 = []
                for k2 in v1:
                    l1.append(k2.to_map() if k2 else None)
                result['fieldPaths'][k1] = l1

        if self.path is not None:
            result['path'] = self.path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.field_paths = {}
        if m.get('fieldPaths') is not None:
            for k1, v1 in m.get('fieldPaths').items():
                l1 = []
                for k2 in v1:
                    temp_model = main_models.DataPathConfigsFieldPathsValue()
                    l1.append(temp_model.from_map(k2))
                self.field_paths[k1] = l1

        if m.get('path') is not None:
            self.path = m.get('path')

        return self

