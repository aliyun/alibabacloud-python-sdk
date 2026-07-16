# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpgradeServiceInstanceShrinkRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: str = None,
        parameters_shrink: str = None,
        region_id: str = None,
        service_instance_id: str = None,
        service_version: str = None,
    ):
        # A client-generated token that ensures the idempotence of the request. The token must be unique for each request. It can contain only ASCII characters and must be no more than 64 characters long.
        self.client_token = client_token
        # Specifies whether to perform a dry run. A dry run checks for issues such as permissions and the instance status. Valid values:
        # 
        # - true: Sends the request without upgrading the service instance.
        # 
        # - false: Sends the request and upgrades the service instance after the check is passed.
        self.dry_run = dry_run
        # The parameters required for the upgrade. This is used when new parameters are added to the new service version.
        self.parameters_shrink = parameters_shrink
        # The region ID.
        self.region_id = region_id
        # The service instance ID.
        self.service_instance_id = service_instance_id
        # The service version to upgrade to.
        self.service_version = service_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.parameters_shrink is not None:
            result['Parameters'] = self.parameters_shrink

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id

        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('Parameters') is not None:
            self.parameters_shrink = m.get('Parameters')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')

        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')

        return self

