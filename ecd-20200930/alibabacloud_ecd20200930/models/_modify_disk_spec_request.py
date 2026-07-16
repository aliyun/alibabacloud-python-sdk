# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDiskSpecRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        desktop_id: str = None,
        promotion_id: str = None,
        region_id: str = None,
        reseller_owner_uid: int = None,
        root_disk_performance_level: str = None,
        user_disk_performance_level: str = None,
    ):
        # Specifies whether to enable automatic payment.
        # 
        # - If set to `true`, ensure your account has a sufficient balance. Otherwise, an abnormal order is generated.
        # 
        # - If set to `false`, log on to the console. Then, go to the **Expenses and Costs** page to pay for the order using the returned order ID.
        self.auto_pay = auto_pay
        # The ID of the cloud desktop.
        # 
        # This parameter is required.
        self.desktop_id = desktop_id
        # The promotion ID. Call a pricing inquiry API to get a list of applicable promotion IDs.
        self.promotion_id = promotion_id
        # The region ID. Call [DescribeRegions](~~DescribeRegions~~) to get a list of supported regions for WUYING Workspace.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.reseller_owner_uid = reseller_owner_uid
        # The performance level of the system disk. You can set the performance level for Graphics or High-frequency workspaces.
        self.root_disk_performance_level = root_disk_performance_level
        # The performance level of the data disk. You can set the performance level for Graphics or High-frequency workspaces.
        self.user_disk_performance_level = user_disk_performance_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.reseller_owner_uid is not None:
            result['ResellerOwnerUid'] = self.reseller_owner_uid

        if self.root_disk_performance_level is not None:
            result['RootDiskPerformanceLevel'] = self.root_disk_performance_level

        if self.user_disk_performance_level is not None:
            result['UserDiskPerformanceLevel'] = self.user_disk_performance_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResellerOwnerUid') is not None:
            self.reseller_owner_uid = m.get('ResellerOwnerUid')

        if m.get('RootDiskPerformanceLevel') is not None:
            self.root_disk_performance_level = m.get('RootDiskPerformanceLevel')

        if m.get('UserDiskPerformanceLevel') is not None:
            self.user_disk_performance_level = m.get('UserDiskPerformanceLevel')

        return self

