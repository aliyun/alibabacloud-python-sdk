# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_agentloop20260520 import models as main_models
from darabonba.model import DaraModel

class GetContextStoreResponseBody(DaraModel):
    def __init__(
        self,
        agent_space: str = None,
        config: main_models.GetContextStoreResponseBodyConfig = None,
        context_store_name: str = None,
        context_type: str = None,
        create_time: str = None,
        description: str = None,
        region_id: str = None,
        request_id: str = None,
        status: str = None,
        update_time: str = None,
    ):
        # The name of the AgentSpace to which the context store belongs.
        self.agent_space = agent_space
        # The configuration of the context store.
        self.config = config
        # The context store name.
        self.context_store_name = context_store_name
        # The type of the context store, such as experience or memory.
        self.context_type = context_type
        # The time when the context store was created, in ISO 8601 UTC format.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.create_time = create_time
        # The description of the context store.
        self.description = description
        # The region ID of the context store.
        self.region_id = region_id
        # The request ID, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The status of the context store. Valid values:
        # - ACTIVE
        # - INITIALIZING
        # - FAILED
        self.status = status
        # The time when the context store was last updated, in ISO 8601 UTC format.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.update_time = update_time

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_space is not None:
            result['agentSpace'] = self.agent_space

        if self.config is not None:
            result['config'] = self.config.to_map()

        if self.context_store_name is not None:
            result['contextStoreName'] = self.context_store_name

        if self.context_type is not None:
            result['contextType'] = self.context_type

        if self.create_time is not None:
            result['createTime'] = self.create_time

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentSpace') is not None:
            self.agent_space = m.get('agentSpace')

        if m.get('config') is not None:
            temp_model = main_models.GetContextStoreResponseBodyConfig()
            self.config = temp_model.from_map(m.get('config'))

        if m.get('contextStoreName') is not None:
            self.context_store_name = m.get('contextStoreName')

        if m.get('contextType') is not None:
            self.context_type = m.get('contextType')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

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

        return self

class GetContextStoreResponseBodyConfig(DaraModel):
    def __init__(
        self,
        metadata_field: Dict[str, str] = None,
        mining_interval: str = None,
        service_names: List[str] = None,
        source: main_models.GetContextStoreResponseBodyConfigSource = None,
    ):
        # The metadata field mapping. The key is the business field and the value is the storage field.
        self.metadata_field = metadata_field
        # The experience mining interval. Valid values: 1h, 6h, 12h, and 1d. Default value: 1d.
        self.mining_interval = mining_interval
        # The list of service names. This works together with source.agentSpace to locate the trace data source. This value cannot be changed in the current version.
        self.service_names = service_names
        # The datasource config passed in by the user. This serves only as the root identifier of the data source.
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

        if self.mining_interval is not None:
            result['miningInterval'] = self.mining_interval

        if self.service_names is not None:
            result['serviceNames'] = self.service_names

        if self.source is not None:
            result['source'] = self.source.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('metadataField') is not None:
            self.metadata_field = m.get('metadataField')

        if m.get('miningInterval') is not None:
            self.mining_interval = m.get('miningInterval')

        if m.get('serviceNames') is not None:
            self.service_names = m.get('serviceNames')

        if m.get('source') is not None:
            temp_model = main_models.GetContextStoreResponseBodyConfigSource()
            self.source = temp_model.from_map(m.get('source'))

        return self

class GetContextStoreResponseBodyConfigSource(DaraModel):
    def __init__(
        self,
        agent_space: str = None,
        start_time: str = None,
    ):
        # The AgentSpace where the trace data source resides. This is the same as the AgentSpace specified during creation.
        self.agent_space = agent_space
        # The start time for data backfill, in ISO 8601 UTC format.
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

