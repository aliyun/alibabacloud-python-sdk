# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RebootInstancesRequest(DaraModel):
    def __init__(
        self,
        batch_optimization: str = None,
        dry_run: bool = None,
        force_reboot: bool = None,
        instance_id: List[str] = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The batch operation mode. Valid values:
        # 
        # - AllTogether: In this mode, a success message is returned if all instances are restarted. If any instance fails validation, all instances fail to restart and an error message is returned.
        # 
        # - SuccessFirst: In this mode, each instance is restarted separately. The response includes the operation result for each instance.
        # 
        # Default value: AllTogether.
        self.batch_optimization = batch_optimization
        # Specifies whether to perform only a dry run. Valid values:
        # 
        # - true: performs only a dry run without restarting the instance. The system checks the required parameters, request format, and instance status. If the check fails, the corresponding error is returned. If the check passes, `DRYRUN.SUCCESS` is returned.
        # > If the BatchOptimization parameter is set to `SuccessFirst`, the dry run result for `DryRun=true` returns only `DRYRUN.SUCCESS`.
        # 
        # - false: performs a dry run and sends the request. After the check passes, the instance is restarted.
        # 
        # Default value: false.
        self.dry_run = dry_run
        # Specifies whether to force restart the instance. Valid values:
        # 
        # -   true: forces a restart. This is equivalent to a power-off operation. Cached data that has not been written to storage devices is lost.
        # 
        # -   false: performs a normal restart.
        # 
        # Default value: false.
        self.force_reboot = force_reboot
        # The instance ID array. Array length: 1 to 100.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the instance. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_optimization is not None:
            result['BatchOptimization'] = self.batch_optimization

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.force_reboot is not None:
            result['ForceReboot'] = self.force_reboot

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchOptimization') is not None:
            self.batch_optimization = m.get('BatchOptimization')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('ForceReboot') is not None:
            self.force_reboot = m.get('ForceReboot')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

