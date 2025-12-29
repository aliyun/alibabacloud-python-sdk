# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class ListClusterAddonInstancesResponseBody(DaraModel):
    def __init__(
        self,
        addons: List[main_models.ListClusterAddonInstancesResponseBodyAddons] = None,
    ):
        # A list of components that are installed in the cluster.
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
                temp_model = main_models.ListClusterAddonInstancesResponseBodyAddons()
                self.addons.append(temp_model.from_map(k1))

        return self

class ListClusterAddonInstancesResponseBodyAddons(DaraModel):
    def __init__(
        self,
        name: str = None,
        state: str = None,
        version: str = None,
    ):
        # The component name.
        self.name = name
        # The status of the component. Valid values:
        # 
        # *   active: The component is installed.
        # *   updating: The component is being modified.
        # *   upgrading: The component is being updated.
        # *   deleting: The component is being uninstalled.
        self.state = state
        # The version of the component.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.state is not None:
            result['state'] = self.state

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('state') is not None:
            self.state = m.get('state')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

