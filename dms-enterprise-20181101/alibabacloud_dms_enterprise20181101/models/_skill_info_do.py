# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SkillInfoDO(DaraModel):
    def __init__(
        self,
        category: str = None,
        compatibility: str = None,
        description: str = None,
        display_name: str = None,
        install_count: str = None,
        name: str = None,
        source: str = None,
        source_type: str = None,
        tags: str = None,
        updated_at: str = None,
        version: str = None,
    ):
        self.category = category
        self.compatibility = compatibility
        self.description = description
        self.display_name = display_name
        self.install_count = install_count
        self.name = name
        self.source = source
        self.source_type = source_type
        self.tags = tags
        self.updated_at = updated_at
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.compatibility is not None:
            result['Compatibility'] = self.compatibility

        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.install_count is not None:
            result['InstallCount'] = self.install_count

        if self.name is not None:
            result['Name'] = self.name

        if self.source is not None:
            result['Source'] = self.source

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Compatibility') is not None:
            self.compatibility = m.get('Compatibility')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('InstallCount') is not None:
            self.install_count = m.get('InstallCount')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

