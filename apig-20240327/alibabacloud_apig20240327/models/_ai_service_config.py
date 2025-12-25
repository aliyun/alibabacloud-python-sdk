# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class AiServiceConfig(DaraModel):
    def __init__(
        self,
        api_key_generate_mode: str = None,
        address: str = None,
        api_keys: List[str] = None,
        bedrock_service_config: main_models.AiServiceConfigBedrockServiceConfig = None,
        enable_health_check: bool = None,
        pai_easservice_config: main_models.AiServiceConfigPaiEASServiceConfig = None,
        protocols: List[str] = None,
        provider: str = None,
    ):
        self.api_key_generate_mode = api_key_generate_mode
        self.address = address
        self.api_keys = api_keys
        self.bedrock_service_config = bedrock_service_config
        self.enable_health_check = enable_health_check
        self.pai_easservice_config = pai_easservice_config
        self.protocols = protocols
        self.provider = provider

    def validate(self):
        if self.bedrock_service_config:
            self.bedrock_service_config.validate()
        if self.pai_easservice_config:
            self.pai_easservice_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key_generate_mode is not None:
            result['ApiKeyGenerateMode'] = self.api_key_generate_mode

        if self.address is not None:
            result['address'] = self.address

        if self.api_keys is not None:
            result['apiKeys'] = self.api_keys

        if self.bedrock_service_config is not None:
            result['bedrockServiceConfig'] = self.bedrock_service_config.to_map()

        if self.enable_health_check is not None:
            result['enableHealthCheck'] = self.enable_health_check

        if self.pai_easservice_config is not None:
            result['paiEASServiceConfig'] = self.pai_easservice_config.to_map()

        if self.protocols is not None:
            result['protocols'] = self.protocols

        if self.provider is not None:
            result['provider'] = self.provider

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKeyGenerateMode') is not None:
            self.api_key_generate_mode = m.get('ApiKeyGenerateMode')

        if m.get('address') is not None:
            self.address = m.get('address')

        if m.get('apiKeys') is not None:
            self.api_keys = m.get('apiKeys')

        if m.get('bedrockServiceConfig') is not None:
            temp_model = main_models.AiServiceConfigBedrockServiceConfig()
            self.bedrock_service_config = temp_model.from_map(m.get('bedrockServiceConfig'))

        if m.get('enableHealthCheck') is not None:
            self.enable_health_check = m.get('enableHealthCheck')

        if m.get('paiEASServiceConfig') is not None:
            temp_model = main_models.AiServiceConfigPaiEASServiceConfig()
            self.pai_easservice_config = temp_model.from_map(m.get('paiEASServiceConfig'))

        if m.get('protocols') is not None:
            self.protocols = m.get('protocols')

        if m.get('provider') is not None:
            self.provider = m.get('provider')

        return self

class AiServiceConfigPaiEASServiceConfig(DaraModel):
    def __init__(
        self,
        endpoint_type: str = None,
        service_id: str = None,
        service_name: str = None,
        workspace_id: str = None,
    ):
        self.endpoint_type = endpoint_type
        self.service_id = service_id
        self.service_name = service_name
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.endpoint_type is not None:
            result['endpointType'] = self.endpoint_type

        if self.service_id is not None:
            result['serviceId'] = self.service_id

        if self.service_name is not None:
            result['serviceName'] = self.service_name

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endpointType') is not None:
            self.endpoint_type = m.get('endpointType')

        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')

        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

class AiServiceConfigBedrockServiceConfig(DaraModel):
    def __init__(
        self,
        aws_access_key: str = None,
        aws_region: str = None,
        aws_secret_key: str = None,
    ):
        self.aws_access_key = aws_access_key
        self.aws_region = aws_region
        self.aws_secret_key = aws_secret_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aws_access_key is not None:
            result['awsAccessKey'] = self.aws_access_key

        if self.aws_region is not None:
            result['awsRegion'] = self.aws_region

        if self.aws_secret_key is not None:
            result['awsSecretKey'] = self.aws_secret_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('awsAccessKey') is not None:
            self.aws_access_key = m.get('awsAccessKey')

        if m.get('awsRegion') is not None:
            self.aws_region = m.get('awsRegion')

        if m.get('awsSecretKey') is not None:
            self.aws_secret_key = m.get('awsSecretKey')

        return self

