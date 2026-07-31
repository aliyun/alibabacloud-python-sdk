# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RebootInstanceRequest(DaraModel):
    def __init__(
        self,
        dry_run: bool = None,
        force_stop: bool = None,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Specifies whether to perform only a dry run. Valid values:
        # 
        # - true: performs only a dry run. The instance is not restarted. The system checks whether required parameters are specified, whether the request format is valid, whether business restrictions are met, and whether ECS resources are available. If the check fails, the corresponding error is returned. If the check succeeds, the `DryRunOperation` error code is returned.
        # - false: performs a dry run and sends the request. If the check succeeds, the instance is restarted.
        # 
        # Default value: false.
        self.dry_run = dry_run
        # Specifies whether to forcefully stop ECS instance before restarting it. Valid values:
        # 
        # -   true: Forcefully stops ECS instance. This is equivalent to a power-off operation. Cached data that has not been written to storage devices is lost.
        # 
        # -   false: Normally stops ECS instance.
        # 
        # Default value: false.
        self.force_stop = force_stop
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.force_stop is not None:
            result['ForceStop'] = self.force_stop

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('ForceStop') is not None:
            self.force_stop = m.get('ForceStop')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

