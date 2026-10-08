# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyRCDiskSpecRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        disk_category: str = None,
        disk_id: str = None,
        dry_run: bool = None,
        performance_level: str = None,
        region_id: str = None,
    ):
        # Specifies whether to enable automatic payment. Valid values:
        # - **true** (default): Automatic payment is enabled. Make sure that your account balance is sufficient.
        # - **false**: Only an order is generated. No payment is made.
        # 
        # > If your payment method has an insufficient balance, set AutoPay to false. An unpaid order is generated. You can log on to the ApsaraDB RDS console to complete the payment.
        # >
        self.auto_pay = auto_pay
        # The type of the cloud disk. Valid values:
        # - **cloud_essd** (default): ESSD cloud disk.
        # - **cloud_auto**: ESSD AutoPL cloud disk.
        # - **cloud_ssd**: standard SSD.
        self.disk_category = disk_category
        # The cloud disk ID.
        self.disk_id = disk_id
        # Specifies whether to perform a dry run for this operation. Valid values:
        # * **true**: A dry run is performed without executing the change. The check items include request parameters, request format, business limits, and inventory.
        # * **false** (default): A normal request is sent. After the check is passed, the change is directly executed.
        self.dry_run = dry_run
        # The performance level (PL) of the ESSD cloud disk. Valid values:
        # 
        # - **PL1** (default): A maximum of 50,000 random read/write IOPS per disk.
        # 
        # - **PL2**: A maximum of 100,000 random read/write IOPS per disk.
        # 
        # - **PL3**: A maximum of 1,000,000 random read/write IOPS per disk.
        self.performance_level = performance_level
        # The region ID of the instance.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.disk_category is not None:
            result['DiskCategory'] = self.disk_category

        if self.disk_id is not None:
            result['DiskId'] = self.disk_id

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('DiskCategory') is not None:
            self.disk_category = m.get('DiskCategory')

        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

