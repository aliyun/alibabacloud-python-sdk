# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class MemoryCollection(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        description: str = None,
        embedder_config: main_models.EmbedderConfig = None,
        execution_role_arn: str = None,
        last_updated_at: str = None,
        llm_config: main_models.LLMConfig = None,
        memory_collection_id: str = None,
        memory_collection_name: str = None,
        network_configuration: main_models.NetworkConfiguration = None,
        vector_store_config: main_models.VectorStoreConfig = None,
    ):
        self.created_at = created_at
        self.description = description
        self.embedder_config = embedder_config
        self.execution_role_arn = execution_role_arn
        self.last_updated_at = last_updated_at
        self.llm_config = llm_config
        self.memory_collection_id = memory_collection_id
        self.memory_collection_name = memory_collection_name
        self.network_configuration = network_configuration
        self.vector_store_config = vector_store_config

    def validate(self):
        if self.embedder_config:
            self.embedder_config.validate()
        if self.llm_config:
            self.llm_config.validate()
        if self.network_configuration:
            self.network_configuration.validate()
        if self.vector_store_config:
            self.vector_store_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.description is not None:
            result['description'] = self.description

        if self.embedder_config is not None:
            result['embedderConfig'] = self.embedder_config.to_map()

        if self.execution_role_arn is not None:
            result['executionRoleArn'] = self.execution_role_arn

        if self.last_updated_at is not None:
            result['lastUpdatedAt'] = self.last_updated_at

        if self.llm_config is not None:
            result['llmConfig'] = self.llm_config.to_map()

        if self.memory_collection_id is not None:
            result['memoryCollectionId'] = self.memory_collection_id

        if self.memory_collection_name is not None:
            result['memoryCollectionName'] = self.memory_collection_name

        if self.network_configuration is not None:
            result['networkConfiguration'] = self.network_configuration.to_map()

        if self.vector_store_config is not None:
            result['vectorStoreConfig'] = self.vector_store_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('embedderConfig') is not None:
            temp_model = main_models.EmbedderConfig()
            self.embedder_config = temp_model.from_map(m.get('embedderConfig'))

        if m.get('executionRoleArn') is not None:
            self.execution_role_arn = m.get('executionRoleArn')

        if m.get('lastUpdatedAt') is not None:
            self.last_updated_at = m.get('lastUpdatedAt')

        if m.get('llmConfig') is not None:
            temp_model = main_models.LLMConfig()
            self.llm_config = temp_model.from_map(m.get('llmConfig'))

        if m.get('memoryCollectionId') is not None:
            self.memory_collection_id = m.get('memoryCollectionId')

        if m.get('memoryCollectionName') is not None:
            self.memory_collection_name = m.get('memoryCollectionName')

        if m.get('networkConfiguration') is not None:
            temp_model = main_models.NetworkConfiguration()
            self.network_configuration = temp_model.from_map(m.get('networkConfiguration'))

        if m.get('vectorStoreConfig') is not None:
            temp_model = main_models.VectorStoreConfig()
            self.vector_store_config = temp_model.from_map(m.get('vectorStoreConfig'))

        return self

