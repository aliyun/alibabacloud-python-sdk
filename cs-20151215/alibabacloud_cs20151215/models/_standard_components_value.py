# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StandardComponentsValue(DaraModel):
    def __init__(
        self,
        name: str = None,
        version: str = None,
        description: str = None,
        required: str = None,
        disabled: bool = None,
    ):
        # The name of the component.
        self.name = name
        # The version of the component.
        self.version = version
        # The description of the component.
        self.description = description
        # Indicates whether the component is required for the cluster. Valid values:
        # 
        # - `true`: The component is required and must be installed when the cluster is created.
        # 
        # - `false`: The component is not required. You can install it through component management after the cluster is created.
        self.required = required
        # Specifies whether to disable default installation. When a cluster is created, in addition to the required components, some log-related or routing-related components (such as Ingress) are installed by default. If you do not want these components to be installed by default, set this parameter to disable default installation. Valid values:
        # 
        # - `true`: Default installation is disabled.
        # - `false`: Default installation is enabled.
        self.disabled = disabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.version is not None:
            result['version'] = self.version

        if self.description is not None:
            result['description'] = self.description

        if self.required is not None:
            result['required'] = self.required

        if self.disabled is not None:
            result['disabled'] = self.disabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('version') is not None:
            self.version = m.get('version')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('required') is not None:
            self.required = m.get('required')

        if m.get('disabled') is not None:
            self.disabled = m.get('disabled')

        return self

