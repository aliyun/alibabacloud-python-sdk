# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class AiServiceConfig(DaraModel):
    def __init__(
        self,
        api_key_generate_mode: str = None,
        address: str = None,
        api_key_failover: main_models.AiServiceConfigApiKeyFailover = None,
        api_key_references: List[str] = None,
        api_keys: List[str] = None,
        auth_header_key: str = None,
        bedrock_service_config: main_models.AiServiceConfigBedrockServiceConfig = None,
        claude_code_mode: bool = None,
        compatible_protocols: List[str] = None,
        config_revision: str = None,
        default_model_name: str = None,
        enable_health_check: bool = None,
        enable_outlier_detection: bool = None,
        kling_service_config: main_models.AiServiceConfigKlingServiceConfig = None,
        pai_easservice_config: main_models.AiServiceConfigPaiEASServiceConfig = None,
        protocols: List[str] = None,
        provider: str = None,
        retry_on_failure: main_models.AiServiceConfigRetryOnFailure = None,
        upstream_auth_mode: str = None,
        vertex_service_config: main_models.AiServiceConfigVertexServiceConfig = None,
    ):
        # The generation mode of the API key.
        self.api_key_generate_mode = api_key_generate_mode
        # The service address.
        self.address = address
        # The configuration for API key failure ejection and recovery.
        self.api_key_failover = api_key_failover
        # The read-only summary of KMS reference names, excluding credential values.
        self.api_key_references = api_key_references
        # The list of API keys.
        self.api_keys = api_keys
        # The name of the request header used to pass authentication credentials to the upstream.
        self.auth_header_key = auth_header_key
        # The Bedrock service-specific configuration.
        self.bedrock_service_config = bedrock_service_config
        # Specifies whether to enable Claude Code compatibility mode.
        self.claude_code_mode = claude_code_mode
        # The list of compatible protocols supported by the service.
        self.compatible_protocols = compatible_protocols
        # The read-only service configuration version. Use expectedConfigRevision for conditional updates.
        self.config_revision = config_revision
        # The name of the default model.
        self.default_model_name = default_model_name
        # Specifies whether to enable health checks.
        self.enable_health_check = enable_health_check
        # Specifies whether to enable the outlier detection feature.
        self.enable_outlier_detection = enable_outlier_detection
        # The authentication and token configuration specific to the KlingAI service.
        self.kling_service_config = kling_service_config
        # The PAI-EAS service-specific configuration.
        self.pai_easservice_config = pai_easservice_config
        # The list of model protocols.
        self.protocols = protocols
        # The large language model provider.
        self.provider = provider
        # The configuration for retrying with a different key after the current request fails.
        self.retry_on_failure = retry_on_failure
        # The upstream authentication mode, which distinguishes between API key authentication, no authentication, and pass-through downstream authentication.
        self.upstream_auth_mode = upstream_auth_mode
        # The configuration information for the Vertex AI service.
        self.vertex_service_config = vertex_service_config

    def validate(self):
        if self.api_key_failover:
            self.api_key_failover.validate()
        if self.bedrock_service_config:
            self.bedrock_service_config.validate()
        if self.kling_service_config:
            self.kling_service_config.validate()
        if self.pai_easservice_config:
            self.pai_easservice_config.validate()
        if self.retry_on_failure:
            self.retry_on_failure.validate()
        if self.vertex_service_config:
            self.vertex_service_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key_generate_mode is not None:
            result['ApiKeyGenerateMode'] = self.api_key_generate_mode

        if self.address is not None:
            result['address'] = self.address

        if self.api_key_failover is not None:
            result['apiKeyFailover'] = self.api_key_failover.to_map()

        if self.api_key_references is not None:
            result['apiKeyReferences'] = self.api_key_references

        if self.api_keys is not None:
            result['apiKeys'] = self.api_keys

        if self.auth_header_key is not None:
            result['authHeaderKey'] = self.auth_header_key

        if self.bedrock_service_config is not None:
            result['bedrockServiceConfig'] = self.bedrock_service_config.to_map()

        if self.claude_code_mode is not None:
            result['claudeCodeMode'] = self.claude_code_mode

        if self.compatible_protocols is not None:
            result['compatibleProtocols'] = self.compatible_protocols

        if self.config_revision is not None:
            result['configRevision'] = self.config_revision

        if self.default_model_name is not None:
            result['defaultModelName'] = self.default_model_name

        if self.enable_health_check is not None:
            result['enableHealthCheck'] = self.enable_health_check

        if self.enable_outlier_detection is not None:
            result['enableOutlierDetection'] = self.enable_outlier_detection

        if self.kling_service_config is not None:
            result['klingServiceConfig'] = self.kling_service_config.to_map()

        if self.pai_easservice_config is not None:
            result['paiEASServiceConfig'] = self.pai_easservice_config.to_map()

        if self.protocols is not None:
            result['protocols'] = self.protocols

        if self.provider is not None:
            result['provider'] = self.provider

        if self.retry_on_failure is not None:
            result['retryOnFailure'] = self.retry_on_failure.to_map()

        if self.upstream_auth_mode is not None:
            result['upstreamAuthMode'] = self.upstream_auth_mode

        if self.vertex_service_config is not None:
            result['vertexServiceConfig'] = self.vertex_service_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKeyGenerateMode') is not None:
            self.api_key_generate_mode = m.get('ApiKeyGenerateMode')

        if m.get('address') is not None:
            self.address = m.get('address')

        if m.get('apiKeyFailover') is not None:
            temp_model = main_models.AiServiceConfigApiKeyFailover()
            self.api_key_failover = temp_model.from_map(m.get('apiKeyFailover'))

        if m.get('apiKeyReferences') is not None:
            self.api_key_references = m.get('apiKeyReferences')

        if m.get('apiKeys') is not None:
            self.api_keys = m.get('apiKeys')

        if m.get('authHeaderKey') is not None:
            self.auth_header_key = m.get('authHeaderKey')

        if m.get('bedrockServiceConfig') is not None:
            temp_model = main_models.AiServiceConfigBedrockServiceConfig()
            self.bedrock_service_config = temp_model.from_map(m.get('bedrockServiceConfig'))

        if m.get('claudeCodeMode') is not None:
            self.claude_code_mode = m.get('claudeCodeMode')

        if m.get('compatibleProtocols') is not None:
            self.compatible_protocols = m.get('compatibleProtocols')

        if m.get('configRevision') is not None:
            self.config_revision = m.get('configRevision')

        if m.get('defaultModelName') is not None:
            self.default_model_name = m.get('defaultModelName')

        if m.get('enableHealthCheck') is not None:
            self.enable_health_check = m.get('enableHealthCheck')

        if m.get('enableOutlierDetection') is not None:
            self.enable_outlier_detection = m.get('enableOutlierDetection')

        if m.get('klingServiceConfig') is not None:
            temp_model = main_models.AiServiceConfigKlingServiceConfig()
            self.kling_service_config = temp_model.from_map(m.get('klingServiceConfig'))

        if m.get('paiEASServiceConfig') is not None:
            temp_model = main_models.AiServiceConfigPaiEASServiceConfig()
            self.pai_easservice_config = temp_model.from_map(m.get('paiEASServiceConfig'))

        if m.get('protocols') is not None:
            self.protocols = m.get('protocols')

        if m.get('provider') is not None:
            self.provider = m.get('provider')

        if m.get('retryOnFailure') is not None:
            temp_model = main_models.AiServiceConfigRetryOnFailure()
            self.retry_on_failure = temp_model.from_map(m.get('retryOnFailure'))

        if m.get('upstreamAuthMode') is not None:
            self.upstream_auth_mode = m.get('upstreamAuthMode')

        if m.get('vertexServiceConfig') is not None:
            temp_model = main_models.AiServiceConfigVertexServiceConfig()
            self.vertex_service_config = temp_model.from_map(m.get('vertexServiceConfig'))

        return self

