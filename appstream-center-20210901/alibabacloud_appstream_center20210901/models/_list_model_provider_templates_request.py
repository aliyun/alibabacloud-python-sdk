# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListModelProviderTemplatesRequest(DaraModel):
    def __init__(
        self,
        agent_platform: str = None,
        agent_provider: str = None,
        biz_type: int = None,
        model_template_id: str = None,
        page_number: int = None,
        page_size: int = None,
        provider_name: str = None,
        provider_template_ids: List[str] = None,
    ):
        self.agent_platform = agent_platform
        # This parameter is required.
        self.agent_provider = agent_provider
        # This parameter is required.
        self.biz_type = biz_type
        self.model_template_id = model_template_id
        self.page_number = page_number
        self.page_size = page_size
        self.provider_name = provider_name
        self.provider_template_ids = provider_template_ids

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

        if self.model_template_id is not None:
            result['ModelTemplateId'] = self.model_template_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.provider_name is not None:
            result['ProviderName'] = self.provider_name

        if self.provider_template_ids is not None:
            result['ProviderTemplateIds'] = self.provider_template_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentPlatform') is not None:
            self.agent_platform = m.get('AgentPlatform')

        if m.get('AgentProvider') is not None:
            self.agent_provider = m.get('AgentProvider')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('ModelTemplateId') is not None:
            self.model_template_id = m.get('ModelTemplateId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProviderName') is not None:
            self.provider_name = m.get('ProviderName')

        if m.get('ProviderTemplateIds') is not None:
            self.provider_template_ids = m.get('ProviderTemplateIds')

        return self

