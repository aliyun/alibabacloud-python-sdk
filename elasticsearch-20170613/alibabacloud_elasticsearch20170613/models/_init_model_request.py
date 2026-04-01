# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class InitModelRequest(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        host: str = None,
        http_schema: str = None,
        models: List[main_models.InitModelRequestModels] = None,
        workspace: str = None,
    ):
        # This parameter is required.
        self.api_key = api_key
        # This parameter is required.
        self.host = host
        # This parameter is required.
        self.http_schema = http_schema
        self.models = models
        # This parameter is required.
        self.workspace = workspace

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
            result['api_key'] = self.api_key

        if self.host is not None:
            result['host'] = self.host

        if self.http_schema is not None:
            result['http_schema'] = self.http_schema

        result['models'] = []
        if self.models is not None:
            for k1 in self.models:
                result['models'].append(k1.to_map() if k1 else None)

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('api_key') is not None:
            self.api_key = m.get('api_key')

        if m.get('host') is not None:
            self.host = m.get('host')

        if m.get('http_schema') is not None:
            self.http_schema = m.get('http_schema')

        self.models = []
        if m.get('models') is not None:
            for k1 in m.get('models'):
                temp_model = main_models.InitModelRequestModels()
                self.models.append(temp_model.from_map(k1))

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

class InitModelRequestModels(DaraModel):
    def __init__(
        self,
        model_type: str = None,
        service_id: str = None,
    ):
        self.model_type = model_type
        self.service_id = service_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_type is not None:
            result['modelType'] = self.model_type

        if self.service_id is not None:
            result['serviceId'] = self.service_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('modelType') is not None:
            self.model_type = m.get('modelType')

        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')

        return self

