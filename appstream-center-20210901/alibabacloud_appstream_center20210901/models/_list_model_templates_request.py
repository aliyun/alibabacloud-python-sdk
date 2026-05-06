# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListModelTemplatesRequest(DaraModel):
    def __init__(
        self,
        agent_platform: str = None,
        agent_provider: str = None,
        biz_type: int = None,
        has_model: bool = None,
        model_template_id_list: List[str] = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.agent_platform = agent_platform
        # This parameter is required.
        self.agent_provider = agent_provider
        # This parameter is required.
        self.biz_type = biz_type
        self.has_model = has_model
        self.model_template_id_list = model_template_id_list
        self.page_number = page_number
        self.page_size = page_size

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

        if self.has_model is not None:
            result['HasModel'] = self.has_model

        if self.model_template_id_list is not None:
            result['ModelTemplateIdList'] = self.model_template_id_list

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentPlatform') is not None:
            self.agent_platform = m.get('AgentPlatform')

        if m.get('AgentProvider') is not None:
            self.agent_provider = m.get('AgentProvider')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('HasModel') is not None:
            self.has_model = m.get('HasModel')

        if m.get('ModelTemplateIdList') is not None:
            self.model_template_id_list = m.get('ModelTemplateIdList')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

