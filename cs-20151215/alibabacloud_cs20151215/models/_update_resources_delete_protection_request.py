# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateResourcesDeleteProtectionRequest(DaraModel):
    def __init__(
        self,
        enable: bool = None,
        namespace: str = None,
        resource_type: str = None,
        resources: List[str] = None,
    ):
        # Specifies whether to enable deletion protection. Set the value to true to enable deletion protection and set the value to false to disable deletion protection.
        self.enable = enable
        # The namespace to which the resource belongs.
        self.namespace = namespace
        # The type of resource for which deletion protection is enabled or disabled. You can specify namespaces or Services.
        self.resource_type = resource_type
        # The resources list.
        self.resources = resources

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['enable'] = self.enable

        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.resource_type is not None:
            result['resource_type'] = self.resource_type

        if self.resources is not None:
            result['resources'] = self.resources

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('resource_type') is not None:
            self.resource_type = m.get('resource_type')

        if m.get('resources') is not None:
            self.resources = m.get('resources')

        return self

