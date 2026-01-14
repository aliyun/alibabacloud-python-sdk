# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetInventoryListRequest(DaraModel):
    def __init__(
        self,
        code: str = None,
        emission_type: str = None,
        group: str = None,
        method_type: str = None,
        product_id: int = None,
        product_type: int = None,
    ):
        # The enterprise code.
        # 
        # This parameter is required.
        self.code = code
        # Type of emission
        # 
        # >  Valid values: footprint | emission. Meaning: footprint: all inventories are involved in the calculation; emission: only inventories with positive and zero emissions are involved in the calculation, and negative numbers are not involved in the calculation.
        # 
        # This parameter is required.
        self.emission_type = emission_type
        # Group by
        # 
        # >  Valid values: resource | process | resourceType | processType. Meaning: resource: aggregation by inventory group, process: aggregation by operation group, resourceType: aggregation by inventory type, processType: aggregation by phase group
        # 
        # This parameter is required.
        self.group = group
        # The type of the obtained environmental impact: gwp indicates the carbon footprint of climate change. 
        # <props="intl">[For more information, see the environment impact category enumeration.](https://www.alibabacloud.com/help/en/energy-expert/developer-reference/enumerated-values-of-energy-expert#RhGn7)
        # 
        # This parameter is required.
        self.method_type = method_type
        # The product id.
        # 
        # This parameter is required.
        self.product_id = product_id
        # Product type: 1 indicates that the carbon footprint of the product is requested, and 5 indicates that the carbon footprint of the supply chain is requested.
        # 
        # This parameter is required.
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.emission_type is not None:
            result['emissionType'] = self.emission_type

        if self.group is not None:
            result['group'] = self.group

        if self.method_type is not None:
            result['methodType'] = self.method_type

        if self.product_id is not None:
            result['productId'] = self.product_id

        if self.product_type is not None:
            result['productType'] = self.product_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('emissionType') is not None:
            self.emission_type = m.get('emissionType')

        if m.get('group') is not None:
            self.group = m.get('group')

        if m.get('methodType') is not None:
            self.method_type = m.get('methodType')

        if m.get('productId') is not None:
            self.product_id = m.get('productId')

        if m.get('productType') is not None:
            self.product_type = m.get('productType')

        return self

