# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class ModifyClusterAddonRequest(DaraModel):
    def __init__(
        self,
        addon: main_models.ModifyClusterAddonRequestAddon = None,
        cluster_id: str = None,
        component_name: str = None,
    ):
        self.addon = addon
        # This parameter is required.
        self.cluster_id = cluster_id
        # This parameter is required.
        self.component_name = component_name

    def validate(self):
        if self.addon:
            self.addon.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addon is not None:
            result['Addon'] = self.addon.to_map()

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.component_name is not None:
            result['ComponentName'] = self.component_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Addon') is not None:
            temp_model = main_models.ModifyClusterAddonRequestAddon()
            self.addon = temp_model.from_map(m.get('Addon'))

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ComponentName') is not None:
            self.component_name = m.get('ComponentName')

        return self

class ModifyClusterAddonRequestAddon(DaraModel):
    def __init__(
        self,
        config_schema: List[main_models.ModifyClusterAddonRequestAddonConfigSchema] = None,
        name: str = None,
        version: str = None,
    ):
        self.config_schema = config_schema
        self.name = name
        self.version = version

    def validate(self):
        if self.config_schema:
            for v1 in self.config_schema:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ConfigSchema'] = []
        if self.config_schema is not None:
            for k1 in self.config_schema:
                result['ConfigSchema'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config_schema = []
        if m.get('ConfigSchema') is not None:
            for k1 in m.get('ConfigSchema'):
                temp_model = main_models.ModifyClusterAddonRequestAddonConfigSchema()
                self.config_schema.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class ModifyClusterAddonRequestAddonConfigSchema(DaraModel):
    def __init__(
        self,
        app_version: str = None,
        config_version: str = None,
        name: str = None,
        params: Dict[str, Any] = None,
    ):
        self.app_version = app_version
        self.config_version = config_version
        self.name = name
        self.params = params

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_version is not None:
            result['AppVersion'] = self.app_version

        if self.config_version is not None:
            result['ConfigVersion'] = self.config_version

        if self.name is not None:
            result['Name'] = self.name

        if self.params is not None:
            result['Params'] = self.params

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')

        if m.get('ConfigVersion') is not None:
            self.config_version = m.get('ConfigVersion')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        return self

