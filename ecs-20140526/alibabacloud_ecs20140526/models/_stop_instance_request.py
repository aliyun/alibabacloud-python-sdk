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
        # This parameter is being deprecated and is retained only for compatibility purposes. Ignore this parameter when you call this operation.
        self.confirm_stop = confirm_stop
        # Specifies whether to perform a dry run. Valid values:
        # 
        # - true: Performs a dry run without stopping the instance. The system checks whether the required parameters are specified, the request format is valid, service limits are met, and ECS inventory is sufficient. If the check fails, the corresponding error is returned. If the check passes, the error code `DryRunOperation` is returned.
        # - false: Performs a normal request. After the check passes, the instance is stopped.
        # 
        # Default value: false.
        self.dry_run = dry_run
        # Specifies whether to forcefully stop the instance. Valid values:
        # 
        # - true: Forcefully stops the instance. This is equivalent to a typical power-off operation. All cached data that is not written to the storage device is lost.
        # - false: Normally stops the instance.
        # 
        # Default value: false.
        self.force_stop = force_stop
        # >This parameter is in invitational preview and is not available for use.
        self.hibernate = hibernate
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The stop mode for a pay-as-you-go ECS instance. Valid values:
        # 
        #   - StopCharging: Economical mode. After economical mode is enabled:
        #     - Billing is suspended for compute resources (vCPUs, memory, and GPUs), image license fees, and the pay-by-bandwidth mode for static public IP addresses.
        #     - Billing continues for system disks, data disks, and the pay-by-bandwidth mode for elastic IP addresses (EIPs).
        #     - Because compute resources are reclaimed, the instance may fail to start due to insufficient inventory. In this case, try again later or change the instance type.
        #     - If an EIP is associated with the instance before the instance is stopped, the IP address remains unchanged after the instance is restarted. Otherwise, the static public IP address may change, but the private IP address remains unchanged. 
        # 
        #     For more information, see [Economical mode](https://help.aliyun.com/document_detail/63353.html).
        #     >Notice: 
        # If the instance does not support economical mode, the API does not return an error. The instance is stopped as a priority. Instance types that do not support economical mode include instances with local disks and subscription instances.
        #     
        # 
        #   - KeepCharging: Standard stop mode. Billing continues after the instance is stopped.
        # 
        # Default value: If you enable the economical mode for instances in a VPC in the ECS console (for more information, see [Enable economical mode by default](~~63353#default~~)) and the conditions are met, the default value is `StopCharging`. Otherwise, the default value is `KeepCharging`.
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

