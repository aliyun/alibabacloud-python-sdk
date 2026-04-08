# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class AiCacheConfig(DaraModel):
    def __init__(
        self,
        cache_key_strategy: str = None,
        cache_mode: str = None,
        cache_ttl: int = None,
        embedding_config: main_models.AiCacheConfigEmbeddingConfig = None,
        plugin_status: main_models.AiPluginStatus = None,
        redis_config: main_models.AiPolicyRedisConfig = None,
        vector_config: main_models.AiCacheConfigVectorConfig = None,
    ):
        self.cache_key_strategy = cache_key_strategy
        self.cache_mode = cache_mode
        self.cache_ttl = cache_ttl
        self.embedding_config = embedding_config
        self.plugin_status = plugin_status
        self.redis_config = redis_config
        self.vector_config = vector_config

    def validate(self):
        if self.embedding_config:
            self.embedding_config.validate()
        if self.plugin_status:
            self.plugin_status.validate()
        if self.redis_config:
            self.redis_config.validate()
        if self.vector_config:
            self.vector_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cache_key_strategy is not None:
            result['cacheKeyStrategy'] = self.cache_key_strategy

        if self.cache_mode is not None:
            result['cacheMode'] = self.cache_mode

        if self.cache_ttl is not None:
            result['cacheTTL'] = self.cache_ttl

        if self.embedding_config is not None:
            result['embeddingConfig'] = self.embedding_config.to_map()

        if self.plugin_status is not None:
            result['pluginStatus'] = self.plugin_status.to_map()

        if self.redis_config is not None:
            result['redisConfig'] = self.redis_config.to_map()

        if self.vector_config is not None:
            result['vectorConfig'] = self.vector_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cacheKeyStrategy') is not None:
            self.cache_key_strategy = m.get('cacheKeyStrategy')

        if m.get('cacheMode') is not None:
            self.cache_mode = m.get('cacheMode')

        if m.get('cacheTTL') is not None:
            self.cache_ttl = m.get('cacheTTL')

        if m.get('embeddingConfig') is not None:
            temp_model = main_models.AiCacheConfigEmbeddingConfig()
            self.embedding_config = temp_model.from_map(m.get('embeddingConfig'))

        if m.get('pluginStatus') is not None:
            temp_model = main_models.AiPluginStatus()
            self.plugin_status = temp_model.from_map(m.get('pluginStatus'))

        if m.get('redisConfig') is not None:
            temp_model = main_models.AiPolicyRedisConfig()
            self.redis_config = temp_model.from_map(m.get('redisConfig'))

        if m.get('vectorConfig') is not None:
            temp_model = main_models.AiCacheConfigVectorConfig()
            self.vector_config = temp_model.from_map(m.get('vectorConfig'))

        return self

class AiCacheConfigVectorConfig(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        collection_id: str = None,
        service_host: str = None,
        threshold: float = None,
        timeout: int = None,
        type: str = None,
    ):
        self.api_key = api_key
        self.collection_id = collection_id
        self.service_host = service_host
        self.threshold = threshold
        self.timeout = timeout
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['apiKey'] = self.api_key

        if self.collection_id is not None:
            result['collectionId'] = self.collection_id

        if self.service_host is not None:
            result['serviceHost'] = self.service_host

        if self.threshold is not None:
            result['threshold'] = self.threshold

        if self.timeout is not None:
            result['timeout'] = self.timeout

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiKey') is not None:
            self.api_key = m.get('apiKey')

        if m.get('collectionId') is not None:
            self.collection_id = m.get('collectionId')

        if m.get('serviceHost') is not None:
            self.service_host = m.get('serviceHost')

        if m.get('threshold') is not None:
            self.threshold = m.get('threshold')

        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class AiCacheConfigEmbeddingConfig(DaraModel):
    def __init__(
        self,
        model_name: str = None,
        service_id: str = None,
        timeout: int = None,
        type: str = None,
    ):
        self.model_name = model_name
        self.service_id = service_id
        self.timeout = timeout
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_name is not None:
            result['modelName'] = self.model_name

        if self.service_id is not None:
            result['serviceId'] = self.service_id

        if self.timeout is not None:
            result['timeout'] = self.timeout

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('modelName') is not None:
            self.model_name = m.get('modelName')

        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')

        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

