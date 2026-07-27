# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAppPluginRequest(DaraModel):
    def __init__(
        self,
        category: str = None,
        config_items: str = None,
        description: str = None,
        extend: str = None,
        hooks: str = None,
        icon: str = None,
        plugin_id: str = None,
        plugin_name: str = None,
        plugin_version: str = None,
        skill_header: str = None,
        tags: str = None,
        visibility: str = None,
    ):
        # The category.
        self.category = category
        # The configuration form in React JSON Schema format.
        self.config_items = config_items
        # The application description.
        self.description = description
        # Other extension information in JSON format for future parameter expansion.
        self.extend = extend
        # The hook definitions.
        self.hooks = hooks
        # The plug-in description.
        self.icon = icon
        # The gateway plug-in ID.
        self.plugin_id = plugin_id
        # The plug-in name.
        self.plugin_name = plugin_name
        # The plug-in version.
        self.plugin_version = plugin_version
        # The skill header information for model selection.
        self.skill_header = skill_header
        # The labels.
        self.tags = tags
        # The visibility.
        self.visibility = visibility

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.config_items is not None:
            result['ConfigItems'] = self.config_items

        if self.description is not None:
            result['Description'] = self.description

        if self.extend is not None:
            result['Extend'] = self.extend

        if self.hooks is not None:
            result['Hooks'] = self.hooks

        if self.icon is not None:
            result['Icon'] = self.icon

        if self.plugin_id is not None:
            result['PluginId'] = self.plugin_id

        if self.plugin_name is not None:
            result['PluginName'] = self.plugin_name

        if self.plugin_version is not None:
            result['PluginVersion'] = self.plugin_version

        if self.skill_header is not None:
            result['SkillHeader'] = self.skill_header

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.visibility is not None:
            result['Visibility'] = self.visibility

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('ConfigItems') is not None:
            self.config_items = m.get('ConfigItems')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Extend') is not None:
            self.extend = m.get('Extend')

        if m.get('Hooks') is not None:
            self.hooks = m.get('Hooks')

        if m.get('Icon') is not None:
            self.icon = m.get('Icon')

        if m.get('PluginId') is not None:
            self.plugin_id = m.get('PluginId')

        if m.get('PluginName') is not None:
            self.plugin_name = m.get('PluginName')

        if m.get('PluginVersion') is not None:
            self.plugin_version = m.get('PluginVersion')

        if m.get('SkillHeader') is not None:
            self.skill_header = m.get('SkillHeader')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')

        return self

