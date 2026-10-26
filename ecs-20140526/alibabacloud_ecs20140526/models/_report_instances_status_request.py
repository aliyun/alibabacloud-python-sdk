# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ReportInstancesStatusRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        device: List[str] = None,
        disk_id: List[str] = None,
        end_time: str = None,
        instance_id: List[str] = None,
        issue_category: str = None,
        owner_account: str = None,
        owner_id: int = None,
        reason: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start_time: str = None,
    ):
        # The detailed description of the exception.
        # 
        # This parameter is required.
        self.description = description
        # The device names of the attached disks that have the same exception. You can specify up to 100 device names. If you use ECS Bare Metal instances, specify the slot information of the disk devices.
        # 
        # > For ECS Bare Metal instances, this parameter is required when the Reason parameter is set to abnormal-local-disk or abnormal-cloud-disk, or when the IssueCategory parameter is set to hardware-disk-error.
        self.device = device
        # The IDs of the disks that have the same exception. You can specify up to 100 disk IDs. If you use ECS Bare Metal instances, specify the serial numbers (SNs) of the disk devices.
        # 
        # > This parameter is required when the Reason parameter is set to abnormal-local-disk or abnormal-cloud-disk, or when the IssueCategory parameter is set to hardware-disk-error.
        self.disk_id = disk_id
        # The end time of the instance failures. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.end_time = end_time
        # The IDs of the ECS instances. You can specify up to 100 instance IDs.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The category of the exception. This parameter is applicable only to ECS Bare Metal instances. Valid values:
        # - hardware-cpu-error: CPU failure
        # - hardware-motherboard-error: Motherboard failure
        # - hardware-mem-error: Memory failure
        # - hardware-power-error: Power supply failure
        # - hardware-disk-error: Disk failure
        # - hardware-networkcard-error: Network interface controller (NIC) failure
        # - hardware-raidcard-error: SAS/RAID card failure
        # - hardware-fan-error: Fan failure
        # - others: Other exceptions
        self.issue_category = issue_category
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The impact of the exception on the ECS instance. Valid values:
        # 
        # - instance-hang: The ECS instance is unavailable or unreachable.
        # - instance-stuck-in-status: The ECS instance remains in a specific state, such as Starting or Stopping, for an extended period.
        # - abnormal-network: A network exception occurs on the ECS instance.
        # - abnormal-local-disk: An exception occurs on the local disk attached to the ECS instance.
        # - abnormal-cloud-disk: An exception occurs on the disk or Shared Block Storage attached to the ECS instance.
        # - others: Other exception types. If none of the preceding impact types apply, you can set Reason to others and provide more information in Description.
        self.reason = reason
        # The region ID of the instance. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The start time of the instance failures. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.device is not None:
            result['Device'] = self.device

        if self.disk_id is not None:
            result['DiskId'] = self.disk_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.issue_category is not None:
            result['IssueCategory'] = self.issue_category

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Device') is not None:
            self.device = m.get('Device')

        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IssueCategory') is not None:
            self.issue_category = m.get('IssueCategory')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

