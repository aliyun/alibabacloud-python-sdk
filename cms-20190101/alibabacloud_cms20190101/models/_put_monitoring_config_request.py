# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PutMonitoringConfigRequest(DaraModel):
    def __init__(
        self,
        auto_install: bool = None,
        client_token: str = None,
        dry_run: bool = None,
        enable_install_agent_new_ecs: bool = None,
        region_id: str = None,
    ):
        # This parameter is not used.
        self.auto_install = auto_install
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can generate the token on your client to ensure that the token is unique across different requests. The client token supports only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** may be different for each API request.
        self.client_token = client_token
        # Specifies whether to perform a dry run on the request. Valid values:
        # - **true**: sends a check request without deleting the endpoint IPAM pool. The check items include whether required parameters are specified, the request format, and service limits. If the request fails the check, an error is returned. If the request passes the check, the `DryRunOperation` error code is returned.
        # - **false** (default value): sends a normal request and directly deletes the endpoint IPAM pool if the request passes the check.
        # Default value: **false**.
        self.dry_run = dry_run
        # Specifies whether to automatically install the CloudMonitor agent on newly purchased ECS instances. Valid values:
        # - true: Automatically installs the CloudMonitor agent on newly purchased ECS instances.
        # - false: Does not automatically install the CloudMonitor agent on newly purchased ECS instances.
        # Default value: true.
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

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.enable_install_agent_new_ecs is not None:
            result['EnableInstallAgentNewECS'] = self.enable_install_agent_new_ecs

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoInstall') is not None:
            self.auto_install = m.get('AutoInstall')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EnableInstallAgentNewECS') is not None:
            self.enable_install_agent_new_ecs = m.get('EnableInstallAgentNewECS')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

