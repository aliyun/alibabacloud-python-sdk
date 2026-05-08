# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class GetContextStoreResponseBody(DaraModel):
    def __init__(
        self,
        config: main_models.GetContextStoreResponseBodyConfig = None,
        context_store_name: str = None,
        context_type: str = None,
        create_time: str = None,
        dataset: main_models.GetContextStoreResponseBodyDataset = None,
        description: str = None,
        region_id: str = None,
        request_id: str = None,
        status: str = None,
        update_time: str = None,
        workspace: str = None,
    ):
        self.config = config
        self.context_store_name = context_store_name
        self.context_type = context_type
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.create_time = create_time
        self.dataset = dataset
        self.description = description
        self.region_id = region_id
        self.request_id = request_id
        self.status = status
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.update_time = update_time
        self.workspace = workspace

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

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.dataset is not None:
            result['dataset'] = self.dataset.to_map()

        if self.description is not None:
            result['description'] = self.description

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.status is not None:
            result['status'] = self.status

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            temp_model = main_models.GetContextStoreResponseBodyConfig()
            self.config = temp_model.from_map(m.get('config'))

        if m.get('contextStoreName') is not None:
            self.context_store_name = m.get('contextStoreName')

        if m.get('contextType') is not None:
            self.context_type = m.get('contextType')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('dataset') is not None:
            temp_model = main_models.GetContextStoreResponseBodyDataset()
            self.dataset = temp_model.from_map(m.get('dataset'))

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

class GetContextStoreResponseBodyDataset(DaraModel):
    def __init__(
        self,
        name: str = None,
    ):
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

class GetContextStoreResponseBodyConfig(DaraModel):
    def __init__(
        self,
        inner_source: main_models.GetContextStoreResponseBodyConfigInnerSource = None,
        metadata_field: Dict[str, str] = None,
        source: main_models.GetContextStoreResponseBodyConfigSource = None,
    ):
        self.inner_source = inner_source
        self.metadata_field = metadata_field
        self.source = source

    def validate(self):
        if self.inner_source:
            self.inner_source.validate()
        if self.source:
            self.source.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.inner_source is not None:
            result['innerSource'] = self.inner_source.to_map()

        if self.metadata_field is not None:
            result['metadataField'] = self.metadata_field

        if self.source is not None:
            result['source'] = self.source.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('innerSource') is not None:
            temp_model = main_models.GetContextStoreResponseBodyConfigInnerSource()
            self.inner_source = temp_model.from_map(m.get('innerSource'))

        if m.get('metadataField') is not None:
            self.metadata_field = m.get('metadataField')

        if m.get('source') is not None:
            temp_model = main_models.GetContextStoreResponseBodyConfigSource()
            self.source = temp_model.from_map(m.get('source'))

        return self

class GetContextStoreResponseBodyConfigSource(DaraModel):
    def __init__(
        self,
        logstore: str = None,
        project: str = None,
        start_time: str = None,
    ):
        self.logstore = logstore
        self.project = project
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

class GetContextStoreResponseBodyConfigInnerSource(DaraModel):
    def __init__(
        self,
        logstore: str = None,
        project: str = None,
    ):
        self.logstore = logstore
        self.project = project

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')

        if m.get('project') is not None:
            self.project = m.get('project')

        return self

