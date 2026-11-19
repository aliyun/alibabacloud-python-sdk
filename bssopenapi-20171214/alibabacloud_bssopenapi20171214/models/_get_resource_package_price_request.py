# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetResourcePackagePriceRequest(DaraModel):
    def __init__(
        self,
        duration: int = None,
        effective_date: str = None,
        instance_id: str = None,
        order_type: str = None,
        owner_id: int = None,
        package_type: str = None,
        pricing_cycle: str = None,
        product_code: str = None,
        specification: str = None,
    ):
        # The validity period of the resource plan. The value must match the available validity period of the specification size.
        # 
        # This parameter is required.
        self.duration = duration
        # The effective period of the resource plan. If you do not specify this parameter, the default is immediate.
        # When the order type is **BUY**, you cannot query the price of a resource plan whose effective period is more than six months later than the current time.
        # When the order type is **UPGRADE**, the effective period must be earlier than or equal to the actual expiration time of the resource plan to be upgraded.
        # Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.effective_date = effective_date
        # The instance ID. **This parameter is required when the order type is renewal or upgrade.**
        self.instance_id = instance_id
        # The order type. Valid values:
        # - BUY: new purchase.
        # - UPGRADE: upgrade.
        # - RENEW: renewal.
        # 
        # Default value: BUY.
        self.order_type = order_type
        self.owner_id = owner_id
        # The resource plan type. The value must be the same as the Code value of **ResourcePackage** returned by the operation that describes resource plans.
        # 
        # This parameter is required.
        self.package_type = package_type
        # The unit of the validity period for the resource plan. Valid values:
        # - Month: months.
        # - Year: years.
        self.pricing_cycle = pricing_cycle
        # The product code. You can obtain the product code by calling the **QueryProductList** operation or referring to the **Alibaba Cloud product code quick reference guide**.
        # 
        # This parameter is required.
        self.product_code = product_code
        # The specification size of the resource plan.
        # 
        # This parameter is required.
        self.specification = specification

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['Duration'] = self.duration

        if self.effective_date is not None:
            result['EffectiveDate'] = self.effective_date

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.package_type is not None:
            result['PackageType'] = self.package_type

        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.specification is not None:
            result['Specification'] = self.specification

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('EffectiveDate') is not None:
            self.effective_date = m.get('EffectiveDate')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')

        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('Specification') is not None:
            self.specification = m.get('Specification')

        return self

