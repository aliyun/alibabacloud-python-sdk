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
        # Agent platform.
        self.agent_platform = agent_platform
        # Agent provider name.
        # 
        # This parameter is required.
        self.agent_provider = agent_provider
        # Business type.
        # 
        # This parameter is required.
        self.biz_type = biz_type
        # Model provider configuration JSON, containing connection information such as baseUrl, apiKey, and api. The apiKey is encrypted after creation. Not required when ProviderType is WuyingCredit, as it is copied from the system template.
        # 
        # This parameter is required.
        self.config = config
        # Model provider template description.
        self.description = description
        # Whether to enable Wuying security proxy. Must be true when ProviderType is WuyingCredit.
        self.enable_wuying_proxy = enable_wuying_proxy
        # Associated model group ID.
        # 
        # This parameter is required.
        self.model_template_id = model_template_id
        # Model provider template name.
        self.name = name
        # Model provider name. Must be unique within the same model template. Naming rules vary by ProviderType. For details, see the ProviderType description.
        # 
        # This parameter is required.
        self.provider_name = provider_name
        # Model provider type. Different types impose different constraints on ProviderName and Config:
        # - WuyingCredit: Wuying credit package. ProviderName must be wuying-credit. Created by copying from the system template. Config is not required.
        # - Managed: Managed provider. System-reserved names such as wuying-credit cannot be used. Config is required.
        # - Custom: User-defined provider. ProviderName must start with the provider- prefix. Config is required.
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