class AiServiceConfigVertexServiceConfig(DaraModel):
    def __init__(
        self,
        gemini_safety_setting: Dict[str, str] = None,
        vertex_auth_key: str = None,
        vertex_auth_service_name: str = None,
        vertex_open_aicompatible: bool = None,
        vertex_project_id: str = None,
        vertex_region: str = None,
        vertex_token_refresh_ahead: int = None,
    ):
        # The safety filtering level settings for the Gemini model.
        self.gemini_safety_setting = gemini_safety_setting
        # The authentication key for Vertex AI.
        self.vertex_auth_key = vertex_auth_key
        # The authentication service name used by Vertex AI.
        self.vertex_auth_service_name = vertex_auth_service_name
        # Specifies whether to use the OpenAI-compatible interface of Vertex AI.
        self.vertex_open_aicompatible = vertex_open_aicompatible
        # The Google Cloud project ID.
        self.vertex_project_id = vertex_project_id
        # The Google Cloud region where the Vertex AI service is located.
        self.vertex_region = vertex_region
        # The number of seconds before access token expiration to trigger an advance refresh.
        self.vertex_token_refresh_ahead = vertex_token_refresh_ahead

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gemini_safety_setting is not None:
            result['geminiSafetySetting'] = self.gemini_safety_setting

        if self.vertex_auth_key is not None:
            result['vertexAuthKey'] = self.vertex_auth_key

        if self.vertex_auth_service_name is not None:
            result['vertexAuthServiceName'] = self.vertex_auth_service_name

        if self.vertex_open_aicompatible is not None:
            result['vertexOpenAICompatible'] = self.vertex_open_aicompatible

        if self.vertex_project_id is not None:
            result['vertexProjectId'] = self.vertex_project_id

        if self.vertex_region is not None:
            result['vertexRegion'] = self.vertex_region

        if self.vertex_token_refresh_ahead is not None:
            result['vertexTokenRefreshAhead'] = self.vertex_token_refresh_ahead

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('geminiSafetySetting') is not None:
            self.gemini_safety_setting = m.get('geminiSafetySetting')

        if m.get('vertexAuthKey') is not None:
            self.vertex_auth_key = m.get('vertexAuthKey')

        if m.get('vertexAuthServiceName') is not None:
            self.vertex_auth_service_name = m.get('vertexAuthServiceName')

        if m.get('vertexOpenAICompatible') is not None:
            self.vertex_open_aicompatible = m.get('vertexOpenAICompatible')

        if m.get('vertexProjectId') is not None:
            self.vertex_project_id = m.get('vertexProjectId')

        if m.get('vertexRegion') is not None:
            self.vertex_region = m.get('vertexRegion')

        if m.get('vertexTokenRefreshAhead') is not None:
            self.vertex_token_refresh_ahead = m.get('vertexTokenRefreshAhead')

        return self

