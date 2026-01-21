# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PutMonitoringConfigRequest(DaraModel):
    def __init__(
        self,
        auto_install: bool = None,
        enable_install_agent_new_ecs: bool = None,
        region_id: str = None,
    ):
        # This parameter is deprecated.
        self.auto_install = auto_install
        # Specifies whether to automatically install the CloudMonitor agent on new ECS instances. Valid values:
        # 
        # *   true (default): The CloudMonitor agent is automatically installed on new ECS instances.
        # *   false: The CloudMonitor agent is not automatically installed on new ECS instances.
        self.enable_install_agent_new_ecs = enable_install_agent_new_ecs
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_install is not None:
            result['AutoInstall'] = self.auto_install

        if self.enable_install_agent_new_ecs is not None:
            result['EnableInstallAgentNewECS'] = self.enable_install_agent_new_ecs

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoInstall') is not None:
            self.auto_install = m.get('AutoInstall')

        if m.get('EnableInstallAgentNewECS') is not None:
            self.enable_install_agent_new_ecs = m.get('EnableInstallAgentNewECS')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

