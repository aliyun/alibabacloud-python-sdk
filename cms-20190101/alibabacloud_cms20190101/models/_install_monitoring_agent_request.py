# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class InstallMonitoringAgentRequest(DaraModel):
    def __init__(
        self,
        dry_run: bool = None,
        force: bool = None,
        install_command: str = None,
        instance_ids: List[str] = None,
        region_id: str = None,
    ):
        # Specifies whether to perform a dry run on the request. The dry run includes checks on permissions and instance status. Valid values:
        # 
        # - **false** (default): Sends a normal request. After the request passes the check, the name and description of the route table are directly modified.
        # - **true**: Sends a dry run request. Only checks are performed, and the name and description of the route table are not modified. Check items include whether required parameters are specified and the request format. If the check fails, an error is returned. If the check succeeds, the DryRunOperation error code is returned.
        self.dry_run = dry_run
        # Specifies whether to forcibly install the CloudMonitor agent. Valid values:
        # - true (default): Forcibly installs the agent.
        # - false: Does not forcibly install the agent.
        self.force = force
        # Installs the CloudMonitor agent on all Alibaba Cloud hosts within the current Alibaba Cloud account. Valid values:
        # 
        # - onlyInstallNotHasAgent: Installs the latest version of the agent only on Alibaba Cloud hosts on which the CloudMonitor agent is not installed.
        # 
        # - onlyUpgradeAgent: Upgrades the agent only on Alibaba Cloud hosts on which a non-latest version of the CloudMonitor agent is installed.
        # 
        # - installAndUpgrade: Installs the latest version of the agent on Alibaba Cloud hosts on which the CloudMonitor agent is not installed, and upgrades the agent on Alibaba Cloud hosts on which a non-latest version of the CloudMonitor agent is installed.
        # 
        # > If you specify this parameter, the InstanceIds parameter becomes invalid.
        self.install_command = install_command
        # The ID of the Alibaba Cloud host.
        # 
        # Valid values of N: 1 to 10.
        # 
        # > You must specify either InstallCommand or InstanceIds.
        self.instance_ids = instance_ids
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

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
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('Force') is not None:
            self.force = m.get('Force')

        if m.get('InstallCommand') is not None:
            self.install_command = m.get('InstallCommand')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

