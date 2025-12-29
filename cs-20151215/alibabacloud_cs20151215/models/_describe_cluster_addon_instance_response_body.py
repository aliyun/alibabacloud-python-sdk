# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeClusterAddonInstanceResponseBody(DaraModel):
    def __init__(
        self,
        config: str = None,
        name: str = None,
        state: str = None,
        version: str = None,
    ):
        # The configuration of the component.
        self.config = config
        # The name of the component.
        self.name = name
        # The status of the component. Valid values:
        # 
        # *   initial: The component is being installed.
        # *   active: The component has been installed.
        # *   unhealthy: The component is in an abnormal state.
        # *   upgrading: The component is undergoing an upgrade.
        # *   updating: Component configuration changes are being applied.
        # *   deleting: The component is being uninstalled.
        # *   deleted: The component has been deleted.
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
        if self.config is not None:
            result['config'] = self.config

        if self.name is not None:
            result['name'] = self.name

        if self.state is not None:
            result['state'] = self.state

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            self.config = m.get('config')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('state') is not None:
            self.state = m.get('state')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

