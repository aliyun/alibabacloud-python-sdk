# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class StopInstancesRequest(DaraModel):
    def __init__(
        self,
        batch_optimization: str = None,
        dry_run: bool = None,
        force_stop: bool = None,
        instance_id: List[str] = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        stopped_mode: str = None,
    ):
        # The batch operation mode. Valid values:
        # 
        # - AllTogether: all operations must succeed for the entire batch operation to be considered successful. If any operation fails, the entire batch operation is considered failed, and all executed operations are rolled back to their original state.
        # 
        # - SuccessFirst: each operation in the batch is executed independently. If an operation fails, other operations can still continue and succeed. In this mode, successful operations are committed, and failed operations are marked as failed without affecting the results of other operations.
        # 
        # Default value: AllTogether.
        self.batch_optimization = batch_optimization
        # Specifies whether to send a dry run request. Valid values:
        # 
        # - true: sends a dry run request without stopping the instances. The system checks whether required parameters are specified, the request format is valid, and the instance status is valid. If the request fails the check, an error is returned. If the request passes the check, `DRYRUN.SUCCESS` is returned.
        # > If the `BatchOptimization` parameter is set to `SuccessFirst`, the dry run result for `DryRun=true` only returns `DRYRUN.SUCCESS`.
        # 
        # - false: sends a regular request and stops the instances directly after the request passes the check.
        # 
        # Default value: false.
        self.dry_run = dry_run
        # Specifies whether to force stop the instances. Valid values:
        # 
        # - true: force stops the instances.
        #   >Warning: Force stopping an instance is equivalent to a power outage and may cause data in the operating system that is not written to the disk to be lost. Proceed with caution.
        # - false: normally stops the instances.
        # 
        # Default value: false.
        self.force_stop = force_stop
        # The instance IDs. Array length: 1 to 100.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the instance. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The stop mode. Valid values:
        #   - StopCharging: economical mode. After you enable economical mode:
        #     - Billing is suspended for computing resources (vCPUs, memory, and GPUs), image licenses, and static public IP addresses that use the pay-by-bandwidth billing method.
        #     - Billing continues for system cloud disks, data cloud disks, and Elastic IP Addresses (EIPs) that use the pay-by-bandwidth billing method.
        #     - Because computing resources are released, the instance may fail to start due to insufficient resource inventory. If this occurs, try again later or change the instance type.
        #     - If an EIP was associated with the instance before it was stopped, the IP address remains unchanged after the instance is restarted. Otherwise, the static public IP address may change, but the private IP address remains unchanged. 
        # 
        #     For more information, see [Economical mode](https://help.aliyun.com/document_detail/63353.html).
        #     >Notice: 
        # If the instance does not support economical mode, the API does not return an error and prioritizes stopping the instance. Instance types that do not support economical mode include instances with local disks and subscription instances.
        #     
        # 
        #   - KeepCharging: standard stop mode. After the instance is stopped, its resources are retained and continue to be billed. The ECS instance type inventory and public IP address are also reserved for you. Select this mode if you stop the instance to perform operations such as replacing the operating system, reinitializing cloud disks, changing the instance type, or modifying the private IP address. This prevents startup failures.
        # 
        # Default value: If you [enable economical mode for instances in a VPC](~~63353#default~~) and the instance meets the requirements, the default value is `StopCharging`. Otherwise, the default value is `KeepCharging`.
        self.stopped_mode = stopped_mode

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

        if self.force_stop is not None:
            result['ForceStop'] = self.force_stop

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

        if self.stopped_mode is not None:
            result['StoppedMode'] = self.stopped_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchOptimization') is not None:
            self.batch_optimization = m.get('BatchOptimization')

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

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('StoppedMode') is not None:
            self.stopped_mode = m.get('StoppedMode')

        return self

