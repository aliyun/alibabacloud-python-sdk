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
        # This parameter will be removed in the future and is retained only to ensure compatibility. We recommend that you ignore this parameter.
        self.confirm_stop = confirm_stop
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   true: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, service limits, and available ECS resources. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   false: performs a dry run and performs the actual request.
        # 
        # Default value: false.
        self.dry_run = dry_run
        # Specifies whether to forcefully stop the ECS instance. Valid values:
        # 
        # *   true: forcefully stops the ECS instance. If you set ForceStop to true, this operation is equivalent to a power-off operation. Cache data that is not written to storage devices on the instance is lost.
        # *   false: normally stops the ECS instance.
        # 
        # Default value: false.
        self.force_stop = force_stop
        # > This parameter is in invitational preview and is not publicly available.
        self.hibernate = hibernate
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The stop mode of the pay-as-you-go instance. Valid values:
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
        #     **Note** If the instance does not support the economical mode, the system stops the instance and does not report errors during the operation call. The following types of instances are not supported: classic network instances, local disks, and monthly instances.
        # 
        # *   KeepCharging: standard mode. After the instance is stopped in standard mode, you continue to be charged for the instance.
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

