# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateModelProviderTemplateShrinkRequest(DaraModel):
    def __init__(
        self,
        config_shrink: str = None,
        description: str = None,
        enable_wuying_proxy: bool = None,
        name: str = None,
        provider_template_id: str = None,
    ):
        # The model provider configuration.
        self.config_shrink = config_shrink
        # The description of the model provider template.
        self.description = description
        # Specifies whether to enable the Wuying security gateway proxy.
        self.enable_wuying_proxy = enable_wuying_proxy
        # The name of the model provider template.
        self.name = name
        # The ID of the model provider template.
        # 
        # This parameter is required.
        self.provider_template_id = provider_template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_shrink is not None:
            result['Config'] = self.config_shrink

        if self.description is not None:
            result['Description'] = self.description

        if self.enable_wuying_proxy is not None:
            result['EnableWuyingProxy'] = self.enable_wuying_proxy

        if self.name is not None:
            result['Name'] = self.name

        if self.provider_template_id is not None:
            result['ProviderTemplateId'] = self.provider_template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config_shrink = m.get('Config')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnableWuyingProxy') is not None:
            self.enable_wuying_proxy = m.get('EnableWuyingProxy')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProviderTemplateId') is not None:
            self.provider_template_id = m.get('ProviderTemplateId')

        return self

