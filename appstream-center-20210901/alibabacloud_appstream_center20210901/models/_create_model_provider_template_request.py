# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateModelProviderTemplateRequest(DaraModel):
    def __init__(
        self,
        agent_platform: str = None,
        agent_provider: str = None,
        biz_type: int = None,
        config: str = None,
        description: str = None,
        enable_wuying_proxy: bool = None,
        model_template_id: str = None,
        name: str = None,
        provider_name: str = None,
        provider_type: str = None,
    ):
        # The Agent platform.
        self.agent_platform = agent_platform
        # The Agent provider name.
        # 
        # This parameter is required.
        self.agent_provider = agent_provider
        # The business type.
        # 
        # This parameter is required.
        self.biz_type = biz_type
        # The model provider configuration in JSON format, which contains connection information such as baseUrl, apiKey, and api. The apiKey is encrypted after creation. When ProviderType is set to WuyingCredit, this parameter is not required because the configuration is copied from the system template.
        # 
        # This parameter is required.
        self.config = config
        # The description of the model provider template.
        self.description = description
        # Specifies whether to enable the WUYING secure proxy. This parameter must be set to true when ProviderType is set to WuyingCredit.
        self.enable_wuying_proxy = enable_wuying_proxy
        # The ID of the associated model template.
        # 
        # This parameter is required.
        self.model_template_id = model_template_id
        # The name of the model provider template.
        self.name = name
        # The model provider name. The name must be unique within the same model template. The naming rules vary based on the value of ProviderType. For more information, see the description of ProviderType.
        # 
        # This parameter is required.
        self.provider_name = provider_name
        # The model provider type. Different types impose different constraints on ProviderName and Config. Valid values:
        # - WuyingCredit: WUYING credit plan. ProviderName must be set to wuying-credit. The template is created by copying from a system template, and Config is not required.
        # - Managed: managed provider. System-reserved names such as wuying-credit cannot be used. Config is required.
        # - Custom: user-defined provider. ProviderName must start with the prefix provider-. Config is required.
        self.provider_type = provider_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_platform is not None:
            result['AgentPlatform'] = self.agent_platform

        if self.agent_provider is not None:
            result['AgentProvider'] = self.agent_provider

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.config is not None:
            result['Config'] = self.config

        if self.description is not None:
            result['Description'] = self.description

        if self.enable_wuying_proxy is not None:
            result['EnableWuyingProxy'] = self.enable_wuying_proxy

        if self.model_template_id is not None:
            result['ModelTemplateId'] = self.model_template_id

        if self.name is not None:
            result['Name'] = self.name

        if self.provider_name is not None:
            result['ProviderName'] = self.provider_name

        if self.provider_type is not None:
            result['ProviderType'] = self.provider_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentPlatform') is not None:
            self.agent_platform = m.get('AgentPlatform')

        if m.get('AgentProvider') is not None:
            self.agent_provider = m.get('AgentProvider')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnableWuyingProxy') is not None:
            self.enable_wuying_proxy = m.get('EnableWuyingProxy')

        if m.get('ModelTemplateId') is not None:
            self.model_template_id = m.get('ModelTemplateId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProviderName') is not None:
            self.provider_name = m.get('ProviderName')

        if m.get('ProviderType') is not None:
            self.provider_type = m.get('ProviderType')

        return self

