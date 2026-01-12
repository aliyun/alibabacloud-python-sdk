# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class CreateMemoryCollectionInput(DaraModel):
    def __init__(
        self,
        description: str = None,
        embedder_config: main_models.EmbedderConfig = None,
        execution_role_arn: str = None,
        llm_config: main_models.LLMConfig = None,
        memory_collection_name: str = None,
        network_configuration: main_models.NetworkConfiguration = None,
        type: str = None,
        vector_store_config: main_models.VectorStoreConfig = None,
    ):
        self.description = description
        self.embedder_config = embedder_config
        self.execution_role_arn = execution_role_arn
        self.llm_config = llm_config
        self.memory_collection_name = memory_collection_name
        self.network_configuration = network_configuration
        self.type = type
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
        if self.description is not None:
            result['description'] = self.description

        if self.embedder_config is not None:
            result['embedderConfig'] = self.embedder_config.to_map()

        if self.execution_role_arn is not None:
            result['executionRoleArn'] = self.execution_role_arn

        if self.llm_config is not None:
            result['llmConfig'] = self.llm_config.to_map()

        if self.memory_collection_name is not None:
            result['memoryCollectionName'] = self.memory_collection_name

        if self.network_configuration is not None:
            result['networkConfiguration'] = self.network_configuration.to_map()

        if self.type is not None:
            result['type'] = self.type

        if self.vector_store_config is not None:
            result['vectorStoreConfig'] = self.vector_store_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('embedderConfig') is not None:
            temp_model = main_models.EmbedderConfig()
            self.embedder_config = temp_model.from_map(m.get('embedderConfig'))

        if m.get('executionRoleArn') is not None:
            self.execution_role_arn = m.get('executionRoleArn')

        if m.get('llmConfig') is not None:
            temp_model = main_models.LLMConfig()
            self.llm_config = temp_model.from_map(m.get('llmConfig'))

        if m.get('memoryCollectionName') is not None:
            self.memory_collection_name = m.get('memoryCollectionName')

        if m.get('networkConfiguration') is not None:
            temp_model = main_models.NetworkConfiguration()
            self.network_configuration = temp_model.from_map(m.get('networkConfiguration'))

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('vectorStoreConfig') is not None:
            temp_model = main_models.VectorStoreConfig()
            self.vector_store_config = temp_model.from_map(m.get('vectorStoreConfig'))

        return self

