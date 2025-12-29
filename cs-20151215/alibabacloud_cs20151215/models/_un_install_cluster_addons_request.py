# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class UnInstallClusterAddonsRequest(DaraModel):
    def __init__(
        self,
        addons: List[main_models.UnInstallClusterAddonsRequestAddons] = None,
    ):
        # The list of add-ons to uninstall.
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
                temp_model = main_models.UnInstallClusterAddonsRequestAddons()
                self.addons.append(temp_model.from_map(k1))

        return self

class UnInstallClusterAddonsRequestAddons(DaraModel):
    def __init__(
        self,
        cleanup_cloud_resources: bool = None,
        name: str = None,
    ):
        # Specifies whether to clean up related cloud resources during uninstallation.
        # 
        # *   true: clean up
        # *   false: retain
        self.cleanup_cloud_resources = cleanup_cloud_resources
        # The name of the add-on to uninstall. You can call the [ListClusterAddonInstances](https://help.aliyun.com/document_detail/2667940.html) operation to query the installed add-ons.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cleanup_cloud_resources is not None:
            result['cleanup_cloud_resources'] = self.cleanup_cloud_resources

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cleanup_cloud_resources') is not None:
            self.cleanup_cloud_resources = m.get('cleanup_cloud_resources')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

