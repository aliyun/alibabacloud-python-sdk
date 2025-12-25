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
        # 
        # *   **true (default)**: automatically completes the payment. Make sure that your account balance is sufficient.
        # *   **false**: does not automatically complete the payment. An unpaid order is generated.
        # 
        # >  If your account balance is insufficient, you can set the AutoPay parameter to false. In this case, an unpaid order is generated. You can complete the payment in the Expenses and Costs console.
        self.auto_pay = auto_pay
        # The new disk type. Valid values:
        # 
        # *   **cloud_essd**: ESSD.
        # *   **cloud_auto**: ESSD AutoPL disk
        # 
        # This parameter is empty by default.
        self.disk_category = disk_category
        # The cloud disk ID.
        self.disk_id = disk_id
        # Specifies whether to perform a dry run. Valid values: Valid values:
        # 
        # *   **true**: performs a dry run and does not perform the actual request. The system checks the request parameters, request syntax, limits, and available resources.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, the operation is performed.
        self.dry_run = dry_run
        # The PL of the disk. Valid values:
        # 
        # *   **PL1** (default): A single ESSD can deliver up to 50,000 random read/write IOPS.
        # *   **PL2**: A single ESSD delivers up to 100,000 random read/write IOPS.
        # *   **PL3**: A single ESSD delivers up to 1,000,000 random read/write IOPS.
        self.performance_level = performance_level
        # The ID of the region in which the instance resides.
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

