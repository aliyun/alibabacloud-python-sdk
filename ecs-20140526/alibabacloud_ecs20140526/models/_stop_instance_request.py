# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StopInstanceRequest(DaraModel):
    def __init__(
        self,
        confirm_stop: bool = None,
        dry_run: bool = None,
        force_stop: bool = None,
        hibernate: bool = None,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        stopped_mode: str = None,
    ):
        # This parameter will be deprecated soon and is retained only for compatibility purposes. Ignore this parameter when you call this operation.
        self.confirm_stop = confirm_stop
        # Specifies whether to perform only a dry run. Valid values:
        # 
        # - true: performs only a dry run. The instance is not stopped. The system checks whether required parameters are specified, whether the request format is valid, whether business restrictions are met, and whether ECS inventory is sufficient. If the check fails, the corresponding error is returned. If the check succeeds, the `DryRunOperation` error code is returned.
        # - false: performs a dry run and sends the request. The instance is stopped after the check succeeds.
        # 
        # Default value: false.
        self.dry_run = dry_run
        # Specifies whether to forcefully stop the instance. Valid values:
        # 
        # - true: forcefully stops the instance. This is equivalent to a power-off operation. All cached data that is not written to storage devices is lost.
        # - false: normally stops the instance.
        # 
        # Default value: false.
        self.force_stop = force_stop
        # > This parameter is in invitational preview and is not available for use.
        self.hibernate = hibernate
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The stop mode for the pay-as-you-go ECS instance. Valid values:
        # 
        #   - StopCharging: economical mode. After the economical mode is enabled:
        #     - Billing is suspended for compute resources (vCPUs, memory, and GPUs), image license fees, and fixed bandwidth of static public IP addresses.
        #     - Billing continues for system disks, data disks, and fixed bandwidth of Elastic IP Addresses (EIPs).
        #     - Because compute resources are released, the instance may fail to restart due to insufficient inventory. Try again later or change the instance type.
        #     - If the instance is associated with an EIP before it is stopped, the IP address remains unchanged after the instance is restarted. Otherwise, the static public IP address may change, but the private IP address remains unchanged. 
        # 
        #     For more information, see [Economical mode](https://help.aliyun.com/document_detail/63353.html).
        #     >Notice: 
        # If the instance does not support the economical mode, no error is returned on the API side. Stopping the instance takes priority. Instance types that do not support the economical mode include instances with local disks and subscription instances.
        #     
        # 
        #   - KeepCharging: standard stop mode. The instance continues to be billed after it is stopped.
        # 
        # Default value: If you enable the economical mode for VPC-connected instances in the ECS console (for more information, see [Enable the economical mode by default](~~63353#default~~)) and the conditions are met, the default value is `StopCharging`. Otherwise, the default value is `KeepCharging`.
        self.stopped_mode = stopped_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.confirm_stop is not None:
            result['ConfirmStop'] = self.confirm_stop

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.force_stop is not None:
            result['ForceStop'] = self.force_stop

        if self.hibernate is not None:
            result['Hibernate'] = self.hibernate

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

        if self.stopped_mode is not None:
            result['StoppedMode'] = self.stopped_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfirmStop') is not None:
            self.confirm_stop = m.get('ConfirmStop')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('ForceStop') is not None:
            self.force_stop = m.get('ForceStop')

        if m.get('Hibernate') is not None:
            self.hibernate = m.get('Hibernate')

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

        if m.get('StoppedMode') is not None:
            self.stopped_mode = m.get('StoppedMode')

        return self