class AiServiceConfigRetryOnFailure(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        max_retries: int = None,
        retry_on_status: List[str] = None,
        retry_timeout: int = None,
    ):
        # Specifies whether to enable retries upon current request failure.
        self.enabled = enabled
        # The maximum number of retries for the current request.
        self.max_retries = max_retries
        # The set of response status matching rules that trigger retries for the current request.
        self.retry_on_status = retry_on_status
        # The retry timeout configuration for the current request.
        self.retry_timeout = retry_timeout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.max_retries is not None:
            result['maxRetries'] = self.max_retries

        if self.retry_on_status is not None:
            result['retryOnStatus'] = self.retry_on_status

        if self.retry_timeout is not None:
            result['retryTimeout'] = self.retry_timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('maxRetries') is not None:
            self.max_retries = m.get('maxRetries')

        if m.get('retryOnStatus') is not None:
            self.retry_on_status = m.get('retryOnStatus')

        if m.get('retryTimeout') is not None:
            self.retry_timeout = m.get('retryTimeout')

        return self

class AiServiceConfigPaiEASServiceConfig(DaraModel):
    def __init__(
        self,
        endpoint_type: str = None,
        service_id: str = None,
        service_name: str = None,
        workspace_id: str = None,
    ):
        # The connection type, which can be a private network (VPC) or a public network.
        self.endpoint_type = endpoint_type
        # The service ID.
        self.service_id = service_id
        # The service name.
        self.service_name = service_name
        # The workspace ID.
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

class AiServiceConfigKlingServiceConfig(DaraModel):
    def __init__(
        self,
        kling_access_key: str = None,
        kling_secret_key: str = None,
        kling_token_refresh_ahead: int = None,
    ):
        # The KlingAI access key identifier. Examples use desensitized values.
        self.kling_access_key = kling_access_key
        # The KlingAI secret key. Examples use desensitized values.
        self.kling_secret_key = kling_secret_key
        # The advance refresh configuration for KlingAI tokens.
        self.kling_token_refresh_ahead = kling_token_refresh_ahead

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.kling_access_key is not None:
            result['klingAccessKey'] = self.kling_access_key

        if self.kling_secret_key is not None:
            result['klingSecretKey'] = self.kling_secret_key

        if self.kling_token_refresh_ahead is not None:
            result['klingTokenRefreshAhead'] = self.kling_token_refresh_ahead

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('klingAccessKey') is not None:
            self.kling_access_key = m.get('klingAccessKey')

        if m.get('klingSecretKey') is not None:
            self.kling_secret_key = m.get('klingSecretKey')

        if m.get('klingTokenRefreshAhead') is not None:
            self.kling_token_refresh_ahead = m.get('klingTokenRefreshAhead')

        return self

