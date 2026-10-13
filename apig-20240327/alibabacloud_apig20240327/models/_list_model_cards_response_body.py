# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class ListModelCardsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListModelCardsResponseBodyData] = None,
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
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.ListModelCardsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListModelCardsResponseBodyData(DaraModel):
    def __init__(
        self,
        available_paths: List[main_models.ListModelCardsResponseBodyDataAvailablePaths] = None,
        features: Dict[str, Any] = None,
        meta: main_models.ListModelCardsResponseBodyDataMeta = None,
        model_name: str = None,
        pricing: Dict[str, Any] = None,
        provider: str = None,
        snapshots: List[Dict[str, Any]] = None,
        source: str = None,
    ):
        # The list of available paths for the model card. Each element consists of a path and a type member. The API definition does not specify the criteria for determining availability.
        self.available_paths = available_paths
        # The feature configuration of the model card in a key-value pair map structure. The set of keys is not specified in the API definition.
        self.features = features
        # The metadata container of the model card. Only the description member is declared in the API definition.
        self.meta = meta
        # The name of the model.
        self.model_name = model_name
        # The pricing information of the model card in a key-value pair map structure. The set of keys and billing criteria are not specified in the API definition.
        self.pricing = pricing
        # The identifier of the model provider for the model card.
        self.provider = provider
        # The list of snapshots for the model card. Array items are map structures with unspecified members. The API definition does not specify the snapshot content or generation rules.
        self.snapshots = snapshots
        # The source identifier of the model card. The valid values are not specified in the API definition.
        self.source = source

    def validate(self):
        if self.available_paths:
            for v1 in self.available_paths:
                 if v1:
                    v1.validate()
        if self.meta:
            self.meta.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['availablePaths'] = []
        if self.available_paths is not None:
            for k1 in self.available_paths:
                result['availablePaths'].append(k1.to_map() if k1 else None)

        if self.features is not None:
            result['features'] = self.features

        if self.meta is not None:
            result['meta'] = self.meta.to_map()

        if self.model_name is not None:
            result['modelName'] = self.model_name

        if self.pricing is not None:
            result['pricing'] = self.pricing

        if self.provider is not None:
            result['provider'] = self.provider

        if self.snapshots is not None:
            result['snapshots'] = self.snapshots

        if self.source is not None:
            result['source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.available_paths = []
        if m.get('availablePaths') is not None:
            for k1 in m.get('availablePaths'):
                temp_model = main_models.ListModelCardsResponseBodyDataAvailablePaths()
                self.available_paths.append(temp_model.from_map(k1))

        if m.get('features') is not None:
            self.features = m.get('features')

        if m.get('meta') is not None:
            temp_model = main_models.ListModelCardsResponseBodyDataMeta()
            self.meta = temp_model.from_map(m.get('meta'))

        if m.get('modelName') is not None:
            self.model_name = m.get('modelName')

        if m.get('pricing') is not None:
            self.pricing = m.get('pricing')

        if m.get('provider') is not None:
            self.provider = m.get('provider')

        if m.get('snapshots') is not None:
            self.snapshots = m.get('snapshots')

        if m.get('source') is not None:
            self.source = m.get('source')

        return self

class ListModelCardsResponseBodyDataMeta(DaraModel):
    def __init__(
        self,
        description: str = None,
    ):
        # The description text of the model card.
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        return self

class ListModelCardsResponseBodyDataAvailablePaths(DaraModel):
    def __init__(
        self,
        path: str = None,
        type: str = None,
    ):
        # The request path of the API.
        self.path = path
        # The type identifier of the available path record. The valid values are not specified in the API definition.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.path is not None:
            result['path'] = self.path

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('path') is not None:
            self.path = m.get('path')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

