# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListModelTemplatesRequest(DaraModel):
    def __init__(
        self,
        agent_platform: str = None,
        agent_platform_list: List[str] = None,
        agent_provider: str = None,
        agent_provider_list: List[str] = None,
        biz_type: int = None,
        has_model: bool = None,
        model_template_id_list: List[str] = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        ref_scope: str = None,
        source: str = None,
    ):
        # The Agent platform.
        self.agent_platform = agent_platform
        # The Agent platform list. Supports COMMON. If specified together with AgentPlatform, AgentPlatform takes precedence and this list is ignored. Defaults to ENTERPRISE if no platform filter is specified. To query Common model groups, explicitly include COMMON. If filtering by Provider simultaneously, set the value to Common.
        self.agent_platform_list = agent_platform_list
        # The Agent provider name.
        self.agent_provider = agent_provider
        # The Agent provider list. Supports Common. If specified together with AgentProvider, AgentProvider takes precedence and this list is ignored. To query Common model groups, explicitly include COMMON in the platform filter.
        self.agent_provider_list = agent_provider_list
        # The business type.
        # 
        # This parameter is required.
        self.biz_type = biz_type
        # Specifies whether models are configured in the group.
        self.has_model = has_model
        # The list of template group IDs to filter by.
        self.model_template_id_list = model_template_id_list
        # The model group name. Fuzzy match is supported.
        self.name = name
        # The page number, starting from 1. Values 0 and 1 return the same result.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The authorization scope filter. Valid values: ALL_USER, USER_MIXED, or RESOURCE_MIXED (strictly uppercase. Case variants or unknown values return InvalidParameter). If not specified, no filtering is applied. Unlike create/update operations, the filter scenario allows RESOURCE_MIXED (to filter non-Common model groups).
        self.ref_scope = ref_scope
        # The template source filter. Valid values:
        # - User: tenant-created (default if not specified).
        # - System: system preset.
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_platform is not None:
            result['AgentPlatform'] = self.agent_platform

        if self.agent_platform_list is not None:
            result['AgentPlatformList'] = self.agent_platform_list

        if self.agent_provider is not None:
            result['AgentProvider'] = self.agent_provider

        if self.agent_provider_list is not None:
            result['AgentProviderList'] = self.agent_provider_list

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.has_model is not None:
            result['HasModel'] = self.has_model

        if self.model_template_id_list is not None:
            result['ModelTemplateIdList'] = self.model_template_id_list

        if self.name is not None:
            result['Name'] = self.name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.ref_scope is not None:
            result['RefScope'] = self.ref_scope

        if self.source is not None:
            result['Source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentPlatform') is not None:
            self.agent_platform = m.get('AgentPlatform')

        if m.get('AgentPlatformList') is not None:
            self.agent_platform_list = m.get('AgentPlatformList')

        if m.get('AgentProvider') is not None:
            self.agent_provider = m.get('AgentProvider')

        if m.get('AgentProviderList') is not None:
            self.agent_provider_list = m.get('AgentProviderList')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('HasModel') is not None:
            self.has_model = m.get('HasModel')

        if m.get('ModelTemplateIdList') is not None:
            self.model_template_id_list = m.get('ModelTemplateIdList')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RefScope') is not None:
            self.ref_scope = m.get('RefScope')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        return self

