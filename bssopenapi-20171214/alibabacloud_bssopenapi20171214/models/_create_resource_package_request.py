# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateResourcePackageRequest(DaraModel):
    def __init__(
        self,
        duration: int = None,
        effective_date: str = None,
        owner_id: int = None,
        package_type: str = None,
        pricing_cycle: str = None,
        product_code: str = None,
        specification: str = None,
    ):
        # The ID of the resource plan.
        # 
        # This parameter is required.
        self.duration = duration
        # The data returned.
        self.effective_date = effective_date
        self.owner_id = owner_id
        # The ID of the order.
        # 
        # This parameter is required.
        self.package_type = package_type
        self.pricing_cycle = pricing_cycle
        # Indicates whether the request is successful.
        # 
        # This parameter is required.
        self.product_code = product_code
        # The ID of the order.
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

