# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAlidingAssistantShrinkRequest(DaraModel):
    def __init__(
        self,
        app_code: str = None,
        description: str = None,
        ext_shrink: str = None,
        icon: str = None,
        instructions: str = None,
        name: str = None,
        recommend_prompts_shrink: str = None,
        source: int = None,
        source_identity_id: str = None,
        tenant_context_shrink: str = None,
        welcome_content: str = None,
    ):
        self.app_code = app_code
        # This parameter is required.
        self.description = description
        self.ext_shrink = ext_shrink
        # This parameter is required.
        self.icon = icon
        # This parameter is required.
        self.instructions = instructions
        # This parameter is required.
        self.name = name
        self.recommend_prompts_shrink = recommend_prompts_shrink
        # This parameter is required.
        self.source = source
        self.source_identity_id = source_identity_id
        self.tenant_context_shrink = tenant_context_shrink
        # This parameter is required.
        self.welcome_content = welcome_content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_code is not None:
            result['AppCode'] = self.app_code

        if self.description is not None:
            result['Description'] = self.description

        if self.ext_shrink is not None:
            result['Ext'] = self.ext_shrink

        if self.icon is not None:
            result['Icon'] = self.icon

        if self.instructions is not None:
            result['Instructions'] = self.instructions

        if self.name is not None:
            result['Name'] = self.name

        if self.recommend_prompts_shrink is not None:
            result['RecommendPrompts'] = self.recommend_prompts_shrink

        if self.source is not None:
            result['Source'] = self.source

        if self.source_identity_id is not None:
            result['SourceIdentityId'] = self.source_identity_id

        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

        if self.welcome_content is not None:
            result['WelcomeContent'] = self.welcome_content

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Ext') is not None:
            self.ext_shrink = m.get('Ext')

        if m.get('Icon') is not None:
            self.icon = m.get('Icon')

        if m.get('Instructions') is not None:
            self.instructions = m.get('Instructions')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RecommendPrompts') is not None:
            self.recommend_prompts_shrink = m.get('RecommendPrompts')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SourceIdentityId') is not None:
            self.source_identity_id = m.get('SourceIdentityId')

        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        if m.get('WelcomeContent') is not None:
            self.welcome_content = m.get('WelcomeContent')

        return self