class AiServiceConfigBedrockServiceConfig(DaraModel):
    def __init__(
        self,
        aws_access_key: str = None,
        aws_region: str = None,
        aws_secret_key: str = None,
        bedrock_prompt_cache_point_positions: Dict[str, bool] = None,
        endpoint_mode: str = None,
        prompt_cache_enable: bool = None,
        prompt_cache_retention: str = None,
        prompt_cache_strategy: str = None,
    ):
        # The AWS access key.
        self.aws_access_key = aws_access_key
        # The AWS region.
        self.aws_region = aws_region
        # The AWS secret key.
        self.aws_secret_key = aws_secret_key
        # Configures whether to insert Bedrock cache markers based on prompt positions.
        self.bedrock_prompt_cache_point_positions = bedrock_prompt_cache_point_positions
        # The Bedrock service endpoint mode, which supports runtime and mantle. If omitted, runtime is used.
        self.endpoint_mode = endpoint_mode
        # Specifies whether to enable prompt caching for the Bedrock upstream.
        self.prompt_cache_enable = prompt_cache_enable
        # The data retention policy for the prompt cache.
        self.prompt_cache_retention = prompt_cache_retention
        # The applicable model strategy for Bedrock prompt caching.
        self.prompt_cache_strategy = prompt_cache_strategy

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

        if self.bedrock_prompt_cache_point_positions is not None:
            result['bedrockPromptCachePointPositions'] = self.bedrock_prompt_cache_point_positions

        if self.endpoint_mode is not None:
            result['endpointMode'] = self.endpoint_mode

        if self.prompt_cache_enable is not None:
            result['promptCacheEnable'] = self.prompt_cache_enable

        if self.prompt_cache_retention is not None:
            result['promptCacheRetention'] = self.prompt_cache_retention

        if self.prompt_cache_strategy is not None:
            result['promptCacheStrategy'] = self.prompt_cache_strategy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('awsAccessKey') is not None:
            self.aws_access_key = m.get('awsAccessKey')

        if m.get('awsRegion') is not None:
            self.aws_region = m.get('awsRegion')

        if m.get('awsSecretKey') is not None:
            self.aws_secret_key = m.get('awsSecretKey')

        if m.get('bedrockPromptCachePointPositions') is not None:
            self.bedrock_prompt_cache_point_positions = m.get('bedrockPromptCachePointPositions')

        if m.get('endpointMode') is not None:
            self.endpoint_mode = m.get('endpointMode')

        if m.get('promptCacheEnable') is not None:
            self.prompt_cache_enable = m.get('promptCacheEnable')

        if m.get('promptCacheRetention') is not None:
            self.prompt_cache_retention = m.get('promptCacheRetention')

        if m.get('promptCacheStrategy') is not None:
            self.prompt_cache_strategy = m.get('promptCacheStrategy')

        return self

class AiServiceConfigApiKeyFailover(DaraModel):
    def __init__(
        self,
        cooldown_duration: int = None,
        enabled: bool = None,
        failover_on_status: List[str] = None,
        failure_threshold: int = None,
    ):
        # The cooldown duration after an API key is ejected.
        self.cooldown_duration = cooldown_duration
        # Specifies whether to enable API key failure ejection.
        self.enabled = enabled
        # The set of response status matching rules that trigger API key failure ejection.
        self.failover_on_status = failover_on_status
        # The failure count threshold that triggers API key ejection.
        self.failure_threshold = failure_threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cooldown_duration is not None:
            result['cooldownDuration'] = self.cooldown_duration

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.failover_on_status is not None:
            result['failoverOnStatus'] = self.failover_on_status

        if self.failure_threshold is not None:
            result['failureThreshold'] = self.failure_threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cooldownDuration') is not None:
            self.cooldown_duration = m.get('cooldownDuration')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('failoverOnStatus') is not None:
            self.failover_on_status = m.get('failoverOnStatus')

        if m.get('failureThreshold') is not None:
            self.failure_threshold = m.get('failureThreshold')

        return self

