# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InstallAddonRequest(DaraModel):
    def __init__(
        self,
        addon_name: str = None,
        addon_version: str = None,
        cluster_id: str = None,
        resources_spec: str = None,
        services_spec: str = None,
    ):
        # The addon name.
        # 
        # This parameter is required.
        self.addon_name = addon_name
        # The addon version.
        # 
        # This parameter is required.
        self.addon_version = addon_version
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The resource configurations of the addon.
        # 
        # This parameter is required.
        self.resources_spec = resources_spec
        # The service configurations of the addon.
        # 
        # This parameter is required.
        self.services_spec = services_spec

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addon_name is not None:
            result['AddonName'] = self.addon_name

        if self.addon_version is not None:
            result['AddonVersion'] = self.addon_version

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.resources_spec is not None:
            result['ResourcesSpec'] = self.resources_spec

        if self.services_spec is not None:
            result['ServicesSpec'] = self.services_spec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddonName') is not None:
            self.addon_name = m.get('AddonName')

        if m.get('AddonVersion') is not None:
            self.addon_version = m.get('AddonVersion')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ResourcesSpec') is not None:
            self.resources_spec = m.get('ResourcesSpec')

        if m.get('ServicesSpec') is not None:
            self.services_spec = m.get('ServicesSpec')

        return self

