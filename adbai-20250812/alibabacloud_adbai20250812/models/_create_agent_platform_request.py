# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_adbai20250812 import models as main_models
from darabonba.model import DaraModel

class CreateAgentPlatformRequest(DaraModel):
    def __init__(
        self,
        ai_platform_config: main_models.CreateAgentPlatformRequestAiPlatformConfig = None,
        dbcluster_id: str = None,
        name: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.ai_platform_config = ai_platform_config
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # This parameter is required.
        self.name = name
        self.region_id = region_id

    def validate(self):
        if self.ai_platform_config:
            self.ai_platform_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ai_platform_config is not None:
            result['AiPlatformConfig'] = self.ai_platform_config.to_map()

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.name is not None:
            result['Name'] = self.name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AiPlatformConfig') is not None:
            temp_model = main_models.CreateAgentPlatformRequestAiPlatformConfig()
            self.ai_platform_config = temp_model.from_map(m.get('AiPlatformConfig'))

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self



class CreateAgentPlatformRequestAiPlatformConfig(DaraModel):
    def __init__(
        self,
        serve_api_key: str = None,
        serve_embedding_endpoint: str = None,
        serve_embedding_model_name: str = None,
        serve_endpoint: str = None,
        serve_model_name: str = None,
        spec_name: str = None,
    ):
        # This parameter is required.
        self.serve_api_key = serve_api_key
        # This parameter is required.
        self.serve_embedding_endpoint = serve_embedding_endpoint
        # This parameter is required.
        self.serve_embedding_model_name = serve_embedding_model_name
        # This parameter is required.
        self.serve_endpoint = serve_endpoint
        # This parameter is required.
        self.serve_model_name = serve_model_name
        # This parameter is required.
        self.spec_name = spec_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.serve_api_key is not None:
            result['ServeApiKey'] = self.serve_api_key

        if self.serve_embedding_endpoint is not None:
            result['ServeEmbeddingEndpoint'] = self.serve_embedding_endpoint

        if self.serve_embedding_model_name is not None:
            result['ServeEmbeddingModelName'] = self.serve_embedding_model_name

        if self.serve_endpoint is not None:
            result['ServeEndpoint'] = self.serve_endpoint

        if self.serve_model_name is not None:
            result['ServeModelName'] = self.serve_model_name

        if self.spec_name is not None:
            result['SpecName'] = self.spec_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServeApiKey') is not None:
            self.serve_api_key = m.get('ServeApiKey')

        if m.get('ServeEmbeddingEndpoint') is not None:
            self.serve_embedding_endpoint = m.get('ServeEmbeddingEndpoint')

        if m.get('ServeEmbeddingModelName') is not None:
            self.serve_embedding_model_name = m.get('ServeEmbeddingModelName')

        if m.get('ServeEndpoint') is not None:
            self.serve_endpoint = m.get('ServeEndpoint')

        if m.get('ServeModelName') is not None:
            self.serve_model_name = m.get('ServeModelName')

        if m.get('SpecName') is not None:
            self.spec_name = m.get('SpecName')

        return self

