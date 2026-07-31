# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartInstanceRequest(DaraModel):
    def __init__(
        self,
        dry_run: bool = None,
        init_local_disk: bool = None,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Specifies whether to perform only a dry run. Valid values:
        # 
        # - true: performs only a dry run. The instance is not started. The system checks whether the AccessKey pair is valid, whether Resource Access Management (RAM) users are granted required permissions, and whether the required parameters are specified. If the check fails, the corresponding error is returned. If the check succeeds, the DryRunOperation error code is returned.
        # - false: performs a dry run and sends the request. If the check succeeds, a 2XX HTTP status code is returned and the instance is started.
        # 
        # Default value: false.
        self.dry_run = dry_run
        # Specifies whether to recover the instance to its initial health state when a local disk fails. This parameter is applicable to instances that use local disks, such as instances in the d1, i1, or i2 instance families. Valid values:
        # 
        # - true: Recovers the instance to its initial health state.
        # >Warning: All data stored on the local disks of the instance is lost.
        # 
        # - false: Does not perform any action and maintains the current state.
        # 
        # Default value: false.
        self.init_local_disk = init_local_disk
        # The instance ID of the instance that you want to start.
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

        if self.init_local_disk is not None:
            result['InitLocalDisk'] = self.init_local_disk

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

        if m.get('InitLocalDisk') is not None:
            self.init_local_disk = m.get('InitLocalDisk')

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

