# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyNetworkPackageBandwidthRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        bandwidth: int = None,
        network_package_id: str = None,
        promotion_id: str = None,
        region_id: str = None,
        reseller_owner_uid: int = None,
    ):
        # Specifies whether to enable automatic payment.
        self.auto_pay = auto_pay
        # The bandwidth of the premium Internet bandwidth plan. Unit: Mbit/s.    
        # 
        # - If the premium bandwidth plan uses the subscription billing method, the valid values are 2 to 1000.
        # - If the premium bandwidth plan uses the pay-as-you-go billing method and the metering method is pay-by-data-transfer (PayByTraffic), the valid values are 2 to 200.
        # - If the premium bandwidth plan uses the pay-as-you-go billing method and the metering method is pay-by-bandwidth (PayByBandwidth), the valid values are 2 to 1000.
        # 
        # This parameter is required.
        self.bandwidth = bandwidth
        # The ID of the premium Internet bandwidth plan.
        # 
        # This parameter is required.
        self.network_package_id = network_package_id
        # The promotion ID.
        self.promotion_id = promotion_id
        # The region ID. You can call [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) to query the regions supported by Elastic Desktop Service.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The user ID of the resource ownership in the reseller pattern. You do not need to specify this parameter if you are not using the reseller pattern.
        self.reseller_owner_uid = reseller_owner_uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.network_package_id is not None:
            result['NetworkPackageId'] = self.network_package_id

        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.reseller_owner_uid is not None:
            result['ResellerOwnerUid'] = self.reseller_owner_uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('NetworkPackageId') is not None:
            self.network_package_id = m.get('NetworkPackageId')

        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResellerOwnerUid') is not None:
            self.reseller_owner_uid = m.get('ResellerOwnerUid')

        return self

