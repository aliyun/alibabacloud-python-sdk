# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class VectorStoreConfig(DaraModel):
    def __init__(
        self,
        config: main_models.VectorStoreConfigConfig = None,
        provider: str = None,
    ):
        self.config = config
        self.provider = provider

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['config'] = self.config.to_map()

        if self.provider is not None:
            result['provider'] = self.provider

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            temp_model = main_models.VectorStoreConfigConfig()
            self.config = temp_model.from_map(m.get('config'))

        if m.get('provider') is not None:
            self.provider = m.get('provider')

        return self

class VectorStoreConfigConfig(DaraModel):
    def __init__(
        self,
        collection_name: str = None,
        endpoint: str = None,
        instance_name: str = None,
        vector_dimension: int = None,
    ):
        self.collection_name = collection_name
        self.endpoint = endpoint
        self.instance_name = instance_name
        self.vector_dimension = vector_dimension

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.collection_name is not None:
            result['collectionName'] = self.collection_name

        if self.endpoint is not None:
            result['endpoint'] = self.endpoint

        if self.instance_name is not None:
            result['instanceName'] = self.instance_name

        if self.vector_dimension is not None:
            result['vectorDimension'] = self.vector_dimension

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('collectionName') is not None:
            self.collection_name = m.get('collectionName')

        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')

        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')

        if m.get('vectorDimension') is not None:
            self.vector_dimension = m.get('vectorDimension')

        return self

