# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class CreateTenantSkillRequest(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        description: str = None,
        display_name: str = None,
        env_vars: Dict[str, str] = None,
        icon_etag: str = None,
        skill_channel: str = None,
        skill_icon: str = None,
        skill_version: str = None,
        slug: str = None,
        task_key: str = None,
    ):
        # The API key of the skill.
        self.api_key = api_key
        # The description of the skill. Maximum length: 500 characters.
        self.description = description
        # The display name.
        self.display_name = display_name
        # The environment variables.
        self.env_vars = env_vars
        # The icon parsing tag. This parameter is required when SkillIcon is specified.
        self.icon_etag = icon_etag
        # The skill channel. Valid values:
        # - ENTERPRISE: Enterprise Edition.
        # - BUSINESS: Business Edition.
        self.skill_channel = skill_channel
        # The skill icon.
        self.skill_icon = skill_icon
        # The skill version.
        self.skill_version = skill_version
        # The slug identifier of the skill. This parameter is user-defined and must be unique within the tenant.
        self.slug = slug
        # The file parsing task key.
        self.task_key = task_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['ApiKey'] = self.api_key

        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.env_vars is not None:
            result['EnvVars'] = self.env_vars

        if self.icon_etag is not None:
            result['IconETag'] = self.icon_etag

        if self.skill_channel is not None:
            result['SkillChannel'] = self.skill_channel

        if self.skill_icon is not None:
            result['SkillIcon'] = self.skill_icon

        if self.skill_version is not None:
            result['SkillVersion'] = self.skill_version

        if self.slug is not None:
            result['Slug'] = self.slug

        if self.task_key is not None:
            result['TaskKey'] = self.task_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('EnvVars') is not None:
            self.env_vars = m.get('EnvVars')

        if m.get('IconETag') is not None:
            self.icon_etag = m.get('IconETag')

        if m.get('SkillChannel') is not None:
            self.skill_channel = m.get('SkillChannel')

        if m.get('SkillIcon') is not None:
            self.skill_icon = m.get('SkillIcon')

        if m.get('SkillVersion') is not None:
            self.skill_version = m.get('SkillVersion')

        if m.get('Slug') is not None:
            self.slug = m.get('Slug')

        if m.get('TaskKey') is not None:
            self.task_key = m.get('TaskKey')

        return self

