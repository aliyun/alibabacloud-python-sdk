# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAlidingAssistantShrinkRequest(DaraModel):
    def __init__(
        self,
        assistant_id: str = None,
        description: str = None,
        ext_shrink: str = None,
        fallback_content: str = None,
        feature_shrink: str = None,
        icon: str = None,
        instructions: str = None,
        name: str = None,
        recommend_prompts_shrink: str = None,
        tenant_context_shrink: str = None,
        welcome_content: str = None,
    ):
        # This parameter is required.
        self.assistant_id = assistant_id
        self.description = description
        self.ext_shrink = ext_shrink
        self.fallback_content = fallback_content
        self.feature_shrink = feature_shrink
        self.icon = icon
        self.instructions = instructions
        self.name = name
        self.recommend_prompts_shrink = recommend_prompts_shrink
        self.tenant_context_shrink = tenant_context_shrink
        self.welcome_content = welcome_content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assistant_id is not None:
            result['AssistantId'] = self.assistant_id

        if self.description is not None:
            result['Description'] = self.description

        if self.ext_shrink is not None:
            result['Ext'] = self.ext_shrink

        if self.fallback_content is not None:
            result['FallbackContent'] = self.fallback_content

        if self.feature_shrink is not None:
            result['Feature'] = self.feature_shrink

        if self.icon is not None:
            result['Icon'] = self.icon

        if self.instructions is not None:
            result['Instructions'] = self.instructions

        if self.name is not None:
            result['Name'] = self.name

        if self.recommend_prompts_shrink is not None:
            result['RecommendPrompts'] = self.recommend_prompts_shrink

        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

        if self.welcome_content is not None:
            result['WelcomeContent'] = self.welcome_content

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssistantId') is not None:
            self.assistant_id = m.get('AssistantId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Ext') is not None:
            self.ext_shrink = m.get('Ext')

        if m.get('FallbackContent') is not None:
            self.fallback_content = m.get('FallbackContent')

        if m.get('Feature') is not None:
            self.feature_shrink = m.get('Feature')

        if m.get('Icon') is not None:
            self.icon = m.get('Icon')

        if m.get('Instructions') is not None:
            self.instructions = m.get('Instructions')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RecommendPrompts') is not None:
            self.recommend_prompts_shrink = m.get('RecommendPrompts')

        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        if m.get('WelcomeContent') is not None:
            self.welcome_content = m.get('WelcomeContent')

        return self

