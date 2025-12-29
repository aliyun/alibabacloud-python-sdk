# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class ListAddonsResponseBody(DaraModel):
    def __init__(
        self,
        addons: List[main_models.ListAddonsResponseBodyAddons] = None,
    ):
        # The list of available components.
        self.addons = addons

    def validate(self):
        if self.addons:
            for v1 in self.addons:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['addons'] = []
        if self.addons is not None:
            for k1 in self.addons:
                result['addons'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.addons = []
        if m.get('addons') is not None:
            for k1 in m.get('addons'):
                temp_model = main_models.ListAddonsResponseBodyAddons()
                self.addons.append(temp_model.from_map(k1))

        return self

class ListAddonsResponseBodyAddons(DaraModel):
    def __init__(
        self,
        architecture: List[str] = None,
        category: str = None,
        config_schema: str = None,
        install_by_default: bool = None,
        managed: bool = None,
        name: str = None,
        supported_actions: List[str] = None,
        version: str = None,
    ):
        # Architectures supported by the component. Valid values:
        # 
        # *   amd64
        # *   arm64
        self.architecture = architecture
        # The category of the component.
        self.category = category
        # The schema of the custom parameters of the component.
        self.config_schema = config_schema
        # Indicates whether the component is automatically installed by default.
        self.install_by_default = install_by_default
        # Indicates whether the component is fully managed.
        self.managed = managed
        # The component name.
        self.name = name
        # Operations supported by the component. Valid values:
        # 
        # *   Install
        # *   Upgrade
        # *   Modify
        # *   Uninstall
        self.supported_actions = supported_actions
        # The version number.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.architecture is not None:
            result['architecture'] = self.architecture

        if self.category is not None:
            result['category'] = self.category

        if self.config_schema is not None:
            result['config_schema'] = self.config_schema

        if self.install_by_default is not None:
            result['install_by_default'] = self.install_by_default

        if self.managed is not None:
            result['managed'] = self.managed

        if self.name is not None:
            result['name'] = self.name

        if self.supported_actions is not None:
            result['supported_actions'] = self.supported_actions

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('architecture') is not None:
            self.architecture = m.get('architecture')

        if m.get('category') is not None:
            self.category = m.get('category')

        if m.get('config_schema') is not None:
            self.config_schema = m.get('config_schema')

        if m.get('install_by_default') is not None:
            self.install_by_default = m.get('install_by_default')

        if m.get('managed') is not None:
            self.managed = m.get('managed')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('supported_actions') is not None:
            self.supported_actions = m.get('supported_actions')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

