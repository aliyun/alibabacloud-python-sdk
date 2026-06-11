# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class CreateContextStoreRequest(DaraModel):
    def __init__(
        self,
        config: main_models.CreateContextStoreRequestConfig = None,
        context_store_name: str = None,
        context_type: str = None,
        dataset: main_models.CreateContextStoreRequestDataset = None,
        description: str = None,
    ):
        # The configuration.
        self.config = config
        # The name of the context store.
        # 
        # This parameter is required.
        self.context_store_name = context_store_name
        # The type of the context store.
        # 
        # This parameter is required.
        self.context_type = context_type
        # The properties of the dataset.
        self.dataset = dataset
        # The description of the context store.
        self.description = description

    def validate(self):
        if self.config:
            self.config.validate()
        if self.dataset:
            self.dataset.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['config'] = self.config.to_map()

        if self.context_store_name is not None:
            result['contextStoreName'] = self.context_store_name

        if self.context_type is not None:
            result['contextType'] = self.context_type

        if self.dataset is not None:
            result['dataset'] = self.dataset.to_map()

        if self.description is not None:
            result['description'] = self.description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            temp_model = main_models.CreateContextStoreRequestConfig()
            self.config = temp_model.from_map(m.get('config'))

        if m.get('contextStoreName') is not None:
            self.context_store_name = m.get('contextStoreName')

        if m.get('contextType') is not None:
            self.context_type = m.get('contextType')

        if m.get('dataset') is not None:
            temp_model = main_models.CreateContextStoreRequestDataset()
            self.dataset = temp_model.from_map(m.get('dataset'))

        if m.get('description') is not None:
            self.description = m.get('description')

        return self

class CreateContextStoreRequestDataset(DaraModel):
    def __init__(
        self,
        name: str = None,
    ):
        # The name of the dataset.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class CreateContextStoreRequestConfig(DaraModel):
    def __init__(
        self,
        metadata_field: Dict[str, str] = None,
        source: main_models.CreateContextStoreRequestConfigSource = None,
    ):
        # The metadata fields.
        self.metadata_field = metadata_field
        # The configuration source.
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
            temp_model = main_models.CreateContextStoreRequestConfigSource()
            self.source = temp_model.from_map(m.get('source'))

        return self

class CreateContextStoreRequestConfigSource(DaraModel):
    def __init__(
        self,
        logstore: str = None,
        project: str = None,
        start_time: str = None,
    ):
        # The name of the Log Service Logstore.
        self.logstore = logstore
        # The name of the Log Service project.
        self.project = project
        # The effective start time.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.logstore is not None:
            result['logstore'] = self.logstore

        if self.project is not None:
            result['project'] = self.project

        if self.start_time is not None:
            result['startTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')

        if m.get('project') is not None:
            self.project = m.get('project')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        return self

