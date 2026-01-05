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
        # Specifies the batch operation mode. Valid values:
        # 
        # *   AllTogether: The batch operation is successful only after all operations are successful. If any operation fails, the batch operation is considered failed, and all operations that have been performed are undone to restore the instances to the status before the batch operation.
        # *   SuccessFirst: allows each operation in a batch to be independently executed. If an operation fails, other operations can continue and confirm success. In this mode, successful operations are committed and failed operations are marked as failed, but the execution results of other operations are not affected.
        # 
        # Default value: AllTogether.
        self.batch_optimization = batch_optimization
        # Specifies whether to send a precheck request. Valid values:
        # 
        # *   true: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and instance status. If the check fails, the corresponding error message is returned. If the request passes the dry run, `DRYRUN.SUCCESS` is returned.
        # 
        # >  If you set `BatchOptimization` to `SuccessFirst` and `DryRun` to true, only `DRYRUN.SUCCESS` is returned, regardless of whether the request passes the dry run.
        # 
        # *   false: performs a dry run and performs the actual request. If the request passes the dry run, instances are stopped.
        # 
        # Default value: false.
        self.dry_run = dry_run
        # Specifies whether to forcefully stop instances. Valid values:
        # 
        # *   true: forcefully stops the ECS instance.
        # 
        #     **
        # 
        #     **Alert** Force Stop: forcefully stops the instance. A force stop is equivalent to a physical shutdown and may cause data loss if instance data has not been written to disks.
        # 
        # *   false: normally stops the ECS instance.
        # 
        # Default value: false.
        self.force_stop = force_stop
        # The IDs of ECS instances. You can specify 1 to 100 instance IDs.
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
        # Stop mode. Valid values:
        # 
        # *   StopCharging: economical mode. After an instance is stopped in economical mode:
        # 
        #     *   Billing for the following resources of the instance stops: computing resources (vCPUs, memory, and GPUs), image licenses, and public bandwidth of the static public IP address (if any) that uses the pay-by-bandwidth metering method.
        #     *   Billing for the following resources of the instance continues: system disk, data disks, and public bandwidth of the elastic IP address (EIP) (if any) that uses the pay-by-bandwidth metering method.
        #     *   The instance may fail to restart due to the reclaimed computing resources or insufficient resources. Try again later or change the instance type of the instance.
        #     *   If an EIP is associated with the instance before the instance is stopped, the EIP remains unchanged after the instance is restarted. If a static public IP address is associated with the instance before the instance is stopped, the static public IP address may change, but the private IP address does not change.
        # 
        #     For more information, see [Economical mode](https://help.aliyun.com/document_detail/63353.html).
        # 
        #     **
        # 
        #     **Note** If the instance itself does not support the economical shutdown mode, the API side does not intercept errors, and the instance is preferentially stopped. The following types of instances are not supported: classic network instances, local disks, and monthly instances.
        # 
        # *   KeepCharging: standard mode. After the instance is stopped in standard mode, you continue to be charged for the instance. If you want to change the operating system, re-initialize disks, change the instance type, or modify the private IP address, we recommend selecting this mode to avoid startup failures.
        # 
        # Default value: If the conditions for [enabling the economical mode for an instance in a VPC](~~63353#default~~) are met and you have enabled this mode in the ECS console, the default value is `StopCharging`. Otherwise, the default value is `KeepCharging`.
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

