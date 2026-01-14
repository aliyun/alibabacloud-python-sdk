# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateBandwidthPackageRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        auto_use_coupon: bool = None,
        bandwidth: int = None,
        bandwidth_package_id: str = None,
        bandwidth_type: str = None,
        description: str = None,
        name: str = None,
        region_id: str = None,
    ):
        # Specifies whether to enable automatic payment. Valid values:
        # 
        # *   **false**: disables automatic payment. This is the default value. If you select this option, you must go to [Order Center](https://usercenter2-intl.aliyun.com/order/list) to complete the payment after an order is generated.
        # *   **true**: enables automatic payment. Payments are automatically completed.
        # 
        # >  This parameter takes effect only if you call the UpdateBandwidthPackage operation to upgrade a bandwidth plan.
        self.auto_pay = auto_pay
        # Specifies whether to use coupons. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        self.auto_use_coupon = auto_use_coupon
        # The bandwidth value of the bandwidth plan. Unit: Mbit/s.
        # 
        # Valid values: **2** to **2000**.
        self.bandwidth = bandwidth
        # The ID of the bandwidth plan that you want to modify.
        # 
        # This parameter is required.
        self.bandwidth_package_id = bandwidth_package_id
        # The type of bandwidth. Valid values:
        # 
        # *   **Basic**
        # *   **Enhanced**
        # *   **Advanced**
        # 
        # >  You can upgrade **Basic** bandwidth to **Enhanced** bandwidth or downgrade Enhanced bandwidth to Basic bandwidth. You cannot change **Advanced** bandwidth to another type of bandwidth.
        self.bandwidth_type = bandwidth_type
        # The description of the bandwidth plan.
        # 
        # The description can be up to 256 characters in length.
        self.description = description
        # The name of the bandwidth plan. The name must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores (_), and hyphens (-). The name must start with a letter.
        self.name = name
        # The region ID of the GA instance. Set the value to **cn-hangzhou**.
        # 
        # This parameter is required.
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

        if self.auto_use_coupon is not None:
            result['AutoUseCoupon'] = self.auto_use_coupon

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id

        if self.bandwidth_type is not None:
            result['BandwidthType'] = self.bandwidth_type

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('AutoUseCoupon') is not None:
            self.auto_use_coupon = m.get('AutoUseCoupon')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')

        if m.get('BandwidthType') is not None:
            self.bandwidth_type = m.get('BandwidthType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

