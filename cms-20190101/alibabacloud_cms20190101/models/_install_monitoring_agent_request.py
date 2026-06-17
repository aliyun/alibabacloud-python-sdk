# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class InstallMonitoringAgentRequest(DaraModel):
    def __init__(
        self,
        force: bool = None,
        install_command: str = None,
        instance_ids: List[str] = None,
        region_id: str = None,
    ):
        # Specifies whether to forcibly install the CloudMonitor agent. Valid values:
        # 
        # - true (default): Forcibly installs the agent.
        # 
        # - false: Does not forcibly install the agent.
        self.force = force
        # The installation command. This command installs the CloudMonitor agent on all Alibaba Cloud hosts that belong to your Alibaba Cloud account. Valid values:
        # 
        # - `onlyInstallNotHasAgent`: Installs the latest version of the CloudMonitor agent only on Alibaba Cloud hosts where the agent is not installed.
        # 
        # - `onlyUpgradeAgent`: Upgrades the CloudMonitor agent only on Alibaba Cloud hosts where an earlier version of the agent is installed.
        # 
        # - `installAndUpgrade`: Installs the latest version of the CloudMonitor agent on Alibaba Cloud hosts where the agent is not installed, and upgrades the agent on Alibaba Cloud hosts where an earlier version of the agent is installed.
        # 
        # > If you set this parameter, the `InstanceIds` parameter is invalid.
        self.install_command = install_command
        # The IDs of the Alibaba Cloud hosts.
        # 
        # You can specify from 1 to 10 instance IDs.
        # 
        # > You must specify either `InstallCommand` or `InstanceIds`.
        self.instance_ids = instance_ids
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.force is not None:
            result['Force'] = self.force

        if self.install_command is not None:
            result['InstallCommand'] = self.install_command

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Force') is not None:
            self.force = m.get('Force')

        if m.get('InstallCommand') is not None:
            self.install_command = m.get('InstallCommand')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

