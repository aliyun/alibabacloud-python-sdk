# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePriceRequest(DaraModel):
    def __init__(
        self,
        commodity: str = None,
        order_type: str = None,
    ):
        # Serialized commodity information based on the specified OrderType. The CommodityType corresponding to each OrderType is as follows:
        # 
        # INSTANCE_BUY: InstanceBuyCommodity
        # INSTANCE_RENEW: InstanceRenewCommodity
        # INSTANCE_UPGRADE: InstanceUpgradeCommodity
        # The parameters in the example are described as follows:
        # 
        # productCode: The product code.
        # skuCode: The product specification code. For non-image products: prepay for subscription, postpay for pay-as-you-go. For image products: ECS for pay-as-you-go, Package for subscription.
        # components: Specification modules. The version package_version is required, and other modules depend on the product settings.
        # duration: Number of cycles, such as 1, 2, 3...
        # pricingCycle: Cycle unit. Day, Month, or Year.
        # 
        # This parameter is required.
        self.commodity = commodity
        # Order type. Valid values:
        # 
        # INSTANCE_BUY: Product purchase
        # INSTANCE_RENEW: Instance renewal
        # INSTANCE_UPGRADE: Instance upgrade
        # Note: For renewal-type price inquiries, you must pass InstanceId in the Commodity parameter.
        # 
        # This parameter is required.
        self.order_type = order_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.commodity is not None:
            result['Commodity'] = self.commodity

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Commodity') is not None:
            self.commodity = m.get('Commodity')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        return self

