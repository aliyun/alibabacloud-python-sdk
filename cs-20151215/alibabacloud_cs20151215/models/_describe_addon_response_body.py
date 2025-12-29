# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class DescribeAddonResponseBody(DaraModel):
    def __init__(
        self,
        architecture: List[str] = None,
        category: str = None,
        config_schema: str = None,
        install_by_default: bool = None,
        managed: bool = None,
        name: str = None,
        newer_versions: List[main_models.DescribeAddonResponseBodyNewerVersions] = None,
        supported_actions: List[str] = None,
        version: str = None,
    ):
        # The CPU architecture supported by the component.
        self.architecture = architecture
        # The category of the component.
        self.category = category
        # The custom parameter schema of the component.
        self.config_schema = config_schema
        # Indicates whether the component is automatically installed by default.
        self.install_by_default = install_by_default
        # Indicates whether the component is fully managed.
        self.managed = managed
        # The name of the component.
        self.name = name
        # The latest version information of the component.
        self.newer_versions = newer_versions
        # The operations supported by the component.
        self.supported_actions = supported_actions
        # The version of the component.
        self.version = version

    def validate(self):
        if self.newer_versions:
            for v1 in self.newer_versions:
                 if v1:
                    v1.validate()

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

        result['newer_versions'] = []
        if self.newer_versions is not None:
            for k1 in self.newer_versions:
                result['newer_versions'].append(k1.to_map() if k1 else None)

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

        self.newer_versions = []
        if m.get('newer_versions') is not None:
            for k1 in m.get('newer_versions'):
                temp_model = main_models.DescribeAddonResponseBodyNewerVersions()
                self.newer_versions.append(temp_model.from_map(k1))

        if m.get('supported_actions') is not None:
            self.supported_actions = m.get('supported_actions')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

class DescribeAddonResponseBodyNewerVersions(DaraModel):
    def __init__(
        self,
        minimum_cluster_version: str = None,
        upgradable: bool = None,
        version: str = None,
    ):
        # The minimum cluster version required by the component version.
        self.minimum_cluster_version = minimum_cluster_version
        # Indicates whether the component can be updated to the version.
        # 
        # *   true: yes
        # *   false: no
        self.upgradable = upgradable
        # The latest version number of the component.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.minimum_cluster_version is not None:
            result['minimum_cluster_version'] = self.minimum_cluster_version

        if self.upgradable is not None:
            result['upgradable'] = self.upgradable

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('minimum_cluster_version') is not None:
            self.minimum_cluster_version = m.get('minimum_cluster_version')

        if m.get('upgradable') is not None:
            self.upgradable = m.get('upgradable')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

