# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InstallPolarClawSkillRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        application_id: str = None,
        force: bool = None,
        scope: str = None,
        skill_version: str = None,
        slug: str = None,
        source: str = None,
        url: str = None,
    ):
        # The target agent in the workspace. If not specified, the default agent is used.
        self.agent_id = agent_id
        # The application ID.
        # 
        # This parameter is required.
        self.application_id = application_id
        # Specifies whether to force reinstallation.
        self.force = force
        # The scope. Valid values: workspace (default) and global (shared directory). This parameter is mutually exclusive with AgentId.
        self.scope = scope
        # The version number.
        self.skill_version = skill_version
        # The skill identifier.
        self.slug = slug
        # The source. Default value: polarhub.
        self.source = source
        # URL
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.force is not None:
            result['Force'] = self.force

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.skill_version is not None:
            result['SkillVersion'] = self.skill_version

        if self.slug is not None:
            result['Slug'] = self.slug

        if self.source is not None:
            result['Source'] = self.source

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('Force') is not None:
            self.force = m.get('Force')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('SkillVersion') is not None:
            self.skill_version = m.get('SkillVersion')

        if m.get('Slug') is not None:
            self.slug = m.get('Slug')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

