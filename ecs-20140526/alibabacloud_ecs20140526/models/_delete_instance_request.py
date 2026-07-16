# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteInstanceRequest(DaraModel):
    def __init__(
        self,
        dry_run: bool = None,
        force: bool = None,
        force_stop: bool = None,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        terminate_subscription: bool = None,
    ):
        # Specifies whether to perform only a dry run. Valid values:
        # 
        # - true: Sends a check request without releasing the instance. The system checks whether the required parameters are specified, the request format is valid, business requirements are met, and ECS resources are sufficient. If the check fails, the corresponding error is returned. If the check succeeds, the error code `DryRunOperation` is returned.
        # - false (default): Sends a normal request. After the request passes the check, the instance is directly deleted.
        self.dry_run = dry_run
        # Specifies whether to forcefully release a **running** (`Running`) instance.
        # 
        # - true: Forcefully releases a **running** (`Running`) instance.
        # - false: Releases the instance in the normal way. The instance must be in the **Stopped** (`Stopped`) state.
        # 
        # Default value: false.
        # >Warning: A forceful release is equivalent to a power-off. Temporary data in the instance memory and storage is erased and cannot be recovered..
        self.force = force
        # Specifies whether to use the forced shutdown policy when releasing a **running** (`Running`) instance. This parameter takes effect only when `Force=true`. Valid values:
        # 
        # - true: Forcefully shuts down and releases the instance. This is equivalent to a typical power-off operation. The instance directly enters the resource release process.
        # >Warning: A forceful release is equivalent to a power-off. Temporary data in the instance memory and storage is erased and cannot be recovered.
        # - false: Before the instance is released, the system preferentially performs a standard shutdown process. This mode causes the instance release to take several minutes. You can configure service draining actions during the operating system shutdown to reduce noise in your business systems.
        # 
        # Default value: true.
        self.force_stop = force_stop
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Specifies whether to release an expired subscription instance.
        # 
        # - true: Releases the instance.
        # - false: Does not release the instance.
        # 
        # Default value: false.
        self.terminate_subscription = terminate_subscription

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

        if self.terminate_subscription is not None:
            result['TerminateSubscription'] = self.terminate_subscription

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('Force') is not None:
            self.force = m.get('Force')

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

        if m.get('TerminateSubscription') is not None:
            self.terminate_subscription = m.get('TerminateSubscription')

        return self

