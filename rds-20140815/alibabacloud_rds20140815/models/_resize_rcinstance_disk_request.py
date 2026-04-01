# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResizeRCInstanceDiskRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        disk_id: str = None,
        dry_run: bool = None,
        instance_id: str = None,
        new_size: int = None,
        region_id: str = None,
        type: str = None,
    ):
        # Specifies whether to enable the automatic payment feature for the instance. Valid values:
        # 
        # *   **true** (default): enables the feature. Make sure that your account balance is sufficient.
        # *   **false**: disables the feature. An unpaid order is generated.
        # 
        # >  If your account balance is insufficient, you can set AutoPay to false. In this case, an unpaid order is generated. You can complete the payment in the Expenses and Costs console.
        self.auto_pay = auto_pay
        self.disk_id = disk_id
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, service limits, and insufficient inventory errors.
        # *   **false**: performs a dry run and performs the actual request. If the request passes the dry run, the instance is created.
        self.dry_run = dry_run
        # The instance ID.
        self.instance_id = instance_id
        # The new disk size. Unit: GiB.
        self.new_size = new_size
        # The region ID of the instance.
        self.region_id = region_id
        # The method that you want to use to resize the disk. Valid values:
        # 
        # *   **offline** (default): resizes disks offline. After you resize a disk offline, you must restart the instance for the resizing operation to take effect.
        # *   **online**: resizes disks online. After you resize a disk online, the resizing operation takes effect immediately and you do not need to restart the instance.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.disk_id is not None:
            result['DiskId'] = self.disk_id

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.new_size is not None:
            result['NewSize'] = self.new_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NewSize') is not None:
            self.new_size = m.get('NewSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

