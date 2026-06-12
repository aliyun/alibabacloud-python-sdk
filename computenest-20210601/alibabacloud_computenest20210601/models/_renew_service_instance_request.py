# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RenewServiceInstanceRequest(DaraModel):
    def __init__(
        self,
        dry_run: bool = None,
        service_instance_id: str = None,
    ):
        # Specifies whether to perform a dry run of the renewal request, including permission and instance status checks. Valid values:
        # 
        # - **true**: Sends the request without renewing the service instance.
        # 
        # - **false**: Sends the request and renews the service instance after the checks pass.
        # 
        # Default value: false. The operation is allowed only when the service instance is in the Pending Renewal or Renewal Failed state.
        self.dry_run = dry_run
        # The service instance ID.
        self.service_instance_id = service_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')

        return self

