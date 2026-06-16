# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_agentloop20260520 import models as main_models
from darabonba.model import DaraModel

class UpdateContextStoreRequest(DaraModel):
    def __init__(
        self,
        config: main_models.UpdateContextStoreRequestConfig = None,
        context_type: str = None,
        description: str = None,
        client_token: str = None,
    ):
        self.config = config
        self.context_type = context_type
        self.description = description
        self.client_token = client_token

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

        if self.context_type is not None:
            result['contextType'] = self.context_type

        if self.description is not None:
            result['description'] = self.description

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            temp_model = main_models.UpdateContextStoreRequestConfig()
            self.config = temp_model.from_map(m.get('config'))

        if m.get('contextType') is not None:
            self.context_type = m.get('contextType')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        return self

class UpdateContextStoreRequestConfig(DaraModel):
    def __init__(
        self,
        metadata_field: Dict[str, str] = None,
        source: main_models.UpdateContextStoreRequestConfigSource = None,
    ):
        self.metadata_field = metadata_field
        self.source = source

    def validate(self):
        if self.source:
            self.source.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.metadata_field is not None:
            result['metadataField'] = self.metadata_field

        if self.source is not None:
            result['source'] = self.source.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('metadataField') is not None:
            self.metadata_field = m.get('metadataField')

        if m.get('source') is not None:
            temp_model = main_models.UpdateContextStoreRequestConfigSource()
            self.source = temp_model.from_map(m.get('source'))

        return self

class UpdateContextStoreRequestConfigSource(DaraModel):
    def __init__(
        self,
        agent_space: str = None,
        start_time: str = None,
    ):
        self.agent_space = agent_space
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_space is not None:
            result['agentSpace'] = self.agent_space

        if self.start_time is not None:
            result['startTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentSpace') is not None:
            self.agent_space = m.get('agentSpace')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        return self

